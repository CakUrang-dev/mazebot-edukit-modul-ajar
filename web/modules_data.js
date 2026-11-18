window.MAZEBOT_DATA = {
  "SD": {
    "id": "SD",
    "name": "Tingkat SD (Kelas 4–6)",
    "Badge": "TINGKAT SD",
    "tagline": "Petualangan Logika & Pengendali Robot Cilik",
    "platform": "Visual Block Programming (Blockly/Scratch) & Web Dashboard D-Pad",
    "sop": "Modul baterai 18650 berada di holder tertutup baut; pemasangan & pengisian daya 100% dilakukan oleh Guru/Instruktur.",
    "book_pdf": "Modul_Ajar_MazeBot_SD.pdf",
    "color": "#5CE1E6",
    "modules": [
      {
        "code": "M-01",
        "title": "Mengenal Si Robot Pintar MazeBot",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mengidentifikasi 4 bagian utama MazeBot: Otak (ESP32), Mata (Sensor Ultrasonik), Kaki (Roda & Motor DC), dan Sumber Energi (Baterai 18650).",
          "Memahami fungsi dasar setiap bagian robot melalui analogi tubuh manusia.",
          "Menerapkan SOP Keselamatan Kelistrikan: larangan membuka baut penutup baterai 18650 dan prosedur menyalakan saklar daya."
        ],
        "theory": "<p><strong>MazeBot EduKit</strong> adalah robot edukasi pintar yang dirancang untuk membantu kita belajar cara berpikir logis seperti ilmuwan komputer. Sama seperti manusia, robot memiliki bagian-bagian tubuh yang bekerja sama:</p> <table class=\"std-table\"> <thead> <tr><th>Bagian Robot</th><th>Komponen Teknis</th><th>Analogi Tubuh Manusia</th><th>Fungsi Utama</th></tr> </thead> <tbody> <tr><td><strong>Otak Robot</strong></td><td>Mikrokontroler ESP32</td><td>Otak Manusia</td><td>Memproses perintah program dan mengatur kerja seluruh bagian robot.</td></tr> <tr><td><strong>Mata Depan/Samping</strong></td><td>3x Sensor Ultrasonik</td><td>Mata / Telinga Kelelawar</td><td>Mendeteksi jarak dinding atau rintangan di depan, kiri, dan kanan.</td></tr> <tr><td><strong>Mata Bawah</strong></td><td>Sensor Garis TCRT5000</td><td>Mata Pengamat Lantai</td><td>Membedakan warna lantai terang (putih) dan garis finish (hitam).</td></tr> <tr><td><strong>Kaki Penggerak</strong></td><td>2x Motor Gearbox TT & Roda</td><td>Kaki Manusia</td><td>Menggerakkan badan robot maju, mundur, belok kanan, dan belok kiri.</td></tr> <tr><td><strong>Jantung Energi</strong></td><td>Baterai Li-Ion 18650</td><td>Jantung & Makanan</td><td>Menyuplai energi listrik agar otak, mata, dan kaki robot dapat bekerja.</td></tr> </tbody> </table>",
        "safety": "Baterai 18650 tersimpan di dalam kotak pelindung yang dikunci dengan baut pengaman. Siswa DILARANG membuka baut penutup baterai atau mencolokkan kabel pengisi daya sendiri. Pemasangan dan pengisian baterai 100% hanya boleh dilakukan oleh Bapak/Ibu Guru.",
        "steps": [
          "Amati unit robot MazeBot yang telah disiapkan oleh guru di atas meja kelompok dalam keadaan saklar OFF.",
          "Temukan dan tunjuk bagian Otak (papan ESP32 di bagian tengah), Mata (3 sensor berbentuk silinder kembar di depan/samping), dan Mata Bawah (di kolong depan robot).",
          "Periksa kotak baterai di bagian belakang/bawah robot. Pastikan penutupnya rapat dan baut pengamannya terpasang kuat.",
          "Dengan aba-aba guru, geser saklar daya dari posisi OFF (0) ke posisi ON (1). Perhatikan lampu indikator daya yang menyala."
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Visualisasi Alur Kerja Sistem Robot (Konsep Dasar M-01)</div> <div><span class=\"block b-event\"> Saat Saklar Robot Dinyalakan (ON)</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Nyalakan Lampu Indikator Power <span class=\"param\">MERAH</span></span></div> <div><span class=\"block b-sensor\"> Siapkan Sensor Jarak (Depan, Kiri, Kanan)</span></div> <div><span class=\"block b-motion\"> Kunci Roda dalam Posisi <span class=\"param\">DIAM / SIAGA</span></span></div> </div> </div>",
        "lks": "<p><strong>Tugas Kelompok:</strong> Cocokkan bagian robot dengan pengamatan langsung pada unit MazeBot kelompokmu!</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Pertanyaan Pengamatan</th><th>Hasil Pengamatan Siswa</th></tr> </thead> <tbody> <tr><td>1</td><td>Berapa jumlah bulatan \"mata\" ultrasonik pada bagian depan dan samping robot?</td><td>......... pasang (......... bulatan)</td></tr> <tr><td>2</td><td>Berapa jumlah roda karet dan roda bebas (caster wheel) di bawah robot?</td><td>Roda Karet: ..... | Roda Caster: .....</td></tr> <tr><td>3</td><td>Apa warna lampu yang menyala pada papan otak ESP32 saat saklar di-ON-kan?</td><td>Warna: ...............................</td></tr> <tr><td>4</td><td>Tuliskan nama Wi-Fi (SSID) yang tertera pada stiker bodi robotmu!</td><td>SSID: ................................</td></tr> </tbody> </table>",
        "troubleshooting": "Jika lampu indikator tidak menyala saat saklar di-ON-kan, segera lapor kepada Guru (jangan mengetuk atau membongkar tempat baterai). Guru akan memeriksa tegangan baterai 18650.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-01_Mengenal_Si_Robot_Pintar_MazeBot.pdf",
        "level": "SD"
      },
      {
        "code": "M-02",
        "title": "Konsep Algoritma: Langkah demi Langkah",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Memahami pengertian Algoritma sebagai urutan langkah-langkah logis untuk menyelesaikan suatu tugas.",
          "Mempraktikkan instruksi sekuensial melalui permainan tanpa komputer (Unplugged Activity: 'Temanku Si Robot').",
          "Menyadari bahwa urutan instruksi yang terbalik akan menghasilkan posisi akhir yang salah."
        ],
        "theory": "<p><strong>Apa itu Algoritma?</strong> Algoritma adalah urutan langkah demi langkah yang jelas dan berurutan untuk menyelesaikan masalah. Robot tidak bisa menebak pikiran kita; ia hanya melakukan persis apa yang kita perintahkan dari baris pertama hingga baris terakhir.</p> <p>Contoh di kehidupan sehari-hari saat memakai sepatu: (1) Pakai kaus kaki, (2) Masukkan kaki ke sepatu, (3) Ikat tali sepatu. Jika urutannya terbalik—pakai sepatu dulu baru pakai kaus kaki—maka hasilnya akan salah! Begitu pula saat kita memprogram MazeBot melewati ubin lantai.</p>",
        "safety": "Kegiatan dilakukan di lantai kelas menggunakan petak ubin keramik (tanpa menyalakan baterai robot). Pastikan lantai bersih dan tidak licin agar siswa tidak terpeleset saat simulasi.",
        "steps": [
          "Bagi kelompok menjadi 2 peran: 'Programmer' (Pemberi Perintah) dan 'MazeBot' (Pelaksana Perintah).",
          "Gunakan 3x3 petak ubin keramik lantai kelas sebagai arena labirin. Letakkan buku di salah satu ubin sebagai rintangan dinding.",
          "Programmer menuliskan kartu perintah berurutan menggunakan 3 kata kunci saja: <strong>MAJU 1 PETAK</strong>, <strong>HADAP KANAN (90°)</strong>, dan <strong>HADAP KIRI (90°)</strong>.",
          "Siswa 'MazeBot' berjalan menutup mata/mengikuti kartu perintah yang dibacakan Programmer satu per satu hingga mencapai ubin Finish."
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Susunan Kartu Algoritma Sekuensial (Unplugged Block)</div> <div><span class=\"block b-event\"> Mulai Dari Petak START (A1)</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\">⬆ Maju <span class=\"param\">2</span> Petak Ubin</span></div> <div><span class=\"block b-motion\">↪ Hadap Kanan <span class=\"param\">90 Derajat</span></span></div> <div><span class=\"block b-motion\">⬆ Maju <span class=\"param\">1</span> Petak Ubin</span></div> <div><span class=\"block b-motion\">↩ Hadap Kiri <span class=\"param\">90 Derajat</span></span></div> <div><span class=\"block b-motion\">⬆ Maju <span class=\"param\">1</span> Petak Ubin</span></div> <div><span class=\"block b-led\"> Berhenti di Petak FINISH!</span></div> </div> </div>",
        "lks": "<p><strong>Tantangan Peta Petak:</strong> Jika robot mulai di petak (1,1) menghadap Utara dan petak (1,2) terhalang dinding kardus, tuliskan urutan 4 langkah agar robot sampai di petak (1,3)!</p> <table class=\"std-table\"> <thead> <tr><th>Langkah Ke-</th><th>Perintah yang Dipilih (Maju / Hadap Kanan / Hadap Kiri)</th><th>Posisi Robot Sekarang</th></tr> </thead> <tbody> <tr><td>Langkah 1</td><td>...........................................................................</td><td>Petak: ..........</td></tr> <tr><td>Langkah 2</td><td>...........................................................................</td><td>Petak: ..........</td></tr> <tr><td>Langkah 3</td><td>...........................................................................</td><td>Petak: ..........</td></tr> <tr><td>Langkah 4</td><td>...........................................................................</td><td>Petak: ..........</td></tr> </tbody> </table>",
        "troubleshooting": "Siswa sering tertukar antara 'Belok Kanan sambil jalan' dengan 'Putar Badan Hadap Kanan di tempat'. Tekankan bahwa perintah belok hanya memutar arah hadap badan 90 derajat di ubin yang sama.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-02_Konsep_Algoritma_Langkah_demi_Langkah.pdf",
        "level": "SD"
      },
      {
        "code": "M-03",
        "title": "Kanvas Kode Visual Pertama",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mengenal antarmuka Kanvas Pemrograman Visual (Blockly MazeBot Studio).",
          "Menyusun balok-balok kode seperti puzzle untuk menyalakan dan mematikan lampu LED indikator pada robot.",
          "Mengirimkan (Upload/Run) program pertama ke robot dan mengamati kedipan lampu."
        ],
        "theory": "<p>Pada <strong>Kanvas Kode Visual</strong>, kita tidak perlu mengetik kode yang rumit. Setiap perintah berbentuk <strong>Balok Puzzle Berwarna</strong>:</p> <ul> <li><strong>Kuning (Kejadian/Events):</strong> Pemicu mulainya program, seperti <em>\"Saat Program Dimulai\"</em>.</li> <li><strong>Hijau (Indikator/LED):</strong> Mengatur nyala lampu indikator atau bunyi bip pada robot.</li> <li><strong>Oranye (Kontrol Waktu):</strong> Mengatur jeda tunggu (<em>tunggu ... detik</em>) atau pengulangan (<em>ulangi selamanya</em>).</li> </ul> <p>Mengapa kita butuh balok <strong>Tunggu (Wait/Delay)</strong>? Karena otak komputer ESP32 bekerja sangat cepat (jutaan kali per detik). Jika kita menyuruh lampu <em>Nyala</em> lalu langsung <em>Mati</em> tanpa jeda tunggu, mata kita tidak akan sempat melihat lampu berkedip!</p>",
        "safety": "Letakkan robot di bagian tengah meja agar aman. Jangan menyentuh kaki-kaki komponen logam pada papan sirkuit ESP32 dengan tangan basah atau benda logam.",
        "steps": [
          "Buka halaman Kanvas Kode Visual MazeBot pada komputer/tablet yang telah terhubung ke robot.",
          "Tarik balok kuning <strong>[Saat Program Dimulai]</strong> ke tengah kanvas kerja.",
          "Pasangkan balok oranye <strong>[Ulangi Selamanya]</strong> di bawah balok mulai.",
          "Di dalam mulut balok <em>Ulangi Selamanya</em>, masukkan berturut-turut: <strong>[Lampu Indikator NYALA]</strong> &rarr; <strong>[Tunggu 1 Detik]</strong> &rarr; <strong>[Lampu Indikator MATI]</strong> &rarr; <strong>[Tunggu 1 Detik]</strong>.",
          "Klik tombol <strong>[Kirim ke Robot / Run]</strong> dan amati lampu biru pada otak ESP32!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-03: Lampu Berkedip (Blink LED)</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Atur Lampu Indikator Robot <span class=\"param\">NYALA (ON)</span></span></div> <div><span class=\"block b-control\"> Tunggu <span class=\"param\">1</span> detik</span></div> <div><span class=\"block b-led\"> Atur Lampu Indikator Robot <span class=\"param\">MATI (OFF)</span></span></div> <div><span class=\"block b-control\"> Tunggu <span class=\"param\">1</span> detik</span></div> </div> </div> </div>",
        "lks": "<p><strong>Eksperimen Waktu Kedip:</strong> Ubahlah angka pada balok <em>Tunggu ... detik</em>, lalu catat apa yang terjadi pada lampu robot!</p> <table class=\"std-table\"> <thead> <tr><th>Percobaan</th><th>Nilai Balok Tunggu Nyala</th><th>Nilai Balok Tunggu Mati</th><th>Bagaimana Kedipan Lampu Robot? (Lambat / Cepat / Sangat Cepat)</th></tr> </thead> <tbody> <tr><td>1</td><td>1 detik</td><td>1 detik</td><td>............................................................</td></tr> <tr><td>2</td><td>0.2 detik</td><td>0.2 detik</td><td>............................................................</td></tr> <tr><td>3</td><td>2 detik</td><td>0.5 detik</td><td>............................................................</td></tr> </tbody> </table>",
        "troubleshooting": "Jika program tidak berefek pada robot, periksa apakah balok di dalam kanvas sudah menempel rapat (terdengar bunyi 'klik') pada balok utama [Saat Program Dimulai]. Balok yang terlepas (abu-abu) tidak akan dijalankan.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-03_Kanvas_Kode_Visual_Pertama.pdf",
        "level": "SD"
      },
      {
        "code": "M-04",
        "title": "Robot Mulai Melangkah (Maju & Mundur)",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Menggunakan balok gerak motor untuk menggerakkan MazeBot maju lurus dan mundur lurus.",
          "Memahami hubungan antara durasi waktu (detik) dengan jauhnya jarak langkah robot.",
          "Memasang balok pengaman [Berhenti] di akhir urutan gerak."
        ],
        "theory": "<p>MazeBot memiliki dua roda penggerak di sisi kiri dan kanan. Agar robot berjalan <strong>Maju Lurus</strong>, kedua roda kiri dan kanan harus berputar ke arah depan secara bersamaan. Sebaliknya, agar robot berjalan <strong>Mundur</strong>, kedua roda harus berputar ke arah belakang bersamaan.</p> <p>Semakin lama durasi waktu (detik) yang kita masukkan pada balok gerak, maka semakin jauh pula jarak yang ditempuh oleh MazeBot di lantai.</p>",
        "safety": "PERHATIAN: Mulai modul ini robot akan bergerak fisik! Uji gerak robot di LANTAI KELAS, BUKAN di atas meja tinggi agar robot tidak terjun jatuh dari tepi meja.",
        "steps": [
          "Siapkan jalur lurus di lantai menggunakan penggaris atau meteran sepanjang 100 cm, tandai garis Start.",
          "Di Kanvas Kode Visual, susun balok: <strong>[Saat Dimulai]</strong> &rarr; <strong>[Gerak MAJU selama 1 detik]</strong> &rarr; <strong>[Berhenti selama 1 detik]</strong> &rarr; <strong>[Gerak MUNDUR selama 1 detik]</strong> &rarr; <strong>[Berhenti Total]</strong>.",
          "Letakkan roda depan MazeBot tepat di garis Start lantai.",
          "Jalankan program dan ukur berapa sentimeter robot melaju ke depan sebelum berhenti dan mundur kembali."
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-04: Maju dan Mundur Terukur</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Tunggu <span class=\"param\">2</span> detik (Waktu siap lepas tangan)</span></div> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> selama <span class=\"param\">2</span> detik</span></div> <div><span class=\"block b-motion\"> Berhenti selama <span class=\"param\">1</span> detik</span></div> <div><span class=\"block b-motion\">⬇ Gerak <span class=\"param\">MUNDUR</span> selama <span class=\"param\">2</span> detik</span></div> <div><span class=\"block b-motion\"> Berhenti Total</span></div> </div> </div>",
        "lks": "<p><strong>Tabel Pengukuran Jarak Tempuh:</strong> Ukur menggunakan penggaris berapa jauh robot maju untuk durasi detik berikut!</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Durasi Balok Maju (Detik)</th><th>Jarak Tempuh di Lantai (cm)</th><th>Apakah Robot Kembali Tepat ke Garis Start Saat Mundur?</th></tr> </thead> <tbody> <tr><td>1</td><td>1 Detik</td><td>............ cm</td><td>Ya / Kurang sedikit / Lebih sedikit</td></tr> <tr><td>2</td><td>2 Detik</td><td>............ cm</td><td>Ya / Kurang sedikit / Lebih sedikit</td></tr> <tr><td>3</td><td>3 Detik</td><td>............ cm</td><td>Ya / Kurang sedikit / Lebih sedikit</td></tr> </tbody> </table>",
        "troubleshooting": "Tambahkan balok [Tunggu 2 detik] paling atas sebelum balok [Gerak Maju], supaya tangan siswa sempat menjauh dari robot setelah menekan tombol mulai.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-04_Robot_Mulai_Melangkah_Maju_Mundur.pdf",
        "level": "SD"
      },
      {
        "code": "M-05",
        "title": "Bermanuver: Belok Kanan & Kiri",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Memahami cara kerja belokan robot dua roda (konsep perputaran roda berlawanan arah / Differential Drive).",
          "Menentukan durasi waktu putar yang tepat agar robot berbelok membentuk sudut siku-siku (90 derajat).",
          "Membuat gerakan kombinasi maju dan belok membentuk huruf 'L' dan kotak persegi."
        ],
        "theory": "<p>Bagaimana robot tanpa roda setir depan (seperti mobil biasa) bisa berbelok? Rahasianya adalah <strong>Perbedaan Putaran Roda (Differential Drive)</strong>, mirip seperti cara tank militer atau kursi roda berbelok!</p> <ul> <li><strong>Belok Kanan di Tempat (Pivot Right):</strong> Roda Kiri berputar MAJU, sedangkan Roda Kanan berputar MUNDUR.</li> <li><strong>Belok Kiri di Tempat (Pivot Left):</strong> Roda Kanan berputar MAJU, sedangkan Roda Kiri berputar MUNDUR.</li> </ul>",
        "safety": "Pastikan ban karet tidak kotor oleh debu tebal atau kertas menempel, karena ban yang licin akan membuat sudut belokan robot tidak konsisten.",
        "steps": [
          "Gunakan garis siku-siku ubin keramik lantai (sudut 90 derajat) sebagai patokan sudut belok.",
          "Pasang balok <strong>[Belok KANAN selama 0.5 detik]</strong> lalu <strong>[Berhenti]</strong>.",
          "Amati apakah putaran robot kurang dari 90° (kurang patah) atau lebih dari 90° (kelewatan).",
          "Ubah angka desimal detiknya (misal 0.45 detik atau 0.6 detik) sampai robot berputar tepat menghadap garis siku ubin!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-05: Manuver Sudut Siku (Jalur Huruf L)</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Tunggu <span class=\"param\">2</span> detik</span></div> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> selama <span class=\"param\">1.5</span> detik</span></div> <div><span class=\"block b-motion\"> Berhenti selama <span class=\"param\">0.5</span> detik</span></div> <div><span class=\"block b-motion\">↪ Belok <span class=\"param\">KANAN 90°</span> (durasi <span class=\"param\">0.55</span> detik)</span></div> <div><span class=\"block b-motion\"> Berhenti selama <span class=\"param\">0.5</span> detik</span></div> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> selama <span class=\"param\">1.5</span> detik</span></div> <div><span class=\"block b-motion\"> Berhenti Total</span></div> </div> </div>",
        "lks": "<p><strong>Kalibrasi Sudut Putar Kelompokmu:</strong> Cari durasi detik paling pas untuk robotmu di lantai kelas!</p> <table class=\"std-table\"> <thead> <tr><th>Target Manuver</th><th>Durasi Detik Percobaan 1</th><th>Durasi Detik Terbaik (Pas)</th><th>Arah Roda Kiri & Kanan</th></tr> </thead> <tbody> <tr><td>Belok Kanan 90° (Siku Kanan)</td><td>....... detik</td><td>....... detik</td><td>Kiri: Maju | Kanan: Mundur</td></tr> <tr><td>Belok Kiri 90° (Siku Kiri)</td><td>....... detik</td><td>....... detik</td><td>Kiri: Mundur | Kanan: Maju</td></tr> <tr><td>Putar Balik 180° (Hadap Belakang)</td><td>....... detik</td><td>....... detik</td><td>Kiri: Maju | Kanan: Mundur</td></tr> </tbody> </table>",
        "troubleshooting": "Selalu sisipkan [Berhenti selama 0.5 detik] di antara gerak Maju dan Belok agar sisa dorongan maju (inersia) berhenti dulu sebelum robot memutar badan.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-05_Bermanuver_Belok_Kanan_Kiri.pdf",
        "level": "SD"
      },
      {
        "code": "M-06",
        "title": "Mengatur Tenaga dan Kecepatan Robot",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Memahami pengaruh pengaturan kecepatan motor (Pelan, Sedang, Cepat) terhadap kestabilan gerak robot.",
          "Menguji perbedaan pengereman dan selip roda saat robot melaju terlalu cepat di lantai licin.",
          "Memilih kecepatan ideal untuk navigasi di dalam lorong labirin sempit."
        ],
        "theory": "<p>Apakah robot yang melaju paling ngebut selalu menjadi pemenang di dalam labirin? <strong>Ternyata tidak!</strong></p> <p>Jika tenaga motor diatur ke <strong>Cepat (100%)</strong> di lantai keramik yang licin, roda karet akan mengalami <em>selip (tergelincir)</em> saat mulai jalan dan susah berhenti tepat waktu saat mengerem. Sebaliknya, jika terlalu <strong>Pelan (<30%)</strong>, motor tidak punya cukup tenaga dorong untuk memutar roda. Kecepatan <strong>Sedang (50%–65%)</strong> adalah kecepatan paling stabil dan akurat!</p>",
        "safety": "Saat menguji kecepatan CEPAT (100%), pastikan area di depan robot minimal sepanjang 2 meter bebas dari kaki meja atau barang pecah belah.",
        "steps": [
          "Buat lintasan lurus sepanjang 1 meter dengan garis batas berhenti di ujungnya.",
          "Susun balok <strong>[Atur Kecepatan Motor ke PELAN (40%)]</strong> dilanjutkan <strong>[Gerak MAJU 2 detik]</strong> dan <strong>[Berhenti]</strong>.",
          "Ulangi percobaan dengan mengubah balok kecepatan ke <strong>SEDANG (65%)</strong> dan <strong>CEPAT (100%)</strong>.",
          "Perhatikan apakah roda robot berdecit/tergelincir saat mulai melaju dan saat mengerem mendadak."
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-06: Eksperimen 3 Tingkat Kecepatan</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Atur Kecepatan Robot ke <span class=\"param\">PELAN (40%)</span></span></div> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> selama <span class=\"param\">1.5</span> detik</span></div> <div><span class=\"block b-motion\"> Atur Kecepatan Robot ke <span class=\"param\">SEDANG (65%)</span></span></div> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> selama <span class=\"param\">1.5</span> detik</span></div> <div><span class=\"block b-motion\"> Berhenti Total</span></div> </div> </div>",
        "lks": "<p><strong>Uji Kestabilan Kecepatan:</strong> Beri tanda centang pada hasil pengamatan kelompokmu!</p> <table class=\"std-table\"> <thead> <tr><th>Mode Kecepatan</th><th>Jarak Tempuh (2 Detik)</th><th>Apakah Roda Tergelincir (Selip)?</th><th>Cocok untuk Lorong Sempit?</th></tr> </thead> <tbody> <tr><td>Pelan (40%)</td><td>......... cm</td><td>Tidak Selip / Selip</td><td>Cocok / Kurang Cocok</td></tr> <tr><td>Sedang (65%)</td><td>......... cm</td><td>Tidak Selip / Selip</td><td>Cocok / Kurang Cocok</td></tr> <tr><td>Cepat (100%)</td><td>......... cm</td><td>Tidak Selip / Selip</td><td>Cocok / Kurang Cocok</td></tr> </tbody> </table>",
        "troubleshooting": "Jika pada kecepatan Pelan (40%) robot hanya berdengung tetapi tidak bergerak, naikkan sedikit ke 45% atau 50% karena gesekan lantai membutuhkan tenaga awal minimal.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-06_Mengatur_Tenaga_dan_Kecepatan_Robot.pdf",
        "level": "SD"
      },
      {
        "code": "M-07",
        "title": "Remote Control Web (Pre-configured Wi-Fi)",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Menghubungkan tablet/laptop ke jaringan Wi-Fi pribadi milik robot (SSID & Password unik pada stiker robot).",
          "Membuka halaman Web Dashboard MazeBot dan mengenali tombol kemudi D-Pad virtual.",
          "Mengemudikan robot secara nirkabel (wireless) melewati jalur berkelok."
        ],
        "theory": "<p>Otak ESP32 pada MazeBot memiliki pemancar <strong>Wi-Fi bawaan</strong>! Artinya, robot ini bisa memancarkan sinyal Wi-Fi sendiri tanpa butuh internet sekolah (disebut mode <em>Access Point</em>). Setiap robot memiliki nama Wi-Fi (<strong>SSID</strong>) yang unik, misalnya <code>MazeBot-SD-01</code>, supaya sinyal antarkelompok tidak saling tertukar!</p> <p>Saat kita menekan tombol panah <strong>Maju (▲)</strong> di layar tablet, tablet mengirimkan pesan kilat melalui udara ke otak robot, lalu robot langsung memutar rodanya.</p>",
        "safety": "Hanya hubungkan tablet ke SSID nomor robot kelompokmu sendiri! Mengendalikan robot kelompok lain tanpa izin dapat mengejutkan teman yang sedang memegang robot.",
        "steps": [
          "Nyalakan saklar MazeBot, lalu baca stiker identitas di punggung robot (contoh: <code>SSID: MazeBot-SD-01</code> | <code>Pass: 12345678</code>).",
          "Buka pengaturan Wi-Fi di tablet/komputer, pilih nama Wi-Fi robot kelompokmu, dan masukkan kata sandinya.",
          "Buka aplikasi Browser (Chrome) dan ketikkan alamat <strong><code>http://192.168.4.1</code></strong> di kolom alamat atas.",
          "Gunakan tombol <strong>D-Pad Virtual (▲ Maju, ▼ Mundur, ◄ Kiri, ► Kanan, ■ Stop)</strong> untuk mengemudikan robot!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Logika Di Balik Layar Tombol D-Pad Web Dashboard (M-07)</div> <div><span class=\"block b-event\"> Saat Tombol D-Pad Web Ditekan</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika Tombol == <span class=\"param\">▲ ATAS</span></span> &rarr; <span class=\"block b-motion\">⬆ Gerak MAJU</span></div> <div><span class=\"block b-control\"> Jika Tombol == <span class=\"param\">▼ BAWAH</span></span> &rarr; <span class=\"block b-motion\">⬇ Gerak MUNDUR</span></div> <div><span class=\"block b-control\"> Jika Tombol == <span class=\"param\">◄ KIRI</span></span> &rarr; <span class=\"block b-motion\">↩ Belok KIRI</span></div> <div><span class=\"block b-control\"> Jika Tombol == <span class=\"param\">► KANAN</span></span> &rarr; <span class=\"block b-motion\">↪ Belok KANAN</span></div> </div> <div><span class=\"block b-event\"> Saat Jari Dilepas dari Tombol D-Pad</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti Seketika (Rem Aktif)</span></div> </div> </div>",
        "lks": "<p><strong>Lembar Uji Kendali Nirkabel:</strong> Uji fungsi setiap tombol pada Web Dashboard!</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Item Pengujian</th><th>Status (Berhasil / Gagal)</th><th>Catatan Respon Robot</th></tr> </thead> <tbody> <tr><td>1</td><td>Koneksi ke Wi-Fi SSID Stiker Robot</td><td>Berhasil / Gagal</td><td>Nama SSID: ........................</td></tr> <tr><td>2</td><td>Membuka halaman <code>192.168.4.1</code></td><td>Berhasil / Gagal</td><td>Tampilan D-Pad muncul jelas</td></tr> <tr><td>3</td><td>Tombol ▲, ▼, ◄, ► merespon cepat</td><td>Berhasil / Gagal</td><td>Jeda respon: Cepat / Lambat</td></tr> <tr><td>4</td><td>Parkir mundur ke dalam kotak garasi</td><td>Berhasil / Gagal</td><td>Waktu parkir: ........ detik</td></tr> </tbody> </table>",
        "troubleshooting": "Jika muncul pesan 'Tidak ada koneksi internet (No Internet)' di tablet saat tersambung ke Wi-Fi robot, pilih 'Tetap Hubungkan (Keep Wi-Fi Connection)' karena Wi-Fi lokal robot memang tidak terhubung ke internet luar.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-07_Remote_Control_Web_Pre_configured_Wi_Fi.pdf",
        "level": "SD"
      },
      {
        "code": "M-08",
        "title": "Ujian Tengah Semester (Proyek Mini 1: Tantangan Jalur Rintangan)",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mengevaluasi keterampilan siswa dalam mengoperasikan robot secara aman, mengatur kecepatan, dan bermanuver.",
          "Menyelesaikan misi mengemudikan robot melewati lorong rintangan berkelok hingga menyentuh garis batas akhir.",
          "Melatih kerja sama tim antara Pengemudi (Driver) dan Pengarah Jalur (Navigator)."
        ],
        "theory": "<p>Selamat datang di <strong>Ujian Tengah Semester (Proyek Mini 1)</strong>! Hari ini kita akan menguji semua kemampuan yang telah dipelajari dari M-01 hingga M-07. Setiap tim akan mengendalikan MazeBot melintasi <strong>Lorong Rintangan Zig-Zag</strong> sepanjang 2,5 meter dengan 3 tikungan sempit menggunakan D-Pad Web Dashboard.</p> <p>Strategi kunci: Gunakan kecepatan <em>Sedang</em> di jalur lurus, dan turunkan ke kecepatan <em>Pelan</em> saat melewati tikungan sempit agar bodi robot tidak menyenggol dinding kardus!</p>",
        "safety": "Siswa dilarang mendorong robot dengan tangan saat ujian berlangsung. Jika robot tersangkut di dinding labirin, gunakan tombol Mundur (▼) pada D-Pad untuk membebaskan robot.",
        "steps": [
          "Guru menyiapkan arena Lorong Rintangan dengan lebar lorong 25 cm dan 3 tikungan siku.",
          "Setiap kelompok mendapatkan 2 kali kesempatan tempuh (Run 1 dan Run 2). Waktu terbaik yang akan diambil.",
          "Saat peluit Start dibunyikan, pengemudi mengarahkan robot dari kotak Start menuju kotak Finish.",
          "Setiap kali bodi robot menyentuh dinding rintangan, dikenakan penalti tambahan waktu +3 detik."
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Aturan Strategi Proyek Mini 1 (Checklist Pengemudi)</div> <div><span class=\"block b-event\"> Persiapan di Garis START</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Pastikan Wi-Fi Terhubung ke <span class=\"param\">SSID Robot Sendiri</span></span></div> <div><span class=\"block b-motion\"> Set Slider Kecepatan Awal ke <span class=\"param\">60% (Stabil)</span></span></div> <div><span class=\"block b-control\"> Navigasi Lorong: Lurus &rarr; Tikungan Kanan &rarr; Tikungan Kiri &rarr; Garis Batas</span></div> <div><span class=\"block b-motion\"> Hentikan Robot Tepat di Dalam Kotak FINISH</span></div> </div> </div>",
        "lks": "<p><strong>Kartu Skor Ujian Tengah Semester (Proyek Mini 1):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Putaran</th><th>Waktu Tempuh Asli (Detik)</th><th>Jumlah Sentuhan Dinding (x 3 dtk)</th><th>Total Skor Waktu Akhir</th><th>Predikat</th></tr> </thead> <tbody> <tr><td>Run 1 (Percobaan 1)</td><td>......... detik</td><td>..... kali (+..... dtk)</td><td>......... detik</td><td>A / B / C</td></tr> <tr><td>Run 2 (Percobaan 2)</td><td>......... detik</td><td>..... kali (+..... dtk)</td><td>......... detik</td><td>A / B / C</td></tr> </tbody> </table> <p><em>Kriteria Predikat: A (Sangat Baik: Total waktu &lt; 25 detik), B (Baik: 25–45 detik), C (Perlu Latihan: &gt; 45 detik).</em></p>",
        "troubleshooting": "Jika tampilan web D-Pad membeku di tengah jalan, tekan tombol Refresh pada browser tablet dan robot akan otomatis berhenti aman berkat fitur pengaman sinyal.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-08_Ujian_Tengah_Semester_Proyek_Mini_1_Tant.pdf",
        "level": "SD"
      },
      {
        "code": "M-09",
        "title": "Mata Ajaib: Membaca Sensor Jarak",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Memahami cara kerja sensor jarak ultrasonik melalui analogi pantulan suara kelelawar (ekolokasi).",
          "Membaca angka jarak halangan (dalam satuan sentimeter) dan grafik warna (Hijau/Kuning/Merah) secara langsung di Web Dashboard.",
          "Membedakan zona Aman (Hijau), Waspada (Kuning), dan Bahaya/Dekat (Merah)."
        ],
        "theory": "<p>Tahukah kamu bagaimana kelelawar bisa terbang di gua yang gelap gulita tanpa menabrak dinding? Kelelawar memancarkan <strong>gelombang bunyi ultrasonik</strong> dari mulutnya. Ketika suara itu menabrak dinding gua, suaranya memantul kembali ke telinga kelelawar!</p> <p>Mata MazeBot (Sensor Ultrasonik HC-SR04) bekerja dengan cara yang persis sama:</p> <ul> <li><strong>Silinder T (Transmitter / Mulut):</strong> Memancarkan gelombang suara ultrasonik.</li> <li><strong>Silinder R (Receiver / Telinga):</strong> Menangkap pantulan gelombang suara dari benda di depannya.</li> </ul> <p>Di Web Dashboard, jarak ditampilkan dengan kode warna: <strong>HIJAU (&gt; 20 cm = Aman)</strong>, <strong>KUNING (10–20 cm = Waspada)</strong>, dan <strong>MERAH (&lt; 10 cm = Terlalu Dekat!)</strong>.</p>",
        "safety": "Jangan menekan jaring kawat halus di bagian dalam silinder mata sensor ultrasonik dengan pensil atau jari karena selaput suaranya bisa rusak.",
        "steps": [
          "Letakkan MazeBot di atas meja menghadap ke arah ruang kosong, lalu buka tab <strong>[Monitor Sensor]</strong> di Web Dashboard.",
          "Ambil sebuah kotak kardus atau buku tebal dan berdirikan di depan mata robot pada jarak 30 cm (ukur dengan penggaris).",
          "Majukan buku perlahan-lahan ke jarak 25 cm, 15 cm, hingga 5 cm di depan mata robot.",
          "Amati perubahan angka sentimeter dan perubahan warna bar indikator di layar tablet!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-09: Indikator Warna Radar Jarak</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-sensor\"> Tampilkan <span class=\"param\">Jarak Sensor Depan (cm)</span> ke Layar Web</span></div> <div><span class=\"block b-control\"> Jika <span class=\"param\">Jarak Depan &lt; 10 cm</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Ubah Status Radar Web ke <span class=\"param\">MERAH (BAHAYA)</span></span></div> </div> <div><span class=\"block b-control\"> Jika Tidak (Jarak Aman) Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Ubah Status Radar Web ke <span class=\"param\">HIJAU (AMAN)</span></span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Eksperimen Uji Akurasi Mata Robot:</strong> Bandingkan ukuran penggaris asli dengan bacaan sensor di layar!</p> <table class=\"std-table\"> <thead> <tr><th>Jarak Buku di Penggaris</th><th>Angka Jarak di Layar Web (cm)</th><th>Warna Bar di Layar Web (Hijau / Kuning / Merah)</th></tr> </thead> <tbody> <tr><td>30 cm</td><td>............ cm</td><td>...........................................</td></tr> <tr><td>15 cm</td><td>............ cm</td><td>...........................................</td></tr> <tr><td>7 cm</td><td>............ cm</td><td>...........................................</td></tr> </tbody> </table>",
        "troubleshooting": "Pastikan buku atau kardus diletakkan tegak lurus di depan sensor. Jika buku dimiringkan terlalu tajam, pantulan suara akan memantul ke arah lain sehingga jarak terbaca jauh.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-09_Mata_Ajaib_Membaca_Sensor_Jarak.pdf",
        "level": "SD"
      },
      {
        "code": "M-10",
        "title": "Sistem Anti-Tabrak Otomatis",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Memahami logika pengambilan keputusan bersyarat: JIKA – MAKA – JIKA TIDAK (IF – THEN – ELSE).",
          "Memprogram sistem pengereman otomatis (AEB / Automatic Emergency Braking) seperti pada mobil pintar modern.",
          "Menguji robot agar melaju lurus dan otomatis berhenti sendiri ketika mendeteksi kotak di depannya pada jarak < 10 cm."
        ],
        "theory": "<p>Mobil pintar zaman sekarang memiliki fitur <strong>Rem Darurat Otomatis</strong>: jika ada pejalan kaki atau penghalang tiba-tiba di depan mobil, mobil akan mengerem sendiri meskipun sopir belum menginjak rem!</p> <p>Kita dapat memberikan kepintaran itu kepada MazeBot menggunakan balok logika <strong>JIKA ... MAKA ... JIKA TIDAK ...</strong>:</p> <ul> <li><strong>JIKA</strong> Jarak Depan kurang dari 10 cm &rarr; <strong>MAKA</strong> Berhenti Seketika!</li> <li><strong>JIKA TIDAK</strong> (artinya jalan di depan masih jauh/kosong) &rarr; <strong>MAKA</strong> Terus Maju!</li> </ul>",
        "safety": "Gunakan kotak kardus ringan atau botol plastik kosong sebagai rintangan uji coba (jangan gunakan dinding semen keras saat percobaan pertama, untuk berjaga-jaga jika logika balok siswa masih terbalik).",
        "steps": [
          "Buka Kanvas Kode Visual dan pasang balok <strong>[Ulangi Selamanya]</strong> di bawah <strong>[Saat Program Dimulai]</strong>.",
          "Masukkan balok logika <strong>[Jika ... Maka ... Jika Tidak ...]</strong> ke dalam perulangan.",
          "Pada syarat <em>Jika</em>, pasang balok sensor <strong>[Jarak Sensor Depan &lt; 10 cm]</strong>.",
          "Pada bagian <em>Maka</em>, pasang balok <strong>[Berhenti Total]</strong> dan <strong>[Lampu Indikator NYALA]</strong>. Pada bagian <em>Jika Tidak</em>, pasang <strong>[Gerak Maju (Kecepatan 50%)]</strong>.",
          "Taruh kardus di tengah jalur, jalankan robot, dan lihat apakah robot mengerem tepat sebelum menabrak kardus!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-10: Rem Otomatis Anti-Tabrak</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika <span class=\"param\"> Jarak Sensor Depan &lt; 10 cm</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti Seketika</span></div> <div><span class=\"block b-led\"> Lampu Indikator <span class=\"param\">NYALA (Peringatan)</span></span></div> </div> <div><span class=\"block b-control\"> Jika Tidak Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> Kecepatan <span class=\"param\">50%</span></span></div> <div><span class=\"block b-led\"> Lampu Indikator <span class=\"param\">MATI</span></span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Eksperimen Uji Rem Darurat:</strong> Apa yang terjadi jika kardus diangkat kembali setelah robot berhenti?</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Skenario Pengujian</th><th>Respon Robot yang Diamati</th></tr> </thead> <tbody> <tr><td>1</td><td>Kardus ditaruh 50 cm di depan robot yang sedang melaju</td><td>Robot berhenti pada jarak ...... cm dari kardus</td></tr> <tr><td>2</td><td>Kardus diangkat/disingkirkan saat robot sedang berhenti</td><td>Robot akan: ..........................................</td></tr> <tr><td>3</td><td>Telapak tangan didekatkan ke depan mata robot</td><td>Robot akan: ..........................................</td></tr> </tbody> </table>",
        "troubleshooting": "Jangan gunakan balok [Gerak Maju selama 2 detik] di dalam [Jika Tidak]! Gunakan balok [Gerak Maju (tanpa detik)] agar robot terus memeriksa sensor mata setiap saat tanpa menunda pemeriksaan selama 2 detik.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-10_Sistem_Anti_Tabrak_Otomatis.pdf",
        "level": "SD"
      },
      {
        "code": "M-11",
        "title": "Robot Menghindar Cerdas",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mengembangkan logika anti-tabrak menjadi navigasi menghindar mandiri (Autonomous Obstacle Avoidance).",
          "Memprogram urutan manuver menghindar: Berhenti sejenak &rarr; Mundur sedikit &rarr; Belok Kanan 90° &rarr; Lanjut Maju.",
          "Mengamati bagaimana robot menjelajahi ruangan dan berbelok sendiri setiap kali menemui dinding."
        ],
        "theory": "<p>Pada modul sebelumnya, robot sudah pintar berhenti saat melihat dinding. Namun, jika hanya berhenti, robot tidak akan pernah keluar dari labirin! Supaya robot bisa melanjutkan petualangannya sendiri, kita harus mengajarinya <strong>Manuver Menghindar Cerdas</strong>:</p> <ol> <li>Saat mendeteksi dinding di depan (&lt; 12 cm), <strong>Berhenti sebentar</strong> (0.3 detik).</li> <li><strong>Mundur sedikit</strong> (0.5 detik) agar hidung robot punya ruang bebas untuk berputar tanpa menyerempet dinding.</li> <li><strong>Belok Kanan 90 derajat</strong> untuk mencari jalan baru yang kosong.</li> </ol>",
        "safety": "Pastikan area jelajah robot dibatasi dengan kotak kardus atau dinding lorong agar robot tidak berjalan keluar pintu kelas.",
        "steps": [
          "Modifikasi program M-10 pada bagian di dalam blok <strong>[Jika Jarak Depan &lt; 12 cm Maka]</strong>.",
          "Di bawah balok <strong>[Berhenti 0.3 detik]</strong>, tambahkan balok <strong>[Gerak MUNDUR selama 0.5 detik]</strong>.",
          "Tambahkan balok <strong>[Belok KANAN selama 0.55 detik]</strong> lalu <strong>[Berhenti 0.3 detik]</strong>.",
          "Unggah program ke robot, letakkan robot menghadap sudut dinding lorong, dan tonton robot berbelok sendiri mencari jalan keluar!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-11: Robot Penjelajah Penghindar Dinding</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika <span class=\"param\"> Jarak Sensor Depan &lt; 12 cm</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti selama <span class=\"param\">0.3</span> detik</span></div> <div><span class=\"block b-motion\">⬇ Gerak <span class=\"param\">MUNDUR</span> selama <span class=\"param\">0.5</span> detik</span></div> <div><span class=\"block b-motion\">↪ Belok <span class=\"param\">KANAN</span> selama <span class=\"param\">0.55</span> detik</span></div> <div><span class=\"block b-motion\"> Berhenti selama <span class=\"param\">0.3</span> detik</span></div> </div> <div><span class=\"block b-control\"> Jika Tidak Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> Kecepatan <span class=\"param\">50%</span></span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Analisis Gerak Menghindar:</strong> Jawablah pertanyaan berdasarkan hasil uji coba kelompokmu!</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Pertanyaan Analisis</th><th>Jawaban Kelompok</th></tr> </thead> <tbody> <tr><td>1</td><td>Mengapa robot harus mundur dulu 0.5 detik sebelum berbelok kanan?</td><td>............................................................</td></tr> <tr><td>2</td><td>Apa yang terjadi jika kita menghapus balok mundur?</td><td>............................................................</td></tr> <tr><td>3</td><td>Berapa kali robot berhasil menghindari dinding kardus dalam 1 menit?</td><td>......... kali berhasil menghindar</td></tr> </tbody> </table>",
        "troubleshooting": "Jika saat berbelok hidung robot masih menyenggol dinding depan, naikkan jarak deteksi dari 12 cm menjadi 15 cm atau tambah durasi mundur menjadi 0.6 detik.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-11_Robot_Menghindar_Cerdas.pdf",
        "level": "SD"
      },
      {
        "code": "M-12",
        "title": "Sensor Bawah: Detektif Warna Lantai",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mengenal cara kerja sensor garis inframerah TCRT5000 yang terpasang di kolong depan robot.",
          "Memahami sifat fisik cahaya: warna putih memantulkan cahaya, sedangkan warna hitam menyerap cahaya.",
          "Melakukan eksperimen membedakan permukaan lantai keramik putih dan pita lakban hitam."
        ],
        "theory": "<p>Selain punya 3 mata ultrasonik untuk melihat dinding, MazeBot punya satu mata rahasia di bagian bawah perutnya yang menghadap ke lantai, bernama <strong>Sensor Inframerah TCRT5000</strong>. Sensor ini memiliki 2 lampu kecil:</p> <ul> <li><strong>Lampu Bening (Pemancar):</strong> Menembakkan sinar inframerah ke lantai.</li> <li><strong>Lampu Hitam (Penerima):</strong> Menangkap pantulan sinar dari lantai.</li> </ul> <p>Sifat cahaya: <strong>Permukaan Putih/Terang</strong> akan <em>memantulkan</em> sinar kembali ke sensor. Sebaliknya, <strong>Garis Lakban Hitam</strong> akan <em>menyerap</em> sinar sehingga tidak ada pantulan yang kembali. Dari situlah robot tahu bahwa ia sedang menginjak garis hitam!</p>",
        "safety": "Saat mengamati kolong robot, pastikan roda tidak sedang berputar agar jari atau rambut tidak terlilit ban karet.",
        "steps": [
          "Tempelkan sepotong lakban hitam selebar 3–5 cm di atas lantai keramik putih.",
          "Nyalakan MazeBot dan buka indikator <strong>[Status Sensor Lantai]</strong> pada layar Web Dashboard.",
          "Pegang bodi robot dan letakkan bagian depan robot di atas keramik putih. Perhatikan lampu LED kecil pada modul sensor bawah dan status di layar.",
          "Geser robot hingga mata sensor bawah berada tepat di atas lakban hitam. Amati perubahan statusnya!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-12: Alarm Detektif Garis Hitam</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika <span class=\"param\"> Sensor Bawah Mendeteksi WARNA HITAM</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Lampu Indikator <span class=\"param\">NYALA</span></span></div> <div><span class=\"block b-led\"> Tampilkan Pesan Web: <span class=\"param\">\"GARIS HITAM DITEMUKAN!\"</span></span></div> </div> <div><span class=\"block b-control\"> Jika Tidak (Lantai Putih) Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Lampu Indikator <span class=\"param\">MATI</span></span></div> <div><span class=\"block b-led\"> Tampilkan Pesan Web: <span class=\"param\">\"LANTAI PUTIH BERSIH\"</span></span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Tabel Detektif Warna Permukaan:</strong> Uji sensor bawah robotmu di atas berbagai benda berikut!</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Permukaan yang Diuji</th><th>Apakah Cahaya Dipantulkan / Diserap?</th><th>Hasil Deteksi Robot (Putih / Hitam)</th></tr> </thead> <tbody> <tr><td>1</td><td>Lantai Keramik Putih</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr> <tr><td>2</td><td>Lakban / Selotip Hitam</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr> <tr><td>3</td><td>Kertas HVS Putih</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr> <tr><td>4</td><td>Sampul Buku Warna Hitam Doff</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr> </tbody> </table>",
        "troubleshooting": "Jika sensor tidak membedakan hitam dan putih, minta bantuan Guru untuk memutar sedikit baut potensiometer biru pada modul TCRT5000 menggunakan obeng kecil hingga lampu indikatornya sensitif tepat di atas lakban hitam.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-12_Sensor_Bawah_Detektif_Warna_Lantai.pdf",
        "level": "SD"
      },
      {
        "code": "M-13",
        "title": "Misi Berhenti Tepat di Garis Finish",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mengintegrasikan sensor bawah TCRT5000 sebagai pengunci penghentian gerak otonom robot.",
          "Membuat program di mana robot melaju lurus sendiri dari garis Start dan langsung mengunci rem saat menginjak garis Finish hitam.",
          "Memahami konsep penghentian perulangan program (Keluar dari Loop / Stop Program) saat misi selesai."
        ],
        "theory": "<p>Dalam perlombaan robot labirin, bagaimana robot tahu bahwa ia sudah berhasil keluar dari labirin dan mencapai <strong>Garis Finish</strong>? Di ujung labirin, kita menempelkan pita lakban hitam tebal sebagai penanda Finish.</p> <p>Saat sensor bawah mendeteksi warna <strong>HITAM</strong>, robot tidak boleh hanya berhenti sesaat lalu jalan lagi. Robot harus menjalankan perintah <strong>[Berhenti &amp; Kunci Program Selesai]</strong> supaya rodanya terkunci permanen sampai kita mengambilnya!</p>",
        "safety": "Gunakan lakban hitam yang cukup lebar (minimal 4–5 cm, atau 2 lapis lakban berjejer) agar sensor bawah punya waktu yang cukup untuk mendeteksinya saat robot sedang melaju.",
        "steps": [
          "Tempelkan lakban hitam tebal di lantai sebagai Garis Finish pada jarak 1 meter dari titik Start.",
          "Susun balok program: di dalam <strong>[Ulangi Selamanya]</strong>, periksa <strong>[Jika Sensor Bawah == HITAM]</strong>.",
          "Jika terdeteksi HITAM: pasang <strong>[Berhenti Total]</strong>, <strong>[Kedipkan Lampu 3 Kali]</strong>, dan <strong>[Hentikan Semua Program (Stop All)]</strong>.",
          "Jika TIDAK (masih lantai putih): pasang <strong>[Gerak MAJU Kecepatan 50%]</strong>. Uji di lintasan!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-13: Berhenti Otomatis di Garis Finish</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika <span class=\"param\"> Sensor Bawah == WARNA HITAM</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti Seketika (Kunci Roda)</span></div> <div><span class=\"block b-led\"> Tampilkan Status: <span class=\"param\">\"MISI FINISH BERHASIL!\"</span></span></div> <div><span class=\"block b-control\"> Hentikan Seluruh Program (Selesai)</span></div> </div> <div><span class=\"block b-control\"> Jika Tidak Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> Kecepatan <span class=\"param\">50%</span></span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Uji Ketepatan Berhenti di Garis Finish:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Percobaan</th><th>Kecepatan Maju</th><th>Lebar Lakban Hitam</th><th>Apakah Robot Berhenti Tepat di Atas Garis Hitam?</th></tr> </thead> <tbody> <tr><td>1</td><td>Pelan (45%)</td><td>5 cm</td><td>Berhenti Tepat / Kelewatan</td></tr> <tr><td>2</td><td>Sedang (60%)</td><td>5 cm</td><td>Berhenti Tepat / Kelewatan</td></tr> <tr><td>3</td><td>Cepat (90%)</td><td>2 cm (Tipis)</td><td>Berhenti Tepat / Kelewatan</td></tr> </tbody> </table>",
        "troubleshooting": "Jika pada kecepatan tinggi robot melindas garis hitam tipis tanpa berhenti, lebarkan garis lakban hitam menjadi 5 cm dan gunakan kecepatan Sedang (50%).",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-13_Misi_Berhenti_Tepat_di_Garis_Finish.pdf",
        "level": "SD"
      },
      {
        "code": "M-14",
        "title": "Simulasi Penuh & Uji Lintasan Terintegrasi",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Menggabungkan dua kepintaran sensor sekaligus: Sensor Jarak Depan (Anti-Tabrak/Belok) dan Sensor Bawah (Detektor Finish).",
          "Memahami urutan prioritas pengecekan sensor: Cek Garis Finish terlebih dahulu, baru Cek Dinding Depan.",
          "Menguji robot secara otonom di dalam miniatur lorong labirin 1 belokan berbentuk huruf 'L'."
        ],
        "theory": "<p>Sekarang tiba saatnya menggabungkan <strong>Mata Bawah (TCRT5000)</strong> dan <strong>Mata Depan (Ultrasonik)</strong> ke dalam satu otak program yang utuh! Bagaimana urutannya?</p> <ol> <li><strong>Pertanyaan Pertama:</strong> <em>\"Apakah aku sudah menginjak Garis Finish Hitam?\"</em> &rarr; Jika YA, langsung Berhenti Pemenang!</li> <li><strong>Pertanyaan Kedua:</strong> <em>\"Jika belum Finish, apakah di depanku ada dinding (&lt; 12 cm)?\"</em> &rarr; Jika YA, mundur sedikit lalu Belok Kanan!</li> <li><strong>Jika Keduanya Tidak:</strong> Artinya jalan masih aman dan belum sampai finish &rarr; <strong>Maju Lurus!</strong></li> </ol>",
        "safety": "Pastikan dinding kardus lorong labirin berdiri kokoh (rekatkan dengan lakban kertas ke lantai) agar tidak bergeser saat didekati robot.",
        "steps": [
          "Susun arena Labirin Huruf 'L' menggunakan dinding kardus: Jalur lurus 80 cm &rarr; Belokan Kanan 90° &rarr; Jalur lurus 80 cm &rarr; Kotak Lakban Hitam Finish.",
          "Susun balok logika bertingkat (<em>Jika ... Maka ... Jika Tidak Jika ... Maka ... Jika Tidak ...</em>) sesuai contoh kode di bawah.",
          "Letakkan MazeBot di mulut Start, nyalakan program, dan amati robot menyelesaikan lintasan tanpa disentuh tangan!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-14: Integrasi Penuh Navigasi &amp; Finish</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Tunggu <span class=\"param\">2</span> detik</span></div> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika <span class=\"param\"> Sensor Bawah == WARNA HITAM</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti Total</span></div> <div><span class=\"block b-led\"> Tampilkan Status: <span class=\"param\">\"FINISH TERCAPAI!\"</span></span></div> <div><span class=\"block b-control\"> Hentikan Seluruh Program</span></div> </div> <div><span class=\"block b-control\"> Jika Tidak, Jika <span class=\"param\"> Jarak Sensor Depan &lt; 12 cm</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti selama <span class=\"param\">0.3</span> detik</span></div> <div><span class=\"block b-motion\">⬇ Gerak <span class=\"param\">MUNDUR</span> selama <span class=\"param\">0.4</span> detik</span></div> <div><span class=\"block b-motion\">↪ Belok <span class=\"param\">KANAN</span> selama <span class=\"param\">0.55</span> detik</span></div> </div> <div><span class=\"block b-control\"> Jika Tidak Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\">⬆ Gerak <span class=\"param\">MAJU</span> Kecepatan <span class=\"param\">50%</span></span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Checklist Uji Integrasi Labirin 1 Belokan:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Tahapan Misi</th><th>Target Perilaku Robot</th><th>Berhasil / Belum</th><th>Catatan Perbaikan</th></tr> </thead> <tbody> <tr><td>Tahap 1: Lorong Awal</td><td>Melaju lurus dari titik Start</td><td>Berhasil / Belum</td><td>.................................</td></tr> <tr><td>Tahap 2: Sudut Belokan</td><td>Mendeteksi dinding &amp; belok kanan 90°</td><td>Berhasil / Belum</td><td>.................................</td></tr> <tr><td>Tahap 3: Lorong Akhir</td><td>Melaju menuju garis finish</td><td>Berhasil / Belum</td><td>.................................</td></tr> <tr><td>Tahap 4: Kotak Finish</td><td>Berhenti tepat di atas lakban hitam</td><td>Berhasil / Belum</td><td>.................................</td></tr> </tbody> </table>",
        "troubleshooting": "Jika robot belok terlalu patah atau kurang patah di sudut L, catat berapa detik durasi belok yang perlu diperbaiki pada sesi Tuning minggu depan (M-15).",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-14_Simulasi_Penuh_Uji_Lintasan_Terintegrasi.pdf",
        "level": "SD"
      },
      {
        "code": "M-15",
        "title": "Troubleshooting, Tuning & Remedial",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mendiagnosis masalah umum pada gerak robot (melenceng ke samping, belok kurang pas, atau sensor terlambat merespon).",
          "Melakukan penyesuaian halus (Fine Tuning) pada angka durasi belok, kecepatan roda kiri/kanan, dan jarak batas sensor.",
          "Memberikan pendampingan remedial bagi kelompok yang belum berhasil menuntaskan simulasi M-14."
        ],
        "theory": "<p>Setiap robot memiliki keunikan mekanik masing-masing! Kadang-kadang, motor roda kiri berputar sedikit lebih cepat daripada motor roda kanan, sehingga saat diperintah <strong>Maju Lurus</strong>, robot agak miring/melenceng ke kanan. Proses menyetel angka-angka pada kode program agar robot bergerak sempurna disebut <strong>Tuning (Penyelarasan)</strong>.</p> <p>Tiga hal yang kita setel hari ini:</p> <ol> <li><strong>Keseimbangan Roda (Trim/Offset):</strong> Menyeimbangkan tenaga roda kiri dan kanan agar jalannya lurus seperti penggaris.</li> <li><strong>Durasi Belok 90°:</strong> Menyesuaikan angka detik belok (misal dari 0.55 detik menjadi 0.50 atau 0.62 detik) sesuai kondisi baterai.</li> <li><strong>Jarak Pengereman Dinding:</strong> Menyesuaikan jarak sensor depan (10–15 cm) agar pas di tengah lorong.</li> </ol>",
        "safety": "Jika baterai mulai melemah (putaran roda terasa sangat lambat), laporkan pada Guru agar diganti dengan baterai 18650 yang sudah terisi penuh.",
        "steps": [
          "Uji jalan lurus 1 meter: Jika robot melenceng ke kanan, kurangi sedikit tenaga roda kiri atau tambahkan koreksi pada balok <strong>[Atur Keseimbangan Roda]</strong>.",
          "Uji belok 90 derajat di sudut keramik: Sesuaikan angka desimal detik pada balok <strong>[Belok Kanan]</strong> sampai robot benar-benar lurus sejajar garis keramik.",
          "Jalankan kembali robot di lintasan Labirin 'L' sebanyak 3 kali berturut-turut untuk memastikan hasilnya konsisten!",
          "Catat 'Angka Emas' (nilai setelan terbaik) kelompokmu di buku catatan agar siap dipakai saat Tantangan Akhir minggu depan."
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Program Balok Visual M-15: Penyetelan Keseimbangan &amp; Parameter Emas</div> <div><span class=\"block b-event\">▶ Saat Program Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Setel Keseimbangan Roda: Kiri <span class=\"param\">50%</span> | Kanan <span class=\"param\">53%</span> (Koreksi Lurus)</span></div> <div><span class=\"block b-var\"> Simpan Nilai Jarak Batas Dinding = <span class=\"param\">13 cm</span></span></div> <div><span class=\"block b-var\"> Simpan Durasi Belok 90° = <span class=\"param\">0.54 detik</span></span></div> <div><span class=\"block b-control\"> Jalankan Siklus Navigasi Labirin (M-14)</span></div> </div> </div>",
        "lks": "<p><strong>Kartu Resep 'Angka Emas' Tuning Robot Kelompok:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Parameter yang Disetel</th><th>Nilai Sebelum Tuning</th><th>Masalah yang Terjadi</th><th>Nilai Terbaik ('Angka Emas')</th></tr> </thead> <tbody> <tr><td>Tenaga Roda Kiri &amp; Kanan</td><td>Kiri: 50% | Kanan: 50%</td><td>Melenceng ke: ...........</td><td>Kiri: ....% | Kanan: ....%</td></tr> <tr><td>Durasi Belok Kanan 90°</td><td>0.55 detik</td><td>Kurang / Kelebihan belok</td><td>............ detik</td></tr> <tr><td>Jarak Deteksi Dinding Depan</td><td>12 cm</td><td>Terlalu dekat / jauh</td><td>............ cm</td></tr> </tbody> </table>",
        "troubleshooting": "Ingat bahwa saat baterai baru diisi penuh oleh Guru, putaran roda sedikit lebih kencang dibanding saat baterai hampir habis. Cek ulang durasi belok sebelum lomba dimulai!",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-15_Troubleshooting_Tuning_Remedial.pdf",
        "level": "SD"
      },
      {
        "code": "M-16",
        "title": "Tantangan Akhir: MazeBot Rescue Mission",
        "duration": "2 JP (2 x 35 Menit)",
        "phase": "Fase B/C (Kelas 4–6 SD)",
        "objectives": [
          "Mendemonstrasikan kemampuan robot bergerak secara 100% mandiri (otonom) dari ruang Start hingga kotak Finish.",
          "Mengevaluasi ketepatan logika pemrograman visual, akurasi manuver belokan, dan penghentian di garis hitam.",
          "Menumbuhkan rasa percaya diri, sportivitas, dan apresiasi atas karya pemrograman tiap kelompok."
        ],
        "theory": "<p>Selamat sampai di puncak petualangan: <strong>MazeBot Rescue Mission (Misi Penyelamatan Akhir Semester)</strong>! Dalam misi ini, robot cilikmu ditugaskan masuk ke dalam lorong penyelamatan secara mandiri (tanpa remote D-Pad!), melewati penghalang dinding, berbelok di tikungan, dan berhenti tepat di atas <strong>Zona Penyelamatan (Kotak Hitam Finish)</strong>.</p> <p>Penilaian dilakukan secara objektif berdasarkan keberhasilan tahapan misi dan kerapian susunan balok kode yang kalian buat.</p>",
        "safety": "Seluruh anggota tim wajib berdiri di luar garis batas arena labirin saat robot sedang menjalankan misi otonom agar sensor ultrasonik tidak salah mendeteksi kaki siswa sebagai dinding.",
        "steps": [
          "Masukkan nilai 'Angka Emas' hasil tuning M-15 ke dalam program lengkap navigasi otonom kelompokmu.",
          "Unggah program ke MazeBot dan letakkan robot di kotak START dalam keadaan siap.",
          "Saat juri/guru memberikan aba-aba 'MULAI!', tekan tombol Run / nyalakan robot dan biarkan robot bekerja sendiri menyelesaikan labirin.",
          "Setelah robot berhenti di kotak Finish hitam, presentasikan secara singkat di depan kelas bagaimana cara kerja balok kode kelompokmu!"
        ],
        "code_block": "<div class=\"blockly-container\"> <div class=\"blockly-title\">Kode Master M-16: MazeBot Rescue Mission (Full Autonomous SD)</div> <div><span class=\"block b-event\">▶ Saat Misi Penyelamatan Dimulai</span></div> <div class=\"block-indent\"> <div><span class=\"block b-led\"> Nyalakan Lampu Indikator &amp; Tunggu <span class=\"param\">2</span> detik</span></div> <div><span class=\"block b-motion\"> Atur Kecepatan Kiri <span class=\"param\">50%</span> &amp; Kanan <span class=\"param\">52%</span></span></div> <div><span class=\"block b-control\"> Ulangi Selamanya</span></div> <div class=\"block-indent\"> <div><span class=\"block b-control\"> Jika <span class=\"param\"> Sensor Bawah == WARNA HITAM</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Kunci Rem Berhenti Total</span></div> <div><span class=\"block b-led\"> Kirim Status Web: <span class=\"param\">\"MISI PENYELAMATAN SUKSES!\"</span></span></div> <div><span class=\"block b-control\"> Selesai (Stop Program)</span></div> </div> <div><span class=\"block b-control\"> Jika Tidak, Jika <span class=\"param\"> Jarak Sensor Depan &lt; 13 cm</span> Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\"> Berhenti <span class=\"param\">0.3</span> dtk &rarr; ⬇ Mundur <span class=\"param\">0.4</span> dtk &rarr; ↪ Belok Kanan <span class=\"param\">0.54</span> dtk</span></div> </div> <div><span class=\"block b-control\"> Jika Tidak Maka</span></div> <div class=\"block-indent\"> <div><span class=\"block b-motion\">⬆ Maju Lurus Menjelajah</span></div> </div> </div> </div> </div>",
        "lks": "<p><strong>Rubrik Penilaian Akhir Semester (MazeBot Rescue Mission - Tingkat SD):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Komponen Penilaian</th><th>Bobot</th><th>Indikator Keberhasilan</th><th>Skor Kelompok (0–100)</th></tr> </thead> <tbody> <tr><td><strong>1. Kepatuhan SOP &amp; Keselamatan</strong></td><td>15%</td><td>Disiplin aturan baterai 18650 &amp; kerapian kerja tim</td><td>.............</td></tr> <tr><td><strong>2. Kerapian Balok Kode Visual</strong></td><td>25%</td><td>Susunan balok logis, lengkap (Start, Loop, If-Else)</td><td>.............</td></tr> <tr><td><strong>3. Keberhasilan Lewati Dinding</strong></td><td>30%</td><td>Mendeteksi rintangan &amp; berbelok 90° tanpa macet</td><td>.............</td></tr> <tr><td><strong>4. Ketepatan Berhenti di Finish</strong></td><td>30%</td><td>Otomatis mengunci roda tepat di atas kotak hitam</td><td>.............</td></tr> <tr><td colspan=\"3\"><strong>TOTAL NILAI AKHIR SEMESTER</strong></td><td><strong>............. / 100</strong></td></tr> </tbody> </table>",
        "troubleshooting": "Apresiasi setiap keberhasilan tahapan siswa! Jika robot berhasil melewati belokan namun meleset sedikit di garis finish, berikan kesempatan percobaan kedua (Run 2) setelah siswa memperbaiki sudut beloknya.",
        "pdf_url": "Modul_PDF_Per_Kode/SD/SD_M-16_Tantangan_Akhir_MazeBot_Rescue_Mission.pdf",
        "level": "SD"
      }
    ]
  },
  "SMP": {
    "id": "SMP",
    "name": "Tingkat SMP (Kelas 8–9)",
    "Badge": "TINGKAT SMP",
    "tagline": "Logika Pemrograman C++ & Navigasi Robot Otonom",
    "platform": "Hybrid Block-to-Text -> Arduino IDE (C++ Dasar) & IPA Fisika Kelas 8",
    "sop": "Pastikan polaritas baterai 18650 benar, hindari hubung singkat VCC-GND, dan uji arah putar motor sebelum ditaruh di lantai.",
    "book_pdf": "Modul_Ajar_MazeBot_SMP.pdf",
    "color": "#FFDE59",
    "modules": [
      {
        "code": "M-01",
        "title": "Pengenalan Komponen & Fungsi Modul MazeBot",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Memahami arsitektur sistem elektronik MazeBot secara modular (Input Sensor -> Mikrokontroler -> Driver Aktuator).",
          "Mengidentifikasi fungsi dan pemetaan pin (Pinout GPIO) pada ESP32, modul driver motor DRV8833, 3x sensor ultrasonik HC-SR04, dan sensor inframerah TCRT5000.",
          "Melakukan pengecekan perangkat keras dan menyalakan sistem uji diagnostik awal."
        ],
        "theory": "<p>Pada tingkat SMP, kita mempelajari MazeBot sebagai sebuah sistem tertanam (<em>Embedded System</em>) yang terdiri dari tiga blok fungsi utama: <strong>Input (Sensor)</strong>, <strong>Proses (Mikrokontroler ESP32)</strong>, dan <strong>Output (Driver Motor DRV8833 &amp; Roda)</strong>. Kita tidak perlu merakit komponen mikro di dalam keping PCB, melainkan memahami bagaimana antarmodul saling berkomunikasi melalui pin GPIO (<em>General Purpose Input/Output</em>).</p> <table class=\"std-table\"> <thead> <tr><th>Nama Modul</th><th>Kategori</th><th>Pin GPIO ESP32</th><th>Fungsi Teknis pada MazeBot</th></tr> </thead> <tbody> <tr><td><strong>ESP32 DevKit V1</strong></td><td>Pemroses Utama</td><td>32-bit Dual Core</td><td>Mengeksekusi program C++, mengolah sinyal sensor, dan memancarkan Wi-Fi.</td></tr> <tr><td><strong>Driver DRV8833</strong></td><td>Output Aktuator</td><td>IN1:25, IN2:26, IN3:27, IN4:14</td><td>Memperkuat arus listrik dari ESP32 untuk memutar 2 motor DC Gearbox TT.</td></tr> <tr><td><strong>3x HC-SR04</strong></td><td>Input Jarak</td><td>Kiri(32,35), Depan(33,34), Kanan(18,19)</td><td>Mengukur jarak dinding labirin dalam satuan sentimeter menggunakan gelombang ultrasonik.</td></tr> <tr><td><strong>TCRT5000</strong></td><td>Input Garis</td><td>DO: GPIO 4</td><td>Mendeteksi kontras warna hitam pada garis Finish di permukaan lantai.</td></tr> </tbody> </table>",
        "safety": "Pastikan polaritas baterai 18650 tidak terbalik dan jangan pernah menghubungkan pin VCC (5V/3.3V) langsung ke pin GND karena akan menyebabkan hubung singkat (short circuit).",
        "steps": [
          "Amati papan utama MazeBot dan identifikasi letak modul ESP32, modul merah/biru DRV8833, ketiga sensor ultrasonik, dan sensor TCRT5000 di bawah sasis.",
          "Hubungkan ESP32 ke komputer menggunakan kabel data Micro-USB / USB-C yang mendukung transfer data.",
          "Buka aplikasi Arduino IDE, pilih Board <strong>DOIT ESP32 DEVKIT V1</strong> dan Port COM yang sesuai.",
          "Unggah kode diagnostik M-01 di bawah ini untuk memastikan lampu indikator internal (GPIO 2) menyala dan pesan serial tampil di layar komputer."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-01: Diagnostik Sistem & Identifikasi Pinout MazeBot SMP\n// =========================================================================\n#define PIN_LED 2\n#define PIN_FINISH 4 void setup() { Serial.begin(115200); pinMode(PIN_LED, OUTPUT); pinMode(PIN_FINISH, INPUT); Serial.println(\"==========================================\"); Serial.println(\" SISTEM MAZEBOT EDUKIT SMP - AKTIF! \"); Serial.println(\" Otak: ESP32 | Driver: DRV8833 \"); Serial.println(\"==========================================\");\n} void loop() { digitalWrite(PIN_LED, HIGH); Serial.println(\"[STATUS] Sistem Normal - Siap Menerima Instruksi...\"); delay(1000); digitalWrite(PIN_LED, LOW); delay(1000);\n}",
        "lks": "<p><strong>Lembar Identifikasi Modul Hardware MazeBot:</strong></p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Komponen yang Diperiksa</th><th>Pin GPIO yang Terhubung</th><th>Mengapa ESP32 Butuh Modul Driver DRV8833?</th></tr> </thead> <tbody> <tr><td>1</td><td>Motor Kiri (Maju &amp; Mundur)</td><td>GPIO ..... &amp; GPIO .....</td><td rowspan=\"3\">Jelaskan: Karena arus dari pin GPIO ESP32 terlalu kecil (~40mA) sehingga tidak kuat memutar motor DC secara langsung tanpa penguat arus DRV8833.</td></tr> <tr><td>2</td><td>Motor Kanan (Maju &amp; Mundur)</td><td>GPIO ..... &amp; GPIO .....</td></tr> <tr><td>3</td><td>Sensor Garis Bawah (TCRT5000)</td><td>GPIO .....</td></tr> </tbody> </table>",
        "troubleshooting": "Jika Port COM tidak muncul di Arduino IDE, pastikan kabel USB yang dipakai bukan kabel 'charge-only' dan driver CP210x / CH340 sudah terinstal di komputer lab.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-01_Pengenalan_Komponen_Fungsi_Modul_MazeBot.pdf",
        "level": "SMP"
      },
      {
        "code": "M-02",
        "title": "Jembatan Transisi: Dari Balok ke Baris Kode",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Menggunakan fitur Side-by-Side Code Viewer untuk membandingkan balok visual (Blockly) dengan sintaks bahasa C++ Arduino.",
          "Memahami aturan penulisan dasar C++: tanda titik koma (;), kurung kurawal ({ }), dan huruf besar-kecil (Case Sensitive).",
          "Menerjemahkan program balok sederhana ke dalam teks C++ secara mandiri."
        ],
        "theory": "<p>Di tingkat SD kita menyusun balok puzzle visual. Tahukah kamu bahwa di balik setiap balok warna-warni tersebut sebenarnya tersimpan baris kode bahasa <strong>C++</strong>? Pada modul jembatan ini, kita membuka jendela <strong>Side-by-Side (Berdampingan)</strong> untuk melihat terjemahan langsung dari balok ke teks C++:</p> <table class=\"std-table\"> <thead> <tr><th>Balok Visual (Blockly)</th><th>Terjemahan Sintaks C++ (Arduino IDE)</th><th>Aturan Penting Sintaks</th></tr> </thead> <tbody> <tr><td><code>[Saat Program Dimulai]</code></td><td><code>void setup() { ... }</code></td><td>Dijalankan 1 kali saja saat robot baru menyala.</td></tr> <tr><td><code>[Ulangi Selamanya]</code></td><td><code>void loop() { ... }</code></td><td>Diulang terus-menerus selama robot menyala.</td></tr> <tr><td><code>[Tunggu 1 detik]</code></td><td><code>delay(1000);</code></td><td>1 detik = 1000 milidetik (ms). Wajib diakhiri titik koma <code>;</code></td></tr> <tr><td><code>[Jika (Jarak &lt; 10) Maka]</code></td><td><code>if (jarak &lt; 10) { ... }</code></td><td>Syarat ditulis di dalam <code>( )</code>, aksi di dalam <code>{ }</code>.</td></tr> </tbody> </table>",
        "safety": "Perhatikan penulisan huruf besar dan kecil pada kode C++. Menulis 'digitalwrite' (huruf w kecil) akan menghasilkan pesan error karena yang benar adalah 'digitalWrite' (huruf W besar).",
        "steps": [
          "Buka mode <strong>Side-by-Side Block-to-C++ Viewer</strong> pada aplikasi MazeBot.",
          "Tarik balok <strong>[Nyalakan LED]</strong> dan <strong>[Tunggu 0.5 detik]</strong> ke kanvas kiri, lalu amati kode C++ yang muncul otomatis di panel kanan.",
          "Salin kode C++ tersebut ke Arduino IDE, lalu coba ubah angka <code>delay(500);</code> menjadi <code>delay(200);</code> langsung pada teks kodenya.",
          "Klik tombol <strong>Verify (Centang)</strong> di Arduino IDE untuk mengecek apakah ada tanda titik koma (<code>;</code>) yang terlupa."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-02: Side-by-Side Translation (Dari Balok Visual ke C++ Murni)\n// =========================================================================\n#define PIN_LED 2 // [BALOK: Saat Program Dimulai]\nvoid setup() { pinMode(PIN_LED, OUTPUT); // Mengatur pin GPIO 2 sebagai keluaran\n} // [BALOK: Ulangi Selamanya]\nvoid loop() { // [BALOK: Lampu Indikator NYALA] digitalWrite(PIN_LED, HIGH); // [BALOK: Tunggu 0.5 Detik (500 milidetik)] delay(500); // [BALOK: Lampu Indikator MATI] digitalWrite(PIN_LED, LOW); // [BALOK: Tunggu 0.5 Detik (500 milidetik)] delay(500);\n}",
        "lks": "<p><strong>Latihan Terjemahan Balok ke C++:</strong> Tuliskan baris kode C++ yang setara dengan balok berikut!</p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Instruksi Balok Visual</th><th>Tuliskan Kode C++ yang Benar</th></tr> </thead> <tbody> <tr><td>1</td><td>Tunggu selama 2.5 detik</td><td><code>delay(..........);</code></td></tr> <tr><td>2</td><td>Nyalakan lampu pada PIN_LED</td><td><code>digitalWrite(.........., ..........);</code></td></tr> <tr><td>3</td><td>Jika jarak kurang dari 15 cm</td><td><code>if (....................) {</code></td></tr> </tbody> </table>",
        "troubleshooting": "Jika muncul error 'expected ; before } token', tunjukkan kepada siswa nomor baris yang berwarna merah di Arduino IDE—itu tandanya baris tepat di atasnya lupa diberi titik koma (;).",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-02_Jembatan_Transisi_Dari_Balok_ke_Baris_Ko.pdf",
        "level": "SMP"
      },
      {
        "code": "M-03",
        "title": "Struktur Program C++ (Setup, Loop, & Variabel)",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Memahami perbedaan peran fungsi void setup() dan void loop() dalam arsitektur program Arduino C++.",
          "Menggunakan tipe data variabel dasar (int untuk bilangan bulat, float untuk bilangan desimal) untuk menyimpan nilai kecepatan dan jarak.",
          "Menampilkan nilai variabel ke layar komputer menggunakan fitur Serial.print() dan Serial.println()."
        ],
        "theory": "<p>Dalam pemrograman C++, <strong>Variabel</strong> adalah sebuah kotak penyimpanan di dalam memori otak ESP32 yang diberi nama. Misalnya, daripada mengetik angka kecepatan berulang-ulang di banyak baris, kita cukup membuat variabel <code>int kecepatan = 180;</code>.</p> <ul> <li><strong><code>int</code> (Integer):</strong> Menyimpan angka bulat tanpa koma (contoh: <code>int kecepatan = 150;</code>, <code>int hitungan = 1;</code>).</li> <li><strong><code>float</code> (Floating Point):</strong> Menyimpan angka desimal berkoma (contoh: <code>float jarakCm = 12.45;</code>).</li> <li><strong>Serial Monitor:</strong> Jendela komunikasi teks antara robot dan layar komputer melalui kabel USB dengan kecepatan baca <code>115200</code> baud.</li> </ul>",
        "safety": "Pastikan angka baudrate di pojok kanan bawah jendela Serial Monitor diatur ke '115200 baud' (sama dengan angka di dalam Serial.begin) agar teks yang muncul tidak berupa simbol acak.",
        "steps": [
          "Ketikkan kode program M-03 di bawah ini pada lembar kerja baru (Sketch) di Arduino IDE.",
          "Perhatikan pendeklarasian variabel <code>int kecepatanMotor</code> dan <code>float batasJarakAman</code> di bagian atas program.",
          "Unggah program ke ESP32, lalu buka <strong>Tools &rarr; Serial Monitor</strong> (atau klik ikon kaca pembesar di pojok kanan atas).",
          "Amati bagaimana nilai variabel <code>hitunganDetik</code> bertambah 1 setiap detiknya di layar!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-03: Struktur C++ (Setup, Loop, Variabel int/float, & Serial Print)\n// ========================================================================= // Deklarasi Variabel Global\nint kecepatanMotor = 160; // Bilangan bulat (0 - 255)\nfloat batasJarakAman = 12.5; // Bilangan desimal (cm)\nint hitunganDetik = 0; // Variabel penghitung waktu void setup() { Serial.begin(115200); // Memulai komunikasi serial ke PC Serial.println(\"--- INISIALISASI VARIABEL MAZEBOT ---\"); Serial.print(\"Kecepatan Awal Motor (PWM): \"); Serial.println(kecepatanMotor); Serial.print(\"Batas Jarak Aman Dinding : \"); Serial.print(batasJarakAman); Serial.println(\" cm\"); Serial.println(\"-------------------------------------\");\n} void loop() { hitunganDetik = hitunganDetik + 1; Serial.print(\"Detik ke-\"); Serial.print(hitunganDetik); Serial.println(\" -> Robot aktif memantau sensor.\"); delay(1000); // Jeda 1000 ms (1 detik)\n}",
        "lks": "<p><strong>Eksperimen Variabel &amp; Tipe Data:</strong></p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Eksperimen Kode</th><th>Hasil yang Muncul di Serial Monitor</th></tr> </thead> <tbody> <tr><td>1</td><td>Simpan angka <code>15.75</code> ke dalam variabel bertipe <code>int</code></td><td>Angka di belakang koma menjadi: ....................</td></tr> <tr><td>2</td><td>Simpan angka <code>15.75</code> ke dalam variabel bertipe <code>float</code></td><td>Angka yang tampil adalah: ..........................</td></tr> <tr><td>3</td><td>Apa bedanya <code>Serial.print()</code> dengan <code>Serial.println()</code>?</td><td><code>println</code> membuat: .................................</td></tr> </tbody> </table>",
        "troubleshooting": "Jika tidak ada teks yang muncul di Serial Monitor setelah upload selesai, tekan tombol kecil bertuliskan 'EN' atau 'RST' (Reset) pada papan ESP32 untuk mengulang fungsi void setup() dari awal.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-03_Struktur_Program_C_Setup_Loop_Variabel.pdf",
        "level": "SMP"
      },
      {
        "code": "M-04",
        "title": "Fungsi Modular Gerak Robot",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Memahami cara kerja tabel kebenaran (Truth Table) H-Bridge modul driver motor DRV8833.",
          "Membuat fungsi modular C++ sendiri (maju(), mundur(), belokKiri(), belokKanan(), dan berhenti()) agar kode utama rapi dan mudah dibaca.",
          "Mengendalikan kecepatan putar motor menggunakan sinyal PWM (analogWrite rentang nilai 0–255)."
        ],
        "theory": "<p>Jika setiap kali ingin maju kita harus menulis 4 baris perintah pin motor di dalam <code>void loop()</code>, kode program kita akan menjadi sangat panjang dan membingungkan! Solusinya adalah <strong>Pemrograman Modular (Function)</strong>: kita membungkus perintah pin motor ke dalam fungsi bernama <code>maju(int spd)</code>, <code>belokKanan(int spd)</code>, dan <code>berhenti()</code>.</p> <table class=\"std-table\"> <thead> <tr><th>Nama Fungsi</th><th>Motor Kiri (IN1:25, IN2:26)</th><th>Motor Kanan (IN3:27, IN4:14)</th><th>Gerakan Fisik Robot</th></tr> </thead> <tbody> <tr><td><code>maju(spd)</code></td><td>IN1 = <code>spd</code>, IN2 = <code>0</code></td><td>IN3 = <code>spd</code>, IN4 = <code>0</code></td><td>Melaju lurus ke depan</td></tr> <tr><td><code>mundur(spd)</code></td><td>IN1 = <code>0</code>, IN2 = <code>spd</code></td><td>IN3 = <code>0</code>, IN4 = <code>spd</code></td><td>Melaju lurus ke belakang</td></tr> <tr><td><code>belokKiri(spd)</code></td><td>IN1 = <code>0</code>, IN2 = <code>spd</code> (Mundur)</td><td>IN3 = <code>spd</code>, IN4 = <code>0</code> (Maju)</td><td>Berputar poros ke kiri (Pivot Left)</td></tr> <tr><td><code>belokKanan(spd)</code></td><td>IN1 = <code>spd</code>, IN2 = <code>0</code> (Maju)</td><td>IN3 = <code>0</code>, IN4 = <code>spd</code> (Mundur)</td><td>Berputar poros ke kanan (Pivot Right)</td></tr> <tr><td><code>berhenti()</code></td><td>IN1 = <code>0</code>, IN2 = <code>0</code></td><td>IN3 = <code>0</code>, IN4 = <code>0</code></td><td>Kedua roda berhenti</td></tr> </tbody> </table>",
        "safety": "Saat pertama kali mengunggah kode motor, angkat sedikit bodi robot (atau letakkan di atas kotak kecil sehingga roda menggantung) untuk memastikan arah putar roda sudah benar sebelum ditaruh di lantai.",
        "steps": [
          "Ketikkan deklarasi pin motor DRV8833 dan kelima fungsi modular gerak seperti pada kode M-04 di bawah.",
          "Perhatikan betapa bersih dan singkatnya isi <code>void loop()</code> karena kita cukup memanggil nama fungsinya saja!",
          "Uji di lantai kelas dan sesuaikan nilai parameter <code>delay(...)</code> pada saat memanggil <code>belokKanan(160)</code> hingga sudut putarannya tepat 90 derajat."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-04: Fungsi Modular Gerak Robot dengan Driver DRV8833 (PWM 0-255)\n// =========================================================================\n#define IN1_KIRI_MAJU 25\n#define IN2_KIRI_MUNDUR 26\n#define IN3_KANAN_MAJU 27\n#define IN4_KANAN_MUNDUR 14 // --- FUNGSI MODULAR GERAK MOTOR ---\nvoid maju(int spd) { analogWrite(IN1_KIRI_MAJU, spd); analogWrite(IN2_KIRI_MUNDUR, 0); analogWrite(IN3_KANAN_MAJU, spd); analogWrite(IN4_KANAN_MUNDUR, 0);\n} void mundur(int spd) { analogWrite(IN1_KIRI_MAJU, 0); analogWrite(IN2_KIRI_MUNDUR, spd); analogWrite(IN3_KANAN_MAJU, 0); analogWrite(IN4_KANAN_MUNDUR, spd);\n} void belokKiri(int spd) { analogWrite(IN1_KIRI_MAJU, 0); analogWrite(IN2_KIRI_MUNDUR, spd); analogWrite(IN3_KANAN_MAJU, spd); analogWrite(IN4_KANAN_MUNDUR, 0);\n} void belokKanan(int spd) { analogWrite(IN1_KIRI_MAJU, spd); analogWrite(IN2_KIRI_MUNDUR, 0); analogWrite(IN3_KANAN_MAJU, 0); analogWrite(IN4_KANAN_MUNDUR, spd);\n} void berhenti() { analogWrite(IN1_KIRI_MAJU, 0); analogWrite(IN2_KIRI_MUNDUR, 0); analogWrite(IN3_KANAN_MAJU, 0); analogWrite(IN4_KANAN_MUNDUR, 0);\n} void setup() { pinMode(IN1_KIRI_MAJU, OUTPUT); pinMode(IN2_KIRI_MUNDUR, OUTPUT); pinMode(IN3_KANAN_MAJU, OUTPUT); pinMode(IN4_KANAN_MUNDUR, OUTPUT); berhenti(); delay(2000); // Jeda aman 2 detik sebelum bergerak\n} void loop() { maju(160); delay(1500); // Maju selama 1.5 detik berhenti(); delay(500); belokKanan(160); delay(450); // Belok Kanan 90 derajat berhenti(); delay(500); maju(160); delay(1500); berhenti(); while(true); // Berhenti selamanya setelah 1 siklus selesai\n}",
        "lks": "<p><strong>Uji Fungsi Modular &amp; Kalibrasi Waktu Belok:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Nama Fungsi yang Dipanggil</th><th>Nilai PWM (0–255)</th><th>Nilai <code>delay(ms)</code> yang Diuji</th><th>Hasil Gerakan Fisik Robot</th></tr> </thead> <tbody> <tr><td><code>maju(160)</code></td><td>160</td><td>1500 ms</td><td>Maju lurus sejauh ......... cm</td></tr> <tr><td><code>belokKanan(160)</code></td><td>160</td><td>....... ms (Cari yang pas 90&deg;)</td><td>Berputar tepat 90&deg; ke kanan</td></tr> <tr><td><code>belokKiri(160)</code></td><td>160</td><td>....... ms (Cari yang pas 90&deg;)</td><td>Berputar tepat 90&deg; ke kiri</td></tr> </tbody> </table>",
        "troubleshooting": "Jika saat dipanggil fungsi maju() salah satu roda justru berputar mundur, tukar definisi nomor pin IN1 dan IN2 (atau IN3 dan IN4) di bagian #define paling atas program.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-04_Fungsi_Modular_Gerak_Robot.pdf",
        "level": "SMP"
      },
      {
        "code": "M-05",
        "title": "Fisika Sensor Ultrasonik: Menghitung Jarak Bunyi",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP — Integrasi IPA Fisika Kelas 8)",
        "objectives": [
          "Menerapkan rumus fisika pemantulan gelombang bunyi s = (v x t) / 2 ke dalam baris kode pemrograman C++.",
          "Memahami konversi satuan cepat rambat bunyi di udara (340 m/s = 0.034 cm/mikrodetik).",
          "Mengukur durasi waktu tempuh gelombang pergi-pulang (Time of Flight) menggunakan fungsi pulseIn() dalam satuan mikrodetik."
        ],
        "theory": "<p>Materi ini terintegrasi langsung dengan pelajaran <strong>IPA Fisika Kelas 8 (Gelombang dan Bunyi)</strong>! Sensor HC-SR04 bekerja dengan memancarkan gelombang ultrasonik berfrekuensi <strong>40 kHz</strong> dari pin <strong>TRIG</strong>, lalu menghitung berapa mikrodetik (&mu;s) waktu yang dibutuhkan sampai pantulan suaranya diterima kembali oleh pin <strong>ECHO</strong>.</p> <div class=\"formula-box\"> Rumus Fisika Pantulan Bunyi: &nbsp;&nbsp; <i>s</i> = (<i>v</i> &times; <i>t</i>) / 2 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Jarak (cm) = (Durasi &mu;s &times; 0.034) / 2 </div> <p><strong>Mengapa harus dibagi 2?</strong> Karena waktu <i>t</i> yang diukur oleh sensor adalah waktu perjalanan gelombang bunyi <em>Pergi (dari robot ke dinding)</em> ditambah waktu <em>Pulang (dari dinding kembali ke robot)</em>. Padahal jarak robot ke dinding hanyalah separuh dari lintasan bolak-balik tersebut!</p>",
        "safety": "Perhatikan bahwa pin ECHO sensor depan terhubung ke GPIO 34 pada ESP32. Pin GPIO 34 dan 35 pada ESP32 adalah pin khusus INPUT-ONLY, sehingga tidak boleh diatur sebagai OUTPUT.",
        "steps": [
          "Siapkan penggaris 30 cm dan sebuah papan/buku tebal sebagai bidang pantul di depan sensor depan robot.",
          "Ketikkan fungsi perhitungan fisika ultrasonik pada kode M-05 di bawah ini.",
          "Unggah program dan buka Serial Monitor. Bandingkan nilai durasi mikrodetik (&mu;s) dan hasil konversi sentimeter (cm) dengan ukuran penggaris asli!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-05: Fisika Gelombang Bunyi pada Sensor Ultrasonik (s = v * t / 2)\n// =========================================================================\n#define TRIG_DEPAN 33\n#define ECHO_DEPAN 34 void setup() { Serial.begin(115200); pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT);\n} void loop() { // 1. Berikan pulsa pemicu (Trigger) selama 10 mikrodetik digitalWrite(TRIG_DEPAN, LOW); delayMicroseconds(2); digitalWrite(TRIG_DEPAN, HIGH); delayMicroseconds(10); digitalWrite(TRIG_DEPAN, LOW); // 2. Ukur waktu tempuh gelombang pergi-pulang (t) dalam mikrodetik (us) long durasiMikrodetik = pulseIn(ECHO_DEPAN, HIGH, 30000); // Timeout 30.000 us // 3. Terapkan Rumus Fisika: s = (v * t) / 2 dengan v = 0.034 cm/us float jarakCm = (durasiMikrodetik * 0.034) / 2.0; // 4. Tampilkan hasil ke Serial Monitor Serial.print(\"Waktu Pantul (t): \"); Serial.print(durasiMikrodetik); Serial.print(\" us | Jarak Hitung (s): \"); Serial.print(jarakCm); Serial.println(\" cm\"); delay(300);\n}",
        "lks": "<p><strong>Lembar Kerja Eksperimen Fisika Bunyi (IPA &times; Robotika):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Jarak Sebenarnya (Penggaris)</th><th>Durasi Pantul <i>t</i> (&mu;s) di Serial Monitor</th><th>Perhitungan Manual (<i>t</i> &times; 0.034) / 2</th><th>Bacaan Sensor Robot (cm)</th></tr> </thead> <tbody> <tr><td>10 cm</td><td>.............. &mu;s</td><td>.............. cm</td><td>.............. cm</td></tr> <tr><td>20 cm</td><td>.............. &mu;s</td><td>.............. cm</td><td>.............. cm</td></tr> <tr><td>30 cm</td><td>.............. &mu;s</td><td>.............. cm</td><td>.............. cm</td></tr> </tbody> </table>",
        "troubleshooting": "Selalu sertakan parameter ke-3 berupa angka timeout 30000 pada pulseIn(ECHO, HIGH, 30000) agar jika tidak ada penghalang di depan robot, program tidak macet menunggu pantulan suara terlalu lama.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-05_Fisika_Sensor_Ultrasonik_Menghitung_Jara.pdf",
        "level": "SMP"
      },
      {
        "code": "M-06",
        "title": "Membaca 3 Arah Sensor (Kiri, Depan, Kanan) & Anti-Crosstalk",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Membuat fungsi berparameter bacaUltrasonik(int trigPin, int echoPin) yang dapat digunakan ulang untuk ketiga sensor.",
          "Memahami fenomena gangguan akustik (Ultrasonic Crosstalk) apabila 3 sensor menembakkan suara terlalu berdekatan.",
          "Menerapkan jeda aman sekuensial (15–25 ms) antar pembacaan sensor Kiri, Depan, dan Kanan."
        ],
        "theory": "<p>MazeBot memiliki 3 sensor ultrasonik yang menghadap ke <strong>Kiri</strong>, <strong>Depan</strong>, dan <strong>Kanan</strong>. Apa yang terjadi jika ketiga sensor memancarkan gelombang bunyi secara bersamaan di dalam lorong labirin yang sempit? Pantulan suara dari sensor Kiri bisa memantul ke dinding lalu masuk ke telinga sensor Depan! Gangguan tabrakan gema ini disebut <strong>Crosstalk</strong>.</p> <p>Untuk mencegahnya, kita membaca ketiga sensor <strong>secara bergantian (sekuensial)</strong> dengan memberikan jeda hening singkat (<code>delay(20)</code> milidetik) supaya gema sensor sebelumnya hilang terlebih dahulu sebelum sensor berikutnya berbunyi.</p>",
        "safety": "Pastikan kabel jumper atau soket ketiga sensor ultrasonik terpasang kencang dan tidak menghalangi putaran roda kiri maupun roda kanan.",
        "steps": [
          "Perhatikan bagaimana kita membuat satu fungsi pintar <code>float bacaUltrasonik(int trig, int echo)</code> yang mengembalikan nilai <code>return jarak;</code>.",
          "Di dalam <code>void loop()</code>, panggil fungsi tersebut berurutan untuk sensor Kiri, jeda 20 ms, sensor Depan, jeda 20 ms, lalu sensor Kanan.",
          "Letakkan robot di dalam lorong kardus dan amati ketiga nilai jarak secara langsung pada Serial Monitor!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-06: Pembacaan 3 Sensor Sekuensial dengan Jeda Aman Anti-Crosstalk\n// =========================================================================\n#define TRIG_KIRI 32\n#define ECHO_KIRI 35\n#define TRIG_DEPAN 33\n#define ECHO_DEPAN 34\n#define TRIG_KANAN 18\n#define ECHO_KANAN 19 // Fungsi Reusable untuk membaca sensor ultrasonik mana saja\nfloat bacaUltrasonik(int trigPin, int echoPin) { digitalWrite(trigPin, LOW); delayMicroseconds(2); digitalWrite(trigPin, HIGH); delayMicroseconds(10); digitalWrite(trigPin, LOW); long durasi = pulseIn(echoPin, HIGH, 25000); // Timeout 25 ms (~4 meter) if (durasi == 0) return 999.0; // Jika ruang kosong jauh (tidak ada pantulan) return (durasi * 0.034) / 2.0;\n} void setup() { Serial.begin(115200); pinMode(TRIG_KIRI, OUTPUT); pinMode(ECHO_KIRI, INPUT); pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT); pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT);\n} void loop() { float jarakKiri = bacaUltrasonik(TRIG_KIRI, ECHO_KIRI); delay(20); // Jeda Anti-Crosstalk agar gema suara kiri reda float jarakDepan = bacaUltrasonik(TRIG_DEPAN, ECHO_DEPAN); delay(20); // Jeda Anti-Crosstalk agar gema suara depan reda float jarakKanan = bacaUltrasonik(TRIG_KANAN, ECHO_KANAN); delay(20); Serial.print(\"[RADAR] Kiri: \"); Serial.print(jarakKiri, 1); Serial.print(\" cm | Depan: \"); Serial.print(jarakDepan, 1); Serial.print(\" cm | Kanan: \"); Serial.print(jarakKanan, 1); Serial.println(\" cm\"); delay(200);\n}",
        "lks": "<p><strong>Tabel Pemetaan Radar 3 Arah di Berbagai Posisi Labirin:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Posisi Robot di Labirin</th><th>Bacaan Sensor Kiri (cm)</th><th>Bacaan Sensor Depan (cm)</th><th>Bacaan Sensor Kanan (cm)</th></tr> </thead> <tbody> <tr><td>Di tengah lorong lurus</td><td>.......... cm</td><td>.......... cm</td><td>.......... cm</td></tr> <tr><td>Menghadap tikungan siku kiri</td><td>.......... cm</td><td>.......... cm</td><td>.......... cm</td></tr> <tr><td>Di ujung jalan buntu (Dead-End)</td><td>.......... cm</td><td>.......... cm</td><td>.......... cm</td></tr> </tbody> </table>",
        "troubleshooting": "Perhatikan baris 'if (durasi == 0) return 999.0;' pada kode! Baris ini sangat penting karena saat di depan robot tidak ada dinding sama sekali, pulseIn menghasilkan angka 0. Jika tidak diubah menjadi 999.0 cm, robot akan mengira di depannya ada dinding menempel (0 cm)!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-06_Membaca_3_Arah_Sensor_Kiri_Depan_Kanan_A.pdf",
        "level": "SMP"
      },
      {
        "code": "M-07",
        "title": "Logika Percabangan Majemuk (IF - ELSE IF - ELSE)",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Menerapkan struktur percabangan majemuk if (...) { } else if (...) { } else { } dalam bahasa C++.",
          "Mengolah data 3 sensor ultrasonik untuk menentukan satu keputusan arah gerak berdasarkan urutan prioritas.",
          "Memahami bahwa dalam struktur if - else if, hanya blok pertama yang bernilai benar (TRUE) yang akan dieksekusi."
        ],
        "theory": "<p>Ketika robot berada di persimpangan yang memiliki lebih dari satu jalur terbuka (misalnya Kiri terbuka dan Depan juga terbuka), robot tidak mungkin membelah diri menjadi dua! Oleh karena itu, kita menggunakan struktur <strong>Percabangan Berjenjang (<code>if - else if - else</code>)</strong> untuk memberikan urutan prioritas berpikir kepada robot:</p> <ol> <li><code>if (jarakDepan &gt; 15)</code> &rarr; Prioritas 1: Jika depan kosong, maju lurus!</li> <li><code>else if (jarakKiri &gt; 15)</code> &rarr; Prioritas 2: Jika depan tertutup tapi kiri terbuka, belok kiri!</li> <li><code>else if (jarakKanan &gt; 15)</code> &rarr; Prioritas 3: Jika depan dan kiri tertutup tapi kanan terbuka, belok kanan!</li> <li><code>else</code> &rarr; Pilihan Terakhir: Jika semua tertutup, berhenti!</li> </ol>",
        "safety": "Uji logika percabangan terlebih dahulu melalui teks di Serial Monitor sebelum mengaktifkan motor agar siswa benar-benar paham alur pengambilan keputusan robot.",
        "steps": [
          "Gabungkan kode pembacaan 3 sensor (M-06) dengan blok logika <code>if - else if - else</code> seperti pada kode M-07.",
          "Gunakan dua buah buku sebagai dinding buatan untuk menutup sensor depan, kiri, atau kanan secara bergantian.",
          "Amati keputusan yang dicetak oleh robot di Serial Monitor, lalu aktifkan pemanggilan fungsi motornya!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-07: Logika Percabangan Majemuk (IF - ELSE IF - ELSE)\n// =========================================================================\n// (Gunakan definisi pin & fungsi bacaUltrasonik dari Modul M-06)\n#define BATAS_TERBUKA 15.0 // Jarak > 15 cm dianggap jalan terbuka/kosong void evaluasiKeputusan(float kiri, float depan, float kanan) { if (depan > BATAS_TERBUKA) { Serial.println(\"KEPUTUSAN: Jalan Depan Kosong -> MAJU LURUS\"); // maju(150); } else if (kiri > BATAS_TERBUKA) { Serial.println(\"KEPUTUSAN: Depan Tertutup, Kiri Terbuka -> BELOK KIRI\"); // belokKiri(160); delay(450); } else if (kanan > BATAS_TERBUKA) { Serial.println(\"KEPUTUSAN: Depan & Kiri Tertutup, Kanan Terbuka -> BELOK KANAN\"); // belokKanan(160); delay(450); } else { Serial.println(\"KEPUTUSAN: Semua Arah Tertutup -> JALAN BUNTU (STOP)\"); // berhenti(); }\n}",
        "lks": "<p><strong>Uji Meja Kebenaran Logika (Truth Table) Percabangan:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Kasus</th><th>Nilai Kiri</th><th>Nilai Depan</th><th>Nilai Kanan</th><th>Keputusan Mana yang Diambil oleh Kode M-07?</th></tr> </thead> <tbody> <tr><td>1</td><td>8 cm</td><td>45 cm</td><td>9 cm</td><td>........................................................</td></tr> <tr><td>2</td><td>35 cm</td><td>7 cm</td><td>40 cm</td><td>........................................................</td></tr> <tr><td>3</td><td>6 cm</td><td>8 cm</td><td>30 cm</td><td>........................................................</td></tr> <tr><td>4</td><td>7 cm</td><td>6 cm</td><td>8 cm</td><td>........................................................</td></tr> </tbody> </table>",
        "troubleshooting": "Perhatikan Kasus nomor 2 pada LKS (Kiri=35 cm, Depan=7 cm, Kanan=40 cm): karena 'else if (kiri > 15)' ditulis lebih dulu di atas 'else if (kanan > 15)', maka robot pasti memilih BELOK KIRI!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-07_Logika_Percabangan_Majemuk_IF_ELSE_IF_EL.pdf",
        "level": "SMP"
      },
      {
        "code": "M-08",
        "title": "Ujian Tengah Semester (Proyek Mini 2: Uji Refleks Radar Persimpangan T)",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Mengintegrasikan fungsi modular motor (M-04), pembacaan 3 sensor ultrasonik (M-06), dan percabangan majemuk (M-07).",
          "Menyelesaikan misi Uji Refleks Radar: robot melaju memasuki Persimpangan T dan secara otonom berbelok ke arah cabang yang tidak buntu.",
          "Mengevaluasi ketepatan sintaks C++ dan kemandirian pemecahan masalah tiap kelompok."
        ],
        "theory": "<p>Pada <strong>Ujian Tengah Semester (Proyek Mini 2)</strong> ini, setiap kelompok diuji pada arena <strong>Persimpangan Huruf T (T-Junction)</strong>. Robot diletakkan di lorong tengah menuju pertigaan T. Penguji (Guru) akan menutup salah satu cabang pertigaan (Kiri atau Kanan) secara acak menggunakan papan penghalang.</p> <p>Begitu robot mendeteksi dinding pertigaan di depannya, robot harus berhenti sejenak, memindai jarak Kiri dan Kanan, lalu <strong>memilih berbelok ke sisi yang terbuka lebar</strong> tanpa menyentuh dinding!</p>",
        "safety": "Pastikan kecepatan maju tidak terlalu kencang (gunakan PWM sekitar 140–160) agar robot sempat berhenti dan memindai pertigaan sebelum hidungnya menabrak dinding depan.",
        "steps": [
          "Tulis dan lengkapi program utuh Proyek Mini 2 di bawah ini pada Arduino IDE.",
          "Unggah ke MazeBot dan lakukan uji coba mandiri di meja kelompok.",
          "Majulah ke arena ujian Persimpangan T. Guru akan melakukan 2 kali pengujian: Skenario A (Cabang Kiri ditutup) dan Skenario B (Cabang Kanan ditutup)."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-08: UTS PROYEK MINI 2 - Uji Refleks Radar di Persimpangan T\n// =========================================================================\n#define IN1 25\n#define IN2 26\n#define IN3 27\n#define IN4 14\n#define TRIG_KIRI 32\n#define ECHO_KIRI 35\n#define TRIG_DEPAN 33\n#define ECHO_DEPAN 34\n#define TRIG_KANAN 18\n#define ECHO_KANAN 19 float bacaSensor(int trig, int echo) { digitalWrite(trig, LOW); delayMicroseconds(2); digitalWrite(trig, HIGH); delayMicroseconds(10); digitalWrite(trig, LOW); long d = pulseIn(echo, HIGH, 25000); return (d == 0) ? 999.0 : (d * 0.034) / 2.0;\n} void gerak(int kiriMaju, int kiriMundur, int kananMaju, int kananMundur) { analogWrite(IN1, kiriMaju); analogWrite(IN2, kiriMundur); analogWrite(IN3, kananMaju); analogWrite(IN4, kananMundur);\n} void setup() { pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); pinMode(TRIG_KIRI, OUTPUT); pinMode(ECHO_KIRI, INPUT); pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT); pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT); gerak(0, 0, 0, 0); delay(2000);\n} void loop() { float depan = bacaSensor(TRIG_DEPAN, ECHO_DEPAN); delay(20); if (depan > 14.0) { gerak(150, 0, 150, 0); // Maju lurus selama depan aman } else { gerak(0, 0, 0, 0); // Berhenti di mulut Persimpangan T delay(300); // Beri waktu stabil untuk memindai kiri & kanan float kiri = bacaSensor(TRIG_KIRI, ECHO_KIRI); delay(20); float kanan = bacaSensor(TRIG_KANAN, ECHO_KANAN); delay(20); if (kiri > kanan && kiri > 18.0) { gerak(0, 160, 160, 0); delay(450); // Belok Kiri 90 derajat } else if (kanan > 18.0) { gerak(160, 0, 0, 160); delay(450); // Belok Kanan 90 derajat } gerak(0, 0, 0, 0); delay(200); }\n}",
        "lks": "<p><strong>Lembar Penilaian Ujian Tengah Semester (Proyek Mini 2 - SMP):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Pengujian</th><th>Kondisi Pertigaan T</th><th>Respon yang Diharapkan</th><th>Hasil Uji (Berhasil / Gagal)</th><th>Skor (Maks 50)</th></tr> </thead> <tbody> <tr><td>Uji 1</td><td>Sisi Kanan Ditutup, Kiri Terbuka</td><td>Berhenti di T &rarr; Belok Kiri &rarr; Maju</td><td>Berhasil / Gagal</td><td>....... / 50</td></tr> <tr><td>Uji 2</td><td>Sisi Kiri Ditutup, Kanan Terbuka</td><td>Berhenti di T &rarr; Belok Kanan &rarr; Maju</td><td>Berhasil / Gagal</td><td>....... / 50</td></tr> <tr><td colspan=\"4\"><strong>TOTAL NILAI UTS PRAKTIKUM SMP</strong></td><td><strong>....... / 100</strong></td></tr> </tbody> </table>",
        "troubleshooting": "Perhatikan kondisi 'if (kiri > kanan && kiri > 18.0)': membandingkan 'kiri > kanan' memastikan robot memilih lorong yang paling lapang di pertigaan T!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-08_Ujian_Tengah_Semester_Proyek_Mini_2_Uji_.pdf",
        "level": "SMP"
      },
      {
        "code": "M-09",
        "title": "Sensor TCRT5000 sebagai Pemicu Garis Finish",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Membaca sinyal digital (HIGH / LOW) dari modul sensor reflektif inframerah TCRT5000 menggunakan digitalRead().",
          "Memahami cara kerja komparator LM393 pada modul TCRT5000 yang mengubah pantulan cahaya menjadi logika biner (1 atau 0).",
          "Menggunakan deteksi garis hitam untuk memutus loop navigasi dan mengunci penghentian robot di garis Finish."
        ],
        "theory": "<p>Pada MazeBot EduKit, sensor <strong>TCRT5000</strong> yang dipasang di kolong depan dikhususkan murni sebagai <strong>Detektor Garis Finish</strong> (bukan pendeteksi persimpangan). Modul ini dilengkapi IC komparator yang mengeluarkan logika digital pada pin <strong>DO (Digital Output - GPIO 4)</strong>:</p> <ul> <li><strong>Lantai Putih (Memantulkan Inframerah):</strong> Pin DO bernilai <code>LOW (0)</code>.</li> <li><strong>Garis Lakban Hitam (Menyerap Inframerah):</strong> Pin DO bernilai <code>HIGH (1)</code>.</li> </ul> <p>Saat bernilai <code>HIGH</code>, program akan mengubah variabel status <code>bool misiSelesai = true;</code> sehingga robot menghentikan seluruh roda dan keluar dari siklus penjelajahan.</p>",
        "safety": "Kalibrasi trimpot (potensiometer biru) pada modul TCRT5000 menggunakan obeng plus kecil hanya bila sensitivitas cahaya ruangan berubah drastis.",
        "steps": [
          "Unggah kode M-09 di bawah ini untuk menguji penguncian status Finish.",
          "Letakkan robot di lantai putih; robot akan berjalan maju perlahan.",
          "Hadang jalur depan robot dengan lakban hitam yang ditempel di lantai. Pastikan begitu sensor TCRT5000 melewati lakban hitam, robot langsung berhenti permanen!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-09: Sensor Inframerah TCRT5000 sebagai Pengunci Garis Finish\n// =========================================================================\n#define PIN_FINISH 4\n#define PIN_LED 2\n#define IN1 25\n#define IN2 26\n#define IN3 27\n#define IN4 14 bool misiSelesai = false; // Flag pengunci status finish void berhentiTotal() { analogWrite(IN1, 0); analogWrite(IN2, 0); analogWrite(IN3, 0); analogWrite(IN4, 0);\n} void setup() { Serial.begin(115200); pinMode(PIN_FINISH, INPUT); pinMode(PIN_LED, OUTPUT); pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); delay(2000);\n} void loop() { // Jika sudah menyentuh finish, kunci robot dalam keadaan diam! if (misiSelesai == true) { berhentiTotal(); return; // Langsung keluar dari loop() } int statusGaris = digitalRead(PIN_FINISH); if (statusGaris == HIGH) { // HIGH = Mendeteksi Garis Hitam Finish berhentiTotal(); digitalWrite(PIN_LED, HIGH); misiSelesai = true; // Kunci flag agar tidak jalan lagi Serial.println(\"GARIS FINISH TERDETEKSI! Navigasi Dihentikan.\"); } else { // Selama masih lantai putih (LOW), terus melaju analogWrite(IN1, 145); analogWrite(IN2, 0); analogWrite(IN3, 145); analogWrite(IN4, 0); }\n}",
        "lks": "<p><strong>Tabel Pengujian Sensor Garis TCRT5000:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Permukaan Lantai</th><th>Nilai <code>digitalRead(PIN_FINISH)</code></th><th>Nilai Variabel <code>misiSelesai</code></th><th>Kondisi Motor Roda</th></tr> </thead> <tbody> <tr><td>Keramik Putih</td><td><code>LOW (0)</code> / <code>HIGH (1)</code></td><td><code>false</code> / <code>true</code></td><td>Berputar / Berhenti</td></tr> <tr><td>Garis Lakban Hitam</td><td><code>LOW (0)</code> / <code>HIGH (1)</code></td><td><code>false</code> / <code>true</code></td><td>Berputar / Berhenti</td></tr> <tr><td>Diangkat kembali ke Putih setelah Finish</td><td><code>LOW (0)</code></td><td>Tetap <code>true</code> (Terkunci)</td><td>Tetap Berhenti</td></tr> </tbody> </table>",
        "troubleshooting": "Beberapa modul TCRT5000 di pasaran memiliki logika terbalik (LOW saat hitam). Jika demikian, cukup ubah syarat 'if (statusGaris == HIGH)' menjadi 'if (statusGaris == LOW)'.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-09_Sensor_TCRT5000_sebagai_Pemicu_Garis_Fin.pdf",
        "level": "SMP"
      },
      {
        "code": "M-10",
        "title": "Teori Algoritma Menyusuri Dinding (Left-Hand Rule)",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Memahami konsep matematis algoritma penelusuran labirin Wall-Follower (Aturan Tangan Kiri / Left-Hand Rule).",
          "Menyusun tabel aturan prioritas keputusan navigasi: Kiri -> Depan -> Kanan -> Putar Balik (U-Turn).",
          "Mensimulasikan jejak perjalanan robot di atas peta labirin kertas sebelum menulis kode."
        ],
        "theory": "<p>Bagaimana seorang penjelajah bisa dijamin keluar dari labirin yang rumit tanpa peta? Dalam ilmu komputer dan matematika topologi, terdapat algoritma klasik bernama <strong>Wall-Follower: Left-Hand Rule (Aturan Tangan Kiri)</strong>. Bayangkan kamu berjalan di dalam labirin sambil terus menyentuhkan tangan kirimu ke dinding sebelah kiri tanpa pernah melepaskannya!</p> <p>Jika diterjemahkan menjadi aturan algoritma prioritas untuk MazeBot setiap kali menemui persimpangan:</p> <ol> <li><strong>Prioritas 1 (Cek Kiri):</strong> Apakah dinding di sebelah KIRI terbuka? Jika YA &rarr; <strong>Wajib Belok Kiri!</strong></li> <li><strong>Prioritas 2 (Cek Depan):</strong> Jika kiri tertutup, apakah DEPAN terbuka? Jika YA &rarr; <strong>Maju Lurus!</strong></li> <li><strong>Prioritas 3 (Cek Kanan):</strong> Jika kiri dan depan tertutup, apakah KANAN terbuka? Jika YA &rarr; <strong>Belok Kanan!</strong></li> <li><strong>Prioritas 4 (Buntu):</strong> Jika Kiri, Depan, dan Kanan semuanya tertutup dinding &rarr; <strong>Putar Balik 180&deg; (U-Turn)!</strong></li> </ol>",
        "safety": "Pada sesi ini siswa fokus merancang flowchart dan simulasi algoritma menggunakan pion robot di atas peta labirin sebelum memprogram gerakan fisik.",
        "steps": [
          "Perhatikan gambar peta labirin yang memiliki 2 jalan buntu dan 1 jalur keluar menuju Finish.",
          "Gunakan penghapus atau miniatur robot, lalu gerakkan mengikuti aturan ketat <em>Left-Hand Rule</em> (selalu utamakan belok kiri setiap ada bukaan kiri).",
          "Tandai rute yang dilalui dengan pensil dan buktikan bahwa meskipun sempat masuk ke jalan buntu, aturan ini selalu berhasil membawa robot keluar ke garis Finish!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-10: Pseudocode & Kerangka Logika Algoritma Left-Hand Rule\n// ========================================================================= void algoritmaLeftHandRule(float jarakKiri, float jarakDepan, float jarakKanan) { const float AMBANG_BUKAAN = 18.0; // Lorong dianggap terbuka jika > 18 cm const float AMBANG_DEPAN = 13.0; // Batas aman depan sebelum menabrak // PRIORITAS 1: Cek apakah ada bukaan belokan di sebelah KIRI if (jarakKiri > AMBANG_BUKAAN) { Serial.println(\"[LHR] Bukaan Kiri Terdeteksi -> Ambil Belok KIRI!\"); // Maju sedikit ke tengah simpang -> Belok Kiri 90 -> Maju masuk lorong baru } // PRIORITAS 2: Jika Kiri tertutup dinding, cek apakah DEPAN bebas else if (jarakDepan > AMBANG_DEPAN) { Serial.println(\"[LHR] Kiri Dinding, Depan Bebas -> MAJU LURUS!\"); } // PRIORITAS 3: Jika Kiri & Depan tertutup, cek apakah KANAN terbuka else if (jarakKanan > AMBANG_BUKAAN) { Serial.println(\"[LHR] Kiri & Depan Tertutup -> Ambil Belok KANAN!\"); } // PRIORITAS 4: Ketiga arah tertutup (Jalan Buntu / Dead-End) else { Serial.println(\"[LHR] JALAN BUNTU! -> Eksekusi Putar Balik 180 Derajat!\"); }\n}",
        "lks": "<p><strong>Uji Pemahaman Algoritma Left-Hand Rule:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Kondisi Persimpangan yang Dihadapi Robot</th><th>Bukaan yang Tersedia</th><th>Keputusan Robot (Left-Hand Rule)</th></tr> </thead> <tbody> <tr><td>Simpang Empat (Crossroad +)</td><td>Kiri, Depan, dan Kanan Terbuka</td><td>Harus memilih: ..........................</td></tr> <tr><td>Simpang Tiga Kiri</td><td>Kiri dan Depan Terbuka</td><td>Harus memilih: ..........................</td></tr> <tr><td>Simpang Tiga Kanan</td><td>Depan dan Kanan Terbuka (Kiri Dinding)</td><td>Harus memilih: ..........................</td></tr> <tr><td>Ujung Lorong Buntu</td><td>Tidak ada yang terbuka</td><td>Harus memilih: ..........................</td></tr> </tbody> </table>",
        "troubleshooting": "Pastikan siswa memahami bahwa pada Simpang Tiga Kanan (Depan & Kanan terbuka, sedangkan Kiri tertutup dinding), robot memilih MAJU LURUS (bukan belok kanan) karena Prioritas 2 adalah Depan!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-10_Teori_Algoritma_Menyusuri_Dinding_Left_H.pdf",
        "level": "SMP"
      },
      {
        "code": "M-11",
        "title": "Implementasi Left-Hand Rule Dasar",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Menerjemahkan algoritma Left-Hand Rule (M-10) menjadi kode C++ utuh yang menggerakkan motor MazeBot.",
          "Memahami teknik Step-Forward Alignment (maju sedikit sebelum belok kiri) agar bodi robot berputar tepat di tengah mulut persimpangan.",
          "Menguji navigasi Left-Hand Rule pada labirin dengan 2 persimpangan."
        ],
        "theory": "<p>Saat mengimplementasikan <em>Left-Hand Rule</em> ke robot nyata, ada satu trik mekanik yang sangat penting: ketika sensor samping kiri pertama kali melihat celah lorong terbuka (<code>jarakKiri &gt; 20 cm</code>), posisi roda robot sebenarnya baru berada di <em>bibir awal</em> persimpangan!</p> <p>Jika robot langsung berputar di tempat saat itu juga, bagian belakang robot akan menyangkut di sudut dinding. Oleh karena itu, sebelum mengeksekusi <code>belokKiri()</code>, robot harus: (1) <strong>Maju sedikit (~250 ms)</strong> agar badan robot pas di tengah simpang, (2) <strong>Belok Kiri 90&deg;</strong>, lalu (3) <strong>Maju masuk ke lorong baru (~400 ms)</strong> agar keluar dari area simpang.</p>",
        "safety": "Awasi gerakan robot di persimpangan. Siapkan tangan di dekat saklar jika sudut belok belum terkalibrasi sehingga robot menyerempet dinding.",
        "steps": [
          "Ketik dan unggah program implementasi Left-Hand Rule Dasar (M-11) di bawah ini.",
          "Perhatikan blok <code>if (kiri &gt; 20.0)</code> yang menyertakan dorongan maju sebelum dan sesudah berputar.",
          "Uji robot di arena labirin dan amati bagaimana robot secara konsisten mengambil belokan kiri setiap kali menemukan lorong di sebelah kirinya!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-11: Implementasi Navigasi Left-Hand Rule Dasar di C++\n// =========================================================================\n#define IN1 25\n#define IN2 26\n#define IN3 27\n#define IN4 14\n#define TRIG_KIRI 32\n#define ECHO_KIRI 35\n#define TRIG_DEPAN 33\n#define ECHO_DEPAN 34\n#define TRIG_KANAN 18\n#define ECHO_KANAN 19 float bacaJarak(int trig, int echo) { digitalWrite(trig, LOW); delayMicroseconds(2); digitalWrite(trig, HIGH); delayMicroseconds(10); digitalWrite(trig, LOW); long d = pulseIn(echo, HIGH, 25000); return (d == 0) ? 999.0 : (d * 0.034) / 2.0;\n} void setMotor(int L1, int L2, int R1, int R2) { analogWrite(IN1, L1); analogWrite(IN2, L2); analogWrite(IN3, R1); analogWrite(IN4, R2);\n} void setup() { pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); pinMode(TRIG_KIRI, OUTPUT); pinMode(ECHO_KIRI, INPUT); pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT); pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT); setMotor(0, 0, 0, 0); delay(2000);\n} void loop() { float kiri = bacaJarak(TRIG_KIRI, ECHO_KIRI); delay(15); float depan = bacaJarak(TRIG_DEPAN, ECHO_DEPAN); delay(15); float kanan = bacaJarak(TRIG_KANAN, ECHO_KANAN); delay(15); if (kiri > 20.0) { // PRIORITAS 1: Kiri Terbuka -> Maju sedikit ke tengah simpang, Belok Kiri, Masuk lorong setMotor(145, 0, 145, 0); delay(250); setMotor(0, 0, 0, 0); delay(150); setMotor(0, 160, 160, 0); delay(440); // Belok Kiri 90 derajat setMotor(0, 0, 0, 0); delay(150); setMotor(145, 0, 145, 0); delay(400); // Masuk ke lorong baru } else if (depan > 12.0) { // PRIORITAS 2: Depan Bebas -> Maju Lurus setMotor(145, 0, 145, 0); } else if (kanan > 20.0) { // PRIORITAS 3: Belok Kanan setMotor(0, 0, 0, 0); delay(150); setMotor(160, 0, 0, 160); delay(440); // Belok Kanan 90 derajat setMotor(0, 0, 0, 0); delay(150); } else { // PRIORITAS 4: Buntu -> Berhenti / Putar Balik setMotor(160, 0, 0, 160); delay(880); // Putar 180 derajat setMotor(0, 0, 0, 0); delay(200); }\n}",
        "lks": "<p><strong>Eksperimen Alignment Persimpangan:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Parameter Waktu (ms)</th><th>Jika Angka Terlalu Kecil</th><th>Jika Angka Terlalu Besar</th><th>Nilai Optimal Kelompokmu</th></tr> </thead> <tbody> <tr><td>Delay Maju Sebelum Belok Kiri (250 ms)</td><td>Belok terlalu cepat (nyangkut sudut kiri)</td><td>Kelewatan mulut simpang</td><td>.......... ms</td></tr> <tr><td>Delay Masuk Lorong Baru (400 ms)</td><td>Belok kiri dua kali di simpang yang sama</td><td>Menabrak dinding depan lorong baru</td><td>.......... ms</td></tr> </tbody> </table>",
        "troubleshooting": "Jika setelah belok kiri robot langsung belok kiri lagi (berputar-putar di tempat), tambah durasi 'Masuk ke lorong baru' dari 400 ms menjadi 500–600 ms agar sensor kiri sudah masuk diapit dinding lorong baru.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-11_Implementasi_Left_Hand_Rule_Dasar.pdf",
        "level": "SMP"
      },
      {
        "code": "M-12",
        "title": "Tuning Jarak Sisi Dinding (Wall Offset)",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Memahami masalah pergeseran arah robot (drifting) saat menyusuri lorong lurus yang panjang.",
          "Mengimplementasikan penjaga jarak dinding samping (Wall Offset Correction) dengan target jarak ideal 5–8 cm dari dinding kiri.",
          "Mencegah bodi robot menyerempet dinding lorong menggunakan koreksi kecepatan PWM roda kiri dan kanan."
        ],
        "theory": "<p>Saat robot berjalan di lorong panjang, sedikit saja posisi awalnya miring 2&deg;, lama-kelamaan robot akan menabrak dinding samping! Agar robot tetap berada di tengah lorong, kita menggunakan sensor ultrasonik samping kiri untuk menjaga <strong>Wall Offset (Jarak Ideal ke Dinding Kiri = 5 s/d 8 cm)</strong>:</p> <ul> <li>Jika <code>jarakKiri &lt; 5.0 cm</code> (Terlalu mepet ke dinding kiri!) &rarr; Kurangi kecepatan roda kanan sedikit agar robot miring menjauh ke kanan.</li> <li>Jika <code>jarakKiri &gt; 8.0 cm</code> dan <code>&lt; 18.0 cm</code> (Terlalu jauh dari dinding kiri!) &rarr; Kurangi kecepatan roda kiri sedikit agar robot kembali mendekat ke tengah.</li> <li>Jika <code>jarakKiri</code> berada di antara 5.0 – 8.0 cm &rarr; Kedua roda melaju dengan kecepatan sama (Lurus).</li> </ul>",
        "safety": "Koreksi kecepatan PWM untuk menjaga dinding cukup berbeda 20–30 poin PWM saja (misal 150 dan 125) agar gerakan robot tetap mulus dan tidak bergoyang patah-patah (zig-zag kasar).",
        "steps": [
          "Buat fungsi <code>majuSusurDindingKiri(float jarakKiri)</code> seperti pada kode M-12 di bawah.",
          "Letakkan robot dengan posisi sengaja agak miring di awal lorong lurus sepanjang 1,5 meter.",
          "Jalankan robot dan amati bagaimana robot memperbaiki posisinya sendiri agar sejajar dengan dinding kiri pada jarak ~6 cm!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-12: Penjaga Jarak Sisi Dinding (Wall Offset 5 - 8 cm)\n// =========================================================================\n// Menggantikan perintah maju biasa saat menyusuri lorong lurus void majuSusurDindingKiri(float jarakKiri) { int spdDasar = 150; int koreksi = 28; // Selisih PWM untuk membelokkan halus ke tengah lorong if (jarakKiri < 5.0) { // Terlalu dekat dinding kiri (< 5 cm) -> Arahkan halus ke KANAN // Roda Kiri lebih cepat, Roda Kanan diperlambat setMotor(spdDasar, 0, spdDasar - koreksi, 0); } else if (jarakKiri > 8.0 && jarakKiri < 18.0) { // Terlalu jauh dari dinding kiri (8 - 18 cm) -> Arahkan halus ke KIRI // Roda Kiri diperlambat, Roda Kanan lebih cepat setMotor(spdDasar - koreksi, 0, spdDasar, 0); } else { // Jarak sudah pas di zona ideal (5.0 s/d 8.0 cm) -> Lurus Stabil setMotor(spdDasar, 0, spdDasar, 0); }\n}",
        "lks": "<p><strong>Eksperimen Tuning Nilai Koreksi Wall Offset:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Nilai Variabel <code>koreksi</code></th><th>Perilaku Gerak Robot di Lorong Panjang 1.5 Meter</th><th>Apakah Menyentuh Dinding?</th></tr> </thead> <tbody> <tr><td><code>koreksi = 10</code> (Terlalu kecil)</td><td>.........................................................</td><td>Ya / Tidak</td></tr> <tr><td><code>koreksi = 28</code> (Sedang/Ideal)</td><td>.........................................................</td><td>Ya / Tidak</td></tr> <tr><td><code>koreksi = 70</code> (Terlalu besar)</td><td>.........................................................</td><td>Ya / Tidak (Bergoyang zig-zag)</td></tr> </tbody> </table>",
        "troubleshooting": "Mengapa syarat kedua memiliki batas '&& jarakKiri < 18.0'? Karena jika jarakKiri > 18.0 cm, itu artinya dinding kiri hilang (ada persimpangan belokan kiri), bukan sekadar bergeser di lorong!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-12_Tuning_Jarak_Sisi_Dinding_Wall_Offset.pdf",
        "level": "SMP"
      },
      {
        "code": "M-13",
        "title": "Penanganan Kondisi Buntu (Dead-End U-Turn)",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Mendeteksi kondisi jalan buntu (Dead-End) ketika sensor Depan, Kiri, dan Kanan semuanya mendeteksi dinding dekat (< 15 cm).",
          "Memprogram manuver putar balik 180 derajat di ruang sempit (Pivot U-Turn) tanpa membuat bodi robot tersangkut.",
          "Memilih arah putar balik yang memiliki ruang samping sedikit lebih lega (Kiri vs Kanan) agar manuver lebih mulus."
        ],
        "theory": "<p>Saat mengikuti <em>Left-Hand Rule</em>, robot pasti akan sesekali masuk ke <strong>Lorong Buntu (Dead-End)</strong> di mana dinding menutup bagian Depan, Kiri, dan Kanan sekaligus. Di dalam kantong jalan buntu yang sempit (lebar ~20–25 cm), memutar badan 180&deg; membutuhkan trik khusus agar bumper robot tidak menyangkut di dinding samping:</p> <ol> <li>Jika <code>jarakDepan &lt; 8 cm</code> (terlalu mepet dinding ujung), <strong>mundur sedikit (~200 ms)</strong>.</li> <li>Bandingkan ruang samping: jika <code>jarakKanan &gt;= jarakKiri</code>, berputarlah 180&deg; ke arah Kanan (begitu pula sebaliknya) agar hidung robot melewati sisi yang lebih longgar!</li> </ol>",
        "safety": "Pastikan kabel baterai atau kabel sensor tidak menjuntai keluar dari sasis belakang robot agar tidak menyangkut di sudut lorong saat berputar 180 derajat.",
        "steps": [
          "Buat sebuah lorong buntu (huruf U terbalik) menggunakan 3 papan dinding kardus.",
          "Tambahkan fungsi <code>manuverPutarBalik(float kiri, float depan, float kanan)</code> ke dalam program robotmu.",
          "Lepaskan robot masuk ke lorong buntu tersebut dan setel durasi <code>delay(...)</code> putar 180&deg; hingga robot keluar lurus kembali!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-13: Penanganan Jalan Buntu Cerdas (Smart Dead-End U-Turn 180)\n// ========================================================================= void manuverPutarBalik(float kiri, float depan, float kanan) { // 1. Berhenti sejenak setMotor(0, 0, 0, 0); delay(200); // 2. Jika hidung robot terlalu dekat ke dinding depan (< 8 cm), mundur sedikit if (depan < 8.0) { setMotor(0, 145, 0, 145); delay(220); setMotor(0, 0, 0, 0); delay(150); } // 3. Putar 180 derajat ke arah sisi samping yang lebih lega ruangnya int durasi180 = 860; // Kalibrasi sesuai lantai (sekitar 2x waktu belok 90) if (kanan >= kiri) { // Putar Balik lewat Kanan setMotor(165, 0, 0, 165); delay(durasi180); } else { // Putar Balik lewat Kiri setMotor(0, 165, 165, 0); delay(durasi180); } // 4. Berhenti stabil sebelum lanjut maju keluar lorong buntu setMotor(0, 0, 0, 0); delay(200);\n}",
        "lks": "<p><strong>Lembar Kalibrasi Manuver Dead-End 180&deg;:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Percobaan</th><th>Nilai <code>durasi180 (ms)</code></th><th>Sudut Putar yang Dihasilkan</th><th>Apakah Bodi Menyenggol Dinding Buntu?</th></tr> </thead> <tbody> <tr><td>1</td><td>800 ms</td><td>Kurang dari 180&deg; / Pas / Lebih</td><td>Ya / Tidak</td></tr> <tr><td>2</td><td>860 ms</td><td>Kurang dari 180&deg; / Pas / Lebih</td><td>Ya / Tidak</td></tr> <tr><td>3</td><td>....... ms (Nilai Terbaik)</td><td>Tepat 180&deg; (Lurus Keluar)</td><td>Tidak Menyenggol</td></tr> </tbody> </table>",
        "troubleshooting": "Jika saat berputar 180 derajat bagian belakang robot menyentuh dinding ujung buntu, itu tandanya robot berhenti terlalu dekat dengan dinding depan. Naikkan batas jarak berhenti depan dari 11 cm menjadi 13–14 cm.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-13_Penanganan_Kondisi_Buntu_Dead_End_U_Turn.pdf",
        "level": "SMP"
      },
      {
        "code": "M-14",
        "title": "Kalibrasi Lintasan & Penyelarasan Kecepatan Roda",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Memahami karakteristik fisik motor DC Gearbox TT tanpa encoder (adanya toleransi perbedaan RPM antara motor kiri dan kanan).",
          "Menentukan konstanta kalibrasi OFFSET_KIRI dan OFFSET_KANAN agar kedua roda berputar dengan kecepatan linear yang identik.",
          "Melakukan kalibrasi menyeluruh pada 4 parameter kritis sebelum uji labirin penuh."
        ],
        "theory": "<p>Motor kuning DC Gearbox TT yang digunakan pada robot edukasi tidak memiliki sensor penghitung putaran roda (<em>no encoder</em>). Akibat toleransi pabrik pada kumparan tembaga dan roda gigi plastik di dalamnya, ketika kita memberi nilai PWM yang sama (misal Kiri = 150, Kanan = 150), salah satu roda hampir pasti berputar sedikit lebih cepat!</p> <p>Untuk mengatasinya secara perangkat lunak, kita menambahkan konstanta kompensasi (<strong>Wheel Trim Offset</strong>) di bagian atas kode program kita, misalnya:</p> <div class=\"formula-box\"> PWM_KIRI = baseSpeed + OFFSET_KIRI &nbsp;&nbsp;|&nbsp;&nbsp; PWM_KANAN = baseSpeed + OFFSET_KANAN </div>",
        "safety": "Lakukan kalibrasi dengan kondisi baterai yang sudah terisi penuh agar nilai offset dan durasi belok akurat saat dipakai berlomba.",
        "steps": [
          "Letakkan robot di atas garis sambungan keramik lurus sepanjang 2 meter.",
          "Jalankan fungsi maju lurus selama 3 detik dengan <code>OFFSET_KIRI = 0</code> dan <code>OFFSET_KANAN = 0</code>.",
          "Jika robot melenceng ke Kanan (berarti roda Kiri lebih kencang), beri nilai <code>OFFSET_KANAN = +6</code> (atau <code>OFFSET_KIRI = -6</code>) lalu uji kembali hingga robot melaju lurus tepat di atas garis keramik!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-14: Parameter Kalibrasi Master (Wheel Trim & Turn Timing)\n// ========================================================================= // --- UBAH KEEMPAT ANGKA KALIBRASI INI SESUAI KARAKTER ROBOT KELOMPOKMU ---\nconst int BASE_SPEED = 145; // Kecepatan dasar jelajah (0-255)\nconst int OFFSET_KIRI = 0; // Tambahan/pengurangan PWM Roda Kiri (-20 s/d +20)\nconst int OFFSET_KANAN = 6; // Tambahan/pengurangan PWM Roda Kanan (-20 s/d +20)\nconst int DELAY_BELOK90 = 435; // Durasi milidetik putar tepat 90 derajat\nconst int DELAY_PUTAR180= 865; // Durasi milidetik putar balik 180 derajat void majuTerkalibrasi(int koreksiDinding) { int pwmKiri = BASE_SPEED + OFFSET_KIRI + koreksiDinding; int pwmKanan = BASE_SPEED + OFFSET_KANAN - koreksiDinding; // Batasi agar nilai PWM tetap berada di rentang aman 0 - 255 pwmKiri = constrain(pwmKiri, 0, 255); pwmKanan = constrain(pwmKanan, 0, 255); setMotor(pwmKiri, 0, pwmKanan, 0);\n}",
        "lks": "<p><strong>Lembar Sertifikasi Kalibrasi Unit MazeBot SMP:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Parameter Konstanta</th><th>Nilai Awal (Default)</th><th>Hasil Kalibrasi Final Kelompok</th><th>Bukti Uji Fisik</th></tr> </thead> <tbody> <tr><td><code>OFFSET_KIRI</code></td><td>0</td><td>..................</td><td rowspan=\"2\">Simpangan lurus 2 meter &lt; 3 cm</td></tr> <tr><td><code>OFFSET_KANAN</code></td><td>0</td><td>..................</td></tr> <tr><td><code>DELAY_BELOK90</code></td><td>450 ms</td><td>.................. ms</td><td>Sudut siku 90&deg; presisi</td></tr> <tr><td><code>DELAY_PUTAR180</code></td><td>900 ms</td><td>.................. ms</td><td>Berbalik arah 180&deg; presisi</td></tr> </tbody> </table>",
        "troubleshooting": "Periksa juga apakah ban karet terpasang lurus pada velg kuning motor TT. Ban yang miring atau bergesekan dengan baut sasis adalah penyebab utama robot melenceng!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-14_Kalibrasi_Lintasan_Penyelarasan_Kecepata.pdf",
        "level": "SMP"
      },
      {
        "code": "M-15",
        "title": "Uji Coba Labirin Lengkap & Integrasi Stopwatch",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Menggunakan fungsi waktu internal millis() pada ESP32 untuk menghitung waktu tempuh robot (Stopwatch Otomatis) dari Start hingga Finish.",
          "Menggabungkan seluruh modul: Left-Hand Rule (M-11), Wall Offset (M-12), Dead-End U-Turn (M-13), Kalibrasi PWM (M-14), dan Garis Finish TCRT5000 (M-09).",
          "Menjalankan uji coba penuh (Full Dress Rehearsal) di arena labirin lengkap dan memantau waktu tempuh."
        ],
        "theory": "<p>Bagaimana robot bisa menghitung sendiri berapa detik waktu yang ia butuhkan dari titik Start sampai menginjak Garis Finish? ESP32 memiliki fungsi pencatat waktu internal bernama <strong><code>millis()</code></strong> yang menghitung jumlah milidetik sejak robot dinyalakan.</p> <div class=\"formula-box\"> Waktu Tempuh (Detik) = (millis() Saat Menyentuh Finish &minus; millis() Saat Start) / 1000.0 </div> <p>Dengan mencatat <code>waktuStart = millis();</code> di akhir <code>setup()</code>, begitu sensor TCRT5000 mendeteksi garis hitam Finish, robot langsung menghitung dan mengirimkan catatan waktu resminya ke Serial Monitor / Web Dashboard!</p>",
        "safety": "Pastikan seluruh dinding labirin terpasang sesuai peta standar kompetisi dan garis lakban hitam di titik Finish menempel rata di lantai.",
        "steps": [
          "Masukkan angka-angka hasil kalibrasi M-14 ke dalam kode integrasi penuh M-15 di bawah ini.",
          "Letakkan robot di titik Start labirin dan nyalakan saklar daya.",
          "Catat waktu tempuh yang berhasil dicapai robot dan identifikasi titik tikungan mana yang masih bisa diperhalus gerakannya!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-15: Integrasi Stopwatch Otomatis (millis) & Uji Labirin Lengkap\n// =========================================================================\nunsigned long waktuStart = 0;\nunsigned long waktuFinish = 0;\nbool sudahFinish = false; // Dipanggil di baris paling akhir void setup() tepat sebelum robot mulai jalan:\nvoid mulaiStopwatch() { waktuStart = millis(); Serial.println(\"[STOPWATCH] Waktu Dimulai! Robot Memasuki Labirin...\");\n} // Dipanggil di dalam void loop() saat sensor TCRT5000 mendeteksi garis hitam:\nvoid cekGarisFinishDanCatatWaktu(int pinFinish) { if (!sudahFinish && digitalRead(pinFinish) == HIGH) { setMotor(0, 0, 0, 0); // Rem darurat waktuFinish = millis(); sudahFinish = true; float totalDetik = (waktuFinish - waktuStart) / 1000.0; Serial.println(\"==========================================\"); Serial.println(\"GARIS FINISH TERCAPAI!\"); Serial.print(\"Waktu Tempuh Resmi: \"); Serial.print(totalDetik, 2); Serial.println(\" detik\"); Serial.println(\"==========================================\"); }\n}",
        "lks": "<p><strong>Jurnal Uji Coba Labirin Lengkap (Simulasi Pra-Kompetisi):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Uji Coba</th><th>Apakah Berhasil Keluar dari Jalan Buntu?</th><th>Berhenti di Garis Finish?</th><th>Catatan Waktu Stopwatch (Detik)</th></tr> </thead> <tbody> <tr><td>Trial 1</td><td>Ya / Tidak</td><td>Ya / Tidak</td><td>.............. detik</td></tr> <tr><td>Trial 2</td><td>Ya / Tidak</td><td>Ya / Tidak</td><td>.............. detik</td></tr> <tr><td>Trial 3</td><td>Ya / Tidak</td><td>Ya / Tidak</td><td>.............. detik</td></tr> </tbody> </table>",
        "troubleshooting": "Jika sensor TCRT5000 tidak sengaja terpicu di tengah jalan karena sambungan nat keramik lantai yang berwarna gelap, atur sedikit trimpot TCRT5000 agar hanya merespon warna hitam pekat lakban.",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-15_Uji_Coba_Labirin_Lengkap_Integrasi_Stopw.pdf",
        "level": "SMP"
      },
      {
        "code": "M-16",
        "title": "Kompetisi Maze Solver Otonom SMP",
        "duration": "2 JP (2 x 40 Menit)",
        "phase": "Fase D (Kelas 8–9 SMP)",
        "objectives": [
          "Mengevaluasi penguasaan komprehensif siswa atas pemrograman C++ Arduino, fisika sensor ultrasonik, dan algoritma navigasi otonom.",
          "Menuntaskan tantangan Kompetisi Maze Solver Otonom SMP: melewati labirin dengan jebakan jalan buntu dan berhenti tepat di garis finish dengan waktu tercepat.",
          "Menunjukkan kemampuan analisis kode dan sportivitas dalam kompetisi STEM."
        ],
        "theory": "<p>Selamat datang di puncak kurikulum tingkat SMP: <strong>Kompetisi Maze Solver Otonom SMP</strong>! Setiap tim akan menurunkan robot MazeBot terbaiknya untuk menaklukkan labirin resmi yang memiliki cabang pengecoh (jalan buntu), tikungan siku, dan lorong lurus hingga berhenti presisi di atas garis Finish hitam.</p> <p>Di bawah ini adalah <strong>Kode Master Lengkap (Full Production Code SMP)</strong> yang merangkum seluruh modul M-01 hingga M-15 dan siap digunakan dalam perlombaan!</p>",
        "safety": "Selama putaran resmi kompetisi berlangsung, anggota tim tidak diperkenankan menyentuh robot kecuali meminta 'Retry' (ulang dari titik Start dengan waktu yang terus berjalan).",
        "steps": [
          "Pastikan nilai konstanta kalibrasi (<code>OFFSET_KIRI</code>, <code>OFFSET_KANAN</code>, <code>DELAY_BELOK90</code>, <code>DELAY_PUTAR180</code>) pada Kode Master M-16 sudah diisi sesuai robot timmu.",
          "Unggah kode ke robot dan lakukan pemeriksaan akhir baterai serta kebersihan roda karet.",
          "Saat dipanggil oleh Juri, letakkan robot di belakang garis Start dan nyalakan saklar saat peluit dibunyikan!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-16: MASTER CODE KOMPETISI MAZE SOLVER OTONOM SMP (FULL C++)\n// =========================================================================\n#define IN1 25\n#define IN2 26\n#define IN3 27\n#define IN4 14\n#define TRIG_KIRI 32\n#define ECHO_KIRI 35\n#define TRIG_DEPAN 33\n#define ECHO_DEPAN 34\n#define TRIG_KANAN 18\n#define ECHO_KANAN 19\n#define PIN_FINISH 4\n#define PIN_LED 2 // --- PARAMETER KALIBRASI TIM ---\nconst int BASE_SPD = 148;\nconst int OFFSET_KIRI = 0;\nconst int OFFSET_KANAN = 5;\nconst int DELAY_BELOK90 = 435;\nconst int DELAY_PUTAR180 = 865; unsigned long startTime = 0;\nbool finished = false; float getDist(int trig, int echo) { digitalWrite(trig, LOW); delayMicroseconds(2); digitalWrite(trig, HIGH); delayMicroseconds(10); digitalWrite(trig, LOW); long d = pulseIn(echo, HIGH, 25000); return (d == 0) ? 999.0 : (d * 0.034) / 2.0;\n} void drive(int L1, int L2, int R1, int R2) { analogWrite(IN1, constrain(L1, 0, 255)); analogWrite(IN2, constrain(L2, 0, 255)); analogWrite(IN3, constrain(R1, 0, 255)); analogWrite(IN4, constrain(R2, 0, 255));\n} void setup() { Serial.begin(115200); pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); pinMode(TRIG_KIRI, OUTPUT); pinMode(ECHO_KIRI, INPUT); pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT); pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT); pinMode(PIN_FINISH, INPUT); pinMode(PIN_LED, OUTPUT); drive(0, 0, 0, 0); delay(2000); // Jeda siap start startTime = millis();\n} void loop() { if (finished) { drive(0, 0, 0, 0); return; } // 1. Cek Garis Finish Hitam (TCRT5000) if (digitalRead(PIN_FINISH) == HIGH) { drive(0, 0, 0, 0); digitalWrite(PIN_LED, HIGH); finished = true; Serial.print(\"FINISH! Waktu: \"); Serial.print((millis() - startTime) / 1000.0, 2); Serial.println(\" dtk\"); return; } // 2. Baca 3 Sensor Ultrasonik dengan Jeda Anti-Crosstalk float kiri = getDist(TRIG_KIRI, ECHO_KIRI); delay(15); float depan = getDist(TRIG_DEPAN, ECHO_DEPAN); delay(15); float kanan = getDist(TRIG_KANAN, ECHO_KANAN); delay(15); // 3. Algoritma Navigasi Left-Hand Rule + Wall Offset if (kiri > 20.0) { drive(BASE_SPD + OFFSET_KIRI, 0, BASE_SPD + OFFSET_KANAN, 0); delay(240); drive(0, 0, 0, 0); delay(120); drive(0, 160, 160, 0); delay(DELAY_BELOK90); drive(0, 0, 0, 0); delay(120); drive(BASE_SPD + OFFSET_KIRI, 0, BASE_SPD + OFFSET_KANAN, 0); delay(380); } else if (depan > 12.0) { int kor = 0; if (kiri < 5.0) kor = 25; else if (kiri > 8.0 && kiri < 18.0) kor = -25; drive(BASE_SPD + OFFSET_KIRI + kor, 0, BASE_SPD + OFFSET_KANAN - kor, 0); } else if (kanan > 20.0) { drive(0, 0, 0, 0); delay(120); drive(160, 0, 0, 160); delay(DELAY_BELOK90); drive(0, 0, 0, 0); delay(120); } else { if (depan < 8.0) { drive(0, 145, 0, 145); delay(200); } drive(0, 0, 0, 0); delay(120); if (kanan >= kiri) drive(165, 0, 0, 165); else drive(0, 165, 165, 0); delay(DELAY_PUTAR180); drive(0, 0, 0, 0); delay(150); }\n}",
        "lks": "<p><strong>Rubrik Penilaian Resmi Kompetisi Maze Solver Otonom SMP:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Kriteria Penilaian</th><th>Bobot</th><th>Indikator Capaian</th><th>Skor Tim (0–100)</th></tr> </thead> <tbody> <tr><td><strong>1. Penguasaan Kode C++ &amp; Kalibrasi</strong></td><td>25%</td><td>Kode terstruktur modular, parameter kalibrasi dipahami</td><td>.............</td></tr> <tr><td><strong>2. Navigasi Persimpangan &amp; Jalan Buntu</strong></td><td>30%</td><td>Berhasil keluar dari jebakan jalan buntu (Left-Hand Rule)</td><td>.............</td></tr> <tr><td><strong>3. Ketepatan Berhenti di Garis Finish</strong></td><td>25%</td><td>Sensor TCRT5000 mengunci penghentian tepat di garis hitam</td><td>.............</td></tr> <tr><td><strong>4. Waktu Tempuh &amp; Minim Tabrakan</strong></td><td>20%</td><td>Menyelesaikan labirin dengan cepat &amp; minim sentuhan dinding</td><td>.............</td></tr> <tr><td colspan=\"3\"><strong>TOTAL NILAI AKHIR SEMESTER (TINGKAT SMP)</strong></td><td><strong>............. / 100</strong></td></tr> </tbody> </table>",
        "troubleshooting": "Berikan penghargaan khusus untuk kategori 'Best Code Architecture', 'Fastest Time', dan 'Most Smooth Wall-Follower' agar seluruh siswa termotivasi!",
        "pdf_url": "Modul_PDF_Per_Kode/SMP/SMP_M-16_Kompetisi_Maze_Solver_Otonom_SMP.pdf",
        "level": "SMP"
      }
    ]
  },
  "SMA": {
    "id": "SMA",
    "name": "Tingkat SMA/SMK (Kelas X–XII)",
    "Badge": "TINGKAT SMA/SMK",
    "tagline": "Algoritma Komputasi Navigasi & Reduksi Rute Labirin",
    "platform": "ESP32 C++ Starter API, Struktur Data Array, & Dead-End Elimination",
    "sop": "Prasyarat dasar C++ wajib dikuasai. Aktifkan fitur Wireless E-Stop dan Stuck Watchdog saat melakukan Speed Run.",
    "book_pdf": "Modul_Ajar_MazeBot_SMA_SMK.pdf",
    "color": "#7ED957",
    "modules": [
      {
        "code": "M-01",
        "title": "Review Arsitektur Robot & Starter Code Platform",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Membedah struktur Starter Project MazeBot (MazeBotStarter.h) tanpa terbebani konfigurasi jaringan tingkat rendah.",
          "Mengenal dan memanggil API standar perangkat keras: bot.drive(leftPWM, rightPWM), bot.readLeft(), bot.readFront(), bot.readRight(), dan bot.isFinishLine().",
          "Melakukan verifikasi integrasi starter firmware dan koneksi Web Dashboard bawaan."
        ],
        "theory": "<p>Pada tingkat SMA/SMK, fokus utama pembelajaran adalah <strong>Algoritma Komputasi Navigasi, Struktur Data Array, dan Optimasi Jalur Terpendek (Shortest Path)</strong>. Oleh sebab itu, fungsi komunikasi Wi-Fi SoftAP dan WebSocket Web Server telah dibungkus di dalam pustaka siap pakai <code>MazeBotStarter.h</code>.</p> <table class=\"std-table\"> <thead> <tr><th>Fungsi Starter API</th><th>Nilai Kembalian / Parameter</th><th>Deskripsi Fungsi</th></tr> </thead> <tbody> <tr><td><code>bot.begin(\"MazeBot-SMA-01\")</code></td><td><code>void</code> (SSID String)</td><td>Menginisialisasi pin GPIO, PWM DRV8833, sensor, dan Wi-Fi Web Server.</td></tr> <tr><td><code>bot.readLeft() / Front() / Right()</code></td><td><code>float</code> (cm)</td><td>Membaca jarak 3 sensor ultrasonik dengan proteksi anti-crosstalk otomatis.</td></tr> <tr><td><code>bot.isFinishLine()</code></td><td><code>bool</code> (true/false)</td><td>Membaca sensor bawah TCRT5000 (<code>true</code> jika mendeteksi garis hitam Finish).</td></tr> <tr><td><code>bot.drive(pwmKiri, pwmKanan)</code></td><td><code>int</code> (-255 s/d 255)</td><td>Menggerakkan motor kiri &amp; kanan (nilai negatif = putar mundur).</td></tr> </tbody> </table>",
        "safety": "Pastikan prasyarat dasar C++ (variabel, fungsi, percabangan) telah dikuasai dan pustaka MazeBotStarter.h berada di dalam satu folder yang sama dengan file .ino utama.",
        "steps": [
          "Buka folder <code>MazeBot_SMA_Starter</code> pada Arduino IDE dan amati deklarasi fungsi pada tab <code>MazeBotStarter.h</code>.",
          "Panggil fungsi inisialisasi <code>bot.begin(\"MazeBot-SMA-01\");</code> di dalam <code>void setup()</code>.",
          "Unggah kode M-01 dan pastikan nilai ketiga sensor jarak serta status garis finish tampil akurat di Serial Monitor."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-01: Arsitektur Starter Code Platform MazeBot SMA/SMK\n// =========================================================================\n#include \"MazeBotStarter.h\" MazeBotCore bot; void setup() { Serial.begin(115200); bot.begin(\"MazeBot-SMA-01\"); // Inisialisasi Hardware & Pre-built Web Server Serial.println(\"[SYSTEM] Starter Platform MazeBot SMA Siap!\");\n} void loop() { bot.updateWeb(); // Menjaga komunikasi background Web Dashboard float L = bot.readLeft(); float F = bot.readFront(); float R = bot.readRight(); bool fin = bot.isFinishLine(); Serial.printf(\"L: %.1f cm | F: %.1f cm | R: %.1f cm | Finish: %s\\n\", L, F, R, fin ? \"HITAM (YA)\" : \"PUTIH (TIDAK)\"); delay(200);\n}",
        "lks": "<p><strong>Lembar Eksplorasi API Starter Code:</strong></p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>Perintah yang Diinginkan</th><th>Pemanggilan Fungsi API <code>bot</code> yang Tepat</th></tr> </thead> <tbody> <tr><td>1</td><td>Maju lurus dengan PWM 150 di kedua roda</td><td><code>bot.drive(........, ........);</code></td></tr> <tr><td>2</td><td>Berputar poros ke kanan (Pivot Right) dengan PWM 160</td><td><code>bot.drive(........, ........);</code></td></tr> <tr><td>3</td><td>Berhenti mengunci roda</td><td><code>bot.drive(........, ........);</code></td></tr> </tbody> </table>",
        "troubleshooting": "Dengan nilai parameter negatif pada bot.drive(160, -160), fungsi secara otomatis mengaktifkan pin mundur pada DRV8833 untuk roda kanan.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-01_Review_Arsitektur_Robot_Starter_Code_Pla.pdf",
        "level": "SMA"
      },
      {
        "code": "M-02",
        "title": "Koreksi Lintasan Proporsional Berbasis Sensor Dinding",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Menggantikan koreksi biner kasar dengan koreksi proporsional halus (Closed-Loop Threshold Correction) berbasis selisih jarak dinding samping.",
          "Menghitung nilai error = targetJarak - jarakAktual dan mengalikan dengan penguat proporsional sederhana Kp.",
          "Membatasi nilai koreksi menggunakan constrain() agar manuver di dalam lorong tetap stabil tanpa osilasi."
        ],
        "theory": "<p>Pada tingkat SMP, koreksi dinding hanya menggunakan sistem biner (jika terlalu dekat koreksi sekian, jika terlalu jauh koreksi sekian). Di tingkat SMA/SMK, kita menerapkan <strong>Closed-Loop Proportional Correction</strong> berbasis umpan balik sensor ultrasonik samping:</p> <div class=\"formula-box\"> error = TARGET_DINDING &minus; jarakKiri &nbsp;&nbsp;|&nbsp;&nbsp; koreksiPWM = constrain(Kp &times; error, &minus;MAX_CORR, +MAX_CORR) </div> <p>Semakin besar penyimpangan posisi robot dari jarak target (6.5 cm), semakin kuat pula koreksi setir yang diberikan. Sebaliknya, jika penyimpangan hanya 0.5 cm, koreksi PWM yang diberikan sangat lembut sehingga robot meluncur mulus di tengah lorong!</p>",
        "safety": "Batasi nilai koreksi maksimum (MAX_CORR) sekitar 35–40 PWM agar salah satu roda tidak berhenti mendadak saat melaju di lorong lurus.",
        "steps": [
          "Implementasikan fungsi <code>majuClosedLoop(float jarakKiri)</code> dengan konstanta <code>TARGET_WALL = 6.5</code> cm dan <code>Kp = 8.0</code>.",
          "Hanya aktifkan koreksi dinding ketika dinding kiri benar-benar ada (<code>jarakKiri &lt; 15.0 cm</code>). Jika dinding kiri hilang (persimpangan), matikan koreksi (<code>koreksi = 0</code>).",
          "Uji pada lorong lurus sepanjang 2 meter dan amati kemulusan lintasan dibanding metode biner."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-02: Closed-Loop Proportional Wall Correction\n// =========================================================================\nconst float TARGET_WALL = 6.5; // Jarak ideal dari dinding kiri (cm)\nconst float KP_WALL = 8.0; // Konstanta penguat proporsional\nconst int BASE_PWM = 150; // Kecepatan dasar\nconst int MAX_CORR = 35; // Batas maksimum koreksi PWM void majuClosedLoop(float jarakKiri) { int koreksi = 0; // Hanya lakukan koreksi jika dinding samping kiri terdeteksi (< 15 cm) if (jarakKiri < 15.0) { float error = TARGET_WALL - jarakKiri; // Positif jika terlalu dekat dinding kiri koreksi = (int)(KP_WALL * error); koreksi = constrain(koreksi, -MAX_CORR, MAX_CORR); } // Jika terlalu dekat kiri (error > 0), roda kiri dipercepat & kanan diperlambat int pwmKiri = BASE_PWM + koreksi; int pwmKanan = BASE_PWM - koreksi; bot.drive(pwmKiri, pwmKanan);\n}",
        "lks": "<p><strong>Analisis Perhitungan Closed-Loop Correction (Target = 6.5 cm, Kp = 8.0):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Jarak Kiri Aktual</th><th>Nilai <code>error (6.5 - aktual)</code></th><th>Nilai <code>koreksi (Kp &times; error)</code></th><th>PWM Kiri &amp; Kanan (Base 150)</th><th>Arah Koreksi Robot</th></tr> </thead> <tbody> <tr><td>4.5 cm (Terlalu dekat)</td><td>+2.0 cm</td><td>+16</td><td>Kiri: 166 | Kanan: 134</td><td>Menjauh ke Kanan</td></tr> <tr><td>6.5 cm (Tepat di target)</td><td>0.0 cm</td><td>0</td><td>Kiri: 150 | Kanan: 150</td><td>Lurus Sempurna</td></tr> <tr><td>9.0 cm (Agak menjauh)</td><td>-2.5 cm</td><td>-20</td><td>Kiri: 130 | Kanan: 170</td><td>Mendekat ke Kiri</td></tr> </tbody> </table>",
        "troubleshooting": "Jika robot terlihat bergoyang kiri-kanan terus menerus (osilasi), turunkan nilai KP_WALL dari 8.0 menjadi 5.0 atau 6.0.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-02_Koreksi_Lintasan_Proporsional_Berbasis_S.pdf",
        "level": "SMA"
      },
      {
        "code": "M-03",
        "title": "Deteksi Persimpangan Berbasis Sensor Ultrasonik",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Mengklasifikasikan topologi persimpangan labirin murni dari kombinasi bukaan 3 sensor ultrasonik (Kiri, Depan, Kanan).",
          "Membuat fungsi klasifikasi untuk membedakan Lorong Lurus, Simpang Kiri, Simpang Kanan, T-Junction, Crossroad (+), dan Dead-End.",
          "Menguji akurasi deteksi jenis persimpangan pada berbagai posisi labirin."
        ],
        "theory": "<p>Sesuai arsitektur perangkat keras MazeBot EduKit, deteksi persimpangan dilakukan <strong>100% menggunakan kombinasi 3x Sensor Ultrasonik</strong> (sedangkan sensor TCRT5000 dikhususkan murni untuk Garis Finish). Sebuah sisi dinyatakan <strong>Terbuka (Open)</strong> apabila jarak ultrasonik melebihi ambang <code>OPEN_THRES = 16.0 cm</code>:</p> <table class=\"std-table\"> <thead> <tr><th>Status Kiri (&gt;16cm)</th><th>Status Depan (&gt;14cm)</th><th>Status Kanan (&gt;16cm)</th><th>Klasifikasi Persimpangan</th></tr> </thead> <tbody> <tr><td>Tertutup</td><td>Terbuka</td><td>Tertutup</td><td><code>CORRIDOR</code> (Lorong Lurus Biasa)</td></tr> <tr><td>Terbuka</td><td>Tertutup</td><td>Tertutup</td><td><code>LEFT_CORNER</code> (Tikungan/Simpang Kiri)</td></tr> <tr><td>Tertutup</td><td>Tertutup</td><td>Terbuka</td><td><code>RIGHT_CORNER</code> (Tikungan/Simpang Kanan)</td></tr> <tr><td>Terbuka</td><td>Terbuka</td><td>Tertutup</td><td><code>T_LEFT</code> (Simpang Tiga Cabang Kiri-Depan)</td></tr> <tr><td>Tertutup</td><td>Terbuka</td><td>Terbuka</td><td><code>T_RIGHT</code> (Simpang Tiga Cabang Depan-Kanan)</td></tr> <tr><td>Terbuka</td><td>Tertutup</td><td>Terbuka</td><td><code>T_JUNCTION</code> (Pertigaan Huruf T)</td></tr> <tr><td>Terbuka</td><td>Terbuka</td><td>Terbuka</td><td><code>CROSSROAD</code> (Simpang Empat +)</td></tr> <tr><td>Tertutup</td><td>Tertutup</td><td>Tertutup</td><td><code>DEAD_END</code> (Jalan Buntu)</td></tr> </tbody> </table>",
        "safety": "Pastikan ambang jarak bukaan samping (16.0 cm) disesuaikan dengan lebar lorong labirin sekolah (umumnya lebar lorong standar adalah 20–25 cm).",
        "steps": [
          "Ketikkan fungsi klasifikasi <code>klasifikasiSimpang(float L, float F, float R)</code> pada Arduino IDE.",
          "Tempatkan robot secara manual di 5 titik berbeda di dalam labirin (lorong lurus, tikungan L, pertigaan T, perempatan +, dan jalan buntu).",
          "Catat hasil klasifikasi yang dicetak pada Serial Monitor dan pastikan akurasinya 100% tepat!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-03: Klasifikasi Persimpangan Berbasis 3x Sensor Ultrasonik\n// =========================================================================\nconst float SIDE_OPEN_THRES = 16.0; // Sisi kiri/kanan terbuka jika > 16 cm\nconst float FRONT_OPEN_THRES = 14.0; // Sisi depan terbuka jika > 14 cm String klasifikasiSimpang(float L, float F, float R) { bool openL = (L > SIDE_OPEN_THRES); bool openF = (F > FRONT_OPEN_THRES); bool openR = (R > SIDE_OPEN_THRES); if (openL && openF && openR) return \"CROSSROAD (+)\"; if (openL && !openF && openR) return \"T_JUNCTION (T)\"; if (openL && openF && !openR) return \"T_LEFT (Simpang Kiri-Lurus)\"; if (!openL && openF && openR) return \"T_RIGHT (Simpang Lurus-Kanan)\"; if (openL && !openF && !openR) return \"LEFT_TURN (Belokan Kiri)\"; if (!openL && !openF && openR) return \"RIGHT_TURN (Belokan Kanan)\"; if (!openL && !openF && !openR) return \"DEAD_END (Jalan Buntu)\"; return \"CORRIDOR (Lorong Lurus)\";\n}",
        "lks": "<p><strong>Verifikasi Klasifikasi Persimpangan Ultrasonik:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Lokasi Uji Robot</th><th>Bacaan (L, F, R) cm</th><th>Status Boolean (openL, openF, openR)</th><th>Output Klasifikasi</th></tr> </thead> <tbody> <tr><td>Pertigaan T</td><td>L:.... | F:.... | R:....</td><td>( true , false , true )</td><td>............................</td></tr> <tr><td>Simpang Kiri-Lurus</td><td>L:.... | F:.... | R:....</td><td>( ..... , ..... , ..... )</td><td>............................</td></tr> <tr><td>Jalan Buntu</td><td>L:.... | F:.... | R:....</td><td>( ..... , ..... , ..... )</td><td>............................</td></tr> </tbody> </table>",
        "troubleshooting": "Saat robot baru saja mendekati bibir simpang, sensor samping mungkin membaca nilai peralihan. Modul M-04 berikutnya akan membahas cara menstabilkan pembacaan tepat di titik tengah simpang!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-03_Deteksi_Persimpangan_Berbasis_Sensor_Ult.pdf",
        "level": "SMA"
      },
      {
        "code": "M-04",
        "title": "Logika Keputusan Persimpangan (Intersection State)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Memprogram robot agar melakukan transisi state: menyusuri lorong -> mendeteksi mulut persimpangan -> maju sedikit ke titik tengah simpang -> berhenti sejenak (stabilisasi) -> memindai ulang 3 sensor -> mengeksekusi keputusan.",
          "Menghindari kesalahan baca (false trigger) akibat pantulan miring dinding di mulut persimpangan.",
          "Membangun fondasi pengambilan keputusan yang deterministik untuk pencatatan array rute."
        ],
        "theory": "<p>Mengapa robot sering salah mengambil keputusan jika langsung berbelok saat melaju kencang? Karena ketika sensor kiri baru menyentuh tepi bukaan simpang, sensor kanan mungkin belum sejajar dengan bukaan kanan! Solusi rekayasa perangkat lunaknya adalah <strong>Intersection State Stabilization</strong>:</p> <ol> <li><strong>Trigger Awal:</strong> Saat berada di lorong, jika <code>L &gt; 16 cm</code> ATAU <code>R &gt; 16 cm</code> ATAU <code>F &lt; 13 cm</code>, tandai bahwa robot memasuki <em>Zona Persimpangan</em>.</li> <li><strong>Centering &amp; Stop:</strong> Maju perlahan selama <code>220 ms</code> (jika depan masih longgar) agar sumbu roda tepat berada di pusat persimpangan, lalu <strong>Berhenti Penuh selama 150 ms</strong>.</li> <li><strong>Stable Re-Scan:</strong> Dalam keadaan diam di pusat simpang, baca ulang ketiga sensor (Kiri, Depan, Kanan) untuk menghasilkan keputusan yang 100% akurat!</li> </ol>",
        "safety": "Pastikan dorongan maju centering (220 ms) hanya dijalankan apabila jarak depan masih > 11 cm agar robot tidak menabrak dinding depan pertigaan T.",
        "steps": [
          "Implementasikan fungsi <code>ambilKeputusanSimpangStabil()</code> seperti pada kode M-04 di bawah.",
          "Uji robot melewati pertigaan T dan perempatan (+). Perhatikan bagaimana robot berhenti sejenak dengan anggun di tengah simpang sebelum berbelok!",
          "Bandingkan kestabilan belokannya dengan gerakan tanpa jeda berhenti."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-04: Intersection State (Stop, Stabilize, Re-Scan, & Execute)\n// ========================================================================= char ambilKeputusanSimpangStabil() { // 1. Jika terdeteksi bukaan samping dan depan masih aman, maju ke pusat simpang float fAwal = bot.readFront(); if (fAwal > 12.0) { bot.drive(140, 140); delay(220); // Centering roda di tengah persimpangan } // 2. Berhenti sejenak agar getaran bodi hilang & pembacaan ultrasonik stabil bot.drive(0, 0); delay(150); // 3. Re-Scan 3 sensor dalam posisi robot diam sempurna float L = bot.readLeft(); float F = bot.readFront(); float R = bot.readRight(); // 4. Evaluasi keputusan berdasarkan aturan Left-Hand Rule: if (L > 16.0) { bot.turnLeft90(); bot.drive(145, 145); delay(350); // Keluar dari zona simpang return 'L'; // Left } else if (F > 13.0) { bot.drive(145, 145); delay(350); // Lurus melewati simpang return 'S'; // Straight } else if (R > 16.0) { bot.turnRight90(); bot.drive(145, 145); delay(350); return 'R'; // Right } else { bot.turnAround180(); return 'U'; // U-Turn (Buntu) }\n}",
        "lks": "<p><strong>Analisis State Persimpangan Stabil:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Tahapan State</th><th>Aksi Fisik Robot</th><th>Tujuan Teknis</th></tr> </thead> <tbody> <tr><td>1. Centering (220 ms)</td><td>Maju ke tengah simpang</td><td>Agar poros roda tepat di tengah jalur belokan</td></tr> <tr><td>2. Stop &amp; Re-Scan (150 ms)</td><td>Berhenti &amp; baca ulang 3 sensor</td><td>..........................................................</td></tr> <tr><td>3. Step-Out (350 ms)</td><td>Maju masuk ke lorong baru</td><td>..........................................................</td></tr> </tbody> </table>",
        "troubleshooting": "Perhatikan bahwa fungsi ambilKeputusanSimpangStabil() mengembalikan satu karakter ('L', 'S', 'R', atau 'U'). Karakter inilah yang nantinya akan kita simpan ke dalam Array pada Modul M-09!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-04_Logika_Keputusan_Persimpangan_Intersecti.pdf",
        "level": "SMA"
      },
      {
        "code": "M-05",
        "title": "Integrasi Garis Finish dengan TCRT5000",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Menghubungkan pembacaan sensor garis bawah TCRT5000 sebagai kondisi penghentian akhir absolut (Terminal State).",
          "Membedakan state robot antara STATE_EXPLORE (sedang menjelajah), STATE_FINISH_COMPUTE (garis finish tercapai & komputasi rute), dan STATE_DONE.",
          "Memicu fungsi komputasi optimasi rute tepat pada saat robot berhenti di atas garis Finish."
        ],
        "theory": "<p>Dalam arsitektur perangkat lunak MazeBot SMA/SMK, sensor bawah <strong>TCRT5000</strong> berperan sebagai pemicu transisi fase utama. Ketika <code>bot.isFinishLine() == true</code> terdeteksi saat penjelajahan:</p> <ol> <li>Robot langsung menghentikan kedua motor (<code>bot.drive(0, 0)</code>).</li> <li>State sistem berpindah dari <code>STATE_EXPLORE</code> menjadi <code>STATE_FINISH_COMPUTE</code>.</li> <li>Otak ESP32 langsung mengeksekusi algoritma pemangkasan jalan buntu (<em>Path Simplification</em>) dan bersiap untuk fase <em>Speed Run</em>!</li> </ol>",
        "safety": "Pengecekan bot.isFinishLine() wajib diletakkan di baris paling atas di dalam void loop() agar memiliki prioritas interupsi tertinggi dibanding pembacaan ultrasonik.",
        "steps": [
          "Buat struktur <code>enum RobotState { STATE_EXPLORE, STATE_FINISH_COMPUTE, STATE_DONE };</code>.",
          "Pasang pengecekan <code>if (bot.isFinishLine())</code> di awal state <code>STATE_EXPLORE</code>.",
          "Uji transisi state tersebut dengan menjalankan robot melewati satu persimpangan menuju lakban hitam Finish."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-05: State Machine Utama & Trigger Garis Finish TCRT5000\n// =========================================================================\nenum RobotState { STATE_EXPLORE, STATE_FINISH_COMPUTE, STATE_DONE\n}; RobotState currentState = STATE_EXPLORE; void loop() { bot.updateWeb(); switch (currentState) { case STATE_EXPLORE: // Prioritas Tertinggi: Cek apakah sensor bawah TCRT5000 menyentuh Garis Finish if (bot.isFinishLine()) { bot.drive(0, 0); Serial.println(\"[FINISH] Garis Hitam Terdeteksi! Memulai Komputasi Rute...\"); currentState = STATE_FINISH_COMPUTE; break; } // Lanjutkan navigasi lorong & persimpangan jalankanNavigasiEksplorasi(); break; case STATE_FINISH_COMPUTE: // Panggil mesin pemangkas jalan buntu (akan dilengkapi di M-12) pangkasRuteJalanBuntu(); currentState = STATE_DONE; break; case STATE_DONE: bot.drive(0, 0); // Siap diangkat kembali ke garis Start untuk Speed Run break; }\n}",
        "lks": "<p><strong>Diagram Alir Transisi State (Finite State Machine Sederhana):</strong></p> <table class=\"std-table\"> <thead> <tr><th>State Saat Ini</th><th>Pemicu (Trigger Event)</th><th>State Berikutnya</th><th>Aksi Robot</th></tr> </thead> <tbody> <tr><td><code>STATE_EXPLORE</code></td><td><code>bot.isFinishLine() == false</code></td><td>Tetap <code>STATE_EXPLORE</code></td><td>Menyusuri labirin</td></tr> <tr><td><code>STATE_EXPLORE</code></td><td><code>bot.isFinishLine() == true</code></td><td><code>STATE_FINISH_COMPUTE</code></td><td>Rem motor &amp; hitung rute</td></tr> <tr><td><code>STATE_FINISH_COMPUTE</code></td><td>Komputasi array selesai</td><td><code>STATE_DONE</code></td><td>Tampilkan rute optimal</td></tr> </tbody> </table>",
        "troubleshooting": "Pastikan lakban hitam Finish dipasang melintang penuh selebar lorong labirin (20–25 cm) agar dari sudut mana pun robot masuk ke kotak Finish, sensor TCRT5000 pasti melintasinya.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-05_Integrasi_Garis_Finish_dengan_TCRT5000.pdf",
        "level": "SMA"
      },
      {
        "code": "M-06",
        "title": "Integrasi Telemetri ke Dashboard Web (Starter API)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Menggunakan fungsi siap pakai bot.sendTelemetry(left, front, right, statusText) untuk mengirimkan data sensor dan status keputusan ke Web Dashboard secara real-time.",
          "Menerapkan pengiriman data non-blocking menggunakan timer millis() (interval 200 ms) agar tidak memperlambat loop navigasi.",
          "Memantau perubahan status persimpangan secara nirkabel melalui layar laptop/smartphone."
        ],
        "theory": "<p>Saat robot bergerak di dalam labirin, kabel USB tentu sudah dilepas sehingga kita tidak bisa melihat Serial Monitor melalui kabel! Sebagai gantinya, Starter Platform menyediakan API <strong>WebSocket Telemetry</strong>: <code>bot.sendTelemetry(L, F, R, status)</code>.</p> <p>Agar pengiriman paket Wi-Fi tidak menghambat respons motor, kita tidak memanggil fungsi ini di setiap milidetik, melainkan menggunakan <strong>Non-Blocking Timer (<code>millis() - lastTel &gt;= 200</code>)</strong> sehingga data dikirim cukup 5 kali per detik.</p>",
        "safety": "Hindari penggunaan delay() panjang saat mengirim telemetri; gunakan pola perbandingan millis() seperti pada contoh kode di bawah.",
        "steps": [
          "Hubungkan laptop/HP ke Wi-Fi robot dan buka halaman Web Dashboard (<code>http://192.168.4.1</code>).",
          "Tambahkan blok pengiriman telemetri berkala menggunakan <code>millis()</code> di dalam program navigasimu.",
          "Jalankan robot di labirin dan amati grafik jarak Kiri, Depan, Kanan serta teks keputusan persimpangan yang berubah secara langsung di layar browser!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-06: Integrasi Telemetri Web Dashboard dengan Non-Blocking Timer\n// =========================================================================\nunsigned long lastTelemetryTime = 0; void kirimTelemetriBerkala(float L, float F, float R, String status) { // Kirim data ke Web Dashboard setiap 200 milidetik (5 Hz) tanpa delay() if (millis() - lastTelemetryTime >= 200) { lastTelemetryTime = millis(); bot.sendTelemetry(L, F, R, status); }\n} // Contoh pemakaian di dalam loop navigasi:\nvoid loop() { bot.updateWeb(); float L = bot.readLeft(); float F = bot.readFront(); float R = bot.readRight(); String tipe = klasifikasiSimpang(L, F, R); kirimTelemetriBerkala(L, F, R, tipe);\n}",
        "lks": "<p><strong>Pengamatan Telemetri Nirkabel Web Dashboard:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Posisi Fisik Robot di Arena</th><th>Nilai (L / F / R) di Web</th><th>Teks Status di Web Dashboard</th><th>Delay Tampilan (Real-time?)</th></tr> </thead> <tbody> <tr><td>Di Lorong Lurus</td><td>.... / .... / .... cm</td><td><code>CORRIDOR (Lorong Lurus)</code></td><td>Real-time (&lt; 0.2 dtk)</td></tr> <tr><td>Di Persimpangan T</td><td>.... / .... / .... cm</td><td><code>T_JUNCTION (T)</code></td><td>Real-time (&lt; 0.2 dtk)</td></tr> <tr><td>Di Atas Garis Hitam</td><td>.... / .... / .... cm</td><td><code>FINISH LINE REACHED!</code></td><td>Real-time (&lt; 0.2 dtk)</td></tr> </tbody> </table>",
        "troubleshooting": "Selain mengirim berkala setiap 200 ms, panggil juga bot.sendTelemetry() secara langsung tepat ketika robot mengambil keputusan belok di persimpangan agar momen belokan langsung tercatat di log web.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-06_Integrasi_Telemetri_ke_Dashboard_Web_Sta.pdf",
        "level": "SMA"
      },
      {
        "code": "M-07",
        "title": "Penyimpanan Nilai Kalibrasi ke Flash (NVS Sederhana)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Memahami perbedaan memori sementara (RAM) dan memori permanen Non-Volatile Storage (NVS Flash) pada mikrokontroler ESP32.",
          "Menggunakan pustaka bawaan <Preferences.h> untuk menyimpan dan membaca kembali parameter kalibrasi (baseSpd, turn90, wallCm).",
          "Memungkinkan perubahan nilai kalibrasi dari Web Dashboard tanpa perlu meng-compile ulang kode program dari komputer."
        ],
        "theory": "<p>Jika kita menyimpan angka kalibrasi hanya pada variabel biasa di RAM, setiap kali baterai dilepas atau saklar dimatikan, perubahan nilai tuning dari Web Dashboard akan hilang kembali ke angka awal! ESP32 menyediakan fitur <strong>NVS (Non-Volatile Storage)</strong> melalui library resmi <code>&lt;Preferences.h&gt;</code> yang menyimpan data di memori Flash layaknya <em>harddisk</em> kecil:</p> <ul> <li><code>prefs.begin(\"mazebot_cfg\", false);</code> &rarr; Membuka ruang penyimpanan bernama <code>\"mazebot_cfg\"</code>.</li> <li><code>prefs.putInt(\"turn90\", 435);</code> &rarr; Menyimpan angka <code>435</code> secara permanen ke Flash.</li> <li><code>prefs.getInt(\"turn90\", 440);</code> &rarr; Membaca angka dari Flash (jika belum pernah disimpan, gunakan angka default <code>440</code>).</li> </ul>",
        "safety": "Jangan memanggil fungsi prefs.putInt() di dalam void loop() yang berulang ribuan kali per detik karena memori Flash memiliki batas usia tulis (~100.000 kali tulis). Panggil putInt() hanya saat tombol 'Simpan Kalibrasi' ditekan!",
        "steps": [
          "Sertakan header <code>#include &lt;Preferences.h&gt;</code> di bagian atas program.",
          "Buat fungsi <code>muatKalibrasiDariFlash()</code> yang dipanggil di dalam <code>void setup()</code>.",
          "Ubah nilai kalibrasi, matikan saklar baterai robot selama 10 detik, lalu nyalakan kembali dan buktikan bahwa nilai kalibrasi tetap tersimpan!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-07: Penyimpanan Parameter Kalibrasi Permanen dengan Preferences.h\n// =========================================================================\n#include <Preferences.h> Preferences prefs; int calBaseSpeed = 150;\nint calTurn90Ms = 440;\nfloat calTargetWall = 6.5; void muatKalibrasiDariFlash() { prefs.begin(\"mazebot_cfg\", true); // Mode Read-Only (true) calBaseSpeed = prefs.getInt(\"baseSpd\", 150); calTurn90Ms = prefs.getInt(\"turn90\", 440); calTargetWall = prefs.getFloat(\"wallCm\", 6.5); prefs.end(); Serial.printf(\"[NVS] Kalibrasi Dimuat -> Spd:%d | Turn90:%d ms | Wall:%.1f cm\\n\", calBaseSpeed, calTurn90Ms, calTargetWall);\n} void simpanKalibrasiKeFlash(int spdBaru, int turnBaru, float wallBaru) { prefs.begin(\"mazebot_cfg\", false); // Mode Read-Write (false) prefs.putInt(\"baseSpd\", spdBaru); prefs.putInt(\"turn90\", turnBaru); prefs.putFloat(\"wallCm\", wallBaru); prefs.end(); calBaseSpeed = spdBaru; calTurn90Ms = turnBaru; calTargetWall = wallBaru; Serial.println(\"[NVS] Parameter Kalibrasi Berhasil Disimpan Permanen ke Flash!\");\n}",
        "lks": "<p><strong>Uji Ketahanan Memori Non-Volatile Storage (NVS):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Key NVS</th><th>Nilai Default Awal</th><th>Nilai Baru yang Disimpan</th><th>Nilai Saat Robot Dimatikan &amp; Dinyalakan Lagi</th></tr> </thead> <tbody> <tr><td><code>\"baseSpd\"</code></td><td>150</td><td>158</td><td>.................. (Tetap Tersimpan!)</td></tr> <tr><td><code>\"turn90\"</code></td><td>440</td><td>425</td><td>.................. (Tetap Tersimpan!)</td></tr> <tr><td><code>\"wallCm\"</code></td><td>6.5</td><td>6.0</td><td>.................. (Tetap Tersimpan!)</td></tr> </tbody> </table>",
        "troubleshooting": "Nama key pada Preferences.h maksimal terdiri dari 15 karakter (contoh: 'baseSpd', 'turn90'). Jangan gunakan nama key yang terlalu panjang.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-07_Penyimpanan_Nilai_Kalibrasi_ke_Flash_NVS.pdf",
        "level": "SMA"
      },
      {
        "code": "M-08",
        "title": "Ujian Tengah Semester (Proyek Mini 3: Navigasi & Telemetri Persimpangan)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Mengevaluasi integrasi Closed-Loop Wall Correction (M-02), Deteksi & State Persimpangan Stabil (M-03 & M-04), Finish TCRT5000 (M-05), Telemetri Web (M-06), dan NVS (M-07).",
          "Menyelesaikan Tantangan Navigasi Persimpangan: robot menavigasi minimal 3 persimpangan berbeda secara mulus dan mengirimkan log deteksi tiap simpang ke Web Dashboard.",
          "Menguji kesiapan perangkat keras dan perangkat lunak sebelum masuk ke materi struktur data pemetaan rute."
        ],
        "theory": "<p>Pada <strong>Ujian Tengah Semester (Proyek Mini 3)</strong> tingkat SMA/SMK, robot diuji melintasi jalur labirin yang memuat <strong>3 jenis persimpangan berurutan</strong> (misalnya: Simpang Tiga Kiri &rarr; Jalan Buntu &rarr; Pertigaan T &rarr; Garis Finish). Setiap kali robot berhenti sejenak di pusat persimpangan, robot wajib mengirimkan jenis persimpangan dan arah belokan yang diambil ke layar Web Dashboard penguji!</p>",
        "safety": "Pastikan parameter NVS telah disesuaikan untuk permukaan lantai arena ujian sebelum giliran tim dipanggil.",
        "steps": [
          "Integrasikan modul M-01 s/d M-07 ke dalam program Proyek Mini 3 di bawah ini.",
          "Buka Web Dashboard pada laptop Juri/Guru untuk memantau kiriman telemetri langsung dari robot timmu.",
          "Lepaskan robot dari kotak Start dan biarkan robot menavigasi ketiga persimpangan hingga berhenti di garis Finish."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-08: UTS PROYEK MINI 3 - Navigasi Persimpangan & Telemetri Web\n// =========================================================================\n#include \"MazeBotStarter.h\"\n#include <Preferences.h> MazeBotCore bot;\nint simpangKe = 0; void setup() { Serial.begin(115200); bot.begin(\"MazeBot-SMA-UTS\"); delay(2000);\n} void loop() { bot.updateWeb(); if (bot.isFinishLine()) { bot.drive(0, 0); bot.sendTelemetry(0, 0, 0, \"FINISH TERCAPAI! Total Simpang: \" + String(simpangKe)); while (true) { bot.updateWeb(); delay(100); } } float L = bot.readLeft(); float F = bot.readFront(); float R = bot.readRight(); // Cek apakah memasuki persimpangan atau jalan buntu if (L > 16.0 || R > 16.0 || F < 13.0) { simpangKe++; String jenis = klasifikasiSimpang(L, F, R); char aksi = ambilKeputusanSimpangStabil(); // Fungsi dari M-04 String logMsg = \"Simpang #\" + String(simpangKe) + \": \" + jenis + \" -> Aksi: \" + String(aksi); bot.sendTelemetry(L, F, R, logMsg); } else { majuClosedLoop(L); // Fungsi dari M-02 }\n}",
        "lks": "<p><strong>Lembar Penilaian UTS Proyek Mini 3 (Tingkat SMA/SMK):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Titik Uji</th><th>Jenis Persimpangan Aktual</th><th>Log Telemetri yang Muncul di Web</th><th>Ketepatan Manuver Fisik</th><th>Skor (0–25)</th></tr> </thead> <tbody> <tr><td>Simpang #1</td><td>........................</td><td>.......................................</td><td>Tepat / Menyenggol</td><td>.......</td></tr> <tr><td>Simpang #2</td><td>........................</td><td>.......................................</td><td>Tepat / Menyenggol</td><td>.......</td></tr> <tr><td>Simpang #3</td><td>........................</td><td>.......................................</td><td>Tepat / Menyenggol</td><td>.......</td></tr> <tr><td>Garis Finish</td><td>Lakban Hitam TCRT5000</td><td><code>FINISH TERCAPAI!</code></td><td>Berhenti Tepat</td><td>.......</td></tr> </tbody> </table>",
        "troubleshooting": "Pastikan fungsi Step-Out (maju 350 ms setelah belok di simpang) berjalan tuntas agar satu persimpangan yang sama tidak terhitung dua kali (double counting).",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-08_Ujian_Tengah_Semester_Proyek_Mini_3_Navi.pdf",
        "level": "SMA"
      },
      {
        "code": "M-09",
        "title": "Struktur Data: Merekam Jejak Perjalanan (Array of Chars)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Memahami penggunaan struktur data Array 1 Dimensi (char rawPath[100]) dan penunjuk indeks (int pathLength) di C++.",
          "Merekam setiap keputusan belokan yang diambil pada persimpangan ke dalam memori array menggunakan kode karakter standar: 'L' (Kiri), 'R' (Kanan), 'S' (Lurus/Straight), dan 'U' (Putar Balik/U-Turn).",
          "Mencetak seluruh isi rekaman jejak perjalanan sebagai sebuah String utuh."
        ],
        "theory": "<p>Agar robot bisa mengingat jalan yang pernah ia lalui, robot membutuhkan struktur data <strong>Array of Characters (<code>char rawPath[100]</code>)</strong>. Setiap kali robot melewati sebuah persimpangan (atau jalan buntu), kita menyisipkan 1 huruf simbol keputusan ke urutan indeks berikutnya:</p> <ul> <li><code>'L'</code> (<em>Left</em>): Belok Kiri 90&deg; di persimpangan.</li> <li><code>'R'</code> (<em>Right</em>): Belok Kanan 90&deg; di persimpangan.</li> <li><code>'S'</code> (<em>Straight</em>): Memilih jalan Lurus melewati persimpangan.</li> <li><code>'U'</code> (<em>U-Turn</em>): Berputar balik 180&deg; karena menemui jalan buntu.</li> </ul> <p>Contoh: Jika robot belok kiri, lalu masuk jalan buntu (putar balik), lalu belok kiri lagi, dan terakhir jalan lurus, maka isi array <code>rawPath</code> adalah: <strong><code>['L', 'U', 'L', 'S']</code></strong> dengan <code>pathLength = 4</code>.</p>",
        "safety": "Selalu periksa batas ukuran array (if (pathLength < MAX_PATH - 1)) sebelum menyimpan elemen baru agar tidak terjadi Buffer Overflow di memori ESP32.",
        "steps": [
          "Deklarasikan <code>const int MAX_PATH = 100;</code>, <code>char rawPath[MAX_PATH];</code>, dan <code>int pathLength = 0;</code>.",
          "Buat fungsi <code>rekamLangkah(char aksi)</code> yang menyimpan karakter ke <code>rawPath[pathLength]</code> lalu menaikkan nilai <code>pathLength++</code>.",
          "Simulasikan penambahan beberapa langkah di <code>void setup()</code> dan tampilkan hasilnya di Serial Monitor!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-09: Struktur Data Array of Chars untuk Perekaman Jejak Labirin\n// =========================================================================\nconst int MAX_PATH = 100;\nchar rawPath[MAX_PATH]; // Array penyimpan riwayat belokan\nint pathLength = 0; // Jumlah langkah yang sudah terekam void resetMemoriJejak() { pathLength = 0; rawPath[0] = '\\0'; // Null-terminator penanda akhir string C\n} void rekamLangkah(char aksi) { if (pathLength < (MAX_PATH - 1)) { rawPath[pathLength] = aksi; pathLength++; rawPath[pathLength] = '\\0'; // Jaga agar selalu valid sebagai C-String Serial.print(\"[MEMORY] Langkah Ditambahkan: \"); Serial.print(aksi); Serial.print(\" | Jejak Saat Ini (\"); Serial.print(pathLength); Serial.print(\"): \"); Serial.println(rawPath); }\n} void setup() { Serial.begin(115200); resetMemoriJejak(); // Simulasi robot melewati 5 titik persimpangan/buntu: rekamLangkah('L'); // Simpang 1: Belok Kiri rekamLangkah('U'); // Buntu: Putar Balik 180 rekamLangkah('L'); // Kembali ke Simpang 1: Belok Kiri (yang berarti lurus dari arah awal) rekamLangkah('R'); // Simpang 2: Belok Kanan rekamLangkah('S'); // Simpang 3: Lurus menuju Finish\n} void loop() {}",
        "lks": "<p><strong>Latihan Representasi Array Jejak Perjalanan:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Indeks Array</th><th><code>rawPath[0]</code></th><th><code>rawPath[1]</code></th><th><code>rawPath[2]</code></th><th><code>rawPath[3]</code></th><th><code>rawPath[4]</code></th><th><code>rawPath[5]</code></th></tr> </thead> <tbody> <tr><td><strong>Isi Karakter</strong></td><td><code>'S'</code></td><td><code>'L'</code></td><td><code>'U'</code></td><td><code>'L'</code></td><td><code>'R'</code></td><td><code>'\\0'</code></td></tr> </tbody> </table> <p>Pertanyaan: Berapakah nilai variabel <code>pathLength</code> pada tabel di atas? Jawab: <strong>.......</strong></p>",
        "troubleshooting": "Menambahkan karakter null-terminator '\\0' setiap kali habis mengisi elemen baru sangat memudahkan kita karena array char tersebut bisa langsung dicetak dengan Serial.println(rawPath)!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-09_Struktur_Data_Merekam_Jejak_Perjalanan_A.pdf",
        "level": "SMA"
      },
      {
        "code": "M-10",
        "title": "Fase Eksplorasi (Mapping Run)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Menggabungkan navigasi Left-Hand Rule dengan perekaman jejak Array of Chars (rekamLangkah()).",
          "Membedakan antara koreksi di dalam koridor biasa vs keputusan di persimpangan/jalan buntu agar array hanya mencatat node keputusan yang relevan.",
          "Menjalankan robot menyusuri labirin dari Start hingga Finish dan memverifikasi hasil rekaman rawPath."
        ],
        "theory": "<p>Pada <strong>Fase Eksplorasi (Mapping Run)</strong>, robot berjalan menyusuri labirin untuk pertama kalinya menggunakan aturan <em>Left-Hand Rule</em>. Setiap kali robot mengeksekusi keputusan pada persimpangan atau jalan buntu, hasil karakter dari fungsi <code>char aksi = ambilKeputusanSimpangStabil();</code> langsung dimasukkan ke dalam fungsi <code>rekamLangkah(aksi);</code>.</p> <p>Begitu sensor bawah TCRT5000 menyentuh garis Finish hitam, robot berhenti dan menampilkan seluruh riwayat jejak penjelajahannya (misalnya: <code>\"SLULSRULLR\"</code>) ke layar Web Dashboard!</p>",
        "safety": "Pastikan memori jejak di-reset (resetMemoriJejak()) setiap kali robot memulai Mapping Run baru dari garis Start.",
        "steps": [
          "Siapkan arena labirin yang memiliki minimal 1 cabang jalan buntu (Dead-End).",
          "Unggah kode Mapping Run M-10 ke robot dan jalankan dari titik Start.",
          "Ikuti perjalanan robot dan catat secara manual huruf keputusan di setiap simpang, lalu cocokkan catatan manualmu dengan string <code>rawPath</code> yang dikirim robot ke Web Dashboard saat menyentuh Finish!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-10: Fase Eksplorasi (Mapping Run) + Perekaman Array Otomatis\n// ========================================================================= void jalankanMappingRun() { // 1. Cek apakah sudah sampai di Garis Finish (TCRT5000) if (bot.isFinishLine()) { bot.drive(0, 0); String pesanFinish = \"MAPPING SELESAI! Raw Path: \" + String(rawPath); bot.sendTelemetry(0, 0, 0, pesanFinish); Serial.println(pesanFinish); currentState = STATE_FINISH_COMPUTE; return; } // 2. Baca ketiga sensor ultrasonik float L = bot.readLeft(); float F = bot.readFront(); float R = bot.readRight(); // 3. Jika mendeteksi persimpangan (bukaan kiri/kanan) atau jalan buntu/dinding depan if (L > 16.0 || R > 16.0 || F < 13.0) { char aksiDiambil = ambilKeputusanSimpangStabil(); rekamLangkah(aksiDiambil); // Simpan 'L', 'R', 'S', atau 'U' ke dalam rawPath[] bot.sendTelemetry(L, F, R, \"Recorded: \" + String(rawPath)); } else { // Selama di lorong lurus biasa, gunakan koreksi dinding proporsional majuClosedLoop(L); }\n}",
        "lks": "<p><strong>Verifikasi Rekaman Mapping Run vs Pengamatan Manual:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Urutan Node</th><th>Kondisi Simpang di Labirin</th><th>Aksi Fisik Robot</th><th>Huruf yang Tercatat di <code>rawPath</code></th></tr> </thead> <tbody> <tr><td>Node 1</td><td>Simpang Tiga (Belok Kiri ke Jalan Buntu)</td><td>Belok Kiri</td><td><code>'L'</code></td></tr> <tr><td>Node 2</td><td>Ujung Jalan Buntu</td><td>Putar Balik 180&deg;</td><td><code>'U'</code></td></tr> <tr><td>Node 3</td><td>Kembali ke Simpang Tiga Awal</td><td>Belok Kiri</td><td><code>'L'</code></td></tr> <tr><td>Node 4</td><td>Simpang Berikutnya Menuju Finish</td><td>.....................</td><td><code>'...'</code></td></tr> </tbody> </table>",
        "troubleshooting": "Perhatikan Node 1, 2, dan 3 pada tabel LKS di atas: ketiganya membentuk pola 'L' -> 'U' -> 'L'. Pada modul M-11 berikutnya, kita akan mempelajari bagaimana memangkas ketiga langkah sia-sia tersebut menjadi 1 langkah 'S' (Lurus)!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-10_Fase_Eksplorasi_Mapping_Run.pdf",
        "level": "SMA"
      },
      {
        "code": "M-11",
        "title": "Teori Algoritma Reduksi Jalan Buntu (Dead-End Elimination)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Memahami logika matematis substitusi pola 3 huruf yang mengandung huruf 'U' (U-Turn / Jalan Buntu) menjadi 1 huruf langkah langsung.",
          "Menguasai ke-5 rumus aturan reduksi jalan buntu: LUL = S, LUS = R, LUR = U, SUL = R, dan SUS = U.",
          "Melakukan reduksi berulang (iteratif) di atas kertas untuk menyederhanakan jejak eksplorasi panjang menjadi rute terpendek."
        ],
        "theory": "<p>Setiap kali di dalam rekaman perjalanan terdapat huruf <strong><code>'U'</code> (Putar Balik)</strong>, itu adalah bukti pasti bahwa robot baru saja tersesat masuk ke dalam <strong>Jalan Buntu</strong>! Tiga langkah berurutan <code>[Aksi Masuk] + 'U' + [Aksi Keluar]</code> sebenarnya dapat digantikan (direduksi) menjadi <strong>1 langkah langsung</strong> seandainya robot tidak masuk ke jalan buntu tersebut:</p> <table class=\"std-table\"> <thead> <tr><th>Pola 3 Karakter (Tersesat ke Buntu)</th><th>Makna Gerakan Fisik Asli</th><th>Hasil Reduksi (1 Karakter)</th><th>Makna Gerakan Baru (Tanpa Tersesat)</th></tr> </thead> <tbody> <tr><td><strong><code>L + U + L</code></strong></td><td>Belok Kiri (-90&deg;), Putar Balik (+180&deg;), Belok Kiri (-90&deg;)</td><td><strong><code>S</code></strong></td><td>Langsung <strong>Lurus (Straight 0&deg;)</strong> melewati simpang!</td></tr> <tr><td><strong><code>L + U + S</code></strong></td><td>Belok Kiri (-90&deg;), Putar Balik (+180&deg;), Jalan Lurus (0&deg;)</td><td><strong><code>R</code></strong></td><td>Langsung <strong>Belok Kanan (+90&deg;)</strong>!</td></tr> <tr><td><strong><code>S + U + L</code></strong></td><td>Jalan Lurus (0&deg;), Putar Balik (+180&deg;), Belok Kiri (-90&deg;)</td><td><strong><code>R</code></strong></td><td>Langsung <strong>Belok Kanan (+90&deg;)</strong>!</td></tr> <tr><td><strong><code>L + U + R</code></strong></td><td>Belok Kiri (-90&deg;), Putar Balik (+180&deg;), Belok Kanan (+90&deg;)</td><td><strong><code>U</code></strong></td><td>Simpang itu sendiri buntu &rarr; <strong>Putar Balik (U)</strong></td></tr> <tr><td><strong><code>S + U + S</code></strong></td><td>Jalan Lurus (0&deg;), Putar Balik (+180&deg;), Jalan Lurus (0&deg;)</td><td><strong><code>U</code></strong></td><td>Simpang itu sendiri buntu &rarr; <strong>Putar Balik (U)</strong></td></tr> </tbody> </table> <div class=\"formula-box\"> Contoh Bertingkat: &nbsp; L L U L U L R &nbsp;&rarr;&nbsp; L (L U L) U L R &nbsp;&rarr;&nbsp; L S U L R &nbsp;&rarr;&nbsp; L (S U L) R &nbsp;&rarr;&nbsp; L R (Rute Terpendek!) </div>",
        "safety": "Pahami penjumlahan sudutnya: Kiri = -90 derajat, Kanan = +90 derajat, Lurus = 0 derajat, Putar Balik = +180 derajat. Contoh: L + U + S = -90 + 180 + 0 = +90 derajat (sama dengan Belok Kanan 'R')!",
        "steps": [
          "Pelajari rumus penjumlahan sudut rotasi mengapa 3 langkah yang mengapit huruf <code>U</code> selalu ekuivalen dengan 1 langkah tunggal.",
          "Ambil kertas kerja LKS dan selesaikan latihan pemangkasan string jejak labirin secara bertahap sampai tidak ada lagi huruf <code>U</code> yang tersisa!",
          "Tuliskan fungsi pencocokan pola <code>char aturanReduksiBuntu(char sebelum, char sesudah)</code> di C++."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-11: Aturan Substitusi Reduksi Jalan Buntu (Dead-End Rules)\n// ========================================================================= // Mengembalikan karakter tunggal pengganti pola [sebelum] + 'U' + [sesudah]\nchar aturanReduksiBuntu(char sebelum, char sesudah) { if (sebelum == 'L' && sesudah == 'L') return 'S'; // L + U + L = S if (sebelum == 'L' && sesudah == 'S') return 'R'; // L + U + S = R if (sebelum == 'L' && sesudah == 'R') return 'U'; // L + U + R = U if (sebelum == 'S' && sesudah == 'L') return 'R'; // S + U + L = R if (sebelum == 'S' && sesudah == 'S') return 'U'; // S + U + S = U if (sebelum == 'R' && sesudah == 'L') return 'U'; // R + U + L = U return '?'; // Pola tidak valid\n}",
        "lks": "<p><strong>Latihan Komputasi Manual Reduksi Rute Labirin:</strong></p> <table class=\"std-table\"> <thead> <tr><th>No</th><th>String Jejak Eksplorasi Mentah (<code>rawPath</code>)</th><th>Tahap Pemangkasan 1</th><th>Hasil Akhir Rute Terpendek (<code>optPath</code>)</th></tr> </thead> <tbody> <tr><td>1</td><td><code>S L U L R</code></td><td><code>S (L U L) R</code> &rarr; ............</td><td>........................</td></tr> <tr><td>2</td><td><code>L U S R L U L</code></td><td><code>(L U S) R (L U L)</code> &rarr; ............</td><td>........................</td></tr> <tr><td>3</td><td><code>S L L U L U S L</code></td><td><code>S L (L U L) U S L</code> &rarr; <code>S L S U S L</code> &rarr; ...</td><td>........................</td></tr> </tbody> </table>",
        "troubleshooting": "Pada soal nomor 3, setelah LUL diubah menjadi S, muncul huruf U berikutnya yang membentuk pola baru! Itulah sebabnya algoritma pemangkasan harus dijalankan di dalam perulangan while sampai seluruh huruf 'U' habis.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-11_Teori_Algoritma_Reduksi_Jalan_Buntu_Dead.pdf",
        "level": "SMA"
      },
      {
        "code": "M-12",
        "title": "Implementasi Fungsi Pemangkasan Array (Path Simplification Engine)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Menulis algoritma Path Simplification Engine di C++ untuk menyalin rawPath[] ke optPath[] dan memangkas semua pola X + U + Y secara otomatis.",
          "Menggunakan pendekatan perulangan while untuk menangani jalan buntu bercabang (nested dead-ends).",
          "Menguji fungsi pemangkasan dengan berbagai skenario string uji melalui Serial Monitor."
        ],
        "theory": "<p>Bagaimana cara paling elegan menulis algoritma pemangkas array di C++? Ketika kita menemukan huruf <code>'U'</code> pada indeks <code>i</code> (yaitu <code>optPath[i] == 'U'</code>), kita mengganti elemen di kirinya (<code>optPath[i-1]</code>) dengan hasil substitusi <code>substitusiBuntu(optPath[i-1], optPath[i+1])</code>, lalu <strong>menggeser seluruh elemen setelahnya maju sebanyak 2 kotak ke kiri</strong> (mengurangi panjang array sebanyak 2)!</p> <p>Proses pencarian ini diulang di dalam <code>while (masihAdaU)</code> sampai tidak ada lagi huruf <code>'U'</code> di dalam array <code>optPath</code>.</p>",
        "safety": "Pastikan indeks pencarian dimulai dari i = 1 hingga i < optLength - 1 agar akses optPath[i-1] dan optPath[i+1] selalu berada di dalam batas memori array yang sah.",
        "steps": [
          "Ketikkan kode lengkap <strong>Path Simplification Engine</strong> (M-12) di bawah ini pada Arduino IDE.",
          "Unggah ke ESP32 dan buka Serial Monitor.",
          "Amati bagaimana string mentah sepanjang 13 langkah seperti <code>\"SLLULUSLRULLS\"</code> dipangkas dalam waktu kurang dari 1 milidetik menjadi rute terpendek yang bersih dari jalan buntu!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-12: Path Simplification Engine (Algoritma Pemangkas Array C++)\n// =========================================================================\nchar rawPath[100] = \"SLLULUSLRULLS\"; // Contoh jejak mentah hasil Mapping Run\nchar optPath[100]; // Array hasil optimasi rute terpendek\nint optLength = 0; char substitusiBuntu(char A, char B) { if (A == 'L' && B == 'L') return 'S'; if (A == 'L' && B == 'S') return 'R'; if (A == 'L' && B == 'R') return 'U'; if (A == 'S' && B == 'L') return 'R'; if (A == 'S' && B == 'S') return 'U'; if (A == 'R' && B == 'L') return 'U'; return 'U';\n} void pangkasRuteJalanBuntu() { // 1. Salin isi rawPath ke optPath agar rawPath asli tetap tersimpan untuk laporan strcpy(optPath, rawPath); optLength = strlen(optPath); bool masihAdaU = true; int tahap = 1; while (masihAdaU) { masihAdaU = false; for (int i = 1; i < optLength - 1; i++) { if (optPath[i] == 'U') { char pengganti = substitusiBuntu(optPath[i - 1], optPath[i + 1]); optPath[i - 1] = pengganti; // Ganti 3 huruf (i-1, i, i+1) dengan 1 huruf // Geser sisa array di sebelah kanan maju 2 langkah ke kiri for (int j = i; j < optLength - 2; j++) { optPath[j] = optPath[j + 2]; } optLength -= 2; optPath[optLength] = '\\0'; Serial.printf(\" [Tahap %d] Reduksi -> %s (Panjang: %d)\\n\", tahap++, optPath, optLength); masihAdaU = true; break; // Mulai scan ulang dari depan untuk menangani nested U-turn } } }\n} void setup() { Serial.begin(115200); Serial.print(\"Jejak Mentah (Raw Path) : \"); Serial.println(rawPath); pangkasRuteJalanBuntu(); Serial.print(\"Rute Terpendek (Optimized) : \"); Serial.println(optPath);\n} void loop() {}",
        "lks": "<p><strong>Hasil Eksekusi Path Simplification Engine di ESP32:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Input <code>rawPath</code></th><th>Panjang Awal</th><th>Output <code>optPath</code> di Serial Monitor</th><th>Panjang Akhir</th><th>Persentase Penghematan Langkah</th></tr> </thead> <tbody> <tr><td><code>\"SLLULUSLRULLS\"</code></td><td>13 langkah</td><td>..............................</td><td>..... langkah</td><td>.......... % lebih singkat</td></tr> <tr><td><code>\"LULSLULR\"</code></td><td>8 langkah</td><td>..............................</td><td>..... langkah</td><td>.......... % lebih singkat</td></tr> </tbody> </table>",
        "troubleshooting": "Mengapa kita menyalin rawPath ke optPath menggunakan strcpy(optPath, rawPath)? Supaya di Web Dashboard kita bisa menampilkan perbandingan 'Before (Raw Path)' dan 'After (Optimized Path)' secara berdampingan!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-12_Implementasi_Fungsi_Pemangkasan_Array_Pa.pdf",
        "level": "SMA"
      },
      {
        "code": "M-13",
        "title": "Visualisasi Reduksi Rute pada Dashboard Web",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Mengirimkan pasangan data rawPath (jalur eksplorasi mentah) dan optPath (jalur hasil reduksi) ke antarmuka Web Dashboard.",
          "Menganalisis efisiensi algoritma berdasarkan metrik jumlah persimpangan yang dipangkas dan estimasi penghematan waktu.",
          "Menggunakan tombol interaktif pada Web Dashboard untuk mengonfirmasi kesiapan mode Speed Run."
        ],
        "theory": "<p>Setelah robot menyentuh garis Finish pada akhir <em>Mapping Run</em> dan menjalankan fungsi <code>pangkasRuteJalanBuntu()</code>, siswa perlu memverifikasi secara visual apakah rute terpendek yang dihitung oleh otak ESP32 sudah sesuai dengan bentuk fisik labirin.</p> <p>Starter API menyediakan fungsi <strong><code>bot.sendRouteSummary(rawPath, optPath, exploreTimeSec)</code></strong> yang langsung menampilkan kartu perbandingan <em>Exploration Path vs Shortest Path</em> pada layar Web Dashboard!</p>",
        "safety": "Saat robot berada pada state selesai eksplorasi (STATE_DONE), pastikan motor terkunci penuh (PWM 0) sembari siswa menganalisis data di layar web dan memindahkan robot kembali ke titik Start.",
        "steps": [
          "Panggil fungsi <code>bot.sendRouteSummary(rawPath, optPath, detikExplore);</code> tepat setelah fungsi <code>pangkasRuteJalanBuntu()</code> selesai dieksekusi.",
          "Amati panel <strong>Path Reduction Visualizer</strong> pada Web Dashboard.",
          "Verifikasi bahwa setiap pola jalan buntu (yang berwarna merah di layar web) telah berubah menjadi langkah langsung (berwarna hijau)."
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-13: Pengiriman & Visualisasi Perbandingan Rute ke Web Dashboard\n// ========================================================================= void tampilkanAnalisisRuteKeWeb(unsigned long waktuExploreMs) { // 1. Jalankan mesin pemangkas jalan buntu pangkasRuteJalanBuntu(); // 2. Hitung metrik efisiensi int langkahAwal = strlen(rawPath); int langkahAkhir = strlen(optPath); int langkahHemat = langkahAwal - langkahAkhir; float detikExplore = waktuExploreMs / 1000.0; // 3. Kirim ke kartu visualisasi Web Dashboard melalui Starter API bot.sendRouteSummary(rawPath, optPath, detikExplore); // 4. Kirim pesan ringkasan ke log telemetri String info = \"RAW: \" + String(rawPath) + \" (\" + String(langkahAwal) + \") -> \" + \"OPT: \" + String(optPath) + \" (\" + String(langkahAkhir) + \") | \" + \"Hemat: \" + String(langkahHemat) + \" simpang!\"; bot.sendTelemetry(0, 0, 0, info);\n}",
        "lks": "<p><strong>Lembar Analisis Data Telemetri Reduksi Rute:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Metrik Evaluasi</th><th>Data pada Web Dashboard</th><th>Analisis Siswa</th></tr> </thead> <tbody> <tr><td>String <code>rawPath</code> (Explore Run)</td><td><code>....................................</code></td><td>Jumlah masuk jalan buntu (huruf U): .... kali</td></tr> <tr><td>String <code>optPath</code> (Optimized)</td><td><code>....................................</code></td><td>Seluruh huruf U berhasil dieliminasi? Ya / Tidak</td></tr> <tr><td>Waktu Tempuh Explore Run</td><td>................ detik</td><td>Prediksi waktu Speed Run: &lt; ............ detik</td></tr> </tbody> </table>",
        "troubleshooting": "Jika tampilan di browser belum memperbarui string optPath, pastikan fungsi bot.updateWeb() tetap dipanggil di dalam perulangan tunggu STATE_DONE.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-13_Visualisasi_Reduksi_Rute_pada_Dashboard_.pdf",
        "level": "SMA"
      },
      {
        "code": "M-14",
        "title": "Fase Eksekusi Jalur Tercepat (Speed Run)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Memprogram pergantian mode dari MODE_EXPLORE ke MODE_SPEED_RUN saat robot ditaruh kembali di garis Start.",
          "Membaca array optPath[stepIndex] langkah demi langkah setiap kali robot mendeteksi persimpangan, tanpa perlu memindai jalan buntu lagi.",
          "Meningkatkan kecepatan jelajah untuk mencapai waktu tempuh tercepat menuju garis Finish."
        ],
        "theory": "<p>Inilah momen paling memukau dalam robotika labirin otonom: <strong>Fase Eksekusi Jalur Tercepat (Speed Run)</strong>! Setelah robot diangkat dari garis Finish dan diletakkan kembali di garis Start, kita menekan tombol <strong>[START SPEED RUN]</strong> di Web Dashboard (atau tombol fisik di robot).</p> <p>Pada mode <em>Speed Run</em>, ketika robot mendeteksi persimpangan ke-<code>stepIndex</code>, robot tidak lagi menebak-nebak dengan <em>Left-Hand Rule</em>, melainkan <strong>langsung mengeksekusi instruksi dari memori <code>optPath[stepIndex]</code></strong>:</p> <ul> <li>Jika <code>optPath[stepIndex] == 'L'</code> &rarr; Langsung eksekusi Belok Kiri!</li> <li>Jika <code>optPath[stepIndex] == 'R'</code> &rarr; Langsung eksekusi Belok Kanan!</li> <li>Jika <code>optPath[stepIndex] == 'S'</code> &rarr; Langsung melaju Lurus melewati simpang tanpa ragu!</li> </ul>",
        "safety": "Saat menaikkan kecepatan untuk Speed Run (misal dari PWM 145 ke 160), pastikan nilai DELAY_BELOK90 disesuaikan sedikit karena putaran motor yang lebih cepat membutuhkan durasi belok yang sedikit lebih singkat.",
        "steps": [
          "Tambahkan variabel <code>int stepIndex = 0;</code> sebagai penunjuk langkah saat Speed Run.",
          "Implementasikan fungsi <code>jalankanSpeedRun()</code> seperti pada kode M-14 di bawah.",
          "Jalankan robot dari Explore Run, biarkan ia memangkas rute di Finish, lalu pindahkan ke Start dan jalankan Speed Run! Bandingkan waktu tempuh keduanya!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-14: Eksekusi Jalur Terpendek (Speed Run Mode) Berbasis Array optPath\n// =========================================================================\nint stepIndex = 0; // Indeks pembacaan array optPath[] saat Speed Run void mulaiSpeedRunDariStart() { stepIndex = 0; bot.sendTelemetry(0, 0, 0, \"SPEED RUN DIMULAI! Mengikuti Rute: \" + String(optPath));\n} void jalankanSpeedRun() { // 1. Cek apakah sudah menyentuh Garis Finish Hitam (TCRT5000) if (bot.isFinishLine()) { bot.drive(0, 0); bot.sendTelemetry(0, 0, 0, \"SPEED RUN FINISH! Rute Terpendek Tuntas!\"); currentState = STATE_DONE; return; } float L = bot.readLeft(); float F = bot.readFront(); float R = bot.readRight(); // 2. Jika mendeteksi persimpangan (bukaan kiri/kanan atau dinding depan) if (L > 16.0 || R > 16.0 || F < 13.0) { // Maju sedikit ke titik pusat simpang if (F > 12.0) { bot.drive(150, 150); delay(200); } bot.drive(0, 0); delay(100); // Baca instruksi matang dari array optPath pada indeks stepIndex! char perintah = optPath[stepIndex]; if (stepIndex < optLength) stepIndex++; bot.sendTelemetry(L, F, R, \"SpeedRun Step #\" + String(stepIndex) + \" -> \" + String(perintah)); if (perintah == 'L') { bot.turnLeft90(); bot.drive(155, 155); delay(350); } else if (perintah == 'R') { bot.turnRight90(); bot.drive(155, 155); delay(350); } else if (perintah == 'S') { bot.drive(160, 160); delay(380); // Lurus cepat melewati mulut simpang! } } else { // Di lorong lurus, gunakan Closed-Loop Wall Correction majuClosedLoop(L); }\n}",
        "lks": "<p><strong>Tabel Perbandingan Performa Explore Run vs Speed Run:</strong></p> <table class=\"std-table\"> <thead> <tr><th>Parameter Perbandingan</th><th>Fase 1: Explore Run (Left-Hand Rule)</th><th>Fase 2: Speed Run (Array <code>optPath</code>)</th></tr> </thead> <tbody> <tr><td>Rute yang Ditempuh</td><td><code>rawPath = ....................</code></td><td><code>optPath = ....................</code></td></tr> <tr><td>Jumlah Masuk Jalan Buntu</td><td>......... kali</td><td><strong>0 kali (Bebas Jalan Buntu!)</strong></td></tr> <tr><td>Catatan Waktu Stopwatch</td><td>................ detik</td><td>................ detik</td></tr> </tbody> </table>",
        "troubleshooting": "Perhatikan saat perintah == 'S' (Lurus melewati persimpangan): kita tidak perlu berhenti lama di simpang, cukup melaju lurus selama 380 ms sampai mulut cabang kiri/kanan terlewati!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-14_Fase_Eksekusi_Jalur_Tercepat_Speed_Run.pdf",
        "level": "SMA"
      },
      {
        "code": "M-15",
        "title": "Sistem Pengaman & Watchdog (Failsafe & E-Stop)",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Mengimplementasikan fitur tombol darurat nirkabel Emergency Stop (bot.isEmergencyStop()) dari Web Dashboard untuk menghentikan motor seketika.",
          "Membangun algoritma pendeteksi roda macet / tersangkut dinding (Stuck Watchdog Timer) apabila jarak depan tidak berubah (< 4.5 cm) selama lebih dari 2 detik.",
          "Meningkatkan keandalan dan keselamatan operasional robot otonom berkecepatan tinggi."
        ],
        "theory": "<p>Dalam standar industri robotika otonom (seperti AGV di pabrik), setiap robot wajib memiliki dua lapis sistem pengaman (<strong>Failsafe</strong>):</p> <ol> <li><strong>Wireless Emergency Stop (E-Stop):</strong> Tombol merah besar di layar Web Dashboard yang jika ditekan oleh operator, langsung memutus sinyal PWM motor (<code>bot.drive(0,0)</code>) dan mengunci state ke <code>STATE_ESTOP</code>.</li> <li><strong>Stuck / Slip Watchdog:</strong> Jika bodi robot tidak sengaja menyangkut di sudut dinding sehingga roda terus berputar selip di tempat (<code>jarakDepan &lt; 4.5 cm</code> terus-menerus selama &gt; 2000 ms), sistem Watchdog otomatis menghentikan motor atau melakukan manuver mundur pembebasan diri (<em>Auto-Recovery</em>) agar motor DC dan driver DRV8833 tidak panas/terbakar!</li> </ol>",
        "safety": "Jangan pernah membiarkan motor DC tertahan (stall) dalam kondisi diberi tegangan PWM tinggi lebih dari 3 detik karena arus stall dapat merusak gigi gearbox dan menguras baterai 18650.",
        "steps": [
          "Tambahkan fungsi <code>cekSistemFailsafe(float jarakDepan)</code> di baris paling awal <code>void loop()</code>.",
          "Uji tombol <strong>[E-STOP DARURAT]</strong> pada layar Web Dashboard saat robot sedang melaju.",
          "Simulasikan kondisi tersangkut dengan menahan penghalang tepat 3 cm di depan robot selama 2 detik; pastikan Watchdog aktif memundurkan/menghentikan robot!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-15: Sistem Pengaman E-Stop Nirkabel & Stuck Watchdog Timer\n// =========================================================================\nunsigned long stuckTimerStart = 0;\nbool isStuckMonitoring = false; bool cekSistemFailsafe(float jarakDepan) { // 1. Cek Tombol Emergency Stop (E-Stop) dari Web Dashboard if (bot.isEmergencyStop()) { bot.drive(0, 0); bot.sendTelemetry(0, jarakDepan, 0, \"E-STOP AKTIF! Motor Dikunci oleh Operator.\"); return true; // Mengindikasikan interupsi darurat aktif } // 2. Stuck Watchdog: Deteksi jika robot nyangkut dinding depan (< 4.5 cm) > 2 detik if (jarakDepan < 4.5) { if (!isStuckMonitoring) { isStuckMonitoring = true; stuckTimerStart = millis(); } else if (millis() - stuckTimerStart > 2000) { // Robot terbukti tersangkut selama 2 detik! Lakukan Auto-Recovery atau Stop: bot.drive(0, 0); bot.sendTelemetry(0, jarakDepan, 0, \"WATCHDOG: Robot Tersangkut! Melakukan Mundur Bebas...\"); bot.drive(-145, -145); delay(350); // Mundur pembebasan diri bot.drive(0, 0); delay(200); isStuckMonitoring = false; return true; } } else { isStuckMonitoring = false; // Reset timer jika jarak depan aman } return false; // Sistem aman, lanjutkan navigasi normal\n}",
        "lks": "<p><strong>Lembar Pengujian Sistem Keamanan (Failsafe &amp; Watchdog):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Skenario Pengujian</th><th>Kondisi Pemicu</th><th>Respon Failsafe Robot</th><th>Status Kelulusan Uji</th></tr> </thead> <tbody> <tr><td>Uji E-Stop Nirkabel</td><td>Tombol E-Stop di Web ditekan</td><td>Motor berhenti dalam &lt; 0.1 detik</td><td>Lulus / Gagal</td></tr> <tr><td>Uji Stuck Watchdog</td><td>Dinding ditahan 3 cm di depan &gt; 2 dtk</td><td>Peringatan Web &amp; Mundur Otomatis</td><td>Lulus / Gagal</td></tr> </tbody> </table>",
        "troubleshooting": "Fitur Auto-Recovery (mundur 350 ms saat tersangkut) sangat berguna di dalam kompetisi karena menyelamatkan robot yang menyerempet dinding tanpa perlu disentuh tangan (bebas penalti retry)!",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-15_Sistem_Pengaman_Watchdog_Failsafe_E_Stop.pdf",
        "level": "SMA"
      },
      {
        "code": "M-16",
        "title": "Capstone Project: Autonomous Maze Grand Prix",
        "duration": "2 JP (2 x 45 Menit)",
        "phase": "Fase E/F (Kelas X–XII SMA/SMK)",
        "objectives": [
          "Mendemonstrasikan penguasaan utuh rekayasa perangkat lunak robot otonom melalui evaluasi 3 tahapan resmi: Explore Run, Data Analysis, dan Speed Run.",
          "Mengeksekusi Kode Master SMA/SMK yang mengintegrasikan Closed-Loop Wall Correction, Ultrasonic Intersection Classification, Array Path Simplification, Web Telemetry, NVS, dan Failsafe.",
          "Mempresentasikan analisis perbandingan rute mentah (rawPath) terhadap rute teroptimasi (optPath) serta efisiensi waktu tempuh."
        ],
        "theory": "<p>Selamat datang di puncak kurikulum tingkat SMA/SMK: <strong>Capstone Project — Autonomous Maze Grand Prix</strong>! Setiap tim dievaluasi dalam 3 tahapan berkesinambungan:</p> <ol> <li><strong>Tahap 1 — Explore Run (Mapping):</strong> Robot dilepas dari Start, memetakan labirin menggunakan <em>Left-Hand Rule</em>, mencatat setiap persimpangan ke dalam <code>rawPath[]</code>, dan berhenti tepat di atas garis Finish hitam (TCRT5000).</li> <li><strong>Tahap 2 — Data Analysis (Web Verification):</strong> Di garis Finish, robot otomatis menjalankan <em>Path Simplification Engine</em> dan mengirimkan <code>rawPath</code> vs <code>optPath</code> ke Web Dashboard. Siswa memverifikasi hasil pemangkasan rute di hadapan Juri.</li> <li><strong>Tahap 3 — Speed Run (Shortest Path Execution):</strong> Robot ditaruh kembali di garis Start, beralih ke mode <em>Speed Run</em>, dan melintasi rute terpendek <code>optPath[]</code> tanpa sekalipun berbelok ke jalan buntu!</li> </ol>",
        "safety": "Pastikan tombol E-Stop di Web Dashboard selalu siap siaga di layar operator tim selama pelaksanaan Explore Run maupun Speed Run.",
        "steps": [
          "Unggah <strong>Kode Master Capstone M-16</strong> di bawah ini ke unit MazeBot timmu.",
          "Lakukan Tahap 1 (Explore Run) dari garis Start hingga robot berhenti di garis Finish.",
          "Tunjukkan layar Web Dashboard kepada Juri untuk memverifikasi hasil reduksi array (Tahap 2).",
          "Pindahkan robot kembali ke garis Start, tekan tombol mode <strong>Speed Run</strong> di Web Dashboard, dan catat rekor waktu tercepat timmu (Tahap 3)!"
        ],
        "cpp_code": "// =========================================================================\n// MODUL M-16: MASTER CODE CAPSTONE SMA/SMK - AUTONOMOUS MAZE GRAND PRIX\n// =========================================================================\n#include \"MazeBotStarter.h\"\n#include <Preferences.h> MazeBotCore bot;\nPreferences prefs; enum Mode { MODE_EXPLORE, MODE_WAIT_SPEEDRUN, MODE_SPEEDRUN, MODE_FINISHED };\nMode currentMode = MODE_EXPLORE; char rawPath[100];\nchar optPath[100];\nint rawLen = 0, optLen = 0, stepIdx = 0;\nunsigned long startTime = 0; char reduceRule(char A, char B) { if (A == 'L' && B == 'L') return 'S'; if (A == 'L' && B == 'S') return 'R'; if (A == 'L' && B == 'R') return 'U'; if (A == 'S' && B == 'L') return 'R'; if (A == 'S' && B == 'S') return 'U'; return 'U';\n} void simplifyPath() { strcpy(optPath, rawPath); optLen = strlen(optPath); bool changed = true; while (changed) { changed = false; for (int i = 1; i < optLen - 1; i++) { if (optPath[i] == 'U') { optPath[i - 1] = reduceRule(optPath[i - 1], optPath[i + 1]); for (int j = i; j < optLen - 2; j++) optPath[j] = optPath[j + 2]; optLen -= 2; optPath[optLen] = '\\0'; changed = true; break; } } }\n} void setup() { Serial.begin(115200); bot.begin(\"MazeBot-SMA-GP\"); rawPath[0] = '\\0'; optPath[0] = '\\0'; delay(2000); startTime = millis();\n} void loop() { bot.updateWeb(); float L = bot.readLeft(), F = bot.readFront(), R = bot.readRight(); if (cekSistemFailsafe(F)) return; if (currentMode == MODE_EXPLORE) { if (bot.isFinishLine()) { bot.drive(0, 0); float expSec = (millis() - startTime) / 1000.0; simplifyPath(); bot.sendRouteSummary(rawPath, optPath, expSec); currentMode = MODE_WAIT_SPEEDRUN; return; } if (L > 16.0 || R > 16.0 || F < 13.0) { char act = ambilKeputusanSimpangStabil(); if (rawLen < 98) { rawPath[rawLen++] = act; rawPath[rawLen] = '\\0'; } bot.sendTelemetry(L, F, R, \"Explore Rec: \" + String(rawPath)); } else { majuClosedLoop(L); } } else if (currentMode == MODE_WAIT_SPEEDRUN) { bot.drive(0, 0); if (bot.isSpeedRunRequested()) { stepIdx = 0; startTime = millis(); currentMode = MODE_SPEEDRUN; } } else if (currentMode == MODE_SPEEDRUN) { if (bot.isFinishLine()) { bot.drive(0, 0); float spdSec = (millis() - startTime) / 1000.0; bot.sendTelemetry(0, 0, 0, \"GRAND PRIX TUNTAS! SpeedRun: \" + String(spdSec, 2) + \" dtk\"); currentMode = MODE_FINISHED; return; } if (L > 16.0 || R > 16.0 || F < 13.0) { if (F > 12.0) { bot.drive(150, 150); delay(200); } bot.drive(0, 0); delay(100); char cmd = (stepIdx < optLen) ? optPath[stepIdx++] : 'S'; if (cmd == 'L') { bot.turnLeft90(); bot.drive(155, 155); delay(350); } else if (cmd == 'R') { bot.turnRight90(); bot.drive(155, 155); delay(350); } else { bot.drive(160, 160); delay(380); } } else { majuClosedLoop(L); } }\n}",
        "lks": "<p><strong>Lembar Penilaian Akhir Capstone Project (Autonomous Maze Grand Prix - SMA/SMK):</strong></p> <table class=\"std-table\"> <thead> <tr><th>Tahapan &amp; Komponen Evaluasi</th><th>Bobot</th><th>Indikator Keberhasilan</th><th>Skor Tim (0–100)</th></tr> </thead> <tbody> <tr><td><strong>1. Tahap 1: Explore Run &amp; Perekaman Array</strong></td><td>30%</td><td>Menyelesaikan eksplorasi ke garis Finish &amp; mencatat <code>rawPath</code> akurat</td><td>.............</td></tr> <tr><td><strong>2. Tahap 2: Reduksi Jalan Buntu &amp; Telemetri</strong></td><td>30%</td><td>Algoritma pemangkasan menghasilkan <code>optPath</code> bebas huruf 'U' di Web</td><td>.............</td></tr> <tr><td><strong>3. Tahap 3: Eksekusi Speed Run Terpendek</strong></td><td>25%</td><td>Menuntaskan rute terpendek tanpa masuk ke jalan buntu</td><td>.............</td></tr> <tr><td><strong>4. Kestabilan Closed-Loop &amp; Failsafe</strong></td><td>15%</td><td>Koreksi dinding halus, NVS berfungsi, &amp; proteksi E-Stop/Watchdog aktif</td><td>.............</td></tr> <tr><td colspan=\"3\"><strong>TOTAL NILAI CAPSTONE PROJECT (TINGKAT SMA/SMK)</strong></td><td><strong>............. / 100</strong></td></tr> </tbody> </table>",
        "troubleshooting": "Selamat! Dengan tuntasnya Modul M-16 ini, siswa telah menguasai konsep struktur data, finite state machine, algoritma optimasi graf/rute sederhana, dan sistem kontrol tertanam berbasis sensor.",
        "pdf_url": "Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_M-16_Capstone_Project_Autonomous_Maze_Grand_P.pdf",
        "level": "SMA"
      }
    ]
  }
};
