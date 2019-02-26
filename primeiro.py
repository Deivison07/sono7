#!/bin/env python
#-*- coding: utf-8 -*-
#
# versao do projeto
# por Deivison de alcantara

import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot
from output import *
import vlc
import os
import motorSlide2
import time
import sqlite3
from scrowcoletanea import scrow
from indexcoletanea import *


class primeiro(QtWidgets.QMainWindow, Ui_MainWindow):

  def __init__(self, parent = None):
    super(primeiro, self).__init__(parent)
    self.setupUi(self)
    #primeiro foi colocado no atributo player a funcao instancia do vlc
    #self.player3 = vlc
    self.player = vlc.Instance()
    self.player2 = vlc.MediaPlayer()



    self.conteudoAlbum.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.conteudoAlbum.customContextMenuRequested.connect(self.context2)
    self.conteudoAlbum.itemClicked.connect(self.itemAtivado)
    self.conteudoAlbum.itemDoubleClicked.connect(self.reproduzir)
    self.conteudoAlbum.itemDoubleClicked.connect(self.mostrar_trecho)


    self.index = scrow()
    self.dadosColetanea = coletanea()
    self.index.scrollArea.setWidget(self.dadosColetanea)
    #self.dadosColetanea.pushButton_3.clicked.connect(self.coletaneax4)
    #self.dadosColetanea.pushButton_5.clicked.connect(self.coletaneax4)
    #self.dadosColetanea.pushButton_4.clicked.connect(self.coletaneax4)
    #self.itemcoletanea = self.dadosColetanea.coletaneaItem


    conn = sqlite3.connect("sono7.db")
    self.cursor = conn.cursor()

    self.pesquisa.returnPressed.connect(self.lista)
    self.botaopesquisa.clicked.connect(self.lista)

    self.pesquisarAlbum.returnPressed.connect(self.lista2)
    self.botaoAlbum.clicked.connect(self.lista2)


    '''foi colocado no atributo mediaListPlayer a funcao media_list_player_new()
      que e o modulo de playlist do vlc
    '''
    self.mediaListPlayer = self.player.media_list_player_new()
    '''
        foi colocado no atributo mediaList a funcao media_list_new funcao que
        cria uma nova lista de arquivos
    '''
    self.mediaList = self.player.media_list_new()
    '''
        aqui a QListWidget clamada de lista_musicais entrega a funcao mostrar
        o item que foi duplamente clicado
    '''

    self.lista_musicas.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lista_musicas.customContextMenuRequested.connect(self.context)

    self.lista_musicas.itemDoubleClicked.connect(self.mostrar)
    self.lista_musicas.itemDoubleClicked.connect(self.mostrar_trecho)
    self.lista_musicas.itemClicked.connect(self.itemAtivado)

    self.lista_trecho.itemDoubleClicked.connect(self.trecho)

    self.verticalSlider.valueChanged.connect(self.volume)
    self.player2.audio_set_volume(100)

    self.listadevalores.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.listadevalores.customContextMenuRequested.connect(self.context3)

    self.listadevalores.itemDoubleClicked.connect(self.mostrar_trecho2)
    self.listadevalores.itemDoubleClicked.connect(self.reproduzir2)
    self.listadevalores.itemClicked.connect(self.itemAtivado)

    self.album.itemDoubleClicked.connect(self.coletanea)

    self.imagem.clicked.connect(self.coletanea2)

    self.ativado = False
    #self.scrollArea_2.setWidget(self.page2)

    '''
        aqui eu instituo a um atributo, uma lista com dois videos
    '''

    '''
        aqui e implementado um for para colocar os videos do atribito playlist
        na funcao de lista do vlc
        tambem e colocado os itens na QListWidget
    '''

    self.mediaListPlayer.set_media_list(self.mediaList)
    self.mediaListPlayer.set_media_player(self.player2)
    self.lista_trecho.setVisible(0)
    self.trechos3.setVisible(0)
    self.adicionar.setVisible(0)
    self.lista_musicas.setVisible(0)

    self.album.clear()
    sql = ("""
          SELECT DISTINCT album FROM teste """)
    self.cursor.execute(sql)
    for x in self.cursor.fetchall():
      self.album.addItem(x[0])

      #self.dicitemp[str(x[0])] = str(x[1]),str(x[2]),str(x[3]),str(x[4])

  def coletanea2(self):
    self.index.show()

  def coletaneax4(self):
    self.dicitemp = {}
    self.conteudoAlbum.clear()

    sql = ("""
          SELECT NOME, linkmusica, linkicone,linktrecho,album FROM teste
          WHERE album LIKE '%{}%' order by nome
            """.format(self.dadosColetanea.coletaneaItem))
    try:
      self.cursor.execute(sql)
      for x in self.cursor.fetchall():
        item1 = str(x[0])
        self.conteudoAlbum.addItem(item1)
        self.dicitemp[str(x[0])] = str(x[1]),str(x[2]),str(x[3]),str(x[4])
    except Exception:
      pass

  def lista2(self):

    self.album.clear()
    sql = ("""
          SELECT DISTINCT album FROM teste
          WHERE album LIKE '%{}%' order by nome

          """.format(self.pesquisarAlbum.text()))
    try:

      self.cursor.execute(sql)
      for x in self.cursor.fetchall():
        self.album.addItem(x[0])

    except Exception:
      pass

  def lista(self):


    try:
      self.listadevalores.clear()
      self.dicitempesq = {}

      if self.nomep.isChecked() == True and self.Profissao.isChecked() == False:

        if self.pesquisa.text() != '':


          sql = ("""
            SELECT NOME, album, linkmusica, linkicone, linktrecho FROM teste
            WHERE NOME || album || numero LIKE '%{}%' order by nome""".format(self.pesquisa.text()))

          self.cursor.execute(sql)

          self.dicitempesq = {}

          for x in self.cursor.fetchall():
            item = str(x[0])+' - '+str(x[1])

            self.dicitempesq[str(x[0])] = str(x[2]),str(x[3]),str(x[4])
            self.listadevalores.addItem(item)

      if self.nomep.isChecked() == False and self.Profissao.isChecked() == True:

        if self.pesquisa.text() != '':

          sql = ("""
            SELECT NOME, album, linkmusica, linkicone, linktrecho FROM teste
            WHERE texto LIKE '%{}%' order by nome""".format(self.pesquisa.text()))

          self.cursor.execute(sql)
          self.dicitempesq = {}
          for x in self.cursor.fetchall():
            item = str(x[0])+' - '+str(x[1])
            self.dicitempesq[str(x[0])] = str(x[2]),str(x[3]),str(x[4])
            self.listadevalores.addItem(item)


      if self.nomep.isChecked() == True and self.Profissao.isChecked() == True:

        if self.pesquisa.text() != '':

          sql = ("""
            SELECT NOME, album, linkmusica, linkicone, linktrecho FROM teste
            WHERE NOME || album || numero || texto LIKE '%{}%' order by nome""".format(self.pesquisa.text()))

          self.cursor.execute(sql)

          self.dicitempesq = {}

          for x in self.cursor.fetchall():
            item = str(x[0])+' - '+str(x[1])

            self.dicitempesq[str(x[0])] = str(x[2]),str(x[3]),str(x[4])
            self.listadevalores.addItem(item)

      if self.pesquisa.text() == '*':

        sql = ("""
            SELECT * FROM teste order by nome
            """)
        self.dicitempesq = {}
        self.cursor.execute(sql)
        for x in self.cursor.fetchall():

          item = str(x[0])+' - '+str(x[1])
          self.dicitempesq[str(x[0])] = str(x[2]),str(x[3]),str(x[4])
          self.listadevalores.addItem(item)
    except Exception:
      pass


  def mostrar(self,item):

    self.mediaListPlayer.play_item_at_index(self.lista_musicas.row(item))
    #print(self.player3.libvlc_media_get_mrl(self.player2.get_media()))
    self.notifica(item)

  def notifica(self,item,icone='listaimagem.jpeg',label='Item da Lista'):

    self.play.setEnabled(True)
    self.stop.setEnabled(True)
    self.mudarTrack.setEnabled(True)
    self.player2.audio_set_track(1)
    self.play.setChecked(False)
    self.mudarTrack.setChecked(False)

    time.sleep(0.5)

    if self.player2.audio_get_track_count() <= 2:
      self.mudarTrack.setVisible(0)
    else:
      self.mudarTrack.setVisible(1)

    self.executado = item.text()
    self.reproduzindo.setText(label)

    self.iconeMusica.setPixmap(QtGui.QPixmap(icone))

  def mostrar_trecho(self,item):

    self.lista_trecho.clear()
    self.lista_trecho.setVisible(0)
    self.trechos3.setVisible(0)
    self.trechostemp = motorSlide2


    try:

      self.trechostemp2 = self.trechostemp.legenda(self.dicitemp[item.text()][2])

      for element in self.trechostemp.coisas:

        nomes = str(element)
        if nomes == 'nao ha legenda':
          self.lista_trecho.setVisible(0)

          break

        self.lista_trecho.setVisible(1)
        self.trechos3.setVisible(1)
        self.lista_trecho.addItem(nomes)

    except Exception:
      pass

  def mostrar_trecho2(self,item):

    itemtrat = item.text()
    item2 = itemtrat.split(' - ')

    self.lista_trecho.clear()
    self.lista_trecho.setVisible(0)
    self.trechos3.setVisible(0)
    self.trechostemp = motorSlide2

    try:
      self.trechostemp2 = self.trechostemp.legenda(self.dicitempesq[item2[0]][2])
      for element in self.trechostemp.coisas:

        nomes = str(element)
        if nomes == 'nao ha legenda':
          self.lista_trecho.setVisible(0)

          break

        self.lista_trecho.setVisible(1)
        self.trechos3.setVisible(1)
        self.lista_trecho.addItem(nomes)

    except Exception:
      pass

  def trecho(self,item):
    self.player2.set_time(self.trechostemp2[item.text()])

  def volume(self):

    self.player2.audio_set_volume(self.verticalSlider.value())

  def pla(self):
    self.mediaListPlayer.pause()

  def sto(self):
    self.player2.stop()
    self.play.setEnabled(False)
    self.stop.setEnabled(False)
    self.lista_trecho.setVisible(0)
    self.trechos3.setVisible(0)
    self.play.setChecked(False)
    self.mudarTrack.setEnabled(False)
    self.mudarTrack.setChecked(False)
    self.mudarTrack.setVisible(0)
    self.reproduzindo.setText('Nada')

  def mudarT(self,status):
    self.player2.audio_set_track(status)
##    print(self.player2.audio_get_track_count())

  def adicione(self):
    self.mediaList.add_media(self.player.media_new(self.nome))
    self.lista_musicas.addItem(self.nometrec2)
    self.adicionar.setVisible(0)
    self.lista_musicas.setVisible(1)

  def itemAtivado(self,item):
    self.ativado = True
    self.ativadosel = item
    self.items = int(self.lista_musicas.row(self.ativadosel))

  def coletanea(self,item):

    self.dicitemp = {}
    self.conteudoAlbum.clear()

    sql = ("""
          SELECT NOME, linkmusica, linkicone,linktrecho,album FROM teste
          WHERE album LIKE '%{}%' order by nome
            """.format(item.text()))

    self.cursor.execute(sql)
    for x in self.cursor.fetchall():
      item1 = str(x[0])
      self.conteudoAlbum.addItem(item1)
      self.dicitemp[str(x[0])] = str(x[1]),str(x[2]),str(x[3]),str(x[4])

  def reproduzir(self,item):

    Media = self.player.media_new(self.dicitemp[item.text()][0])
    self.player2.set_media(Media)
    self.player2.play()
    self.notifica(item,self.dicitemp[item.text()][1],item.text())

  def reproduzir2(self,item):


    itemtrat = item.text()
    item2 = itemtrat.split(' - ')
    Media = self.player.media_new(self.dicitempesq[item2[0]][0])
    self.player2.set_media(Media)
    self.player2.play()
    self.notifica(item,self.dicitempesq[item2[0]][1],item.text())

  def context(self,position):

    if self.ativado == True:
      menu = QtWidgets.QMenu(self)
      menu.addAction('Remover')
      escolha =  menu.exec_(self.lista_musicas.mapToGlobal(position))

      if str(type(escolha)) == "<class 'PyQt5.QtWidgets.QAction'>":
        if escolha.text() == 'Remover':
          self.removerList()

  def removerList(self):

    item = self.items
    self.lista_musicas.takeItem(item)
    self.mediaList.remove_index(item)
    if self.mediaList.count() == 0:
      self.lista_musicas.setVisible(0)

  def context3(self,position):

    if self.ativado == True:
        menu = QtWidgets.QMenu(self)
        menu.addAction('Adicionar a play List')
        escolha =  menu.exec_(self.listadevalores.mapToGlobal(position))
        item3 = self.ativadosel.text()
        item4 = item3.split(' - ')

        if str(type(escolha)) == "<class 'PyQt5.QtWidgets.QAction'>":

          self.lista_musicas.setVisible(1)

          if escolha.text() == 'Adicionar a play List':
            print('ate aquuiii')

            self.mediaList.add_media(self.player.media_new(self.dicitempesq[item4[0]][0]))
            item = self.ativadosel.text()
            self.lista_musicas.addItem(item)

    self.ativado = False


  def context2(self,position):

      if self.ativado == True:
        menu = QtWidgets.QMenu(self)
        menu.addAction('Adicionar a play List')
        menu.addAction('Adicionar Tudo a play List')
        escolha =  menu.exec_(self.conteudoAlbum.mapToGlobal(position))

        if str(type(escolha)) == "<class 'PyQt5.QtWidgets.QAction'>":

          self.lista_musicas.setVisible(1)

          if escolha.text() == 'Adicionar a play List':

            self.mediaList.add_media(self.player.media_new(self.dicitemp[self.ativadosel.text()][0]))
            item = self.ativadosel.text()+ ' - ' +self.dicitemp[self.ativadosel.text()][3]
            self.lista_musicas.addItem(item)

          if escolha.text() ==  'Adicionar Tudo a play List':
            for element in self.dicitemp:

              self.mediaList.add_media(self.player.media_new(self.dicitemp[element][0]))
              item2 = element+ ' - ' +self.dicitemp[element][3]
              self.lista_musicas.addItem(item2)

      self.ativado = False

  @pyqtSlot()
  def on_pushButton_6_clicked(self):
    print('funcionou')

  @pyqtSlot("bool")
  def on_play_clicked(self):
    self.pla()

  @pyqtSlot("bool")
  def on_mudarTrack_clicked(self,status):
    if status == True:
        self.mudarT(2)
    if status == False:
        self.mudarT(1)

  @pyqtSlot("bool")
  def on_stop_clicked(self):
    self.sto()

  @pyqtSlot()
  def on_adicionar_clicked(self):
    self.adicione()


  @pyqtSlot("bool")
  def on_toolButton_2_clicked(self, status):

    self.nomet =( QFileDialog.getOpenFileName(None, 'Open file','.','all (*);;Imagem (*.jpeg);;Audio (*.wav)(*.mp3);; Video (*.mp4 *.avi)'))

    if self.nomet[0]!= '':
      self.nome = self.nomet[0]
      self.adicionar.setEnabled(1)
      self.nometrec = self.nome.split('/')
      self.nometrec2 = self.nometrec[-1]
      self.label_2.setText(self.nometrec2)
      self.adicionar.setVisible(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = primeiro()
    ui.show()
    sys.exit(app.exec_())








