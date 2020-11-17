# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 591)
        MainWindow.setStyleSheet("background-color:#DCDCDC;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        #search
        self.pushButton.setGeometry(QtCore.QRect(215, 230, 171, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";background-color:#F8F8FF;")
        self.pushButton.clicked.connect(self.open_search)

        #register
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(215, 300, 171, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";background-color:#F8F8FF;")
        self.pushButton_2.clicked.connect(self.open_register)


        # random
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(215, 370, 171, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";background-color:#F8F8FF;")
        self.pushButton_3.clicked.connect(self.open_random)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 60, 151, 51))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 71, 51))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #color
        MainWindow.setWindowIcon(QtGui.QIcon('./image/icon.png'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ข้อมูลภาพยนตร์"))
        self.pushButton_2.setText(_translate("MainWindow", "สมัครสมาชิก"))
        self.pushButton_3.setText(_translate("MainWindow", "สุ่มแนะนำภาพยนตร์"))
        self.label.setText(_translate("MainWindow", "Movies"))
        self.label_2.setText(_translate("MainWindow", "Menu"))

    def open_search(self):
        from search_movie import Ui_SearchWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def open_register(self):
        from register import Ui_Register
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        self.window.show()


    def open_random(self):
        from random_movie import Ui_RandomMovies
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RandomMovies()
        self.ui.setupUi(self.window)
        self.window.show()

        #MainWindow.close()#close main




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

