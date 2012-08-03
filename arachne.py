#!/usr/bin/python

from PySide import QtGui, QtCore
#from lexiabase import *

def main():
  app = QtGui.QApplication([])
  mw = QtGui.QMainWindow()
  mw.setCentralWidget(AppWidget(mw))
  mw.show()
  app.exec_()

class AppWidget (QtGui.QWidget):
  def __init__(self, parent):
    super(AppWidget,self).__init__(parent)
    lay = QtGui.QHBoxLayout()
    listbox = QtGui.QListView()
    edit1 = EditBox()
    linkbutton = QtGui.QPushButton("Link ->")
    edit2 = EditBox()
    lay.addWidget(listbox)
    lay.addWidget(edit1)
    lay.addWidget(linkbutton)
    lay.addWidget(edit2)
    self.setLayout(lay)  

class EditBox (QtGui.QWidget):
  def __init__(self, parent=None):
    super(EditBox,self).__init__(parent)
    lay = QtGui.QVBoxLayout()
    nodeidbox = QtGui.QLineEdit()
    lexiabox = QtGui.QTextEdit()
    lay.addWidget(nodeidbox)
    lay.addWidget(lexiabox)
    self.setLayout(lay)
    QtCore.Signal

if __name__ == '__main__':
  main()
