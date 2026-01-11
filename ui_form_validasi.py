# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_validasi.ui'
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

class Ui_Validasi_Ahli(object):
    def setupUi(self, Validasi_Ahli):
        if not Validasi_Ahli.objectName():
            Validasi_Ahli.setObjectName(u"Validasi_Ahli")
        Validasi_Ahli.resize(400, 300)
        self.inputAhli = QLineEdit(Validasi_Ahli)
        self.inputAhli.setObjectName(u"inputAhli")
        self.inputAhli.setGeometry(QRect(90, 10, 113, 24))
        self.comboBidang = QComboBox(Validasi_Ahli)
        self.comboBidang.setObjectName(u"comboBidang")
        self.comboBidang.setGeometry(QRect(90, 40, 111, 24))
        self.spinSkor = QSpinBox(Validasi_Ahli)
        self.spinSkor.setObjectName(u"spinSkor")
        self.spinSkor.setGeometry(QRect(90, 70, 111, 25))
        self.textSaran = QTextEdit(Validasi_Ahli)
        self.textSaran.setObjectName(u"textSaran")
        self.textSaran.setGeometry(QRect(230, 40, 161, 101))
        self.btnSimpan = QPushButton(Validasi_Ahli)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 120, 61, 24))
        self.btnHapus = QPushButton(Validasi_Ahli)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(150, 120, 61, 24))
        self.btnBatal = QPushButton(Validasi_Ahli)
        self.btnBatal.setObjectName(u"btnBatal")
        self.btnBatal.setGeometry(QRect(80, 120, 61, 24))
        self.tableWidget = QTableWidget(Validasi_Ahli)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 150, 381, 141))
        self.label = QLabel(Validasi_Ahli)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 49, 21))
        self.label_2 = QLabel(Validasi_Ahli)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 49, 16))
        self.label_3 = QLabel(Validasi_Ahli)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 61, 16))
        self.label_4 = QLabel(Validasi_Ahli)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 10, 81, 21))
        self.btnCetak = QPushButton(Validasi_Ahli)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(10, 90, 61, 24))

        self.retranslateUi(Validasi_Ahli)

        QMetaObject.connectSlotsByName(Validasi_Ahli)
    # setupUi

    def retranslateUi(self, Validasi_Ahli):
        Validasi_Ahli.setWindowTitle(QCoreApplication.translate("Validasi_Ahli", u"FormValidasi", None))
        self.btnSimpan.setText(QCoreApplication.translate("Validasi_Ahli", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("Validasi_Ahli", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Validasi_Ahli", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Validasi_Ahli", u"Penilaian", None))
        self.label_2.setText(QCoreApplication.translate("Validasi_Ahli", u"Bidang", None))
        self.label_3.setText(QCoreApplication.translate("Validasi_Ahli", u"Kuantitatif", None))
        self.label_4.setText(QCoreApplication.translate("Validasi_Ahli", u"Saran/Keritik", None))
        self.btnCetak.setText(QCoreApplication.translate("Validasi_Ahli", u"Cetak", None))
    # retranslateUi

