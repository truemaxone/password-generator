from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 345)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(330, 345))
        MainWindow.setMaximumSize(QtCore.QSize(330, 345))
        MainWindow.setStyleSheet("background-color: rgb(141, 184, 124);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 30, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 70, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(10, 90, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(10, 110, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(10, 130, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.check_box1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box1.setGeometry(QtCore.QRect(290, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.check_box1.setFont(font)
        self.check_box1.setStyleSheet("")
        self.check_box1.setText("")
        self.check_box1.setObjectName("check_box1")
        self.check_box2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box2.setGeometry(QtCore.QRect(290, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.check_box2.setFont(font)
        self.check_box2.setText("")
        self.check_box2.setObjectName("check_box2")
        self.check_box3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box3.setGeometry(QtCore.QRect(290, 90, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.check_box3.setFont(font)
        self.check_box3.setText("")
        self.check_box3.setObjectName("check_box3")
        self.check_box4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box4.setGeometry(QtCore.QRect(290, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.check_box4.setFont(font)
        self.check_box4.setText("")
        self.check_box4.setObjectName("check_box4")
        self.check_box5 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box5.setGeometry(QtCore.QRect(290, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.check_box5.setFont(font)
        self.check_box5.setText("")
        self.check_box5.setObjectName("check_box5")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(10, 150, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.check_box6 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box6.setGeometry(QtCore.QRect(290, 150, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.check_box6.setFont(font)
        self.check_box6.setText("")
        self.check_box6.setObjectName("check_box6")
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(100, 170, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.generate_button.setFont(font)
        self.generate_button.setStyleSheet("background-color: rgb(255, 204, 102);")
        self.generate_button.setObjectName("generate_button")
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(10, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label1_2.setFont(font)
        self.label1_2.setStyleSheet("")
        self.label1_2.setObjectName("label1_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 10, 50, 16))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 30, 50, 16))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.password_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.password_browser.setGeometry(QtCore.QRect(90, 195, 230, 140))
        self.password_browser.setStyleSheet("background-color: rgb(212, 232, 193);")
        self.password_browser.setDocumentTitle("")
        self.password_browser.setPlaceholderText("")
        self.password_browser.setObjectName("password_browser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????? ??????????????"))
        self.label1.setText(_translate("MainWindow", "?????????? ???????????? (???? 1 ???? 25 ????????????????)"))
        self.label2.setText(_translate("MainWindow", "???????????????? ?????????????? (@#$%)"))
        self.label3.setText(_translate("MainWindow", "???????????????? ?????????? (123456789)"))
        self.label4.setText(_translate("MainWindow", "???????????????? ???????????????? ?????????? (abcd)"))
        self.label5.setText(_translate("MainWindow", "???????????????? ?????????????????? ?????????? (ABCD)"))
        self.label6.setText(_translate("MainWindow", "???????????????? ?????????????? ?????????????? (i, l, 1, L, o, 0, O)"))
        self.label7.setText(_translate("MainWindow", "???????????????? ???????? ?????????????? ({ } [ ] ( ) / \\  \' \" ~ , ; : < >)"))
        self.generate_button.setText(_translate("MainWindow", "????????????????????????"))
        self.label8.setText(_translate("MainWindow", "?????? ????????????:"))
        self.label1_2.setText(_translate("MainWindow", "???????????????????? ??????????????"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "25"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
