import sys
import os

from PySide6.QtWidgets import (
    QDialog,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
    QFileDialog
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# ===== REPORTLAB (IMPORT LENGKAP & BENAR) =====
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


class ValidasiController(QDialog):
    def __init__(self, db_connection):
        super().__init__()

        # DEBUG interpreter (boleh dihapus kalau sudah yakin)
        print("Python Validasi:", sys.executable)

        self.db = db_connection
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.selected_id = None

        # ===== 1. LOAD UI =====
        loader = QUiLoader()
        ui_path = os.path.join(self.base_dir, "form_validasi.ui")
        ui_file = QFile(ui_path)

        if not ui_file.open(QFile.ReadOnly):
            QMessageBox.critical(self, "Error", "File UI tidak ditemukan!")
            return

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # ===== 2. SETUP AWAL =====
        self.setup_combobox()
        self.setup_table()
        self.load_data()

        # ===== 3. EVENT =====
        self.ui.tableWidget.itemClicked.connect(self.pilih_data)
        self.ui.btnSimpan.clicked.connect(self.proses_simpan_atau_update)
        self.ui.btnBatal.clicked.connect(self.reset_form)

        if hasattr(self.ui, "btnCetak"):
            self.ui.btnCetak.clicked.connect(self.cetak_laporan)

    # ==================================================
    # SETUP COMBOBOX
    # ==================================================
    def setup_combobox(self):
        self.ui.comboBidang.clear()
        self.ui.comboBidang.addItems([
            "Ahli Bahasa",
            "Ahli Materi",
            "Ahli Media",
            "Ahli Desain"
        ])
        self.ui.comboBidang.setCurrentIndex(-1)

    # ==================================================
    # SETUP TABLE
    # ==================================================
    def setup_table(self):
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "ID",
            "Nama Ahli",
            "Bidang",
            "Skor",
            "Saran / Kritik"
        ])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # ==================================================
    # LOAD DATA
    # ==================================================
    def load_data(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id, nama_ahli, bidang, skor, catatan
                FROM validasi_ahli
            """)
            rows = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)

            for row_idx, row in enumerate(rows):
                self.ui.tableWidget.insertRow(row_idx)
                for col_idx, value in enumerate(row):
                    self.ui.tableWidget.setItem(
                        row_idx,
                        col_idx,
                        QTableWidgetItem(str(value))
                    )

        except Exception as e:
            QMessageBox.critical(self.ui, "Error", f"Gagal load data:\n{e}")

    # ==================================================
    # PILIH DATA
    # ==================================================
    def pilih_data(self, item):
        row = item.row()
        self.selected_id = self.ui.tableWidget.item(row, 0).text()

        self.ui.inputAhli.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.comboBidang.setCurrentText(self.ui.tableWidget.item(row, 2).text())
        self.ui.spinSkor.setValue(int(self.ui.tableWidget.item(row, 3).text()))

        saran = self.ui.tableWidget.item(row, 4).text()
        self.ui.textSaran.setPlainText("" if saran == "None" else saran)

        self.ui.btnSimpan.setText("Update")

    # ==================================================
    # SIMPAN / UPDATE
    # ==================================================
    def proses_simpan_atau_update(self):
        nama = self.ui.inputAhli.text().strip()
        bidang = self.ui.comboBidang.currentText()
        skor = self.ui.spinSkor.value()
        saran = self.ui.textSaran.toPlainText()

        if not nama or self.ui.comboBidang.currentIndex() == -1:
            QMessageBox.warning(self.ui, "Peringatan", "Data belum lengkap!")
            return

        try:
            cursor = self.db.cursor()

            if self.ui.btnSimpan.text() == "Update":
                cursor.execute("""
                    UPDATE validasi_ahli
                    SET nama_ahli=%s, bidang=%s, skor=%s, catatan=%s
                    WHERE id=%s
                """, (nama, bidang, skor, saran, self.selected_id))
            else:
                cursor.execute("""
                    INSERT INTO validasi_ahli (nama_ahli, bidang, skor, catatan)
                    VALUES (%s, %s, %s, %s)
                """, (nama, bidang, skor, saran))

            self.db.commit()
            QMessageBox.information(self.ui, "Sukses", "Data berhasil disimpan")
            self.reset_form()
            self.load_data()

        except Exception as e:
            QMessageBox.critical(self.ui, "Error", f"Gagal simpan data:\n{e}")

    # ==================================================
    # RESET FORM
    # ==================================================
    def reset_form(self):
        self.ui.inputAhli.clear()
        self.ui.comboBidang.setCurrentIndex(-1)
        self.ui.spinSkor.setValue(0)
        self.ui.textSaran.clear()
        self.ui.btnSimpan.setText("Simpan")
        self.selected_id = None

    # ==================================================
    # CETAK PDF (FINAL & JUDUL MUNCUL)
    # ==================================================
    def cetak_laporan(self):
        path, _ = QFileDialog.getSaveFileName(
            self.ui,
            "Simpan PDF",
            "Laporan_Validasi.pdf",
            "PDF Files (*.pdf)"
        )

        if not path:
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT nama_ahli, bidang, skor, catatan
                FROM validasi_ahli
            """)
            rows = cursor.fetchall()

            data = [["Nama Ahli", "Bidang", "Skor", "Saran / Kritik"]]
            for r in rows:
                data.append(list(r))

            pdf = SimpleDocTemplate(path, pagesize=A4)

            styles = getSampleStyleSheet()
            judul = Paragraph(
                "<b>LAPORAN VALIDASI AHLI</b>",
                styles["Title"]
            )

            table = Table(data, colWidths=[120, 120, 60, 200])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ALIGN', (2, 1), (2, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))

            pdf.build([
                judul,
                Spacer(1, 20),
                table
            ])

            QMessageBox.information(self.ui, "Sukses", "PDF berhasil dibuat!")

        except Exception as e:
            QMessageBox.critical(self.ui, "Error", f"Gagal cetak PDF:\n{e}")
