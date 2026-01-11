# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_materi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_Materi_Pembelajaran(object):
    def setupUi(self, Materi_Pembelajaran):
        if not Materi_Pembelajaran.objectName():
            Materi_Pembelajaran.setObjectName(u"Materi_Pembelajaran")
        Materi_Pembelajaran.resize(400, 403)
        self.comboSub = QComboBox(Materi_Pembelajaran)
        self.comboSub.setObjectName(u"comboSub")
        self.comboSub.setGeometry(QRect(90, 10, 111, 24))
        self.inputJudul = QLineEdit(Materi_Pembelajaran)
        self.inputJudul.setObjectName(u"inputJudul")
        self.inputJudul.setGeometry(QRect(90, 40, 111, 24))
        self.inputIsi = QTextEdit(Materi_Pembelajaran)
        self.inputIsi.setObjectName(u"inputIsi")
        self.inputIsi.setGeometry(QRect(90, 70, 111, 41))
        self.spinHalaman = QSpinBox(Materi_Pembelajaran)
        self.spinHalaman.setObjectName(u"spinHalaman")
        self.spinHalaman.setGeometry(QRect(90, 120, 111, 25))
        self.inputCari = QLineEdit(Materi_Pembelajaran)
        self.inputCari.setObjectName(u"inputCari")
        self.inputCari.setGeometry(QRect(270, 80, 113, 24))
        self.btnSimpan = QPushButton(Materi_Pembelajaran)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(50, 190, 80, 24))
        self.btnHapus = QPushButton(Materi_Pembelajaran)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 190, 80, 24))
        self.btnBatal = QPushButton(Materi_Pembelajaran)
        self.btnBatal.setObjectName(u"btnBatal")
        self.btnBatal.setGeometry(QRect(280, 190, 80, 24))
        self.tableWidget = QTableWidget(Materi_Pembelajaran)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 230, 381, 161))
        self.label = QLabel(Materi_Pembelajaran)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 21))
        self.label_2 = QLabel(Materi_Pembelajaran)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 71, 21))
        self.label_3 = QLabel(Materi_Pembelajaran)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 71, 21))
        self.label_4 = QLabel(Materi_Pembelajaran)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 49, 21))
        self.label_5 = QLabel(Materi_Pembelajaran)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 80, 31, 21))

        self.retranslateUi(Materi_Pembelajaran)

        QMetaObject.connectSlotsByName(Materi_Pembelajaran)
    # setupUi

    def retranslateUi(self, Materi_Pembelajaran):
        Materi_Pembelajaran.setWindowTitle(QCoreApplication.translate("Materi_Pembelajaran", u"FormMateri", None))
        self.btnSimpan.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Relasi Data", None))
        self.label_2.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Judul Materi", None))
        self.label_3.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Input Konten", None))
        self.label_4.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Navigasi", None))
        self.label_5.setText(QCoreApplication.translate("Materi_Pembelajaran", u"Cari", None))
    # retranslateUi

