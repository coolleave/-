# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\笔记\2024\2.11.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui(object):
    def setupUi(self, ui):
        ui.setObjectName("ui")
        ui.resize(398, 265)
        ui.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4CAF50, stop:1 #45a049);\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #45a049, stop:1 #4CAF50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #379e3b, stop:1 #3d8b3d);\n"
"    border-style: inset;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(ui)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 70, 209, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_sinlge = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sinlge.setObjectName("btn_sinlge")
        self.horizontalLayout.addWidget(self.btn_sinlge)
        self.btn_mult = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_mult.setStyleSheet("")
        self.btn_mult.setObjectName("btn_mult")
        self.horizontalLayout.addWidget(self.btn_mult)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)

    def retranslateUi(self, ui):
        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("ui", "Form"))
        self.btn_sinlge.setText(_translate("ui", "single"))
        self.btn_mult.setText(_translate("ui", "mult"))