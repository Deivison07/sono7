#!/bin/env python
#-*- coding: utf-8 -*-
#
# versao do projeto
# por Deivison de alcantara 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from coletaneas import Ui_Frame

class coletanea(QtWidgets.QFrame, Ui_Frame):
  
  def __init__(self, parent = None):
    super(coletanea, self).__init__(parent)
    self.setupUi(self)

    #self.pushButton_4.clicked.connect(self.adoradores1)
    #self.pushButton_3.clicked.connect(self.adoradores2)
    #self.pushButton_5.clicked.connect(self.adoradores3)
    
    
  def adoradores1(self):
    self.coletaneaItem = 'adoradores1'
    
  def adoradores2(self):
    self.coletaneaItem = 'diferente'

  def adoradores3(self):
    self.coletaneaItem = 'video'
    
    

    
    
  
