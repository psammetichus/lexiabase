#!/usr/bin/python

from PySide import QtGui, QtCore
from lexiabase import *

lbase = None

def populatebase(lb):
  a = lb.new_node(u'Now is the hour of our discontent.')
  b = lb.new_node(u'Whatever you\'re thinking, just stop')
  c = lb.new_node(u'This is time when all bears can come together and rut.')
  lb.link(a,b)
  lb.link(a,c)


def main():
  app = QtGui.QApplication([])
  global lbase
  lbase = Lexiabase()
  populatebase(lbase)
  mw = QtGui.QMainWindow()
  mw.setCentralWidget(AppWidget(mw))
  mw.show()
  app.exec_()

def receive_item(item):
  global lbase
  
  
class AppWidget (QtGui.QWidget):
  def __init__(self, parent):
    super(AppWidget,self).__init__(parent)
    global lbase
    lay = QtGui.QHBoxLayout()
    self.listbox = QtGui.QListWidget()
    edit1 = EditBox()
    linkbutton = QtGui.QPushButton("Link ->")
    edit2 = EditBox()
    lay.addWidget(self.listbox)
    lay.addWidget(edit1)
    lay.addWidget(linkbutton)
    lay.addWidget(edit2)
    self.setLayout(lay)
    #set up items
    self.displayItems()
    self.listbox.itemActivated.connect(edit1.receive_item)
  def displayItems(self):
    for i in lbase.index.values():
		litem = QtGui.QListWidgetItem("%d::%s" % (i.nodeid, i.contents[:20]))
		litem.setData(50, i)
		self.listbox.addItem(litem)
		
		
	
    

class EditBox (QtGui.QWidget):
  def __init__(self, parent=None):
    super(EditBox,self).__init__(parent)
    lay = QtGui.QVBoxLayout()
    self.nodeidbox = QtGui.QLineEdit()
    self.lexiabox = QtGui.QTextEdit()
    lay.addWidget(self.nodeidbox)
    lay.addWidget(self.lexiabox)
    self.setLayout(lay)
  def receive_item(self,item):
	global lbase
	self.lexiabox.clear()
	self.lexiabox.insertPlainText(item.data(50).contents)
	self.nodeidbox.setText(str(item.data(50).nodeid))

if __name__ == '__main__':
  main()
