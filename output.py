# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface01.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 572)
        MainWindow.setMinimumSize(QtCore.QSize(771, 310))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1456, 331))
        self.tabWidget.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.iconeMusica = QtWidgets.QLabel(self.tab)
        self.iconeMusica.setGeometry(QtCore.QRect(10, 30, 81, 81))
        self.iconeMusica.setText("")
        self.iconeMusica.setPixmap(QtGui.QPixmap("logoAdv.png"))
        self.iconeMusica.setScaledContents(True)
        self.iconeMusica.setObjectName("iconeMusica")
        self.play = QtWidgets.QPushButton(self.tab)
        self.play.setEnabled(False)
        self.play.setGeometry(QtCore.QRect(110, 30, 101, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("botao-de-play-pause_318-43701.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
        self.play.setCheckable(True)
        self.play.setChecked(False)
        self.play.setObjectName("play")
        self.stop = QtWidgets.QPushButton(self.tab)
        self.stop.setEnabled(False)
        self.stop.setGeometry(QtCore.QRect(110, 60, 101, 23))
        self.stop.setObjectName("stop")
        self.mudarTrack = QtWidgets.QPushButton(self.tab)
        self.mudarTrack.setEnabled(False)
        self.mudarTrack.setGeometry(QtCore.QRect(110, 90, 101, 25))
        self.mudarTrack.setStyleSheet("")
        self.mudarTrack.setIconSize(QtCore.QSize(30, 16))
        self.mudarTrack.setCheckable(True)
        self.mudarTrack.setObjectName("mudarTrack")
        self.verticalSlider = QtWidgets.QSlider(self.tab)
        self.verticalSlider.setGeometry(QtCore.QRect(220, 30, 20, 81))
        self.verticalSlider.setStyleSheet("background-color: rgb(84, 255, 147);")
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setProperty("value", 100)
        self.verticalSlider.setSliderPosition(100)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.reproduzindo = QtWidgets.QLabel(self.tab)
        self.reproduzindo.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.reproduzindo.setStyleSheet("font: 75 italic 12pt \"Sans Serif\";")
        self.reproduzindo.setObjectName("reproduzindo")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 120, 251, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.adicionar = QtWidgets.QToolButton(self.gridLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("botao-de-play_318-40670.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adicionar.setIcon(icon1)
        self.adicionar.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.adicionar.setObjectName("adicionar")
        self.gridLayout.addWidget(self.adicionar, 1, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 1, 2, 1, 1)
        self.lista_musicas = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lista_musicas.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lista_musicas.setAcceptDrops(True)
        self.lista_musicas.setToolTip("")
        self.lista_musicas.setStatusTip("")
        self.lista_musicas.setWhatsThis("")
        self.lista_musicas.setAccessibleName("")
        self.lista_musicas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lista_musicas.setViewMode(QtWidgets.QListView.ListMode)
        self.lista_musicas.setModelColumn(0)
        self.lista_musicas.setUniformItemSizes(True)
        self.lista_musicas.setObjectName("lista_musicas")
        self.gridLayout.addWidget(self.lista_musicas, 2, 0, 1, 4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(260, 0, 501, 291))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.trechos3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.trechos3.setStyleSheet("font: 75 14pt \"Sans Serif\";")
        self.trechos3.setObjectName("trechos3")
        self.verticalLayout_2.addWidget(self.trechos3, 0, QtCore.Qt.AlignHCenter)
        self.lista_trecho = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.lista_trecho.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.lista_trecho.setObjectName("lista_trecho")
        self.verticalLayout_2.addWidget(self.lista_trecho)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setStyleSheet("font: 75 14pt \"Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pesquisa = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.pesquisa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pesquisa.setObjectName("pesquisa")
        self.horizontalLayout.addWidget(self.pesquisa)
        self.botaopesquisa = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.botaopesquisa.setObjectName("botaopesquisa")
        self.horizontalLayout.addWidget(self.botaopesquisa)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nomep = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.nomep.setChecked(True)
        self.nomep.setObjectName("nomep")
        self.horizontalLayout_2.addWidget(self.nomep)
        self.Profissao = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.Profissao.setObjectName("Profissao")
        self.horizontalLayout_2.addWidget(self.Profissao)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listadevalores = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listadevalores.setStyleSheet("font: 75 italic 9pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Sans Serif\";")
        self.listadevalores.setObjectName("listadevalores")
        self.verticalLayout.addWidget(self.listadevalores)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 340, 771, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setStyleSheet("font: 75 12pt \"Sans Serif\";")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pesquisarAlbum = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.pesquisarAlbum.setObjectName("pesquisarAlbum")
        self.horizontalLayout_3.addWidget(self.pesquisarAlbum)
        self.botaoAlbum = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.botaoAlbum.setObjectName("botaoAlbum")
        self.horizontalLayout_3.addWidget(self.botaoAlbum)
        self.imagem = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.imagem.setObjectName("imagem")
        self.horizontalLayout_3.addWidget(self.imagem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.album = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.album.setObjectName("album")
        self.verticalLayout_3.addWidget(self.album)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.conteudoAlbum = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.conteudoAlbum.setObjectName("conteudoAlbum")
        self.horizontalLayout_4.addWidget(self.conteudoAlbum)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.iconeMusica.setBuddy(self.mudarTrack)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sono7"))
        self.play.setText(_translate("MainWindow", "Play - Pause"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.mudarTrack.setText(_translate("MainWindow", "Playback / Trilha"))
        self.reproduzindo.setText(_translate("MainWindow", "Sem Midia"))
        self.label_2.setText(_translate("MainWindow", "Informe a midia externa.."))
        self.adicionar.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.trechos3.setText(_translate("MainWindow", "Trechos"))
        self.label_3.setText(_translate("MainWindow", "Pesquisa"))
        self.botaopesquisa.setText(_translate("MainWindow", "Go"))
        self.nomep.setText(_translate("MainWindow", "Nome ou Album"))
        self.Profissao.setText(_translate("MainWindow", "Trecho"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Midia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Utilidade"))
        self.label.setText(_translate("MainWindow", "Albums"))
        self.botaoAlbum.setText(_translate("MainWindow", "Go"))
        self.imagem.setText(_translate("MainWindow", "Capa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

