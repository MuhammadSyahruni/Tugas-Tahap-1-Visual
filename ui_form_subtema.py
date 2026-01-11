# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_subtema.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Sub_Tema(object):
    def setupUi(self, Sub_Tema):
        if not Sub_Tema.objectName():
            Sub_Tema.setObjectName(u"Sub_Tema")
        Sub_Tema.resize(400, 377)
        self.inputNamaSub = QLineEdit(Sub_Tema)
        self.inputNamaSub.setObjectName(u"inputNamaSub")
        self.inputNamaSub.setGeometry(QRect(70, 10, 121, 24))
        self.inputDeskripsi = QTextEdit(Sub_Tema)
        self.inputDeskripsi.setObjectName(u"inputDeskripsi")
        self.inputDeskripsi.setGeometry(QRect(70, 40, 121, 41))
        self.spinUrutan = QSpinBox(Sub_Tema)
        self.spinUrutan.setObjectName(u"spinUrutan")
        self.spinUrutan.setGeometry(QRect(70, 90, 121, 21))
        self.inputCari = QLineEdit(Sub_Tema)
        self.inputCari.setObjectName(u"inputCari")
        self.inputCari.setGeometry(QRect(260, 50, 113, 24))
        self.btnSimpan = QPushButton(Sub_Tema)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(50, 140, 80, 24))
        self.btnHapus = QPushButton(Sub_Tema)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(280, 140, 80, 24))
        self.btnBatal = QPushButton(Sub_Tema)
        self.btnBatal.setObjectName(u"btnBatal")
        self.btnBatal.setGeometry(QRect(170, 140, 80, 24))
        self.tableWidget = QTableWidget(Sub_Tema)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 180, 381, 181))
        self.label = QLabel(Sub_Tema)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 21))
        self.label_2 = QLabel(Sub_Tema)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 49, 21))
        self.label_3 = QLabel(Sub_Tema)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 51, 21))
        self.label_4 = QLabel(Sub_Tema)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 50, 31, 21))

        self.retranslateUi(Sub_Tema)

        QMetaObject.connectSlotsByName(Sub_Tema)
    # setupUi

    def retranslateUi(self, Sub_Tema):
        Sub_Tema.setWindowTitle(QCoreApplication.translate("Sub_Tema", u"FormSubTema", None))
        self.btnSimpan.setText(QCoreApplication.translate("Sub_Tema", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("Sub_Tema", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Sub_Tema", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Sub_Tema", u"NamaSub", None))
        self.label_2.setText(QCoreApplication.translate("Sub_Tema", u"Deskripsi", None))
        self.label_3.setText(QCoreApplication.translate("Sub_Tema", u"No Urut", None))
        self.label_4.setText(QCoreApplication.translate("Sub_Tema", u"Cari", None))
    # retranslateUi

