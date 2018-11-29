#!/usr/bin/env python3
#coding: utf8
from PyQt5 import QtCore, QtGui, QtWidgets
from img import imagens_rc
from os import system as rodar
import EscreverHTML

class Ui_Ordenar_Elementos(object):
    def setupUi(self, Ordenar_Elementos):
        Ordenar_Elementos.setObjectName("Ordenar_Elementos")
        Ordenar_Elementos.resize(470, 550)
        Ordenar_Elementos.setMinimumSize(QtCore.QSize(470, 550))
        Ordenar_Elementos.setMaximumSize(QtCore.QSize(470, 550))
        self.verticalLayoutWidget = QtWidgets.QWidget(Ordenar_Elementos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 451, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listaElementos = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.listaElementos.setMaximumSize(QtCore.QSize(350, 70))
        self.listaElementos.setObjectName("listaElementos")
        self.horizontalLayout_5.addWidget(self.listaElementos, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox.setObjectName("groupBox")
        self.heapButton = QtWidgets.QRadioButton(self.groupBox)
        self.heapButton.setGeometry(QtCore.QRect(270, 25, 100, 20))
        self.heapButton.setObjectName("heapButton")
        self.shellButton = QtWidgets.QRadioButton(self.groupBox)
        self.shellButton.setGeometry(QtCore.QRect(100, 25, 100, 20))
        self.shellButton.setObjectName("shellButton")
        self.shellButton.setChecked(True)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 64, 91))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(290, 30, 64, 91))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ascButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.ascButton.setGeometry(QtCore.QRect(45, 35, 110, 20))
        self.ascButton.setObjectName("ascButton")
        self.ascButton.setChecked(True)
        self.descButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.descButton.setGeometry(QtCore.QRect(45, 65, 110, 20))
        self.descButton.setObjectName("descButton")
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.sortButton = QtWidgets.QPushButton(Ordenar_Elementos)
        self.sortButton.setGeometry(QtCore.QRect(370, 490, 93, 28))
        self.sortButton.setObjectName("sortButton")

        self.retranslateUi(Ordenar_Elementos)
        QtCore.QMetaObject.connectSlotsByName(Ordenar_Elementos)

        self.sortButton.clicked.connect(self.ordenar)


    def ordenar(self):

        _translate = QtCore.QCoreApplication.translate

        self.texto = self.listaElementos.toPlainText()
        self.alg = {0: "./shellSort", 1: "./heapSort"}
        self.ord = {0: "Ascendente", 1: "Descendente"}

        if (self.shellButton.isChecked() or self.heapButton.isChecked()):

            if self.shellButton.isChecked():
                self.tipoAlg = 0
            else:
                self.tipoAlg = 1


            if (self.ascButton.isChecked() or self.descButton.isChecked()):
                if self.ascButton.isChecked():
                    self.tipoOrd = 0
                else:
                    self.tipoOrd = 1

        if "," in self.texto:
            self.texto = [i.replace(" ", "") for i in self.texto.split(',')]
        else:
            self.texto = self.texto.split(" ")

        self.texto = [int(i) for i in self.texto if i.isdigit()]

        self.args = ""

        for e, i in enumerate(self.texto):
            if e != len(self.texto)-1:
                self.args += str(i)
                self.args += " "
            else:
                self.args += str(i)

        if (self.alg and self.ord and self.texto):
            Ordenar_Elementos.setWindowTitle(_translate("Ordenar_Elementos", "Carregando..."))
            if (rodar("%s -tipo=%s %s" % (self.alg[self.tipoAlg], self.tipoOrd, self.args))) == 0:
                Ordenar_Elementos.setWindowTitle(_translate("Ordenar_Elementos", "Números ordenados"))
                self.label_3.setText(_translate("Ordenar_Elementos", "<html><head/><body><p><span style=\" font-size:20pt;\">%s<br/>%s</span></p></body></html>" % (self.alg[self.tipoAlg], self.ord[self.tipoOrd]) ))

                if self.shellButton.isChecked():
                	EscreverHTML.escreverShell()


    def retranslateUi(self, Ordenar_Elementos):
        _translate = QtCore.QCoreApplication.translate
        Ordenar_Elementos.setWindowTitle(_translate("Ordenar_Elementos", "Ordenar elementos"))
        self.label_3.setText(_translate("Ordenar_Elementos", "<html><head/><body><p><span style=\" font-size:20pt;\">Ordenar Elementos - IC2</span></p></body></html>"))
        self.listaElementos.setPlaceholderText(_translate("Ordenar_Elementos", "10, 3, 25, 7..."))
        self.groupBox.setTitle(_translate("Ordenar_Elementos", "Ordenação"))
        self.heapButton.setText(_translate("Ordenar_Elementos", "Heap Sort"))
        self.shellButton.setText(_translate("Ordenar_Elementos", "Shell Sort"))
        self.label_2.setText(_translate("Ordenar_Elementos", "<html><head/><body><p><img src=\":/sort/shell.png\"/></p></body></html>"))
        self.label.setText(_translate("Ordenar_Elementos", "<html><head/><body><p><img src=\":/sort/heap.png\"/></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Ordenar_Elementos", "Modo"))
        self.ascButton.setText(_translate("Ordenar_Elementos", "Ascendente"))
        self.descButton.setText(_translate("Ordenar_Elementos", "Descendente"))
        self.label_4.setText(_translate("Ordenar_Elementos", "<html><head/><body><p><span style=\" color:#686868;\">Grupo:</span></p><p><span style=\" color:#686868;\">Rafael Biagioni de Fazio</span></p><p><span style=\" color:#686868;\">Victor Girelli</span></p></body></html>"))
        self.sortButton.setText(_translate("Ordenar_Elementos", "Ordenar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    Ordenar_Elementos = QtWidgets.QDialog()
    ui = Ui_Ordenar_Elementos()
    ui.setupUi(Ordenar_Elementos)
    Ordenar_Elementos.show()
    sys.exit(app.exec_())

