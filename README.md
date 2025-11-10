# HypercontentCrudQt — Python Ready-to-Run

Versi **PyQt5 + SQLite** yang sudah disiapkan: tinggal jalankan `RUN.bat` (Windows) atau `./run.sh` (Linux/macOS).
Database sudah terisi data yang sama dengan MySQL Anda (file: `db/app.db`).

## Jalankan di Windows (paling mudah)
1. Ekstrak ZIP
2. Double-click **RUN.bat**
   - Script akan memasang PyQt5 (jika belum ada) lalu membuka aplikasi.

## Jalankan manual (opsional)
```bash
pip install -r requirements.txt
python main.py
```

## Struktur
- `ui/mainwindow.ui` — file UI
- `main.py` — logic CRUD GUI
- `db.py` — koneksi & migrasi database (SEED dimatikan)
- `db/app.db` — database SQLite siap pakai (sinkron dgn MySQL Anda)
- `RUN.bat`, `run.sh` — script cepat untuk menjalankan

## Catatan
- Jika ingin mengganti database dengan versi terbaru, cukup timpa `db/app.db` dengan file SQLite lain (nama tetap `app.db`).
- SEED otomatis dimatikan agar data Anda tidak terisi ulang.
