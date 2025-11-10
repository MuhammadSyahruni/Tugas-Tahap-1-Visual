BEGIN TRANSACTION;
CREATE TABLE resources (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      type TEXT CHECK(type IN ('video','audio','image','document','link')) NOT NULL DEFAULT 'link',
      url TEXT NOT NULL,
      subtheme_id INTEGER NOT NULL,
      qrcode_path TEXT,
      FOREIGN KEY(subtheme_id) REFERENCES subthemes(id) ON DELETE CASCADE ON UPDATE CASCADE
    );
CREATE TABLE students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      class TEXT NOT NULL,
      guardian TEXT
    );
INSERT INTO "students" VALUES(1,'Muhammad Syahruni','5A','Ramli');
CREATE TABLE subthemes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      description TEXT
    );
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('students',1);
COMMIT;
