# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(500, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWin.sizePolicy().hasHeightForWidth())
        MainWin.setSizePolicy(sizePolicy)
        MainWin.setMinimumSize(QtCore.QSize(500, 280))
        MainWin.setMaximumSize(QtCore.QSize(500, 280))
        self.pushButton_openfile = QtWidgets.QPushButton(MainWin)
        self.pushButton_openfile.setGeometry(QtCore.QRect(420, 100, 75, 31))
        self.pushButton_openfile.setObjectName("pushButton_openfile")
        self.label = QtWidgets.QLabel(MainWin)
        self.label.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(MainWin)
        self.lineEdit.setGeometry(QtCore.QRect(10, 100, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_startcreat = QtWidgets.QPushButton(MainWin)
        self.pushButton_startcreat.setGeometry(QtCore.QRect(180, 210, 151, 51))
        self.pushButton_startcreat.setObjectName("pushButton_startcreat")
        self.lineEdit_authorName = QtWidgets.QLineEdit(MainWin)
        self.lineEdit_authorName.setGeometry(QtCore.QRect(10, 40, 141, 31))
        self.lineEdit_authorName.setObjectName("lineEdit_authorName")
        self.label_author = QtWidgets.QLabel(MainWin)
        self.label_author.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_author.setObjectName("label_author")
        self.lineEdit_codesave_path = QtWidgets.QLineEdit(MainWin)
        self.lineEdit_codesave_path.setGeometry(QtCore.QRect(10, 160, 401, 31))
        self.lineEdit_codesave_path.setObjectName("lineEdit_codesave_path")
        self.pushButton_filesave = QtWidgets.QPushButton(MainWin)
        self.pushButton_filesave.setGeometry(QtCore.QRect(420, 160, 75, 31))
        self.pushButton_filesave.setObjectName("pushButton_filesave")
        self.label_2 = QtWidgets.QLabel(MainWin)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "Rte代码生成工具"))
        self.pushButton_openfile.setToolTip(_translate("MainWin", "选择要打开的配置文件"))
        self.pushButton_openfile.setText(_translate("MainWin", "打开文件"))
        self.label.setText(_translate("MainWin", "配置文件路径"))
        self.pushButton_startcreat.setText(_translate("MainWin", "生成代码"))
        self.label_author.setText(_translate("MainWin", "输入作者:"))
        self.pushButton_filesave.setToolTip(_translate("MainWin", "默认为程序所在路径"))
        self.pushButton_filesave.setText(_translate("MainWin", "更改路径"))
        self.label_2.setText(_translate("MainWin", "生成代码路径"))
