# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moviedata.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo,webbrowser
import requests
from PyQt5.QtGui import QIcon, QPixmap
from tmdbv3api import TMDb
from tmdbv3api import Movie


class Ui_moviedataWindow(object):
    def setupUi(self, Moviedata,movie_title):
        Moviedata.setObjectName("Moviedata")
        #Moviedata.resize(742, 740)
        Moviedata.resize(742, 750)
        self.centralwidget = QtWidgets.QWidget(Moviedata)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(280, 20, 131, 41))
        self.label_title.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_title.setObjectName("label_title")

        self.movie_name = QtWidgets.QLabel(self.centralwidget)
        self.movie_name.setGeometry(QtCore.QRect(410, 20, 331, 50))
        self.movie_name.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.movie_name.setObjectName("movie_name")
        self.movie_name.setWordWrap(True)

        self.label_score = QtWidgets.QLabel(self.centralwidget)
        self.label_score.setGeometry(QtCore.QRect(280, 220, 71, 41))
        self.label_score.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_score.setObjectName("label_score")

        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(410, 220, 71, 41))
        self.score.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.score.setObjectName("score")

        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(500, 220, 71, 41))
        self.label_date.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_date.setObjectName("label_date")
        self.label_date.setText("วันที่ฉาย")

        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(590, 220, 121, 41))
        self.date.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.date.setObjectName("date")

        self.label_director = QtWidgets.QLabel(self.centralwidget)
        self.label_director.setGeometry(QtCore.QRect(280, 100, 111, 41))
        self.label_director.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_director.setObjectName("label_director")

        self.director_name = QtWidgets.QLabel(self.centralwidget)
        self.director_name.setGeometry(QtCore.QRect(410, 100, 331, 41))
        self.director_name.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.director_name.setObjectName("director_name")
        self.director_name.setWordWrap(True)


        self.tableReview = QtWidgets.QTableWidget(self.centralwidget)
        self.tableReview.setGeometry(QtCore.QRect(30, 520, 670, 201))
        self.tableReview.setObjectName("tableReview")
        self.tableReview.setColumnCount(3)
        self.tableReview.setRowCount(0)
        self.tableReview.setHorizontalHeaderLabels(["User","Comment","Score"])

        # size_table
        header = self.tableReview.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
        header.resizeSection(0, 200)#sizecolumn_user
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # disable_edit_table
        self.tableReview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.tableReview.verticalHeader().setVisible(True)
        self.tableReview.horizontalHeader().setVisible(True)
        #update_realtime
        self.tableReview.setUpdatesEnabled(True)

        #reviewtxt
        self.label_review = QtWidgets.QLabel(self.centralwidget)
        self.label_review.setGeometry(QtCore.QRect(30, 475, 181, 41))
        self.label_review.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_review.setObjectName("label_review")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 475, 151, 41))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickreview)

        #refresh table
        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(510, 475, 40, 41))
        self.Refresh.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.Refresh.setObjectName("Refresh")
        self.Refresh.setIcon(QtGui.QIcon('./image/Refresh.png'))
        self.Refresh.setStyleSheet("QToolTip {font-size:9pt;color:white; "
                                   "padding:2px;border-width:2px;"
                                   "border-style:solid;border-radius:20px;"
                                   "background-color: black;"
                                   "border: 1px solid white;"
                                   "overflow:hidden;}");
        self.Refresh.setToolTip("Refresh Table")
        self.Refresh.clicked.connect(self.refreshtable)

        self.label_detail = QtWidgets.QLabel(self.centralwidget)
        self.label_detail.setGeometry(QtCore.QRect(280, 270, 71, 41))
        self.label_detail.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_detail.setObjectName("label_detail")

        self.type_movie = QtWidgets.QLabel(self.centralwidget)
        self.type_movie.setGeometry(QtCore.QRect(410, 160, 331, 41))
        self.type_movie.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.type_movie.setObjectName("type_movie")
        self.type_movie.setWordWrap(True)

        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(280, 160, 121, 41))
        self.label_type.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_type.setObjectName("label_type")

        self.movie_detail = QtWidgets.QLabel(self.centralwidget)
        #self.movie_detail.setGeometry(QtCore.QRect(360, 280, 351, 151))
        self.movie_detail.setGeometry(QtCore.QRect(280, 310, 450, 150))
        self.movie_detail.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.movie_detail.setObjectName("movie_detail")
        self.movie_detail.setWordWrap(True)

        #poster
        self.poster = QtWidgets.QLabel(self.centralwidget)
        self.poster.setGeometry(QtCore.QRect(20, 40, 211, 281))
        self.poster.setObjectName("poster")


        self.trailerButton = QtWidgets.QPushButton(self.centralwidget)
        self.trailerButton.setGeometry(QtCore.QRect(20, 340, 201, 51))
        self.trailerButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.trailerButton.setObjectName("trailerButton")
        self.trailerButton.clicked.connect(self.checkyoutube)

        Moviedata.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Moviedata)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        Moviedata.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Moviedata)
        self.statusbar.setObjectName("statusbar")
        Moviedata.setStatusBar(self.statusbar)

        self.retranslateUi(Moviedata)
        QtCore.QMetaObject.connectSlotsByName(Moviedata)

        #setting page
        self.data_from_search(movie_title)
        self.add_poster(movie_title)
        self.show_reviewtable(movie_title)
        #color
        Moviedata.setWindowIcon(QtGui.QIcon('./image/icon.png'))

    #select form movie_title
    def data_from_search(self,movie_title):
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        cursor = db.myMovies.find({"original_title":movie_title})

        for e in cursor:
            self.movie_name.setText(e['original_title'])
            if e['director'] == "":
                self.director_name.setText("-")
            else:
                self.director_name.setText(e['director'])

            if e['genres'] == "":
                self.type_movie.setText("-")
            else:
                self.type_movie.setText(e['genres'])

            if e['vote_average'] == "":
                self.score.setText("-")
            else:
                self.score.setText(str(e['vote_average']))

            if e['overview'] == "":
                self.movie_detail.setText("-")
            else:
                self.movie_detail.setText(e['overview'])

            if e['release_date'] == "":
                self.date.setText("-")
            else:
                self.date.setText(e['release_date'])

    def retranslateUi(self, Moviedata):
        _translate = QtCore.QCoreApplication.translate
        Moviedata.setWindowTitle(_translate("Moviedata", "Movies Data"))
        self.label_title.setText(_translate("Moviedata", "ชื่อภาพยนตร์"))
        self.label_score.setText(_translate("Moviedata", "คะแนน"))
        self.label_director.setText(_translate("Moviedata", "ชื่อผู้กำกับ"))
        self.label_review.setText(_translate("Moviedata", "Review จากผู้ชม"))
        self.pushButton.setText(_translate("Moviedata", "เพิ่ม Review"))
        self.label_detail.setText(_translate("Moviedata", "เรื่องย่อ"))
        self.label_type.setText(_translate("Moviedata", "ประเภทหนัง"))
        self.trailerButton.setText(_translate("Moviedata", "ชมตัวอย่างภาพยนตร์"))

    def add_poster(self,movie_title):
        tmdb = TMDb()
        tmdb.api_key = '1437062848d1dda19bd3907cf120e9f4'
        tmdb.language = 'en'
        movie = Movie()
        m = movie.search(movie_title)
        for i in m:
            continue_path = i.poster_path
            if continue_path != "None":
                continue_path = i.poster_path
                #print(continue_path)
                break

        url = 'http://image.tmdb.org/t/p/w185'
        combine = url+continue_path
        #readlink
        href = combine
        r = requests.get(href, stream=True)

        pixmap = QPixmap()
        pixmap.loadFromData(r.content)

        self.poster.setPixmap(pixmap)
        self.poster.setScaledContents(True)#fullsizepic

    def refreshtable(self):
        movie_title = self.movie_name.text()
        self.show_reviewtable(movie_title)

    def show_reviewtable(self,movie_title):
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        cursor = db.review.find({"original_title": movie_title})
        countrow = cursor.count()

        self.tableReview.setRowCount(countrow)
        i = 0
        for e in cursor:
            self.tableReview.setItem(i, 0, QtWidgets.QTableWidgetItem(e['nickname']))
            self.tableReview.setItem(i, 1, QtWidgets.QTableWidgetItem(e['comment']))
            self.tableReview.setItem(i, 2, QtWidgets.QTableWidgetItem("{0:.1f}".format(e['score'])))
            i = i + 1

    def checkyoutube(self):
        movie_title = self.movie_name.text()
        self.event_youtube(movie_title)

    def event_youtube(self,movie_title):
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        cursor = db.trailer.find({"original_title": movie_title})
        countrow = cursor.count()

        if countrow != 0:
            for e in cursor:
                title = e['original_title']
                link = e['linkyoutube']
            if movie_title == title:
                headlink = "http://www.youtube.com/watch?v="
                combinelink = headlink+link
                webbrowser.open(combinelink)
        else:
            headlink = "http://www.youtube.com/results?search_query=" + movie_title +" trailer"
            webbrowser.open(headlink)

    def clickreview(self):
        movie_title = self.movie_name.text()
        self.open_insert_reviewtable(movie_title)

    def open_insert_reviewtable(self,movie_title):
        from review import Ui_Reviewform as ui_review
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_review()
        self.ui.setupUi(self.window, movie_title)
        self.window.show()
        #Moviedata.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Moviedata = QtWidgets.QMainWindow()
    ui = Ui_moviedataWindow()
    ui.setupUi(Moviedata)
    Moviedata.show()
    sys.exit(app.exec_())

