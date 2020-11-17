# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_movie.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo , time
import sys

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(718, 695)
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(270, 20, 211, 41))
        self.label_main.setObjectName("label_main")
        self.label_main.setText("<html><head/><body><p><span style=\" font-size:24pt;\">Search Movies</span></p></body></html>")

        self.label_main_add = QtWidgets.QLabel(self.centralwidget)
        self.label_main_add.setGeometry(QtCore.QRect(270, 20, 211, 41))
        self.label_main_add.setObjectName("label_main_add")
        self.label_main_add.setText("<html><head/><body><p><span style=\" font-size:24pt;\">Add Movies</span></p></body></html>")
        self.label_main_add.hide()

        self.textEdit = QtWidgets.QTextEdit(SearchWindow)
        self.textEdit.setGeometry(QtCore.QRect(300, 140, 251, 41))
        self.textEdit.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("กรอกชื่อภาพยนตร์")
        # print(self.textEdit.toPlainText())

        self.comboDirecters = QtWidgets.QComboBox(SearchWindow)
        self.comboDirecters.setGeometry(QtCore.QRect(300, 140, 251, 41))
        self.comboDirecters.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.comboDirecters.setObjectName("comboDirecters")
        self.insertdirectersname()  # insert_directersname
        self.comboDirecters.hide()

        self.DoubleSpinBox = QtWidgets.QDoubleSpinBox(SearchWindow)
        self.DoubleSpinBox.setGeometry(QtCore.QRect(300, 140, 251, 41))
        self.DoubleSpinBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.DoubleSpinBox.setObjectName("DoubleSpinBox")
        self.DoubleSpinBox.setMinimum(0)
        self.DoubleSpinBox.setMaximum(10)
        self.DoubleSpinBox.setDecimals(1)
        self.DoubleSpinBox.setSingleStep(0.1)
        self.DoubleSpinBox.setValue(0)
        self.DoubleSpinBox.hide()

        self.comboBox_score = QtWidgets.QComboBox(SearchWindow)
        self.comboBox_score.setGeometry(QtCore.QRect(60, 190, 120, 41))
        self.comboBox_score.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.comboBox_score.setObjectName("comboBox_score")
        self.comboBox_score.addItem("เท่ากับ")
        self.comboBox_score.addItem("มากกว่า")
        self.comboBox_score.addItem("น้อยกว่า")
        self.comboBox_score.hide()

        self.comboBox_option_search = QtWidgets.QComboBox(SearchWindow)
        self.comboBox_option_search.setGeometry(QtCore.QRect(60, 190, 120, 41))
        self.comboBox_option_search.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.comboBox_option_search.setObjectName("comboBox_option_search")
        self.comboBox_option_search.addItem("ขึ้นต้นด้วย")
        self.comboBox_option_search.addItem("ลงท้ายด้วย")
        self.comboBox_option_search.addItem("มีคำว่า")
        self.comboBox_option_search.show()

        self.textnewMovie = QtWidgets.QTextEdit(SearchWindow)
        self.textnewMovie.setGeometry(QtCore.QRect(300, 140, 251, 41))
        self.textnewMovie.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.textnewMovie.setObjectName("textnewMovie")
        self.textnewMovie.setPlaceholderText("กรอกชื่อภาพยนตร์ที่หาไม่พบ")
        self.textnewMovie.hide()


        self.pushButton = QtWidgets.QPushButton(SearchWindow)
        self.pushButton.setGeometry(QtCore.QRect(570, 140, 91, 41))
        self.pushButton.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)

        self.comboBox = QtWidgets.QComboBox(SearchWindow)
        self.comboBox.setGeometry(QtCore.QRect(60, 140, 221, 41))
        self.comboBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("ชื่อภาพยนตร์")
        self.comboBox.addItem("ชื่อผู้กำกับ")
        self.comboBox.addItem("คะแนน")
        self.comboBox.addItem("เพิ่มภาพยนตร์ลงระบบ")

        # active when change combobox
        self.comboBox.currentIndexChanged.connect(self.eventcombobox)

        self.tableWidget = QtWidgets.QTableWidget(SearchWindow)
        self.tableWidget.setGeometry(QtCore.QRect(60, 240, 591, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Movies Name"])

        # size_table
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # disable_edit_table
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setVisible(True)

        # click_table
        self.tableWidget.clicked.connect(self.on_click)

        #addmovie
        self.tableAddmovie = QtWidgets.QTableWidget(SearchWindow)
        self.tableAddmovie.setGeometry(QtCore.QRect(60, 240, 591, 361))
        self.tableAddmovie.setObjectName("tableAddmovie")
        self.tableAddmovie.setColumnCount(1)
        self.tableAddmovie.setRowCount(0)
        self.tableAddmovie.setHorizontalHeaderLabels(["Movies Name"])
        # size_table
        header = self.tableAddmovie.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # disable_edit_table
        self.tableAddmovie.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAddmovie.verticalHeader().setVisible(True)
        self.tableAddmovie.horizontalHeader().setVisible(True)
        # click_table
        self.tableAddmovie.hide()
        self.tableAddmovie.clicked.connect(self.addnewmovie)

        SearchWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

        #set color
        SearchWindow.setWindowIcon(QtGui.QIcon('./image/icon.png'))


    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "SearchWindow"))
        self.pushButton.setText(_translate("SearchWindow", "ค้นหา"))
        self.comboBox.setItemText(0, _translate("SearchWindow", "ชื่อภาพยนตร์"))

    def eventcombobox(self):
        if self.comboBox.currentText()=="ชื่อภาพยนตร์":
            self.textEdit.show()
            self.comboBox_option_search.show()
            self.tableWidget.show()
            self.label_main.show()
            ##show/hide##
            self.comboDirecters.hide()
            self.DoubleSpinBox.hide()
            self.comboBox_score.hide()
            self.textnewMovie.hide()
            self.tableAddmovie.hide()
            self.label_main_add.hide()
        elif self.comboBox.currentText()=="ชื่อผู้กำกับ":
            self.comboDirecters.show()
            self.tableWidget.show()
            self.label_main.show()
            ##show/hide##
            self.comboBox_option_search.hide()
            self.textEdit.hide()
            self.DoubleSpinBox.hide()
            self.comboBox_score.hide()
            self.textnewMovie.hide()
            self.tableAddmovie.hide()
            self.label_main_add.hide()
        elif self.comboBox.currentText()=="คะแนน":
            self.DoubleSpinBox.show()
            self.tableWidget.show()
            self.comboBox_score.show()
            self.label_main.show()
            ##show/hide##
            self.comboBox_option_search.hide()
            self.textEdit.hide()
            self.comboDirecters.hide()
            self.textnewMovie.hide()
            self.tableAddmovie.hide()
            self.label_main_add.hide()
        elif self.comboBox.currentText()=="เพิ่มภาพยนตร์ลงระบบ":
            self.textnewMovie.show()
            self.tableAddmovie.show()
            self.label_main_add.show()
            ##show/hide##
            self.comboBox_option_search.hide()
            self.tableWidget.hide()
            self.DoubleSpinBox.hide()
            self.comboBox_score.hide()
            self.textEdit.hide()
            self.comboDirecters.hide()
            self.label_main.hide()



    #add_directername to combobox
    def insertdirectersname(self):
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        cursor = sorted(db.myMovies.find({"director": {"$ne": ""}}).distinct("director"))

        self.comboDirecters.addItem("กรุณาเลือกชื่อผู้กำกับ")
        for e in cursor:
            self.comboDirecters.addItem(e)

    def search(self):
        if self.comboBox.currentText()=="ชื่อภาพยนตร์":
            inputdata = self.textEdit.toPlainText()
            self.select_titlemovies(inputdata)
        elif self.comboBox.currentText()=="ชื่อผู้กำกับ":
            inputdata = self.comboDirecters.currentText()
            self.select_titlemovies(inputdata)
        elif self.comboBox.currentText()=="คะแนน":
            inputdata = self.DoubleSpinBox.value()
            self.select_titlemovies(inputdata)
        elif self.comboBox.currentText()=="เพิ่มภาพยนตร์ลงระบบ":
            inputdata = self.textnewMovie.toPlainText()
            self.show_addmovie(inputdata)

    def show_addmovie(self,inputdata):
        from tmdbv3api import TMDb, Movie
        tmdb = TMDb()
        tmdb.api_key = '1437062848d1dda19bd3907cf120e9f4'
        tmdb.language = 'en'

        if inputdata =="":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("{0}".format("กรุณากรอกข้อมูล"))
            msg.setWindowTitle("Messages")
            msg.exec_()
        else:
            movie = Movie()
            search = movie.search(inputdata)
            countrow = len(search)
            self.tableAddmovie.setRowCount(countrow)
            i = 0
            for res in search:
                movie_title = res.title
                self.tableAddmovie.setItem(i, 0, QtWidgets.QTableWidgetItem(movie_title))
                i = i + 1



    def addnewmovie(self):
        from tmdbv3api import TMDb, Movie
        tmdb = TMDb()
        tmdb.api_key = '1437062848d1dda19bd3907cf120e9f4'
        tmdb.language = 'en'
        #tmdb.debug = True

        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")

        for currentQTableWidgetItem in self.tableAddmovie.selectedItems():
            userselect = currentQTableWidgetItem.text()

        movie = Movie()
        search = movie.search(userselect)

        for res in search:
            title = res.title
            movieid = res.id
            break
        print(title,movieid)


        if title == userselect:
            searchM = movie.details(movieid)
            overview = searchM.overview
            score = searchM.vote_average
            date = searchM.release_date
            datecut = date.split("-")
            release_date = datecut[1] + "/" + datecut[2] + "/" + datecut[0]


            cursorall = db.myMovies.find_one(sort=[("ID", pymongo.DESCENDING)])
            currentID = int(cursorall["ID"]) + 1

            datadic = {"ID": currentID, "original_title": userselect, "cast": "",
                           "director": "", "overview": overview,"runtime": "", "genres": "",
                           "release_date": release_date, "release_year": datecut[0],
                           "homepage": "", "vote_average": (float(score))}

            cursorid = db.myMovies.find({"ID": currentID})
            cursortitle = db.myMovies.find({"original_title":userselect})
            countid = cursorid.count()
            counttitle = cursortitle.count()
            print(countid,counttitle)


            if countid == 0 and counttitle==0:
                time.sleep(1)
                db.myMovies.insert_one(datadic)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("เพิ่มข้อมูลเรื่อง {0} สำเร็จ".format(userselect))
                msg.setWindowTitle("Messages")
                msg.exec_()
                time.sleep(1)

            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("มีข้อมูลนี้ในระบบแล้ว")
                msg.setWindowTitle("Messages")
                msg.exec_()


    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            movie_title = currentQTableWidgetItem.text()
        self.open_moviedatawindow(movie_title)

    def select_titlemovies(self,inputdata):
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        if self.comboBox.currentText() == "ชื่อภาพยนตร์":
            if self.comboBox_option_search.currentText() == "ขึ้นต้นด้วย":
                sort = {"$regex": "^" + inputdata.lstrip(), "$options": "i"}
            elif self.comboBox_option_search.currentText() == "ลงท้ายด้วย":
                sort = {"$regex": inputdata.strip()+"$", "$options": "i"}
            elif self.comboBox_option_search.currentText() == "มีคำว่า":
                sort = {"$regex": inputdata.strip(), "$options": "im"}

            cursor = sorted(db.myMovies.find({"original_title": sort}).distinct("original_title"))


        elif self.comboBox.currentText() == "ชื่อผู้กำกับ":
            cursor = sorted(db.myMovies.find({"director": inputdata}).distinct("original_title"))


        elif self.comboBox.currentText() == "คะแนน":
            if self.comboBox_score.currentText()=="มากกว่า":
                sortby = {"$gt": int(inputdata)}
            elif self.comboBox_score.currentText()=="น้อยกว่า":
                sortby = {"$lt": int(inputdata)}
            else:
                sortby = int(inputdata)
            cursor = sorted(db.myMovies.find({"vote_average": sortby}).distinct("original_title"))

        #countrow
        countrow = len(cursor)

        if inputdata ==""or inputdata=="กรุณาเลือกชื่อผู้กำกับ":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("{0}".format("กรุณากรอกข้อมูล"))
            msg.setWindowTitle("Messages")
            msg.exec_()
        elif countrow == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("{0}".format("ไม่พบข้อมูล"))
            msg.setWindowTitle("Messages")
            msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("พบข้อมูลจำนวน {0} ข้อมูล".format(countrow))
            msg.setWindowTitle("Messages")
            msg.exec_()
            self.tableWidget.setRowCount(countrow)
            i = 0
            for e in cursor:
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(e))
                i = i + 1

    def open_moviedatawindow(self,movie_title):
        from moviedata import Ui_moviedataWindow as ui_moviedata
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_moviedata()
        self.ui.setupUi(self.window,movie_title)
        time.sleep(0.5)  # delay time
        self.window.show()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())
