import os
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class LinkController(QDialog):
    def __init__(self, db_connection):
        super().__init__()
        self.db = db_connection
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # Load UI form_link.ui secara aman
        loader = QUiLoader()
        ui_file = QFile(os.path.join(self.base_dir, "form_link.ui"))
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.selected_id = None

        # Koneksi Tombol sesuai Object Name di gambar kamu
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnQR.clicked.connect(self.buat_qr) # Fungsi tambahan untuk QR
        self.ui.tableWidget.itemClicked.connect(self.pilih_data)

        # Inisialisasi
        self.setup_table()
        self.isi_combo_materi()
        self.load_data()

    def setup_table(self):
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Judul Materi", "Label Link", "URL / Link"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def isi_combo_materi(self):
        """Mengambil data dari tabel materi untuk pilihan"""
        cursor = self.db.cursor()
        cursor.execute("SELECT id, judul FROM materi")
        self.ui.comboMateri.clear()
        for row in cursor.fetchall():
            self.ui.comboMateri.addItem(f"{row[0]} - {row[1]}")

    def load_data(self):
        """Menampilkan data link dengan JOIN ke tabel materi"""
        try:
            cursor = self.db.cursor()
            sql = """SELECT h.id, m.judul, h.label_link, h.url_video
                     FROM hyperlink h
                     JOIN materi m ON h.id_materi = m.id"""
            cursor.execute(sql)
            rows = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for r_idx, row in enumerate(rows):
                self.ui.tableWidget.insertRow(r_idx)
                for c_idx, val in enumerate(row):
                    self.ui.tableWidget.setItem(r_idx, c_idx, QTableWidgetItem(str(val)))
        except Exception as e:
            print(f"Error load data link: {e}")

    def simpan(self):
        try:
            cursor = self.db.cursor()
            # Ambil ID Materi dari combo box
            combo_text = self.ui.comboMateri.currentText()
            if not combo_text:
                QMessageBox.warning(self, "Peringatan", "Isi materi dulu!")
                return
            id_materi = combo_text.split(" - ")[0]

            label = self.ui.inputLabel.text()
            url = self.ui.inputUrl.text()

            if self.selected_id is None:
                sql = "INSERT INTO hyperlink (id_materi, label_link, url_video) VALUES (%s, %s, %s)"
                cursor.execute(sql, (id_materi, label, url))
            else:
                sql = "UPDATE hyperlink SET id_materi=%s, label_link=%s, url_video=%s WHERE id=%s"
                cursor.execute(sql, (id_materi, label, url, self.selected_id))

            self.db.commit()
            self.load_data()
            self.reset_form()
            QMessageBox.information(self, "Sukses", "Link berhasil disimpan!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal simpan: {e}")

    def pilih_data(self, item):
        row = item.row()
        self.selected_id = self.ui.tableWidget.item(row, 0).text()
        self.ui.inputLabel.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.inputUrl.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.btnSimpan.setText("Update Link")

    def reset_form(self):
        self.selected_id = None
        self.ui.inputLabel.clear()
        self.ui.inputUrl.clear()
        self.ui.btnSimpan.setText("Simpan")

    def buat_qr(self):
        url = self.ui.inputUrl.text()
        if url:
            QMessageBox.information(self, "QR Generator", f"QR Code untuk {url} akan dibuat.")
            # Di sini kamu bisa tambahkan library qrcode jika ingin benar-benar buat gambar

    def hapus(self):
        if self.selected_id:
            cursor = self.db.cursor()
            cursor.execute("DELETE FROM hyperlink WHERE id=%s", (self.selected_id,))
            self.db.commit()
            self.load_data()
            self.reset_form()
