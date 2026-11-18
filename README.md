# MazeBot EduKit — Learning Portal & Modul Ajar (SD, SMP, SMA/SMK)

Platform media pembelajaran robotika **MazeBot EduKit (ESP32)** bergaya **Neo-Brutalist**, mencakup **48 Modul Ajar & LKS PDF (`M-01` s/d `M-16` untuk SD, SMP, dan SMA/SMK)**, pembaca kurikulum interaktif, kode program **Arduino C++ (.ino)** siap unduh, **Simulator 2D MazeBot**, serta **Kalkulator Reduksi Rute Jalan Buntu (*Dead-End Elimination*)**.

---

## Cara Langsung Menjalankan di PC Lain atau Server

Proyek ini dirancang **Zero-Dependency** (tidak membutuhkan instalasi *database* atau *library* berat) sehingga dapat langsung dijalankan di komputer atau server mana pun.

### 1. Clone Repository
```bash
git clone https://github.com/CakUrang-dev/mazebot-edukit-modul-ajar.git
cd mazebot-edukit-modul-ajar
```

### 2. Menjalankan di PC Windows (1-Klik)
- Klik dua kali file **`start_windows.bat`**, **ATAU**
- Jalankan melalui terminal:
  ```powershell
  python server.py
  ```
- Browser akan otomatis terbuka di **`http://localhost:8080`** (dan dapat diakses oleh perangkat lain di jaringan Wi-Fi/LAN yang sama).
- *Mode Tanpa Server (Offline Langsung)*: Anda juga dapat langsung klik dua kali file **`index.html`** di Windows Explorer.

### 3. Menjalankan di Linux / macOS / Server VPS
```bash
chmod +x start_linux_mac.sh
./start_linux_mac.sh
```
Atau menggunakan Python secara langsung di port tertentu (misal port `8080`):
```bash
python3 server.py --port 8080 --no-browser
```

### 4. Menjalankan Menggunakan Docker (Server Production)
```bash
docker compose up -d --build
```
Aplikasi langsung aktif di port `8080` (`http://IP-SERVER:8080`).

### 5. Menjalankan Menggunakan Node.js
```bash
npm start
```

---

## Struktur Kurikulum & Dokumen PDF

1. **Buku Gabungan Lengkap**:
   - `Modul_Ajar_MazeBot_SD.pdf` — Tingkat SD (Kelas 4–6: *Visual Block & Web D-Pad*)
   - `Modul_Ajar_MazeBot_SMP.pdf` — Tingkat SMP (Kelas 8–9: *Arduino C++, IPA Fisika Bunyi, & Left-Hand Rule*)
   - `Modul_Ajar_MazeBot_SMA_SMK.pdf` — Tingkat SMA/SMK (Kelas X–XII: *Starter API, Closed-Loop Wall, Array & Shortest Path*)
2. **48 File PDF Terpisah Sesuai Kode Modul (`M-01` s/d `M-16`)**:
   - Tersedia di dalam direktori `Modul_PDF_Per_Kode/SD/`, `Modul_PDF_Per_Kode/SMP/`, dan `Modul_PDF_Per_Kode/SMA_SMK/`.

---

## Mengompilasi Ulang Data Web atau PDF (Opsional)

Jika Anda mengubah isi materi di `generate_sd.py`, `generate_smp.py`, atau `generate_sma.py`:
```bash
# Perbarui bundle data website (web/modules_data.js):
python build_website.py

# Kompilasi ulang seluruh 51 file PDF (membutuhkan paket playwright):
pip install -r requirements.txt
playwright install chromium
python build_all_pdfs.py
```
