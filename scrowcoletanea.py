#!/bin/env python
#-*- coding: utf-8 -*-
#
# versao do projeto
# por Deivison de alcantara 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from coletaneaScrow import *
#from indexcoletanea import *



class scrow(QtWidgets.QFrame, Ui_Frame):
  def __init__(self, parent = None):
    super(scrow, self).__init__(parent)
    self.setupUi(self)
    
    

    
