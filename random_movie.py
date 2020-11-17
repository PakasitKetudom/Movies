# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'random.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_RandomMovies(object):
    def setupUi(self, RandomMovies):
        RandomMovies.setObjectName("RandomMovies")
        RandomMovies.resize(611, 592)
        self.centralwidget = QtWidgets.QWidget(RandomMovies)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, -10, 131, 71))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.poster = QtWidgets.QLabel(self.centralwidget)
        self.poster.setGeometry(QtCore.QRect(200, 50, 211, 261))
        self.poster.setObjectName("poster")
        self.poster.hide()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 131, 41))
        self.label_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_3.hide()

        self.movie_title = QtWidgets.QLabel(self.centralwidget)
        self.movie_title.setGeometry(QtCore.QRect(180, 410, 391, 41))
        self.movie_title.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.movie_title.setText("")
        self.movie_title.setObjectName("movie_title")
        #self.movie_title.setDisabled(True)
        self.movie_title.hide()

        self.Button_random = QtWidgets.QPushButton(self.centralwidget)
        self.Button_random.setGeometry(QtCore.QRect(230, 320, 151, 51))
        self.Button_random.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.Button_random.setObjectName("Button_random")
        self.Button_random.clicked.connect(self.random_id)

        self.Button_detail = QtWidgets.QPushButton(self.centralwidget)
        self.Button_detail.setGeometry(QtCore.QRect(30, 490, 551, 51))
        self.Button_detail.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.Button_detail.setObjectName("Button_detail")
        self.Button_detail.setText("ดูรายละเอียดภาพยนตร์")
        self.Button_detail.clicked.connect(self.event_button)
        self.Button_detail.hide()


        RandomMovies.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RandomMovies)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 21))
        self.menubar.setObjectName("menubar")
        RandomMovies.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RandomMovies)
        self.statusbar.setObjectName("statusbar")
        RandomMovies.setStatusBar(self.statusbar)

        self.retranslateUi(RandomMovies)
        QtCore.QMetaObject.connectSlotsByName(RandomMovies)

        #color
        RandomMovies.setWindowIcon(QtGui.QIcon('./image/icon.png'))


    def retranslateUi(self, RandomMovies):
        _translate = QtCore.QCoreApplication.translate
        RandomMovies.setWindowTitle(_translate("RandomMovies", "RandomMovies"))
        self.label.setText(_translate("RandomMovies", "Random"))
        self.label_3.setText(_translate("RandomMovies", "ชื่อภาพยนตร์"))
        self.Button_random.setText(_translate("RandomMovies", "คลิกเพื่อสุ่ม"))

    def random_id(self):
        import random
        import pymongo
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("movies")
        countid = len(db.myMovies.distinct('ID'))
        ran = random.randint(1, countid)
        cursor = db.myMovies.find({"ID": ran})
        for e in cursor:
            movie_title = e['original_title']
        #setting_newpage
        time.sleep(1)
        self.add_poster(movie_title)
        self.movie_title.setText(movie_title)
        self.movie_title.show()
        self.Button_detail.show()
        self.label_3.show()



    def add_poster(self,movie_title):
        import requests
        from PyQt5.QtGui import QIcon, QPixmap
        from tmdbv3api import TMDb
        from tmdbv3api import Movie
        tmdb = TMDb()
        tmdb.api_key = '1437062848d1dda19bd3907cf120e9f4'
        tmdb.language = 'en'
        #tmdb.debug = True
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
        self.poster.show()

    #button_detail
    def event_button(self):
        movie_title = self.movie_title.text()
        self.open_moviedatawindow(movie_title)


    def open_moviedatawindow(self,movie_title):
        from moviedata import Ui_moviedataWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_moviedataWindow()
        self.ui.setupUi(self.window,movie_title)
        self.window.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RandomMovies = QtWidgets.QMainWindow()
    ui = Ui_RandomMovies()
    ui.setupUi(RandomMovies)
    RandomMovies.show()
    sys.exit(app.exec_())
