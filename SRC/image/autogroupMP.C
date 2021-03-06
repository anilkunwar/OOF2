// -*- C++ -*-
// $RCSfile: autogroupMP.C,v $
// $Revision: 1.15 $
// $Author: langer $
// $Date: 2012/10/16 18:19:12 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/cmicrostructure.h"
#include "common/coord.h"
#include "common/oofomp.h"
#include "common/pixelgroup.h"
#include "common/progress.h"
#include "common/switchboard.h"
#include "common/tostring.h"
#include "image/oofimage.h"
#include <string>
#include <vector>
#include <map>
#include <fstream>

CColor packet2color(const Magick::PixelPacket &packet) {
  using namespace Magick;
  double scale = 1./MaxRGB;
  return CColor(packet.red*scale, packet.green*scale, packet.blue*scale);
}

// Replace all instances of a by b within source and return the
// result.  Used when constructing group names.
std::string substitute(const std::string &source, const std::string &a,
		       const std::string &b)
{
  std::string result = source;
  std::string::size_type pos = result.find(a, 0);
  while(pos != std::string::npos) {
    result = result.replace(pos, a.size(), b);
    pos = result.find(a, pos+a.size());
  }
  return result;
}

typedef std::vector<ICoord> PixelList;
typedef std::map<const CColor, PixelList> ColorListMap;

const std::string *autogroup(CMicrostructure *ms, OOFImage *image,
			     const std::string &name_template)
{
  ICoord size(ms->sizeInPixels());
  const int width = size(0);
  const int height = size(1);
  const double npixels = height*width; // double, used as denominator
  int ndone = 0;	    // number of pixels that have been checked
  int nlists = 0;	    // number of pixel lists created by all threads

  std::vector<ColorListMap> colorlists;
  
  Progress *progress=dynamic_cast<DefiniteProgress*>(findProgress("AutoGroup"));

  // OOFImage::operator[] doesn't appear to be threadsafe, due to some
  // ImageMagick problem.  But getting data from the PixelPacket is
  // faster anyway.
  const Magick::PixelPacket *packet = image->pixelPacket();

#pragma omp parallel  shared(colorlists) //if(npixels > 1000000)
  {
    // Each thread has its own ColorListMap called 'colorlist', but
    // they're all stored in a global 'colorlists' array so that they
    // can be accessed from other threads later.
#pragma omp single 
    {
      progress->setMessage("Categorizing pixels");
      colorlists.resize(omp_get_num_threads());
    }
    ColorListMap &colorlist = colorlists[omp_get_thread_num()];

    // Put pixels with the same color into lists.
#pragma omp for schedule(dynamic,10)
    for(int j=0; j<height; ++j) {
      #pragma omp critical
      if(!progress->stopped()) {
	for(int i=0; i<width && !progress->stopped(); ++i) {
	  ICoord pxl(i, j);
	  // Direct lookup in the ImageMagick image is not thread safe
	  // somehow.
//  	  const CColor color((*image)[pxl]);
	  // This is uglier but faster and also apparently thread
	  // safe.
 	  const CColor color(packet2color(packet[i + j*width]));
	  // Look for a list for this color.
	  ColorListMap::iterator findlist = colorlist.find(color);
	  if(findlist == colorlist.end()) {
	    // didn't find existing list of pixels for this color
 	    colorlist[color] = PixelList(1, pxl);
	  }
	  else {
	    (*findlist).second.push_back(pxl);
	  }
	} // loop over i
#pragma omp critical
	{
	  ndone += width;
	  progress->setFraction(ndone/npixels);
	}
      }
    } // loop over j
  } // end parallel

  if(progress->stopped())
    return new std::string("");

  // Create pixel groups in the Microstructure for each Color.  This
  // has to be done serially.
  progress->setMessage("Creating groups");
  progress->setFraction(0.0);
  ndone = 0;
  // How many sets of pixels have been created in all threads?  We
  // need to know this so that we can update the progress bar.
  for(unsigned int i=0; i<colorlists.size(); i++)
    nlists += colorlists[i].size();

  typedef std::map<const CColor, PixelGroup*> ColorGroupMap;
  ColorGroupMap colorgroupmap;
  typedef std::map<PixelGroup*, const CColor, PixelGroupCompare> GroupColorMap;
  GroupColorMap groupcolormap;

  std::vector<PixelGroup*> groups;
  std::string *newgroupname = new std::string(""); // last new group, if any

  // Loop over all the pixel lists created by all the threads to find
  // the unique colors in the image.  Each thread may have created a
  // separate list of pixels for every color.
  int grpcount = 0;

  for(unsigned int ic=0; ic<colorlists.size() && !progress->stopped(); ++ic) {
    ColorListMap &colorlist = colorlists[ic];
    for(ColorListMap::iterator i=colorlist.begin(); i!=colorlist.end(); ++i) {
      const CColor &color = (*i).first;
      // Have we already found the group for this color?
      ColorGroupMap::iterator findgrp = colorgroupmap.find(color);
      if(findgrp == colorgroupmap.end()) { // Didn't find it.
	std::string grpname = name_template;
	grpname = substitute(grpname, "%c", color.name());
	grpname = substitute(grpname, "%n", to_string(grpcount++));
	bool newness = false;
	PixelGroup *grp = ms->getGroup(grpname, &newness); // create group
	groups.push_back(grp);
	// Can't use cologroupmap[color] = grp since the key is const.
	colorgroupmap.insert(ColorGroupMap::value_type(color, grp));
	groupcolormap.insert(GroupColorMap::value_type(grp, color));
	if(newness)
	  *newgroupname = grpname;
      }
      progress->setFraction(++ndone/(double)nlists);
    }
  }

  if(progress->stopped())
    return new std::string("");

  ndone = 0;
  progress->setFraction(0.0);
  progress->setMessage("Adding pixels to groups");
  
  // Add pixels to groups.  Each group is handled by only one thread,
  // but different groups can be done simultaneously by different
  // threads.

#pragma omp parallel // if(npixels > 1000000)
  {
#pragma omp for nowait 
    // loop over groups
    for(unsigned int igrp=0; igrp<groups.size(); igrp++) {
      PixelGroup *grp = groups[igrp];
      const CColor &color = groupcolormap[grp];
      // loop over maps of lists created by different threads
      for(unsigned int c=0; c<colorlists.size(); c++) {
	const ColorListMap &colorlist = colorlists[c];
	// See if this color has a list in this map
	ColorListMap::const_iterator listptr = colorlist.find(color);
	if(listptr != colorlist.end()) {
	  grp->add(&(*listptr).second);
	}
      }
#pragma omp atomic 
      ++ndone;
      if(omp_get_thread_num() == 0) {
	progress->setFraction(ndone/(double) grpcount);
      }
    }	// end loop over groups
  }	// end parallel

  // Return the name of the last pixel group created, if any.
  if(!progress->stopped()) {
    return newgroupname;
  }
  return new std::string("");		// empty string
} 
