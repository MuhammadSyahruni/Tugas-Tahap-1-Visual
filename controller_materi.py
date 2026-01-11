import os
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MateriController(QDialog):
    def __init__(self, db_connection):
        super().__init__()
        self.db = db_connection
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # Load UI
        loader = QUiLoader()
        ui_file = QFile(os.path.join(self.base_dir, "form_materi.ui"))
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.selected_id = None

        # Koneksi Tombol
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.tableWidget.itemClicked.connect(self.pilih_data)

        # Jalankan fungsi pengisian data
        self.setup_table()
        self.isi_combobox() # Mengisi pilihan Sub-Tema
        self.load_data()    # Menampilkan data ke tabel

    def setup_table(self):
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Sub-Tema", "Judul", "Isi", "Hal"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def isi_combobox(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT id, nama_sub_tema FROM sub_tema")
        self.ui.comboSub.clear()
        for row in cursor.fetchall():
            self.ui.comboSub.addItem(f"{row[0]} - {row[1]}")

    def load_data(self):
        """PENTING: Menarik data dari MySQL agar muncul di Tabel UI"""
        try:
            cursor = self.db.cursor()
            # JOIN digunakan agar muncul Nama Sub-Tema, bukan ID angkanya saja
            sql = """SELECT m.id, s.nama_sub_tema, m.judul, m.isi_materi, m.halaman
                     FROM materi m
                     JOIN sub_tema s ON m.id_subtema = s.id"""
            cursor.execute(sql)
            rows = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for r_idx, row in enumerate(rows):
                self.ui.tableWidget.insertRow(r_idx)
                for c_idx, val in enumerate(row):
                    self.ui.tableWidget.setItem(r_idx, c_idx, QTableWidgetItem(str(val)))
        except Exception as e:
            print(f"Gagal memuat materi: {e}")

    def simpan(self):
        cursor = self.db.cursor()
        id_sub = self.ui.comboSub.currentText().split(" - ")[0]
        judul = self.ui.inputJudul.text()
        isi = self.ui.inputIsi.toPlainText()
        hal = self.ui.spinHalaman.value()

        if self.selected_id is None:
            sql = "INSERT INTO materi (id_subtema, judul, isi_materi, halaman) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_sub, judul, isi, hal))
        else:
            sql = "UPDATE materi SET id_subtema=%s, judul=%s, isi_materi=%s, halaman=%s WHERE id=%s"
            cursor.execute(sql, (id_sub, judul, isi, hal, self.selected_id))

        self.db.commit()
        self.load_data() # Refresh tabel setelah simpan
        self.selected_id = None
        self.ui.btnSimpan.setText("Simpan")

    def pilih_data(self, item):
        row = item.row()
        self.selected_id = self.ui.tableWidget.item(row, 0).text()
        self.ui.inputJudul.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.btnSimpan.setText("Update")
