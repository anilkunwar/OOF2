// -*- C++ -*-
// $RCSfile: color.swg,v $
// $Revision: 1.18 $
// $Author: langer $
// $Date: 2014/09/27 21:41:10 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module colorproperty

%{
#include "engine/property/color/color.h"
#include "common/ccolor.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%pragma(python) code="from ooflib.SWIG.common.ccolor import CColorPtr"
%extern "common/ccolor.swg"

// // Converts color from common.IO.color object into a CColor object.
// %typemap(python, in) CColor * {
//   PyObject *rval = PyObject_CallMethod($source,(char*)"getRed",NULL);
//   PyObject *gval = PyObject_CallMethod($source,(char*)"getGreen",NULL);
//   PyObject *bval = PyObject_CallMethod($source,(char*)"getBlue",NULL);

//   double red = PyFloat_AsDouble(rval);
//   double green = PyFloat_AsDouble(gval);
//   double blue = PyFloat_AsDouble(bval);

//   $target = new CColor(red, green, blue);
// }

// %typemap(python,freearg) CColor * {
//   delete $source;
// }


class ColorProp : public Property {
public:
  ColorProp(PyObject *self, char *name, CColor *cv);
  CColor color();
};

%pragma(python) include="engine/property/color/color.spy"
