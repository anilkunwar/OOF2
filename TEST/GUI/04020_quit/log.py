# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2014/09/27 21:42:13 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Microstructure.New
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(358, 94)
findWidget('Questioner:gtk-save').clicked()
checkpoint toplevel widget mapped Dialog-Save Log File
findWidget('Dialog-Save Log File').resize(194, 72)
findWidget('Dialog-Save Log File:filename').set_text('q')
findWidget('Dialog-Save Log File:filename').set_text('qu')
findWidget('Dialog-Save Log File:filename').set_text('qui')
findWidget('Dialog-Save Log File:filename').set_text('quit')
findWidget('Dialog-Save Log File:filename').set_text('quit.')
findWidget('Dialog-Save Log File:filename').set_text('quit.l')
findWidget('Dialog-Save Log File:filename').set_text('quit.lo')
findWidget('Dialog-Save Log File:filename').set_text('quit.log')
findWidget('Dialog-Save Log File:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
