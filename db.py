import os, sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "app.db")
SEED_ON_START = False  # ubah ke True jika ingin isi awal otomatis (sekali run)

SCHEMA_SQL = """
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  class TEXT NOT NULL,
  guardian TEXT
);
CREATE TABLE IF NOT EXISTS subthemes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  description TEXT
);
CREATE TABLE IF NOT EXISTS resources (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  type TEXT CHECK(type IN ('video','audio','image','document','link')) NOT NULL DEFAULT 'link',
  url TEXT NOT NULL,
  subtheme_id INTEGER NOT NULL,
  qrcode_path TEXT,
  FOREIGN KEY(subtheme_id) REFERENCES subthemes(id) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

def connect():
    os.makedirs(os.path.join(os.path.dirname(__file__), "db"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn

def migrate(conn):
    conn.executescript(SCHEMA_SQL)
    conn.commit()

def seed(conn):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM subthemes")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO subthemes(name,description) VALUES(?,?)", [
            ("Lingkungan Tempat Tinggalku", "Observasi lingkungan sekitar rumah dan sekolah"),
            ("Keunikan Daerah Tempat Tinggalku", "Cerita rakyat, legenda, budaya daerah"),
            ("Bangga Terhadap Daerah Tempat Tinggalku", "Refleksi identitas dan potensi daerah"),
        ])
    c.execute("SELECT COUNT(*) FROM students")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO students(name,class,guardian) VALUES(?,?,?)", [
            ("Alya Putri","IV-A","Ibu Sari"),
            ("Bima Pratama","IV-B","Bapak Rudi"),
        ])
    conn.commit()
