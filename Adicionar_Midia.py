#!/bin/env python
#-*- coding: utf-8 -*-
#
# versao do projeto
# por Deivison de alcantara 

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from adicionar import *
from segundo import primeiro
import os
import sqlite3

class primeiro1(QFrame, Ui_Frame):
  
  def __init__(self, parent = None):
    super(primeiro1, self).__init__(parent)
    self.setupUi(self)
    self.limpar.clicked.connect(self.limparcampos)
    self.salvar.clicked.connect(self.salvarcampos)
    self.pesquisar.clicked.connect(self.pesquise)
    self.conn = sqlite3.connect("sono7.db")
    self.cursor = self.conn.cursor()
    self.linhasnum()
    self.numero.clear()
    
    
  def pesquise(self):
      self.tela2 = primeiro()
      self.tela2.show()
      '''commit'''
    
  def linhasnum(self):
    self.cursor.execute ("""SELECT count(*) FROM teste""")
    for x in self.cursor.fetchall():
      self.linhas.setText(str(x[0]))
    
    
  def limparcampos(self):
    self.nome.clear()
    self.album.clear()
    self.numero.clear()
    self.texto.clear()
    self.linkmusica.clear()
    self.linkicone.clear()
    self.linktrecho.clear()
    self.linhasnum()
    
    

  def salvarcampos(self):
    self.linhasnum()
    
    self.cursor.execute("""INSERT INTO teste VALUES (
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}'
                    )""".format(self.nome.text() , self.album.text() , self.numero.text(),self.autor.text(),self.linkmusica.text(),self.linkicone.text(),self.linktrecho.text(),self.texto.toPlainText()))
    self.conn.commit()
    self.linhasnum()
    
app = QApplication(sys.argv)
dlg = primeiro1()
dlg.show()
sys.exit(app.exec_())

