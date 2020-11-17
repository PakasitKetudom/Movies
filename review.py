# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

class Ui_Reviewform(object):
    def setupUi(self, Reviewform, movie_title):
        Reviewform.setObjectName("Reviewform")
        Reviewform.resize(670, 600)
        self.centralwidget = QtWidgets.QWidget(Reviewform)
        self.centralwidget.setObjectName("centralwidget")

        type_text = QtCore.QRegExp("[a-zA-Z0-9_]*")
        tText = QtGui.QRegExpValidator(type_text)

        self.textId = QtWidgets.QLineEdit(self.centralwidget)
        self.textId.setGeometry(QtCore.QRect(80, 110, 221, 41))
        self.textId.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textId.setObjectName("textId")
        self.textId.setPlaceholderText("กรุณากรอกID")
        self.textId.setValidator(tText)

        self.textPass = QtWidgets.QLineEdit(self.centralwidget)
        self.textPass.setGeometry(QtCore.QRect(420, 110, 221, 41))
        self.textPass.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textPass.setObjectName("textPass")
        self.textPass.setPlaceholderText("กรุณากรอกPassword")
        self.textPass.setValidator(tText)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 270, 121, 31))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(430, 310, 121, 31))
        self.doubleSpinBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setMaximum(10)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setValue(0)

        self.pushButton_regis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_regis.setGeometry(QtCore.QRect(220, 180, 161, 41))
        self.pushButton_regis.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_regis.setObjectName("pushButton_regis")
        self.pushButton_regis.clicked.connect(self.open_register)

        self.label_Id = QtWidgets.QLabel(self.centralwidget)
        self.label_Id.setGeometry(QtCore.QRect(40, 110, 41, 31))
        self.label_Id.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_Id.setObjectName("label_Id")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 321, 31))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.moviename = QtWidgets.QLabel(self.centralwidget)
        self.moviename.setGeometry(QtCore.QRect(30, 310, 350, 50))
        self.moviename.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.moviename.setObjectName("moviename")
        self.moviename.setText(movie_title)
        self.moviename.setWordWrap(True)

        #send to db
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 460, 141, 41))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check_review)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 191, 41))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 141, 31))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")

        self.label_Pass = QtWidgets.QLabel(self.centralwidget)
        self.label_Pass.setGeometry(QtCore.QRect(320, 110, 91, 31))
        self.label_Pass.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_Pass.setObjectName("label_Pass")

        self.textComment = QtWidgets.QTextEdit(self.centralwidget)
        self.textComment.setGeometry(QtCore.QRect(30, 370, 321, 161))
        self.textComment.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textComment.setObjectName("textComment")
        self.textComment.setPlaceholderText("กรอก คําวิจารณ์...")

        Reviewform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Reviewform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        Reviewform.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Reviewform)
        self.statusbar.setObjectName("statusbar")
        Reviewform.setStatusBar(self.statusbar)

        self.retranslateUi(Reviewform)
        QtCore.QMetaObject.connectSlotsByName(Reviewform)

        #color
        Reviewform.setWindowIcon(QtGui.QIcon('./image/icon.png'))


    def retranslateUi(self, Reviewform):
        _translate = QtCore.QCoreApplication.translate
        Reviewform.setWindowTitle(_translate("Reviewform", "Reviews"))
        self.label_3.setText(_translate("Reviewform", "คะแนนที่ให้"))
        self.pushButton_regis.setText(_translate("Reviewform", "สมัครสมาชิก"))
        self.label_Id.setText(_translate("Reviewform", "ID"))
        self.label_2.setText(_translate("Reviewform", "ความรู้สึกที่มีต่อภาพยนตร์ เรื่อง"))
        self.pushButton.setText(_translate("Reviewform", "ส่ง"))
        self.label.setText(_translate("Reviewform", "Review Form"))
        self.label_4.setText(_translate("Reviewform", "ยังไม่เป็นสมาชิก ?"))
        self.label_Pass.setText(_translate("Reviewform", "Password"))

    def open_register(self):
        from register import Ui_Register
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        self.window.show()

    def check_review(self):
        movie_title = self.moviename.text()
        self.event_review(movie_title)

    def event_review(self,movie_title):
        #check login
        id = self.textId.text().strip()
        password = self.textPass.text().strip()

        #review
        comment = self.textComment.toPlainText().strip()
        score = self.doubleSpinBox.value()

        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        cursor = db.users.find({"id": id})
        count = cursor.count()
        for e in cursor:
            nickname = e['nickname']
            passwordcollection = e['password']

        #not check score
        if id=="" or password=="" or comment=="":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("{0}".format("กรุณากรอกข้อมูลให้ครบ"))
            msg.setWindowTitle("Check Review")
            msg.exec_()
        else:
            if count != 0:
                if password == passwordcollection:
                    scoreformat = "{0:.1f}".format(score)
                    userdata = {"original_title":movie_title, "comment": comment, "score": float(scoreformat), "id": id,"nickname": nickname}
                    db.review.insert_one(userdata)

                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("{0}".format("เพิ่มรีวิวสำเร็จ"))
                    msg.setWindowTitle("Success Review")
                    msg.exec_()

                    #self.open_moviedatawindow(movie_title)

                    self.textId.setText("")
                    self.textPass.setText("")
                    self.textComment.setText("")
                    self.doubleSpinBox.setValue(0)


                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("{0}".format("กรอก Password ผิด"))
                    msg.setWindowTitle("Check Password")
                    msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("{0}".format("ไม่มี ID นี้ในระบบ"))
                msg.setWindowTitle("Check ID")
                msg.exec_()

    def open_moviedatawindow(self,movie_title):
        from moviedata import Ui_moviedataWindow as ui_moviedata
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_moviedata()
        self.ui.setupUi(self.window,movie_title)
        self.window.show()

    def go_back(self):
        movie_title = self.moviename.text()
        self.open_moviedatawindow(movie_title)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reviewform = QtWidgets.QMainWindow()
    ui = Ui_Reviewform()
    ui.setupUi(Reviewform)
    Reviewform.show()
    sys.exit(app.exec_())

