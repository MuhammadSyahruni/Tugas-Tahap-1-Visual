# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSub_Tema = QAction(MainWindow)
        self.actionSub_Tema.setObjectName(u"actionSub_Tema")
        self.actionMateri = QAction(MainWindow)
        self.actionMateri.setObjectName(u"actionMateri")
        self.actionHyperlink = QAction(MainWindow)
        self.actionHyperlink.setObjectName(u"actionHyperlink")
        self.actionValidasi = QAction(MainWindow)
        self.actionValidasi.setObjectName(u"actionValidasi")
        self.actionCetak_PDF = QAction(MainWindow)
        self.actionCetak_PDF.setObjectName(u"actionCetak_PDF")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuData_Master = QMenu(self.menubar)
        self.menuData_Master.setObjectName(u"menuData_Master")
        self.menuLaporan = QMenu(self.menubar)
        self.menuLaporan.setObjectName(u"menuLaporan")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuData_Master.menuAction())
        self.menubar.addAction(self.menuLaporan.menuAction())
        self.menuData_Master.addAction(self.actionSub_Tema)
        self.menuData_Master.addAction(self.actionMateri)
        self.menuData_Master.addAction(self.actionHyperlink)
        self.menuData_Master.addAction(self.actionValidasi)
        self.menuLaporan.addAction(self.actionCetak_PDF)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSub_Tema.setText(QCoreApplication.translate("MainWindow", u"Sub Tema", None))
        self.actionMateri.setText(QCoreApplication.translate("MainWindow", u"Materi Pembelajaran", None))
        self.actionHyperlink.setText(QCoreApplication.translate("MainWindow", u"Resource Multimedia", None))
        self.actionValidasi.setText(QCoreApplication.translate("MainWindow", u"Validasi Ahli", None))
        self.actionCetak_PDF.setText(QCoreApplication.translate("MainWindow", u"Cetak PDF", None))
        self.menuData_Master.setTitle(QCoreApplication.translate("MainWindow", u"Data Master", None))
        self.menuLaporan.setTitle(QCoreApplication.translate("MainWindow", u"Laporan", None))
    # retranslateUi

