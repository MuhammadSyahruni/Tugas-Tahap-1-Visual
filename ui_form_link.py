# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_link.ui'
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
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(400, 300)
        self.comboMateri = QComboBox(dialog)
        self.comboMateri.setObjectName(u"comboMateri")
        self.comboMateri.setGeometry(QRect(110, 10, 65, 24))
        self.inputLabel = QLineEdit(dialog)
        self.inputLabel.setObjectName(u"inputLabel")
        self.inputLabel.setGeometry(QRect(110, 40, 113, 24))
        self.inputUrl = QLineEdit(dialog)
        self.inputUrl.setObjectName(u"inputUrl")
        self.inputUrl.setGeometry(QRect(110, 70, 113, 24))
        self.inputCari = QLineEdit(dialog)
        self.inputCari.setObjectName(u"inputCari")
        self.inputCari.setGeometry(QRect(270, 60, 113, 24))
        self.btnSimpan = QPushButton(dialog)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(20, 120, 80, 24))
        self.btnHapus = QPushButton(dialog)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(150, 120, 80, 24))
        self.btnQR = QPushButton(dialog)
        self.btnQR.setObjectName(u"btnQR")
        self.btnQR.setGeometry(QRect(280, 120, 80, 24))
        self.tableWidget = QTableWidget(dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 160, 341, 121))
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 21))
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 71, 21))
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 71, 21))
        self.label_4 = QLabel(dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 40, 49, 21))

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"FormLink", None))
        self.btnSimpan.setText(QCoreApplication.translate("dialog", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("dialog", u"Hapus", None))
        self.btnQR.setText(QCoreApplication.translate("dialog", u"QR", None))
        self.label.setText(QCoreApplication.translate("dialog", u"Daftar Materi", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"Nama Link", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"Alamat Link", None))
        self.label_4.setText(QCoreApplication.translate("dialog", u"Cari", None))
    # retranslateUi

