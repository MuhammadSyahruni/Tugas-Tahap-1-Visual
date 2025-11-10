import os, sys, sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QTableWidgetItem
import db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "mainwindow.ui"), self)
        self.conn = db.connect()
        db.migrate(self.conn)
        if db.SEED_ON_START:
            db.seed(self.conn)

        # connect buttons
        self.btnAddStudent.clicked.connect(self.add_student)
        self.btnEditStudent.clicked.connect(self.edit_student)
        self.btnDelStudent.clicked.connect(self.del_student)

        self.btnAddSub.clicked.connect(self.add_sub)
        self.btnEditSub.clicked.connect(self.edit_sub)
        self.btnDelSub.clicked.connect(self.del_sub)

        self.btnAddRes.clicked.connect(self.add_res)
        self.btnEditRes.clicked.connect(self.edit_res)
        self.btnDelRes.clicked.connect(self.del_res)

        # load data
        self.refresh_students()
        self.refresh_subthemes()
        self.refresh_resources()

    def selected_id(self, table):
        row = table.currentRow()
        if row < 0: return None
        try:
            return int(table.item(row, 0).text())
        except Exception:
            return None

    def refresh_students(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id,name,class,guardian FROM students ORDER BY id DESC")
        rows = cur.fetchall()
        self.tblStudents.clear()
        self.tblStudents.setColumnCount(4)
        self.tblStudents.setHorizontalHeaderLabels(["id","name","class","guardian"])
        self.tblStudents.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.tblStudents.setItem(r, c, QTableWidgetItem(str(val)))
        self.tblStudents.resizeColumnsToContents()

    def refresh_subthemes(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id,name,description FROM subthemes ORDER BY id ASC")
        rows = cur.fetchall()
        self.tblSubthemes.clear()
        self.tblSubthemes.setColumnCount(3)
        self.tblSubthemes.setHorizontalHeaderLabels(["id","name","description"])
        self.tblSubthemes.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.tblSubthemes.setItem(r, c, QTableWidgetItem(str(val)))
        self.tblSubthemes.resizeColumnsToContents()

    def refresh_resources(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT r.id, r.title, r.type, r.url, r.subtheme_id, s.name as subname, r.qrcode_path
            FROM resources r JOIN subthemes s ON s.id=r.subtheme_id
            ORDER BY r.id DESC
        """)
        rows = cur.fetchall()
        self.tblResources.clear()
        self.tblResources.setColumnCount(7)
        self.tblResources.setHorizontalHeaderLabels(["id","title","type","url","subtheme_id","subtheme_name","qrcode_path"])
        self.tblResources.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.tblResources.setItem(r, c, QTableWidgetItem(str(val)))
        self.tblResources.resizeColumnsToContents()

    # CRUD Students
    def add_student(self):
        name, ok = QInputDialog.getText(self, "Siswa", "Nama:")
        if not ok or not name: return
        kelas, ok = QInputDialog.getText(self, "Siswa", "Kelas:")
        if not ok or not kelas: return
        wali, ok = QInputDialog.getText(self, "Siswa", "Wali:")
        cur = self.conn.cursor()
        cur.execute("INSERT INTO students(name,class,guardian) VALUES(?,?,?)", (name, kelas, wali))
        self.conn.commit()
        self.refresh_students()

    def edit_student(self):
        sid = self.selected_id(self.tblStudents)
        if not sid: return
        cur = self.conn.cursor()
        cur.execute("SELECT name,class,guardian FROM students WHERE id=?", (sid,))
        row = cur.fetchone()
        if not row: return
        name, ok = QInputDialog.getText(self, "Ubah Siswa", "Nama:", text=row[0])
        if not ok or not name: return
        kelas, ok = QInputDialog.getText(self, "Ubah Siswa", "Kelas:", text=row[1])
        if not ok or not kelas: return
        wali, ok = QInputDialog.getText(self, "Ubah Siswa", "Wali:", text=row[2] or "")
        cur.execute("UPDATE students SET name=?, class=?, guardian=? WHERE id=?", (name, kelas, wali, sid))
        self.conn.commit()
        self.refresh_students()

    def del_student(self):
        sid = self.selected_id(self.tblStudents)
        if not sid: return
        if QMessageBox.question(self, "Hapus", "Yakin hapus siswa?") != QMessageBox.Yes: return
        cur = self.conn.cursor()
        cur.execute("DELETE FROM students WHERE id=?", (sid,))
        self.conn.commit()
        self.refresh_students()

    # CRUD Subthemes
    def add_sub(self):
        name, ok = QInputDialog.getText(self, "Subtema", "Nama:")
        if not ok or not name: return
        desc = QInputDialog.getMultiLineText(self, "Subtema", "Deskripsi:")
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO subthemes(name,description) VALUES(?,?)", (name, desc))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            QMessageBox.warning(self, "DB", f"Gagal: {e}")
        self.refresh_subthemes()

    def edit_sub(self):
        sid = self.selected_id(self.tblSubthemes)
        if not sid: return
        cur = self.conn.cursor()
        cur.execute("SELECT name,description FROM subthemes WHERE id=?", (sid,))
        row = cur.fetchone()
        if not row: return
        name, ok = QInputDialog.getText(self, "Ubah Subtema", "Nama:", text=row[0])
        if not ok or not name: return
        desc = QInputDialog.getMultiLineText(self, "Ubah Subtema", "Deskripsi:", text=row[1] or "")
        cur.execute("UPDATE subthemes SET name=?, description=? WHERE id=?", (name, desc, sid))
        self.conn.commit()
        self.refresh_subthemes()
        self.refresh_resources()

    def del_sub(self):
        sid = self.selected_id(self.tblSubthemes)
        if not sid: return
        if QMessageBox.question(self, "Hapus", "Yakin hapus subtema? Resource terkait akan ikut terhapus.") != QMessageBox.Yes: return
        cur = self.conn.cursor()
        cur.execute("DELETE FROM subthemes WHERE id=?", (sid,))
        self.conn.commit()
        self.refresh_subthemes()
        self.refresh_resources()

    # CRUD Resources
    def add_res(self):
        title, ok = QInputDialog.getText(self, "Resource", "Judul:")
        if not ok or not title: return
        url, ok = QInputDialog.getText(self, "Resource", "URL:")
        if not ok or not url: return
        types = ["video","audio","image","document","link"]
        type_, ok = QInputDialog.getItem(self, "Resource", "Jenis:", types, len(types)-1, False)
        if not ok: return

        cur = self.conn.cursor()
        cur.execute("SELECT id,name FROM subthemes ORDER BY id ASC")
        subs = cur.fetchall()
        if not subs:
            QMessageBox.warning(self, "DB", "Subtema belum ada")
            return
        items = [f"{name} (#{sid})" for sid,name in subs]
        picked, ok = QInputDialog.getItem(self, "Resource", "Subtema:", items, 0, False)
        if not ok: return
        sub_id = int(picked.split('#')[-1].rstrip(')'))

        cur.execute("INSERT INTO resources(title,type,url,subtheme_id,qrcode_path) VALUES(?,?,?,?,?)",
                    (title, type_, url, sub_id, ""))
        self.conn.commit()
        self.refresh_resources()

    def edit_res(self):
        rid = self.selected_id(self.tblResources)
        if not rid: return
        cur = self.conn.cursor()
        cur.execute("SELECT title,type,url,subtheme_id FROM resources WHERE id=?", (rid,))
        row = cur.fetchone()
        if not row: return
        title, ok = QInputDialog.getText(self, "Ubah Resource", "Judul:", text=row[0])
        if not ok or not title: return
        url, ok = QInputDialog.getText(self, "Ubah Resource", "URL:", text=row[2])
        if not ok or not url: return
        types = ["video","audio","image","document","link"]
        try_index = types.index(row[1]) if row[1] in types else len(types)-1
        type_, ok = QInputDialog.getItem(self, "Ubah Resource", "Jenis:", types, try_index, False)
        if not ok: return

        cur.execute("UPDATE resources SET title=?, type=?, url=?, subtheme_id=? WHERE id=?",
                    (title, type_, url, row[3], rid))
        self.conn.commit()
        self.refresh_resources()

    def del_res(self):
        rid = self.selected_id(self.tblResources)
        if not rid: return
        if QMessageBox.question(self, "Hapus", "Yakin hapus resource?") != QMessageBox.Yes: return
        cur = self.conn.cursor()
        cur.execute("DELETE FROM resources WHERE id=?", (rid,))
        self.conn.commit()
        self.refresh_resources()

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
