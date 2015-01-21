# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.3 $
# $Author: langer $
# $Date: 2014/09/27 21:42:00 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def sensitivity0():
    return sensitizationCheck({'gtk-ok' : 0,
                               'gtk-apply' : 0,
                               'gtk-cancel' : 1},
                              base = 'Dialog-New Boundary Condition')

