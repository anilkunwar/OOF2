// -*- C++ -*-
// $RCSfile: materialsubproblem.C,v $
// $Revision: 1.8 $
// $Author: langer $
// $Date: 2011/03/04 19:48:13 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "engine/material.h"
#include "engine/materialsubproblem.h"
#include <iostream>

MaterialPredicate::MaterialPredicate(Material *const mat)
  : material(mat)
{}

bool MaterialPredicate::operator()(const FEMesh*, const Element *element) const
{
  return element->material() == material;
}

MaterialSet *CMaterialSubProblem::getMaterials() const {
  MaterialSet *mats = new MaterialSet;
  mats->insert(predicate.material);
  return mats;
}
