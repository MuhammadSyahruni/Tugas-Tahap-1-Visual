import os
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# Di dalam file controller_subtema.py
class SubTemaController(QDialog): # <--- Pastikan namanya TEPAT seperti ini
    def __init__(self, db_connection):
        super().__init__()
        # ... isi kodingan lainnya ...
        self.db = db_connection

        # 1. LOAD UI SECARA AMAN
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(self.base_dir, "form_subtema.ui")

        loader = QUiLoader()
        ui_file = QFile(ui_path)
        if not ui_file.exists():
            print(f"File UI tidak ditemukan di: {ui_path}")
            return

        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.selected_id = None

        # 2. PENGATURAN TABEL (Agar Kolom Tidak Hilang)
        self.setup_table_widget()

        # 3. KONEKSI TOMBOL (Sesuai Object Name di Designer kamu)
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBatal.clicked.connect(self.reset_form)
        self.ui.inputCari.textChanged.connect(self.load_data)
        self.ui.tableWidget.itemClicked.connect(self.pilih_data)

        # 4. LOAD DATA PERTAMA KALI
        self.load_data()

    def setup_table_widget(self):
        """Memastikan tabel memiliki kolom yang benar"""
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Nama Sub-Tema", "Deskripsi", "Urutan"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Sembunyikan kolom ID jika ingin tampilan lebih bersih, tapi tetap ada datanya
        # self.ui.tableWidget.setColumnHidden(0, True)

    def load_data(self):
        """Mengambil data dan menampilkannya dengan presisi kolom"""
        try:
            cari = self.ui.inputCari.text()
            cursor = self.db.cursor()

            # Gunakan alias jika perlu, pastikan urutan SELECT sesuai dengan kolom tabel UI
            sql = "SELECT id, nama_sub_tema, deskripsi, urutan FROM sub_tema WHERE nama_sub_tema LIKE %s ORDER BY urutan ASC"
            cursor.execute(sql, (f"%{cari}%",))
            rows = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)

            for r_idx, row in enumerate(rows):
                self.ui.tableWidget.insertRow(r_idx)
                for c_idx, val in enumerate(row):
                    # Pastikan setiap sel diisi, jika None ganti jadi string kosong
                    item_text = str(val) if val is not None else ""
                    item = QTableWidgetItem(item_text)
                    self.ui.tableWidget.setItem(r_idx, c_idx, item)

        except Exception as e:
            print(f"Error saat memuat data: {e}")

    def simpan(self):
        """Logika Simpan & Update yang Sempurna"""
        try:
            cursor = self.db.cursor()
            nama = self.ui.inputNamaSub.text()
            desk = self.ui.inputDeskripsi.toPlainText()
            urut = self.ui.spinUrutan.value()

            if not nama:
                QMessageBox.warning(self, "Validasi", "Nama Sub-Tema wajib diisi!")
                return

            if self.selected_id is None:
                # Mode Tambah
                sql = "INSERT INTO sub_tema (nama_sub_tema, deskripsi, urutan) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nama, desk, urut))
            else:
                # Mode Update
                sql = "UPDATE sub_tema SET nama_sub_tema=%s, deskripsi=%s, urutan=%s WHERE id=%s"
                cursor.execute(sql, (nama, desk, urut, self.selected_id))

            self.db.commit()
            self.load_data() # Refresh Tabel
            self.reset_form() # Reset Input & Tombol
            QMessageBox.information(self, "Berhasil", "Data telah diperbarui di database dan tabel.")

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Gagal menyimpan: {e}")

    def pilih_data(self, item):
        """Mengisi kembali form saat baris tabel diklik"""
        row = item.row()
        try:
            self.selected_id = self.ui.tableWidget.item(row, 0).text()
            self.ui.inputNamaSub.setText(self.ui.tableWidget.item(row, 1).text())
            self.ui.inputDeskripsi.setPlainText(self.ui.tableWidget.item(row, 2).text())
            self.ui.spinUrutan.setValue(int(self.ui.tableWidget.item(row, 3).text()))

            self.ui.btnSimpan.setText("Update Data")
        except AttributeError:
            pass

    def reset_form(self):
        """Membersihkan form ke kondisi awal"""
        self.selected_id = None
        self.ui.inputNamaSub.clear()
        self.ui.inputDeskripsi.clear()
        self.ui.spinUrutan.setValue(0)
        self.ui.btnSimpan.setText("Simpan")

    def hapus(self):
        if self.selected_id:
            confirm = QMessageBox.question(self, "Hapus", "Yakin ingin menghapus data ini?", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                cursor = self.db.cursor()
                cursor.execute("DELETE FROM sub_tema WHERE id=%s", (self.selected_id,))
                self.db.commit()
                self.load_data()
                self.reset_form()
