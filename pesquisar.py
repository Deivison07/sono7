# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testedepesquisa.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(447, 359)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.pesquisa = QtGui.QLineEdit(Frame)
        self.pesquisa.setGeometry(QtCore.QRect(80, 40, 271, 21))
        self.pesquisa.setObjectName(_fromUtf8("pesquisa"))
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(180, 20, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.listadevalores = QtGui.QListWidget(Frame)
        self.listadevalores.setGeometry(QtCore.QRect(75, 100, 281, 221))
        self.listadevalores.setObjectName(_fromUtf8("listadevalores"))
        self.verificar = QtGui.QPushButton(Frame)
        self.verificar.setGeometry(QtCore.QRect(170, 70, 79, 25))
        self.verificar.setObjectName(_fromUtf8("verificar"))
        self.nome = QtGui.QCheckBox(Frame)
        self.nome.setGeometry(QtCore.QRect(60, 330, 121, 20))
        self.nome.setChecked(True)
        self.nome.setObjectName(_fromUtf8("nome"))
        self.Profissao = QtGui.QCheckBox(Frame)
        self.Profissao.setGeometry(QtCore.QRect(210, 330, 85, 20))
        self.Profissao.setObjectName(_fromUtf8("Profissao"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", " Pesquisa", None))
        self.verificar.setText(_translate("Frame", "Verificar", None))
        self.nome.setText(_translate("Frame", "Nome ou Album", None))
        self.Profissao.setText(_translate("Frame", "Trecho", None))

