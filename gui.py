from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QFileDialog
import sys
from PyQt5.QtCore import Qt
from tools import copy_save,replace_latest_save
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 441)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.main = QtWidgets.QFrame(Form)
        self.main.setGeometry(QtCore.QRect(0, 0, 351, 441))
        self.main.setStyleSheet("QFrame#main{\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 10px;\n"
"}")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.drag = QtWidgets.QFrame(self.main)
        self.drag.setGeometry(QtCore.QRect(0, 0, 351, 51))
        self.drag.setStyleSheet("QFrame#drag {\n"
"background:transparent;\n"
"border-radius:10px;\n"
"}")
        self.drag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drag.setObjectName("drag")
        self.label = QtWidgets.QLabel(self.drag)
        self.label.setGeometry(QtCore.QRect(60, 0, 231, 51))
        self.label.setStyleSheet("QLabel{\n"
"font: 75 20pt \"Reem Kufi\";\n"
"color:rgb(11, 148, 198);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.close = QtWidgets.QPushButton(self.drag)
        self.close.setGeometry(QtCore.QRect(325, 10, 20, 20))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("QPushButton#close{\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#close:hover {\n"
"background-color:rgb(107,107,107);\n"
"}")
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setObjectName("close")
        self.close.clicked.connect(self.Close)
        self.backup = QtWidgets.QPushButton(self.main)
        self.backup.setGeometry(QtCore.QRect(30, 80, 291, 41))
        self.backup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backup.setStyleSheet("QPushButton#backup{\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius:10px;\n"
"border: 2px solid rgb(107, 107, 107);\n"
"    font: 75 12pt \"Reem Kufi\";\n"
"color:rgb(11, 148, 198);\n"
"}\n"
"QPushButton#backup:hover {\n"
"background-color:rgb(107,107,107);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/refresh-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backup.setIcon(icon1)
        self.backup.setIconSize(QtCore.QSize(16, 16))
        self.backup.setObjectName("backup")
        self.backup.clicked.connect(self.backUp)
        self.replace = QtWidgets.QPushButton(self.main)
        self.replace.setGeometry(QtCore.QRect(30, 140, 291, 41))
        self.replace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.replace.setStyleSheet("QPushButton#replace{\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius:10px;\n"
"border: 2px solid rgb(107, 107, 107);\n"
"    font: 75 12pt \"Reem Kufi\";\n"
"color:rgb(11, 148, 198);;\n"
"\n"
"}\n"
"QPushButton#replace:hover {\n"
"background-color: rgb(107, 107, 107);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.replace.setIcon(icon2)
        self.replace.setObjectName("replace")
        self.replace.clicked.connect(self.Replace)
        self.label_2 = QtWidgets.QLabel(self.main)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 281, 51))
        self.label_2.setStyleSheet("QLabel{\n"
"font: 75 20pt \"Reem Kufi\";\n"
"color:rgb(11, 148, 198);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.github = QtWidgets.QPushButton(self.main)
        self.github.setGeometry(QtCore.QRect(30, 310, 291, 71))
        self.github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.github.setStyleSheet("QPushButton#github{\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius:10px;\n"
"border: 2px solid rgb(107, 107, 107);\n"
"    font: 75 20pt \"Reem Kufi\";\n"
"color:rgb(11, 148, 198);;\n"
"\n"
"}\n"
"QPushButton#github:hover {\n"
"background-color: rgb(107, 107, 107);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.github.setIcon(icon3)
        self.github.setIconSize(QtCore.QSize(32, 32))
        self.github.setObjectName("github")
        self.label_3 = QtWidgets.QLabel(self.main)
        self.label_3.setGeometry(QtCore.QRect(250, 400, 101, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"font: 75 12pt \"Reem Kufi\";\n"
"color:rgb(11, 148, 198);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.drag.mouseMoveEvent = self.mouseMoveEvent1
        self.drag.mousePressEvent = self.mousePressEvent1

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def backUp(self):
        if os.path.exists('./backups') is not True:
            os.mkdir('backups')
            copy_save()
        else:
            copy_save()

    def Replace(self):
        file_path = QFileDialog.getOpenFileName(Form, "Select a old Save!", "", "All Files (*);;Text Files (*.txt)")
        if file_path != None:
            replace_latest_save(file_path[0])

    def Close(self):
        Form.close()

    def mousePressEvent1(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()

    def mouseMoveEvent1(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            delta = event.globalPos() - self.clickPosition
            Form.move(Form.pos() + delta)
            self.clickPosition = event.globalPos()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "FH5 Save Changer"))
        self.backup.setText(_translate("Form", "Backup Latest Save"))
        self.replace.setText(_translate("Form", "Replace Save"))
        self.label_2.setText(_translate("Form", "Credits"))
        self.github.setText(_translate("Form", "Clarifey"))
        self.label_3.setText(_translate("Form", "Version 1.0"))

app = QtWidgets.QApplication(sys.argv)
Form = QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec())