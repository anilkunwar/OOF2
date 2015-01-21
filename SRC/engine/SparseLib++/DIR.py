# -*- python -*-
# $RCSfile: DIR.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2014/09/27 21:41:04 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'SparseLib++'
if not DIM_3:
    clib = 'oof2engine'
else:
    clib = 'oof3dengine'

hfiles = [
    'bicg.h', 'cg.h', 'bicgstab.h', 'gmres.h'
    ]

