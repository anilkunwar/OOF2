// -*- C++ -*-
// $RCSfile: intarray.swg,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:40:20 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef INTARRAY_SWG
#define INTARRAY_SWG

%module intarray
%include "common/typemaps.swg"
%extern "common/coord.swg"
 //%pragma(python) code="from ooflib.SWIG.common.intarray import IntArrayPtr"

%{
#include "common/intarray.h"
%}

class IntArray {
public:
//  IntArray(ICoord*,int);
  ~IntArray();
  ICoord size();
};

%new IntArray makeIntArray(ICoord *iPoint,int);
#endif // INTARRAY_SWG
