#!/bin/env python
#-*- coding: utf-8 -*-
#
# versao do projeto
# por Deivison de alcantara 

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pesquisar import *
import os
import sqlite3

class primeiro(QFrame, Ui_Frame):
  
  def __init__(self, parent = None):
    super(primeiro, self).__init__(parent)
    self.setupUi(self)
    self.pesquisa.returnPressed.connect(self.lista)
    self.verificar.clicked.connect(self.lista)
    conn = sqlite3.connect("sono7.db")
    self.cursor = conn.cursor()
    
    
    
  def lista(self):

    self.listadevalores.clear()
    
    if self.nome.isChecked() == True and self.Profissao.isChecked() == False:
      
      if self.pesquisa.text() != '':
      
        sql = ("""
          SELECT rowid, NOME, album  FROM teste
          WHERE NOME || album || numero LIKE '%{}%' order by nome""".format(self.pesquisa.text()))
        
        self.cursor.execute(sql)
      
        for x in self.cursor.fetchall():
          item = str(x[0])+ ' - ' + str(x[1]) + ' - ' + str(x[2])
          self.listadevalores.addItem(item)
          
     
    if self.nome.isChecked() == False and self.Profissao.isChecked() == True:
      
      if self.pesquisa.text() != '':
      
        sql = ("""
          SELECT rowid, NOME, album FROM teste
          WHERE texto LIKE '%{}%' order by nome""".format(self.pesquisa.text()))
        self.cursor.execute(sql)
      
        for x in self.cursor.fetchall():
          item = str(x[0])+ ' - ' + str(x[1]) + ' - ' + str(x[2])
          self.listadevalores.addItem(item)
    
    
    if self.nome.isChecked() == True and self.Profissao.isChecked() == True:

      if self.pesquisa.text() != '':
      
        sql = ("""
          SELECT rowid, NOME, album FROM teste
          WHERE nome || album || texto || numero LIKE '%{}%' order by nome""".format(self.pesquisa.text()))
        self.cursor.execute(sql)
      
        for x in self.cursor.fetchall():
          item = str(x[0])+ ' - ' + str(x[1]) + ' - ' + str(x[2])
          self.listadevalores.addItem(item)

    if self.pesquisa.text() == '*':
      
      sql = ("""
          SELECT * FROM teste order by rowid
          """)
      self.cursor.execute(sql)
      for x in self.cursor.fetchall():
        item = str(x[0])+' - '+str(x[1])+' - '+str(x[2])
        self.listadevalores.addItem(item)


    
## tirar o comentario para execultar sem pai        
##app = QApplication(sys.argv)
##dlg = primeiro()
##dlg.show()
##sys.exit(app.exec_())
  

