import sys, os
import mysql.connector
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# controller
from controller_subtema import SubTemaController
from controller_materi import MateriController
from controller_link import LinkController
from controller_validasi import ValidasiController


class MainApp:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # ===== LOAD UI =====
        loader = QUiLoader()
        ui_file = QFile(os.path.join(self.base_dir, "form.ui"))
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        # ===== DATABASE =====
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_hypercontent"
        )

        # ===== WINDOW CONTROLLER =====
        self.win_sub = None
        self.win_mat = None
        self.win_link = None
        self.win_val = None

        # ===== MENU =====
        self.ui.actionSub_Tema.triggered.connect(self.buka_subtema)
        self.ui.actionMateri.triggered.connect(self.buka_materi)
        self.ui.actionHyperlink.triggered.connect(self.buka_link)
        self.ui.actionValidasi.triggered.connect(self.buka_validasi)
        self.ui.actionCetak_PDF.triggered.connect(self.proses_cetak)

        self.ui.show()

    def buka_subtema(self):
        self.win_sub = SubTemaController(self.db)
        self.win_sub.ui.show()

    def buka_materi(self):
        self.win_mat = MateriController(self.db)
        self.win_mat.ui.show()

    def buka_link(self):
        self.win_link = LinkController(self.db)
        self.win_link.ui.show()

    def buka_validasi(self):
        self.win_val = ValidasiController(self.db)
        self.win_val.ui.show()

    def proses_cetak(self):
        if not self.win_val:
            self.win_val = ValidasiController(self.db)
        self.win_val.cetak_laporan()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec())
