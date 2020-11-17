# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(612, 589)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 450, 151, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.regisEvent)

        type_text = QtCore.QRegExp("[a-zA-Z0-9_]*")
        tText = QtGui.QRegExpValidator(type_text)

        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(30, 100, 111, 51))
        self.label_id.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_id.setObjectName("label_id")

        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(30, 160, 111, 51))
        self.label_pass.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_pass.setObjectName("label_pass")

        self.label_passcon = QtWidgets.QLabel(self.centralwidget)
        self.label_passcon.setGeometry(QtCore.QRect(30, 220, 181, 51))
        self.label_passcon.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_passcon.setObjectName("label_passcon")

        self.label_nick = QtWidgets.QLabel(self.centralwidget)
        self.label_nick.setGeometry(QtCore.QRect(30, 340, 101, 51))
        self.label_nick.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_nick.setObjectName("label_nick")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 131, 41))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.textEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_id.setGeometry(QtCore.QRect(240, 100, 361, 41))
        self.textEdit_id.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textEdit_id.setObjectName("textEdit_id")
        self.textEdit_id.setPlaceholderText("กรอก ID")
        self.textEdit_id.setValidator(tText)


        self.textEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_pass.setGeometry(QtCore.QRect(240, 160, 361, 41))
        self.textEdit_pass.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textEdit_pass.setObjectName("textEdit_pass")
        self.textEdit_pass.setPlaceholderText("กรอก Password")
        self.textEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit_pass.setValidator(tText)

        self.textEdit_passcon = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_passcon.setGeometry(QtCore.QRect(240, 220, 361, 41))
        self.textEdit_passcon.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textEdit_passcon.setObjectName("textEdit_passcon")
        self.textEdit_passcon.setPlaceholderText("กรอก Password อีกครั้ง")
        self.textEdit_passcon.setValidator(tText)
        self.textEdit_passcon.setEchoMode(QtWidgets.QLineEdit.Password)

        self.textEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_email.setGeometry(QtCore.QRect(240, 280, 181, 41))
        self.textEdit_email.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textEdit_email.setObjectName("textEdit_email")
        self.textEdit_email.setPlaceholderText("กรอก E-mail")
        self.textEdit_email.setValidator(tText)

        self.combo_email = QtWidgets.QComboBox(self.centralwidget)
        self.combo_email.setGeometry(QtCore.QRect(430, 280, 170, 41))
        self.combo_email.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.combo_email.setObjectName("combo_email")
        self.combo_email.addItem("@hotmail.com")
        self.combo_email.addItem("@gmail.com")

        self.textEdit_nick = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_nick.setGeometry(QtCore.QRect(240, 340, 361, 41))
        self.textEdit_nick.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textEdit_nick.setObjectName("textEdit_nick")
        self.textEdit_nick.setPlaceholderText("กรอกชื่อที่ใช้แสดงเมื่อทำการรีวิว")

        self.label_nick_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick_2.setGeometry(QtCore.QRect(30, 280, 101, 51))
        self.label_nick_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_nick_2.setObjectName("label_nick_2")

        Register.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Register)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        Register.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        #color
        Register.setWindowIcon(QtGui.QIcon('./image/icon.png'))
        Register.setWindowTitle("Register")


    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.pushButton.setText(_translate("Register", "สมัครสมาชิก"))
        self.label_id.setText(_translate("Register", "ID"))
        self.label_pass.setText(_translate("Register", "Password"))
        self.label_passcon.setText(_translate("Register", "Password Confirm"))
        self.label_nick.setText(_translate("Register", "Nickname"))
        self.label.setText(_translate("Register", "Register"))
        self.label_nick_2.setText(_translate("Register", "E-mail"))

    def regisEvent(self):
        id = self.textEdit_id.text().strip()
        password = self.textEdit_pass.text().strip()
        passcon = self.textEdit_passcon.text().strip()
        email = self.textEdit_email.text().strip()+self.combo_email.currentText().strip()
        nick = self.textEdit_nick.text().strip()

        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")

        cursor = db.users.find({"id":id})
        count = cursor.count()

        if id=="" or password=="" or passcon=="" or email=="" or nick=="":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("{0}".format("กรุณากรอกข้อมูลให้ครบ"))
            msg.setWindowTitle("Check Register")
            msg.exec_()
        else:
            if count == 0:
                if password == passcon:
                    userdata = {"id": id, "password": password, "email": email,"nickname": nick}
                    db.users.insert_one(userdata)
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("{0}".format("สมัครสมาชิกสำเร็จ"))
                    msg.setWindowTitle("Wellcome")
                    msg.exec_()

                    self.textEdit_id.setText("")
                    self.textEdit_pass.setText("")
                    self.textEdit_passcon.setText("")
                    self.textEdit_email.setText("")
                    self.combo_email.setCurrentIndex(0)
                    self.textEdit_nick.setText("")
                    #Register.close()#ปิดwindowregis
                    #Register.destroy()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("{0}".format("กรอก Password ไม่ตรงกัน"))
                    msg.setWindowTitle("Check Password")
                    msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("{0}".format("ID นี้มีในระบบแล้ว กรุณาใช้ ID อื่น"))
                msg.setWindowTitle("Check ID")
                msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

