import os

def get_sd_modules():
    return [
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
            "theory": """
                <p><strong>MazeBot EduKit</strong> adalah robot edukasi pintar yang dirancang untuk membantu kita belajar cara berpikir logis seperti ilmuwan komputer. Sama seperti manusia, robot memiliki bagian-bagian tubuh yang bekerja sama:</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Bagian Robot</th><th>Komponen Teknis</th><th>Analogi Tubuh Manusia</th><th>Fungsi Utama</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Otak Robot</strong></td><td>Mikrokontroler ESP32</td><td>Otak Manusia</td><td>Memproses perintah program dan mengatur kerja seluruh bagian robot.</td></tr>
                        <tr><td><strong>Mata Depan/Samping</strong></td><td>3x Sensor Ultrasonik</td><td>Mata / Telinga Kelelawar</td><td>Mendeteksi jarak dinding atau rintangan di depan, kiri, dan kanan.</td></tr>
                        <tr><td><strong>Mata Bawah</strong></td><td>Sensor Garis TCRT5000</td><td>Mata Pengamat Lantai</td><td>Membedakan warna lantai terang (putih) dan garis finish (hitam).</td></tr>
                        <tr><td><strong>Kaki Penggerak</strong></td><td>2x Motor Gearbox TT & Roda</td><td>Kaki Manusia</td><td>Menggerakkan badan robot maju, mundur, belok kanan, dan belok kiri.</td></tr>
                        <tr><td><strong>Jantung Energi</strong></td><td>Baterai Li-Ion 18650</td><td>Jantung & Makanan</td><td>Menyuplai energi listrik agar otak, mata, dan kaki robot dapat bekerja.</td></tr>
                    </tbody>
                </table>
            """,
            "safety": "Baterai 18650 tersimpan di dalam kotak pelindung yang dikunci dengan baut pengaman. Siswa DILARANG membuka baut penutup baterai atau mencolokkan kabel pengisi daya sendiri. Pemasangan dan pengisian baterai 100% hanya boleh dilakukan oleh Bapak/Ibu Guru.",
            "steps": [
                "Amati unit robot MazeBot yang telah disiapkan oleh guru di atas meja kelompok dalam keadaan saklar OFF.",
                "Temukan dan tunjuk bagian Otak (papan ESP32 di bagian tengah), Mata (3 sensor berbentuk silinder kembar di depan/samping), dan Mata Bawah (di kolong depan robot).",
                "Periksa kotak baterai di bagian belakang/bawah robot. Pastikan penutupnya rapat dan baut pengamannya terpasang kuat.",
                "Dengan aba-aba guru, geser saklar daya dari posisi OFF (0) ke posisi ON (1). Perhatikan lampu indikator daya yang menyala."
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Visualisasi Alur Kerja Sistem Robot (Konsep Dasar M-01)</div>
                    <div><span class="block b-event">⚡ Saat Saklar Robot Dinyalakan (ON)</span></div>
                    <div class="block-indent">
                        <div><span class="block b-led">💡 Nyalakan Lampu Indikator Power <span class="param">MERAH</span></span></div>
                        <div><span class="block b-sensor">👀 Siapkan Sensor Jarak (Depan, Kiri, Kanan)</span></div>
                        <div><span class="block b-motion">🛞 Kunci Roda dalam Posisi <span class="param">DIAM / SIAGA</span></span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Tugas Kelompok:</strong> Cocokkan bagian robot dengan pengamatan langsung pada unit MazeBot kelompokmu!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Pertanyaan Pengamatan</th><th>Hasil Pengamatan Siswa</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Berapa jumlah bulatan "mata" ultrasonik pada bagian depan dan samping robot?</td><td>......... pasang (......... bulatan)</td></tr>
                        <tr><td>2</td><td>Berapa jumlah roda karet dan roda bebas (caster wheel) di bawah robot?</td><td>Roda Karet: ..... | Roda Caster: .....</td></tr>
                        <tr><td>3</td><td>Apa warna lampu yang menyala pada papan otak ESP32 saat saklar di-ON-kan?</td><td>Warna: ...............................</td></tr>
                        <tr><td>4</td><td>Tuliskan nama Wi-Fi (SSID) yang tertera pada stiker bodi robotmu!</td><td>SSID: ................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika lampu indikator tidak menyala saat saklar di-ON-kan, segera lapor kepada Guru (jangan mengetuk atau membongkar tempat baterai). Guru akan memeriksa tegangan baterai 18650."
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
            "theory": """
                <p><strong>Apa itu Algoritma?</strong> Algoritma adalah urutan langkah demi langkah yang jelas dan berurutan untuk menyelesaikan masalah. Robot tidak bisa menebak pikiran kita; ia hanya melakukan persis apa yang kita perintahkan dari baris pertama hingga baris terakhir.</p>
                <p>Contoh di kehidupan sehari-hari saat memakai sepatu: (1) Pakai kaus kaki, (2) Masukkan kaki ke sepatu, (3) Ikat tali sepatu. Jika urutannya terbalik—pakai sepatu dulu baru pakai kaus kaki—maka hasilnya akan salah! Begitu pula saat kita memprogram MazeBot melewati ubin lantai.</p>
            """,
            "safety": "Kegiatan dilakukan di lantai kelas menggunakan petak ubin keramik (tanpa menyalakan baterai robot). Pastikan lantai bersih dan tidak licin agar siswa tidak terpeleset saat simulasi.",
            "steps": [
                "Bagi kelompok menjadi 2 peran: 'Programmer' (Pemberi Perintah) dan 'MazeBot' (Pelaksana Perintah).",
                "Gunakan 3x3 petak ubin keramik lantai kelas sebagai arena labirin. Letakkan buku di salah satu ubin sebagai rintangan dinding.",
                "Programmer menuliskan kartu perintah berurutan menggunakan 3 kata kunci saja: <strong>MAJU 1 PETAK</strong>, <strong>HADAP KANAN (90°)</strong>, dan <strong>HADAP KIRI (90°)</strong>.",
                "Siswa 'MazeBot' berjalan menutup mata/mengikuti kartu perintah yang dibacakan Programmer satu per satu hingga mencapai ubin Finish."
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Susunan Kartu Algoritma Sekuensial (Unplugged Block)</div>
                    <div><span class="block b-event">🏁 Mulai Dari Petak START (A1)</span></div>
                    <div class="block-indent">
                        <div><span class="block b-motion">⬆️ Maju <span class="param">2</span> Petak Ubin</span></div>
                        <div><span class="block b-motion">↪️ Hadap Kanan <span class="param">90 Derajat</span></span></div>
                        <div><span class="block b-motion">⬆️ Maju <span class="param">1</span> Petak Ubin</span></div>
                        <div><span class="block b-motion">↩️ Hadap Kiri <span class="param">90 Derajat</span></span></div>
                        <div><span class="block b-motion">⬆️ Maju <span class="param">1</span> Petak Ubin</span></div>
                        <div><span class="block b-led">🎉 Berhenti di Petak FINISH!</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Tantangan Peta Petak:</strong> Jika robot mulai di petak (1,1) menghadap Utara dan petak (1,2) terhalang dinding kardus, tuliskan urutan 4 langkah agar robot sampai di petak (1,3)!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Langkah Ke-</th><th>Perintah yang Dipilih (Maju / Hadap Kanan / Hadap Kiri)</th><th>Posisi Robot Sekarang</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Langkah 1</td><td>...........................................................................</td><td>Petak: ..........</td></tr>
                        <tr><td>Langkah 2</td><td>...........................................................................</td><td>Petak: ..........</td></tr>
                        <tr><td>Langkah 3</td><td>...........................................................................</td><td>Petak: ..........</td></tr>
                        <tr><td>Langkah 4</td><td>...........................................................................</td><td>Petak: ..........</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Siswa sering tertukar antara 'Belok Kanan sambil jalan' dengan 'Putar Badan Hadap Kanan di tempat'. Tekankan bahwa perintah belok hanya memutar arah hadap badan 90 derajat di ubin yang sama."
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
            "theory": """
                <p>Pada <strong>Kanvas Kode Visual</strong>, kita tidak perlu mengetik kode yang rumit. Setiap perintah berbentuk <strong>Balok Puzzle Berwarna</strong>:</p>
                <ul>
                    <li><strong>Kuning (Kejadian/Events):</strong> Pemicu mulainya program, seperti <em>"Saat Program Dimulai"</em>.</li>
                    <li><strong>Hijau (Indikator/LED):</strong> Mengatur nyala lampu indikator atau bunyi bip pada robot.</li>
                    <li><strong>Oranye (Kontrol Waktu):</strong> Mengatur jeda tunggu (<em>tunggu ... detik</em>) atau pengulangan (<em>ulangi selamanya</em>).</li>
                </ul>
                <p>Mengapa kita butuh balok <strong>Tunggu (Wait/Delay)</strong>? Karena otak komputer ESP32 bekerja sangat cepat (jutaan kali per detik). Jika kita menyuruh lampu <em>Nyala</em> lalu langsung <em>Mati</em> tanpa jeda tunggu, mata kita tidak akan sempat melihat lampu berkedip!</p>
            """,
            "safety": "Letakkan robot di bagian tengah meja agar aman. Jangan menyentuh kaki-kaki komponen logam pada papan sirkuit ESP32 dengan tangan basah atau benda logam.",
            "steps": [
                "Buka halaman Kanvas Kode Visual MazeBot pada komputer/tablet yang telah terhubung ke robot.",
                "Tarik balok kuning <strong>[Saat Program Dimulai]</strong> ke tengah kanvas kerja.",
                "Pasangkan balok oranye <strong>[Ulangi Selamanya]</strong> di bawah balok mulai.",
                "Di dalam mulut balok <em>Ulangi Selamanya</em>, masukkan berturut-turut: <strong>[Lampu Indikator NYALA]</strong> &rarr; <strong>[Tunggu 1 Detik]</strong> &rarr; <strong>[Lampu Indikator MATI]</strong> &rarr; <strong>[Tunggu 1 Detik]</strong>.",
                "Klik tombol <strong>[Kirim ke Robot / Run]</strong> dan amati lampu biru pada otak ESP32!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-03: Lampu Berkedip (Blink LED)</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-led">💡 Atur Lampu Indikator Robot <span class="param">NYALA (ON)</span></span></div>
                            <div><span class="block b-control">⏱️ Tunggu <span class="param">1</span> detik</span></div>
                            <div><span class="block b-led">💡 Atur Lampu Indikator Robot <span class="param">MATI (OFF)</span></span></div>
                            <div><span class="block b-control">⏱️ Tunggu <span class="param">1</span> detik</span></div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Eksperimen Waktu Kedip:</strong> Ubahlah angka pada balok <em>Tunggu ... detik</em>, lalu catat apa yang terjadi pada lampu robot!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Percobaan</th><th>Nilai Balok Tunggu Nyala</th><th>Nilai Balok Tunggu Mati</th><th>Bagaimana Kedipan Lampu Robot? (Lambat / Cepat / Sangat Cepat)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>1 detik</td><td>1 detik</td><td>............................................................</td></tr>
                        <tr><td>2</td><td>0.2 detik</td><td>0.2 detik</td><td>............................................................</td></tr>
                        <tr><td>3</td><td>2 detik</td><td>0.5 detik</td><td>............................................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika program tidak berefek pada robot, periksa apakah balok di dalam kanvas sudah menempel rapat (terdengar bunyi 'klik') pada balok utama [Saat Program Dimulai]. Balok yang terlepas (abu-abu) tidak akan dijalankan."
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
            "theory": """
                <p>MazeBot memiliki dua roda penggerak di sisi kiri dan kanan. Agar robot berjalan <strong>Maju Lurus</strong>, kedua roda kiri dan kanan harus berputar ke arah depan secara bersamaan. Sebaliknya, agar robot berjalan <strong>Mundur</strong>, kedua roda harus berputar ke arah belakang bersamaan.</p>
                <p>Semakin lama durasi waktu (detik) yang kita masukkan pada balok gerak, maka semakin jauh pula jarak yang ditempuh oleh MazeBot di lantai.</p>
            """,
            "safety": "PERHATIAN: Mulai modul ini robot akan bergerak fisik! Uji gerak robot di LANTAI KELAS, BUKAN di atas meja tinggi agar robot tidak terjun jatuh dari tepi meja.",
            "steps": [
                "Siapkan jalur lurus di lantai menggunakan penggaris atau meteran sepanjang 100 cm, tandai garis Start.",
                "Di Kanvas Kode Visual, susun balok: <strong>[Saat Dimulai]</strong> &rarr; <strong>[Gerak MAJU selama 1 detik]</strong> &rarr; <strong>[Berhenti selama 1 detik]</strong> &rarr; <strong>[Gerak MUNDUR selama 1 detik]</strong> &rarr; <strong>[Berhenti Total]</strong>.",
                "Letakkan roda depan MazeBot tepat di garis Start lantai.",
                "Jalankan program dan ukur berapa sentimeter robot melaju ke depan sebelum berhenti dan mundur kembali."
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-04: Maju dan Mundur Terukur</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">⏱️ Tunggu <span class="param">2</span> detik (Waktu siap lepas tangan)</span></div>
                        <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> selama <span class="param">2</span> detik</span></div>
                        <div><span class="block b-motion">🛑 Berhenti selama <span class="param">1</span> detik</span></div>
                        <div><span class="block b-motion">⬇️ Gerak <span class="param">MUNDUR</span> selama <span class="param">2</span> detik</span></div>
                        <div><span class="block b-motion">🛑 Berhenti Total</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Tabel Pengukuran Jarak Tempuh:</strong> Ukur menggunakan penggaris berapa jauh robot maju untuk durasi detik berikut!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Durasi Balok Maju (Detik)</th><th>Jarak Tempuh di Lantai (cm)</th><th>Apakah Robot Kembali Tepat ke Garis Start Saat Mundur?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>1 Detik</td><td>............ cm</td><td>Ya / Kurang sedikit / Lebih sedikit</td></tr>
                        <tr><td>2</td><td>2 Detik</td><td>............ cm</td><td>Ya / Kurang sedikit / Lebih sedikit</td></tr>
                        <tr><td>3</td><td>3 Detik</td><td>............ cm</td><td>Ya / Kurang sedikit / Lebih sedikit</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Tambahkan balok [Tunggu 2 detik] paling atas sebelum balok [Gerak Maju], supaya tangan siswa sempat menjauh dari robot setelah menekan tombol mulai."
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
            "theory": """
                <p>Bagaimana robot tanpa roda setir depan (seperti mobil biasa) bisa berbelok? Rahasianya adalah <strong>Perbedaan Putaran Roda (Differential Drive)</strong>, mirip seperti cara tank militer atau kursi roda berbelok!</p>
                <ul>
                    <li><strong>Belok Kanan di Tempat (Pivot Right):</strong> Roda Kiri berputar MAJU, sedangkan Roda Kanan berputar MUNDUR.</li>
                    <li><strong>Belok Kiri di Tempat (Pivot Left):</strong> Roda Kanan berputar MAJU, sedangkan Roda Kiri berputar MUNDUR.</li>
                </ul>
            """,
            "safety": "Pastikan ban karet tidak kotor oleh debu tebal atau kertas menempel, karena ban yang licin akan membuat sudut belokan robot tidak konsisten.",
            "steps": [
                "Gunakan garis siku-siku ubin keramik lantai (sudut 90 derajat) sebagai patokan sudut belok.",
                "Pasang balok <strong>[Belok KANAN selama 0.5 detik]</strong> lalu <strong>[Berhenti]</strong>.",
                "Amati apakah putaran robot kurang dari 90° (kurang patah) atau lebih dari 90° (kelewatan).",
                "Ubah angka desimal detiknya (misal 0.45 detik atau 0.6 detik) sampai robot berputar tepat menghadap garis siku ubin!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-05: Manuver Sudut Siku (Jalur Huruf L)</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">⏱️ Tunggu <span class="param">2</span> detik</span></div>
                        <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> selama <span class="param">1.5</span> detik</span></div>
                        <div><span class="block b-motion">🛑 Berhenti selama <span class="param">0.5</span> detik</span></div>
                        <div><span class="block b-motion">↪️ Belok <span class="param">KANAN 90°</span> (durasi <span class="param">0.55</span> detik)</span></div>
                        <div><span class="block b-motion">🛑 Berhenti selama <span class="param">0.5</span> detik</span></div>
                        <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> selama <span class="param">1.5</span> detik</span></div>
                        <div><span class="block b-motion">🛑 Berhenti Total</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Kalibrasi Sudut Putar Kelompokmu:</strong> Cari durasi detik paling pas untuk robotmu di lantai kelas!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Target Manuver</th><th>Durasi Detik Percobaan 1</th><th>Durasi Detik Terbaik (Pas)</th><th>Arah Roda Kiri & Kanan</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Belok Kanan 90° (Siku Kanan)</td><td>....... detik</td><td>....... detik</td><td>Kiri: Maju | Kanan: Mundur</td></tr>
                        <tr><td>Belok Kiri 90° (Siku Kiri)</td><td>....... detik</td><td>....... detik</td><td>Kiri: Mundur | Kanan: Maju</td></tr>
                        <tr><td>Putar Balik 180° (Hadap Belakang)</td><td>....... detik</td><td>....... detik</td><td>Kiri: Maju | Kanan: Mundur</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Selalu sisipkan [Berhenti selama 0.5 detik] di antara gerak Maju dan Belok agar sisa dorongan maju (inersia) berhenti dulu sebelum robot memutar badan."
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
            "theory": """
                <p>Apakah robot yang melaju paling ngebut selalu menjadi pemenang di dalam labirin? <strong>Ternyata tidak!</strong></p>
                <p>Jika tenaga motor diatur ke <strong>Cepat (100%)</strong> di lantai keramik yang licin, roda karet akan mengalami <em>selip (tergelincir)</em> saat mulai jalan dan susah berhenti tepat waktu saat mengerem. Sebaliknya, jika terlalu <strong>Pelan (<30%)</strong>, motor tidak punya cukup tenaga dorong untuk memutar roda. Kecepatan <strong>Sedang (50%–65%)</strong> adalah kecepatan paling stabil dan akurat!</p>
            """,
            "safety": "Saat menguji kecepatan CEPAT (100%), pastikan area di depan robot minimal sepanjang 2 meter bebas dari kaki meja atau barang pecah belah.",
            "steps": [
                "Buat lintasan lurus sepanjang 1 meter dengan garis batas berhenti di ujungnya.",
                "Susun balok <strong>[Atur Kecepatan Motor ke PELAN (40%)]</strong> dilanjutkan <strong>[Gerak MAJU 2 detik]</strong> dan <strong>[Berhenti]</strong>.",
                "Ulangi percobaan dengan mengubah balok kecepatan ke <strong>SEDANG (65%)</strong> dan <strong>CEPAT (100%)</strong>.",
                "Perhatikan apakah roda robot berdecit/tergelincir saat mulai melaju dan saat mengerem mendadak."
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-06: Eksperimen 3 Tingkat Kecepatan</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-motion">⚙️ Atur Kecepatan Robot ke <span class="param">PELAN (40%)</span></span></div>
                        <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> selama <span class="param">1.5</span> detik</span></div>
                        <div><span class="block b-motion">⚙️ Atur Kecepatan Robot ke <span class="param">SEDANG (65%)</span></span></div>
                        <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> selama <span class="param">1.5</span> detik</span></div>
                        <div><span class="block b-motion">🛑 Berhenti Total</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Uji Kestabilan Kecepatan:</strong> Beri tanda centang pada hasil pengamatan kelompokmu!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Mode Kecepatan</th><th>Jarak Tempuh (2 Detik)</th><th>Apakah Roda Tergelincir (Selip)?</th><th>Cocok untuk Lorong Sempit?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Pelan (40%)</td><td>......... cm</td><td>Tidak Selip / Selip</td><td>Cocok / Kurang Cocok</td></tr>
                        <tr><td>Sedang (65%)</td><td>......... cm</td><td>Tidak Selip / Selip</td><td>Cocok / Kurang Cocok</td></tr>
                        <tr><td>Cepat (100%)</td><td>......... cm</td><td>Tidak Selip / Selip</td><td>Cocok / Kurang Cocok</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika pada kecepatan Pelan (40%) robot hanya berdengung tetapi tidak bergerak, naikkan sedikit ke 45% atau 50% karena gesekan lantai membutuhkan tenaga awal minimal."
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
            "theory": """
                <p>Otak ESP32 pada MazeBot memiliki pemancar <strong>Wi-Fi bawaan</strong>! Artinya, robot ini bisa memancarkan sinyal Wi-Fi sendiri tanpa butuh internet sekolah (disebut mode <em>Access Point</em>). Setiap robot memiliki nama Wi-Fi (<strong>SSID</strong>) yang unik, misalnya <code>MazeBot-SD-01</code>, supaya sinyal antarkelompok tidak saling tertukar!</p>
                <p>Saat kita menekan tombol panah <strong>Maju (▲)</strong> di layar tablet, tablet mengirimkan pesan kilat melalui udara ke otak robot, lalu robot langsung memutar rodanya.</p>
            """,
            "safety": "Hanya hubungkan tablet ke SSID nomor robot kelompokmu sendiri! Mengendalikan robot kelompok lain tanpa izin dapat mengejutkan teman yang sedang memegang robot.",
            "steps": [
                "Nyalakan saklar MazeBot, lalu baca stiker identitas di punggung robot (contoh: <code>SSID: MazeBot-SD-01</code> | <code>Pass: 12345678</code>).",
                "Buka pengaturan Wi-Fi di tablet/komputer, pilih nama Wi-Fi robot kelompokmu, dan masukkan kata sandinya.",
                "Buka aplikasi Browser (Chrome) dan ketikkan alamat <strong><code>http://192.168.4.1</code></strong> di kolom alamat atas.",
                "Gunakan tombol <strong>D-Pad Virtual (▲ Maju, ▼ Mundur, ◄ Kiri, ► Kanan, ■ Stop)</strong> untuk mengemudikan robot!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Logika Di Balik Layar Tombol D-Pad Web Dashboard (M-07)</div>
                    <div><span class="block b-event">📱 Saat Tombol D-Pad Web Ditekan</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">❓ Jika Tombol == <span class="param">▲ ATAS</span></span> &rarr; <span class="block b-motion">⬆️ Gerak MAJU</span></div>
                        <div><span class="block b-control">❓ Jika Tombol == <span class="param">▼ BAWAH</span></span> &rarr; <span class="block b-motion">⬇️ Gerak MUNDUR</span></div>
                        <div><span class="block b-control">❓ Jika Tombol == <span class="param">◄ KIRI</span></span> &rarr; <span class="block b-motion">↩️ Belok KIRI</span></div>
                        <div><span class="block b-control">❓ Jika Tombol == <span class="param">► KANAN</span></span> &rarr; <span class="block b-motion">↪️ Belok KANAN</span></div>
                    </div>
                    <div><span class="block b-event">🖐️ Saat Jari Dilepas dari Tombol D-Pad</span></div>
                    <div class="block-indent">
                        <div><span class="block b-motion">🛑 Berhenti Seketika (Rem Aktif)</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Lembar Uji Kendali Nirkabel:</strong> Uji fungsi setiap tombol pada Web Dashboard!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Item Pengujian</th><th>Status (Berhasil / Gagal)</th><th>Catatan Respon Robot</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Koneksi ke Wi-Fi SSID Stiker Robot</td><td>Berhasil / Gagal</td><td>Nama SSID: ........................</td></tr>
                        <tr><td>2</td><td>Membuka halaman <code>192.168.4.1</code></td><td>Berhasil / Gagal</td><td>Tampilan D-Pad muncul jelas</td></tr>
                        <tr><td>3</td><td>Tombol ▲, ▼, ◄, ► merespon cepat</td><td>Berhasil / Gagal</td><td>Jeda respon: Cepat / Lambat</td></tr>
                        <tr><td>4</td><td>Parkir mundur ke dalam kotak garasi</td><td>Berhasil / Gagal</td><td>Waktu parkir: ........ detik</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika muncul pesan 'Tidak ada koneksi internet (No Internet)' di tablet saat tersambung ke Wi-Fi robot, pilih 'Tetap Hubungkan (Keep Wi-Fi Connection)' karena Wi-Fi lokal robot memang tidak terhubung ke internet luar."
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
            "theory": """
                <p>Selamat datang di <strong>Ujian Tengah Semester (Proyek Mini 1)</strong>! Hari ini kita akan menguji semua kemampuan yang telah dipelajari dari M-01 hingga M-07. Setiap tim akan mengendalikan MazeBot melintasi <strong>Lorong Rintangan Zig-Zag</strong> sepanjang 2,5 meter dengan 3 tikungan sempit menggunakan D-Pad Web Dashboard.</p>
                <p>Strategi kunci: Gunakan kecepatan <em>Sedang</em> di jalur lurus, dan turunkan ke kecepatan <em>Pelan</em> saat melewati tikungan sempit agar bodi robot tidak menyenggol dinding kardus!</p>
            """,
            "safety": "Siswa dilarang mendorong robot dengan tangan saat ujian berlangsung. Jika robot tersangkut di dinding labirin, gunakan tombol Mundur (▼) pada D-Pad untuk membebaskan robot.",
            "steps": [
                "Guru menyiapkan arena Lorong Rintangan dengan lebar lorong 25 cm dan 3 tikungan siku.",
                "Setiap kelompok mendapatkan 2 kali kesempatan tempuh (Run 1 dan Run 2). Waktu terbaik yang akan diambil.",
                "Saat peluit Start dibunyikan, pengemudi mengarahkan robot dari kotak Start menuju kotak Finish.",
                "Setiap kali bodi robot menyentuh dinding rintangan, dikenakan penalti tambahan waktu +3 detik."
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Aturan Strategi Proyek Mini 1 (Checklist Pengemudi)</div>
                    <div><span class="block b-event">🏁 Persiapan di Garis START</span></div>
                    <div class="block-indent">
                        <div><span class="block b-led">📶 Pastikan Wi-Fi Terhubung ke <span class="param">SSID Robot Sendiri</span></span></div>
                        <div><span class="block b-motion">⚙️ Set Slider Kecepatan Awal ke <span class="param">60% (Stabil)</span></span></div>
                        <div><span class="block b-control">🏆 Navigasi Lorong: Lurus &rarr; Tikungan Kanan &rarr; Tikungan Kiri &rarr; Garis Batas</span></div>
                        <div><span class="block b-motion">🛑 Hentikan Robot Tepat di Dalam Kotak FINISH</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Kartu Skor Ujian Tengah Semester (Proyek Mini 1):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Putaran</th><th>Waktu Tempuh Asli (Detik)</th><th>Jumlah Sentuhan Dinding (x 3 dtk)</th><th>Total Skor Waktu Akhir</th><th>Predikat</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Run 1 (Percobaan 1)</td><td>......... detik</td><td>..... kali (+..... dtk)</td><td>......... detik</td><td>A / B / C</td></tr>
                        <tr><td>Run 2 (Percobaan 2)</td><td>......... detik</td><td>..... kali (+..... dtk)</td><td>......... detik</td><td>A / B / C</td></tr>
                    </tbody>
                </table>
                <p><em>Kriteria Predikat: A (Sangat Baik: Total waktu &lt; 25 detik), B (Baik: 25–45 detik), C (Perlu Latihan: &gt; 45 detik).</em></p>
            """,
            "troubleshooting": "Jika tampilan web D-Pad membeku di tengah jalan, tekan tombol Refresh pada browser tablet dan robot akan otomatis berhenti aman berkat fitur pengaman sinyal."
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
            "theory": """
                <p>Tahukah kamu bagaimana kelelawar bisa terbang di gua yang gelap gulita tanpa menabrak dinding? Kelelawar memancarkan <strong>gelombang bunyi ultrasonik</strong> dari mulutnya. Ketika suara itu menabrak dinding gua, suaranya memantul kembali ke telinga kelelawar!</p>
                <p>Mata MazeBot (Sensor Ultrasonik HC-SR04) bekerja dengan cara yang persis sama:</p>
                <ul>
                    <li><strong>Silinder T (Transmitter / Mulut):</strong> Memancarkan gelombang suara ultrasonik.</li>
                    <li><strong>Silinder R (Receiver / Telinga):</strong> Menangkap pantulan gelombang suara dari benda di depannya.</li>
                </ul>
                <p>Di Web Dashboard, jarak ditampilkan dengan kode warna: <strong>HIJAU (&gt; 20 cm = Aman)</strong>, <strong>KUNING (10–20 cm = Waspada)</strong>, dan <strong>MERAH (&lt; 10 cm = Terlalu Dekat!)</strong>.</p>
            """,
            "safety": "Jangan menekan jaring kawat halus di bagian dalam silinder mata sensor ultrasonik dengan pensil atau jari karena selaput suaranya bisa rusak.",
            "steps": [
                "Letakkan MazeBot di atas meja menghadap ke arah ruang kosong, lalu buka tab <strong>[Monitor Sensor]</strong> di Web Dashboard.",
                "Ambil sebuah kotak kardus atau buku tebal dan berdirikan di depan mata robot pada jarak 30 cm (ukur dengan penggaris).",
                "Majukan buku perlahan-lahan ke jarak 25 cm, 15 cm, hingga 5 cm di depan mata robot.",
                "Amati perubahan angka sentimeter dan perubahan warna bar indikator di layar tablet!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-09: Indikator Warna Radar Jarak</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-sensor">📡 Tampilkan <span class="param">Jarak Sensor Depan (cm)</span> ke Layar Web</span></div>
                            <div><span class="block b-control">❓ Jika <span class="param">Jarak Depan &lt; 10 cm</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-led">🔴 Ubah Status Radar Web ke <span class="param">MERAH (BAHAYA)</span></span></div>
                            </div>
                            <div><span class="block b-control">❓ Jika Tidak (Jarak Aman) Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-led">🟢 Ubah Status Radar Web ke <span class="param">HIJAU (AMAN)</span></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Eksperimen Uji Akurasi Mata Robot:</strong> Bandingkan ukuran penggaris asli dengan bacaan sensor di layar!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Jarak Buku di Penggaris</th><th>Angka Jarak di Layar Web (cm)</th><th>Warna Bar di Layar Web (Hijau / Kuning / Merah)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>30 cm</td><td>............ cm</td><td>...........................................</td></tr>
                        <tr><td>15 cm</td><td>............ cm</td><td>...........................................</td></tr>
                        <tr><td>7 cm</td><td>............ cm</td><td>...........................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Pastikan buku atau kardus diletakkan tegak lurus di depan sensor. Jika buku dimiringkan terlalu tajam, pantulan suara akan memantul ke arah lain sehingga jarak terbaca jauh."
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
            "theory": """
                <p>Mobil pintar zaman sekarang memiliki fitur <strong>Rem Darurat Otomatis</strong>: jika ada pejalan kaki atau penghalang tiba-tiba di depan mobil, mobil akan mengerem sendiri meskipun sopir belum menginjak rem!</p>
                <p>Kita dapat memberikan kepintaran itu kepada MazeBot menggunakan balok logika <strong>JIKA ... MAKA ... JIKA TIDAK ...</strong>:</p>
                <ul>
                    <li><strong>JIKA</strong> Jarak Depan kurang dari 10 cm &rarr; <strong>MAKA</strong> Berhenti Seketika!</li>
                    <li><strong>JIKA TIDAK</strong> (artinya jalan di depan masih jauh/kosong) &rarr; <strong>MAKA</strong> Terus Maju!</li>
                </ul>
            """,
            "safety": "Gunakan kotak kardus ringan atau botol plastik kosong sebagai rintangan uji coba (jangan gunakan dinding semen keras saat percobaan pertama, untuk berjaga-jaga jika logika balok siswa masih terbalik).",
            "steps": [
                "Buka Kanvas Kode Visual dan pasang balok <strong>[Ulangi Selamanya]</strong> di bawah <strong>[Saat Program Dimulai]</strong>.",
                "Masukkan balok logika <strong>[Jika ... Maka ... Jika Tidak ...]</strong> ke dalam perulangan.",
                "Pada syarat <em>Jika</em>, pasang balok sensor <strong>[Jarak Sensor Depan &lt; 10 cm]</strong>.",
                "Pada bagian <em>Maka</em>, pasang balok <strong>[Berhenti Total]</strong> dan <strong>[Lampu Indikator NYALA]</strong>. Pada bagian <em>Jika Tidak</em>, pasang <strong>[Gerak Maju (Kecepatan 50%)]</strong>.",
                "Taruh kardus di tengah jalur, jalankan robot, dan lihat apakah robot mengerem tepat sebelum menabrak kardus!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-10: Rem Otomatis Anti-Tabrak</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-control">❓ Jika <span class="param">📡 Jarak Sensor Depan &lt; 10 cm</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Berhenti Seketika</span></div>
                                <div><span class="block b-led">💡 Lampu Indikator <span class="param">NYALA (Peringatan)</span></span></div>
                            </div>
                            <div><span class="block b-control">🔄 Jika Tidak Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> Kecepatan <span class="param">50%</span></span></div>
                                <div><span class="block b-led">💡 Lampu Indikator <span class="param">MATI</span></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Eksperimen Uji Rem Darurat:</strong> Apa yang terjadi jika kardus diangkat kembali setelah robot berhenti?</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Skenario Pengujian</th><th>Respon Robot yang Diamati</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Kardus ditaruh 50 cm di depan robot yang sedang melaju</td><td>Robot berhenti pada jarak ...... cm dari kardus</td></tr>
                        <tr><td>2</td><td>Kardus diangkat/disingkirkan saat robot sedang berhenti</td><td>Robot akan: ..........................................</td></tr>
                        <tr><td>3</td><td>Telapak tangan didekatkan ke depan mata robot</td><td>Robot akan: ..........................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jangan gunakan balok [Gerak Maju selama 2 detik] di dalam [Jika Tidak]! Gunakan balok [Gerak Maju (tanpa detik)] agar robot terus memeriksa sensor mata setiap saat tanpa menunda pemeriksaan selama 2 detik."
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
            "theory": """
                <p>Pada modul sebelumnya, robot sudah pintar berhenti saat melihat dinding. Namun, jika hanya berhenti, robot tidak akan pernah keluar dari labirin! Supaya robot bisa melanjutkan petualangannya sendiri, kita harus mengajarinya <strong>Manuver Menghindar Cerdas</strong>:</p>
                <ol>
                    <li>Saat mendeteksi dinding di depan (&lt; 12 cm), <strong>Berhenti sebentar</strong> (0.3 detik).</li>
                    <li><strong>Mundur sedikit</strong> (0.5 detik) agar hidung robot punya ruang bebas untuk berputar tanpa menyerempet dinding.</li>
                    <li><strong>Belok Kanan 90 derajat</strong> untuk mencari jalan baru yang kosong.</li>
                </ol>
            """,
            "safety": "Pastikan area jelajah robot dibatasi dengan kotak kardus atau dinding lorong agar robot tidak berjalan keluar pintu kelas.",
            "steps": [
                "Modifikasi program M-10 pada bagian di dalam blok <strong>[Jika Jarak Depan &lt; 12 cm Maka]</strong>.",
                "Di bawah balok <strong>[Berhenti 0.3 detik]</strong>, tambahkan balok <strong>[Gerak MUNDUR selama 0.5 detik]</strong>.",
                "Tambahkan balok <strong>[Belok KANAN selama 0.55 detik]</strong> lalu <strong>[Berhenti 0.3 detik]</strong>.",
                "Unggah program ke robot, letakkan robot menghadap sudut dinding lorong, dan tonton robot berbelok sendiri mencari jalan keluar!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-11: Robot Penjelajah Penghindar Dinding</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-control">❓ Jika <span class="param">📡 Jarak Sensor Depan &lt; 12 cm</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Berhenti selama <span class="param">0.3</span> detik</span></div>
                                <div><span class="block b-motion">⬇️ Gerak <span class="param">MUNDUR</span> selama <span class="param">0.5</span> detik</span></div>
                                <div><span class="block b-motion">↪️ Belok <span class="param">KANAN</span> selama <span class="param">0.55</span> detik</span></div>
                                <div><span class="block b-motion">🛑 Berhenti selama <span class="param">0.3</span> detik</span></div>
                            </div>
                            <div><span class="block b-control">🔄 Jika Tidak Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> Kecepatan <span class="param">50%</span></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Analisis Gerak Menghindar:</strong> Jawablah pertanyaan berdasarkan hasil uji coba kelompokmu!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Pertanyaan Analisis</th><th>Jawaban Kelompok</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Mengapa robot harus mundur dulu 0.5 detik sebelum berbelok kanan?</td><td>............................................................</td></tr>
                        <tr><td>2</td><td>Apa yang terjadi jika kita menghapus balok mundur?</td><td>............................................................</td></tr>
                        <tr><td>3</td><td>Berapa kali robot berhasil menghindari dinding kardus dalam 1 menit?</td><td>......... kali berhasil menghindar</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika saat berbelok hidung robot masih menyenggol dinding depan, naikkan jarak deteksi dari 12 cm menjadi 15 cm atau tambah durasi mundur menjadi 0.6 detik."
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
            "theory": """
                <p>Selain punya 3 mata ultrasonik untuk melihat dinding, MazeBot punya satu mata rahasia di bagian bawah perutnya yang menghadap ke lantai, bernama <strong>Sensor Inframerah TCRT5000</strong>. Sensor ini memiliki 2 lampu kecil:</p>
                <ul>
                    <li><strong>Lampu Bening (Pemancar):</strong> Menembakkan sinar inframerah ke lantai.</li>
                    <li><strong>Lampu Hitam (Penerima):</strong> Menangkap pantulan sinar dari lantai.</li>
                </ul>
                <p>Sifat cahaya: <strong>Permukaan Putih/Terang</strong> akan <em>memantulkan</em> sinar kembali ke sensor. Sebaliknya, <strong>Garis Lakban Hitam</strong> akan <em>menyerap</em> sinar sehingga tidak ada pantulan yang kembali. Dari situlah robot tahu bahwa ia sedang menginjak garis hitam!</p>
            """,
            "safety": "Saat mengamati kolong robot, pastikan roda tidak sedang berputar agar jari atau rambut tidak terlilit ban karet.",
            "steps": [
                "Tempelkan sepotong lakban hitam selebar 3–5 cm di atas lantai keramik putih.",
                "Nyalakan MazeBot dan buka indikator <strong>[Status Sensor Lantai]</strong> pada layar Web Dashboard.",
                "Pegang bodi robot dan letakkan bagian depan robot di atas keramik putih. Perhatikan lampu LED kecil pada modul sensor bawah dan status di layar.",
                "Geser robot hingga mata sensor bawah berada tepat di atas lakban hitam. Amati perubahan statusnya!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-12: Alarm Detektif Garis Hitam</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-control">❓ Jika <span class="param">🔍 Sensor Bawah Mendeteksi WARNA HITAM</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-led">💡 Lampu Indikator <span class="param">NYALA</span></span></div>
                                <div><span class="block b-led">📢 Tampilkan Pesan Web: <span class="param">"GARIS HITAM DITEMUKAN!"</span></span></div>
                            </div>
                            <div><span class="block b-control">🔄 Jika Tidak (Lantai Putih) Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-led">💡 Lampu Indikator <span class="param">MATI</span></span></div>
                                <div><span class="block b-led">📢 Tampilkan Pesan Web: <span class="param">"LANTAI PUTIH BERSIH"</span></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Tabel Detektif Warna Permukaan:</strong> Uji sensor bawah robotmu di atas berbagai benda berikut!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Permukaan yang Diuji</th><th>Apakah Cahaya Dipantulkan / Diserap?</th><th>Hasil Deteksi Robot (Putih / Hitam)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Lantai Keramik Putih</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr>
                        <tr><td>2</td><td>Lakban / Selotip Hitam</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr>
                        <tr><td>3</td><td>Kertas HVS Putih</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr>
                        <tr><td>4</td><td>Sampul Buku Warna Hitam Doff</td><td>Dipantulkan / Diserap</td><td>.......................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika sensor tidak membedakan hitam dan putih, minta bantuan Guru untuk memutar sedikit baut potensiometer biru pada modul TCRT5000 menggunakan obeng kecil hingga lampu indikatornya sensitif tepat di atas lakban hitam."
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
            "theory": """
                <p>Dalam perlombaan robot labirin, bagaimana robot tahu bahwa ia sudah berhasil keluar dari labirin dan mencapai <strong>Garis Finish</strong>? Di ujung labirin, kita menempelkan pita lakban hitam tebal sebagai penanda Finish.</p>
                <p>Saat sensor bawah mendeteksi warna <strong>HITAM</strong>, robot tidak boleh hanya berhenti sesaat lalu jalan lagi. Robot harus menjalankan perintah <strong>[Berhenti &amp; Kunci Program Selesai]</strong> supaya rodanya terkunci permanen sampai kita mengambilnya!</p>
            """,
            "safety": "Gunakan lakban hitam yang cukup lebar (minimal 4–5 cm, atau 2 lapis lakban berjejer) agar sensor bawah punya waktu yang cukup untuk mendeteksinya saat robot sedang melaju.",
            "steps": [
                "Tempelkan lakban hitam tebal di lantai sebagai Garis Finish pada jarak 1 meter dari titik Start.",
                "Susun balok program: di dalam <strong>[Ulangi Selamanya]</strong>, periksa <strong>[Jika Sensor Bawah == HITAM]</strong>.",
                "Jika terdeteksi HITAM: pasang <strong>[Berhenti Total]</strong>, <strong>[Kedipkan Lampu 3 Kali]</strong>, dan <strong>[Hentikan Semua Program (Stop All)]</strong>.",
                "Jika TIDAK (masih lantai putih): pasang <strong>[Gerak MAJU Kecepatan 50%]</strong>. Uji di lintasan!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-13: Berhenti Otomatis di Garis Finish</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-control">❓ Jika <span class="param">🔍 Sensor Bawah == WARNA HITAM</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Berhenti Seketika (Kunci Roda)</span></div>
                                <div><span class="block b-led">🎉 Tampilkan Status: <span class="param">"MISI FINISH BERHASIL!"</span></span></div>
                                <div><span class="block b-control">⏹️ Hentikan Seluruh Program (Selesai)</span></div>
                            </div>
                            <div><span class="block b-control">🔄 Jika Tidak Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> Kecepatan <span class="param">50%</span></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Uji Ketepatan Berhenti di Garis Finish:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Percobaan</th><th>Kecepatan Maju</th><th>Lebar Lakban Hitam</th><th>Apakah Robot Berhenti Tepat di Atas Garis Hitam?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Pelan (45%)</td><td>5 cm</td><td>Berhenti Tepat / Kelewatan</td></tr>
                        <tr><td>2</td><td>Sedang (60%)</td><td>5 cm</td><td>Berhenti Tepat / Kelewatan</td></tr>
                        <tr><td>3</td><td>Cepat (90%)</td><td>2 cm (Tipis)</td><td>Berhenti Tepat / Kelewatan</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika pada kecepatan tinggi robot melindas garis hitam tipis tanpa berhenti, lebarkan garis lakban hitam menjadi 5 cm dan gunakan kecepatan Sedang (50%)."
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
            "theory": """
                <p>Sekarang tiba saatnya menggabungkan <strong>Mata Bawah (TCRT5000)</strong> dan <strong>Mata Depan (Ultrasonik)</strong> ke dalam satu otak program yang utuh! Bagaimana urutannya?</p>
                <ol>
                    <li><strong>Pertanyaan Pertama:</strong> <em>"Apakah aku sudah menginjak Garis Finish Hitam?"</em> &rarr; Jika YA, langsung Berhenti Pemenang!</li>
                    <li><strong>Pertanyaan Kedua:</strong> <em>"Jika belum Finish, apakah di depanku ada dinding (&lt; 12 cm)?"</em> &rarr; Jika YA, mundur sedikit lalu Belok Kanan!</li>
                    <li><strong>Jika Keduanya Tidak:</strong> Artinya jalan masih aman dan belum sampai finish &rarr; <strong>Maju Lurus!</strong></li>
                </ol>
            """,
            "safety": "Pastikan dinding kardus lorong labirin berdiri kokoh (rekatkan dengan lakban kertas ke lantai) agar tidak bergeser saat didekati robot.",
            "steps": [
                "Susun arena Labirin Huruf 'L' menggunakan dinding kardus: Jalur lurus 80 cm &rarr; Belokan Kanan 90° &rarr; Jalur lurus 80 cm &rarr; Kotak Lakban Hitam Finish.",
                "Susun balok logika bertingkat (<em>Jika ... Maka ... Jika Tidak Jika ... Maka ... Jika Tidak ...</em>) sesuai contoh kode di bawah.",
                "Letakkan MazeBot di mulut Start, nyalakan program, dan amati robot menyelesaikan lintasan tanpa disentuh tangan!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-14: Integrasi Penuh Navigasi &amp; Finish</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-control">⏱️ Tunggu <span class="param">2</span> detik</span></div>
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-control">❓ Jika <span class="param">🔍 Sensor Bawah == WARNA HITAM</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Berhenti Total</span></div>
                                <div><span class="block b-led">🎉 Tampilkan Status: <span class="param">"FINISH TERCAPAI!"</span></span></div>
                                <div><span class="block b-control">⏹️ Hentikan Seluruh Program</span></div>
                            </div>
                            <div><span class="block b-control">❓ Jika Tidak, Jika <span class="param">📡 Jarak Sensor Depan &lt; 12 cm</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Berhenti selama <span class="param">0.3</span> detik</span></div>
                                <div><span class="block b-motion">⬇️ Gerak <span class="param">MUNDUR</span> selama <span class="param">0.4</span> detik</span></div>
                                <div><span class="block b-motion">↪️ Belok <span class="param">KANAN</span> selama <span class="param">0.55</span> detik</span></div>
                            </div>
                            <div><span class="block b-control">🔄 Jika Tidak Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">⬆️ Gerak <span class="param">MAJU</span> Kecepatan <span class="param">50%</span></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Checklist Uji Integrasi Labirin 1 Belokan:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Tahapan Misi</th><th>Target Perilaku Robot</th><th>Berhasil / Belum</th><th>Catatan Perbaikan</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Tahap 1: Lorong Awal</td><td>Melaju lurus dari titik Start</td><td>Berhasil / Belum</td><td>.................................</td></tr>
                        <tr><td>Tahap 2: Sudut Belokan</td><td>Mendeteksi dinding &amp; belok kanan 90°</td><td>Berhasil / Belum</td><td>.................................</td></tr>
                        <tr><td>Tahap 3: Lorong Akhir</td><td>Melaju menuju garis finish</td><td>Berhasil / Belum</td><td>.................................</td></tr>
                        <tr><td>Tahap 4: Kotak Finish</td><td>Berhenti tepat di atas lakban hitam</td><td>Berhasil / Belum</td><td>.................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika robot belok terlalu patah atau kurang patah di sudut L, catat berapa detik durasi belok yang perlu diperbaiki pada sesi Tuning minggu depan (M-15)."
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
            "theory": """
                <p>Setiap robot memiliki keunikan mekanik masing-masing! Kadang-kadang, motor roda kiri berputar sedikit lebih cepat daripada motor roda kanan, sehingga saat diperintah <strong>Maju Lurus</strong>, robot agak miring/melenceng ke kanan. Proses menyetel angka-angka pada kode program agar robot bergerak sempurna disebut <strong>Tuning (Penyelarasan)</strong>.</p>
                <p>Tiga hal yang kita setel hari ini:</p>
                <ol>
                    <li><strong>Keseimbangan Roda (Trim/Offset):</strong> Menyeimbangkan tenaga roda kiri dan kanan agar jalannya lurus seperti penggaris.</li>
                    <li><strong>Durasi Belok 90°:</strong> Menyesuaikan angka detik belok (misal dari 0.55 detik menjadi 0.50 atau 0.62 detik) sesuai kondisi baterai.</li>
                    <li><strong>Jarak Pengereman Dinding:</strong> Menyesuaikan jarak sensor depan (10–15 cm) agar pas di tengah lorong.</li>
                </ol>
            """,
            "safety": "Jika baterai mulai melemah (putaran roda terasa sangat lambat), laporkan pada Guru agar diganti dengan baterai 18650 yang sudah terisi penuh.",
            "steps": [
                "Uji jalan lurus 1 meter: Jika robot melenceng ke kanan, kurangi sedikit tenaga roda kiri atau tambahkan koreksi pada balok <strong>[Atur Keseimbangan Roda]</strong>.",
                "Uji belok 90 derajat di sudut keramik: Sesuaikan angka desimal detik pada balok <strong>[Belok Kanan]</strong> sampai robot benar-benar lurus sejajar garis keramik.",
                "Jalankan kembali robot di lintasan Labirin 'L' sebanyak 3 kali berturut-turut untuk memastikan hasilnya konsisten!",
                "Catat 'Angka Emas' (nilai setelan terbaik) kelompokmu di buku catatan agar siap dipakai saat Tantangan Akhir minggu depan."
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Program Balok Visual M-15: Penyetelan Keseimbangan &amp; Parameter Emas</div>
                    <div><span class="block b-event">▶️ Saat Program Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-motion">⚖️ Setel Keseimbangan Roda: Kiri <span class="param">50%</span> | Kanan <span class="param">53%</span> (Koreksi Lurus)</span></div>
                        <div><span class="block b-var">📌 Simpan Nilai Jarak Batas Dinding = <span class="param">13 cm</span></span></div>
                        <div><span class="block b-var">📌 Simpan Durasi Belok 90° = <span class="param">0.54 detik</span></span></div>
                        <div><span class="block b-control">🔁 Jalankan Siklus Navigasi Labirin (M-14)</span></div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Kartu Resep 'Angka Emas' Tuning Robot Kelompok:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Parameter yang Disetel</th><th>Nilai Sebelum Tuning</th><th>Masalah yang Terjadi</th><th>Nilai Terbaik ('Angka Emas')</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Tenaga Roda Kiri &amp; Kanan</td><td>Kiri: 50% | Kanan: 50%</td><td>Melenceng ke: ...........</td><td>Kiri: ....% | Kanan: ....%</td></tr>
                        <tr><td>Durasi Belok Kanan 90°</td><td>0.55 detik</td><td>Kurang / Kelebihan belok</td><td>............ detik</td></tr>
                        <tr><td>Jarak Deteksi Dinding Depan</td><td>12 cm</td><td>Terlalu dekat / jauh</td><td>............ cm</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Ingat bahwa saat baterai baru diisi penuh oleh Guru, putaran roda sedikit lebih kencang dibanding saat baterai hampir habis. Cek ulang durasi belok sebelum lomba dimulai!"
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
            "theory": """
                <p>Selamat sampai di puncak petualangan: <strong>MazeBot Rescue Mission (Misi Penyelamatan Akhir Semester)</strong>! Dalam misi ini, robot cilikmu ditugaskan masuk ke dalam lorong penyelamatan secara mandiri (tanpa remote D-Pad!), melewati penghalang dinding, berbelok di tikungan, dan berhenti tepat di atas <strong>Zona Penyelamatan (Kotak Hitam Finish)</strong>.</p>
                <p>Penilaian dilakukan secara objektif berdasarkan keberhasilan tahapan misi dan kerapian susunan balok kode yang kalian buat.</p>
            """,
            "safety": "Seluruh anggota tim wajib berdiri di luar garis batas arena labirin saat robot sedang menjalankan misi otonom agar sensor ultrasonik tidak salah mendeteksi kaki siswa sebagai dinding.",
            "steps": [
                "Masukkan nilai 'Angka Emas' hasil tuning M-15 ke dalam program lengkap navigasi otonom kelompokmu.",
                "Unggah program ke MazeBot dan letakkan robot di kotak START dalam keadaan siap.",
                "Saat juri/guru memberikan aba-aba 'MULAI!', tekan tombol Run / nyalakan robot dan biarkan robot bekerja sendiri menyelesaikan labirin.",
                "Setelah robot berhenti di kotak Finish hitam, presentasikan secara singkat di depan kelas bagaimana cara kerja balok kode kelompokmu!"
            ],
            "code_block": """
                <div class="blockly-container">
                    <div class="blockly-title">Kode Master M-16: MazeBot Rescue Mission (Full Autonomous SD)</div>
                    <div><span class="block b-event">▶️ Saat Misi Penyelamatan Dimulai</span></div>
                    <div class="block-indent">
                        <div><span class="block b-led">💡 Nyalakan Lampu Indikator &amp; Tunggu <span class="param">2</span> detik</span></div>
                        <div><span class="block b-motion">⚖️ Atur Kecepatan Kiri <span class="param">50%</span> &amp; Kanan <span class="param">52%</span></span></div>
                        <div><span class="block b-control">🔁 Ulangi Selamanya</span></div>
                        <div class="block-indent">
                            <div><span class="block b-control">❓ Jika <span class="param">🔍 Sensor Bawah == WARNA HITAM</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Kunci Rem Berhenti Total</span></div>
                                <div><span class="block b-led">🏆 Kirim Status Web: <span class="param">"MISI PENYELAMATAN SUKSES!"</span></span></div>
                                <div><span class="block b-control">⏹️ Selesai (Stop Program)</span></div>
                            </div>
                            <div><span class="block b-control">❓ Jika Tidak, Jika <span class="param">📡 Jarak Sensor Depan &lt; 13 cm</span> Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">🛑 Berhenti <span class="param">0.3</span> dtk &rarr; ⬇️ Mundur <span class="param">0.4</span> dtk &rarr; ↪️ Belok Kanan <span class="param">0.54</span> dtk</span></div>
                            </div>
                            <div><span class="block b-control">🔄 Jika Tidak Maka</span></div>
                            <div class="block-indent">
                                <div><span class="block b-motion">⬆️ Maju Lurus Menjelajah</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            """,
            "lks": """
                <p><strong>Rubrik Penilaian Akhir Semester (MazeBot Rescue Mission - Tingkat SD):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Komponen Penilaian</th><th>Bobot</th><th>Indikator Keberhasilan</th><th>Skor Kelompok (0–100)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>1. Kepatuhan SOP &amp; Keselamatan</strong></td><td>15%</td><td>Disiplin aturan baterai 18650 &amp; kerapian kerja tim</td><td>.............</td></tr>
                        <tr><td><strong>2. Kerapian Balok Kode Visual</strong></td><td>25%</td><td>Susunan balok logis, lengkap (Start, Loop, If-Else)</td><td>.............</td></tr>
                        <tr><td><strong>3. Keberhasilan Lewati Dinding</strong></td><td>30%</td><td>Mendeteksi rintangan &amp; berbelok 90° tanpa macet</td><td>.............</td></tr>
                        <tr><td><strong>4. Ketepatan Berhenti di Finish</strong></td><td>30%</td><td>Otomatis mengunci roda tepat di atas kotak hitam</td><td>.............</td></tr>
                        <tr><td colspan="3"><strong>TOTAL NILAI AKHIR SEMESTER</strong></td><td><strong>............. / 100</strong></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Apresiasi setiap keberhasilan tahapan siswa! Jika robot berhasil melewati belokan namun meleset sedikit di garis finish, berikan kesempatan percobaan kedua (Run 2) setelah siswa memperbaiki sudut beloknya."
        }
    ]

def generate_sd_html():
    modules = get_sd_modules()
    toc_rows = ""
    for m in modules:
        toc_rows += f"""
        <tr>
            <td class="toc-code">{m['code']}</td>
            <td><strong>{m['title']}</strong></td>
            <td>{m['duration']}</td>
            <td>Visual Block / Web D-Pad</td>
        </tr>
        """

    modules_html = ""
    for m in modules:
        objectives_li = "".join([f"<li>{obj}</li>" for obj in m["objectives"]])
        steps_li = "".join([f'<li><span class="step-num">{i+1}</span>{s}</li>' for i, s in enumerate(m["steps"])])

        modules_html += f"""
        <div class="module-page" id="{m['code']}">
            <div class="module-banner">
                <div class="module-banner-left">
                    <span class="mod-code">MODUL {m['code']} &bull; KURIKULUM SD (KELAS 4–6)</span>
                    <h2>{m['title']}</h2>
                </div>
                <div class="module-banner-right">
                    <div><strong>Alokasi:</strong> {m['duration']}</div>
                    <div><strong>Fase:</strong> {m['phase']}</div>
                    <div><strong>Mode:</strong> Blockly &amp; Web</div>
                </div>
            </div>

            <div class="card">
                <h3>🎯 Target Kemampuan &amp; Capaian Pembelajaran</h3>
                <ul>{objectives_li}</ul>
            </div>

            <div class="alert alert-danger">
                <span class="alert-title">🛡️ SOP Keselamatan Kerja &amp; Baterai 18650 (Wajib Dipatuhi)</span>
                {m['safety']}
            </div>

            <h3 class="sub-heading">📖 A. Konsep Kunci &amp; Materi Pembelajaran</h3>
            {m['theory']}

            <h3 class="sub-heading">🛠️ B. Langkah Kerja Praktikum</h3>
            <ul class="steps-list">
                {steps_li}
            </ul>

            <h3 class="sub-heading">💻 C. Susunan Balok Kode Visual &amp; Logika Program</h3>
            {m['code_block']}

            <div class="lks-box">
                <div class="lks-header">
                    <span>📝 D. Lembar Kerja Siswa (LKS) — {m['code']}</span>
                    <span>Nama Kelompok: ..............................</span>
                </div>
                {m['lks']}
            </div>

            <div class="alert alert-warning">
                <span class="alert-title">🔧 Panduan Guru: Troubleshooting &amp; Tips Kelas</span>
                {m['troubleshooting']}
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Modul Ajar MazeBot EduKit - Tingkat SD (Kelas 4-6)</title>
    <link rel="stylesheet" href="css/modul_style.css">
</head>
<body class="theme-sd">

    <!-- COVER PAGE -->
    <div class="cover-page">
        <div>
            <span class="cover-badge">Kurikulum Robotika &amp; Pemrograman STEM Nasional</span>
            <div class="cover-title">MODUL AJAR &amp; LKS<br>MAZEBOT EDUKIT</div>
            <div class="cover-subtitle">📘 TINGKAT SD (Target: Kelas 4–6)<br>"Petualangan Logika &amp; Pengendali Robot Cilik"</div>
            <div class="cover-divider"></div>

            <div class="cover-highlights">
                <h3>Spesifikasi Pedagogis &amp; Standar Keamanan SD</h3>
                <ul>
                    <li><strong>Platform Ramah Anak:</strong> Visual Block Programming (Blockly/Scratch) &amp; Web Dashboard D-Pad Interaktif.</li>
                    <li><strong>SOP Keselamatan Baterai 18650 (Guru Only):</strong> Baterai terkunci rapat di dalam holder tertutup baut; pemasangan dan pengisian daya 100% dilakukan oleh Guru/Instruktur.</li>
                    <li><strong>Pre-Configured Wi-Fi SoftAP:</strong> Setiap unit robot memiliki SSID &amp; Password unik tertera pada stiker bodi robot (langsung sambung tanpa koding jaringan).</li>
                    <li><strong>16 Modul Terstruktur (M-01 s/d M-16):</strong> Lengkap dari pengenalan bagian robot, algoritma unplugged, kendali D-Pad, sensor ultrasonik, sensor garis TCRT5000, hingga sesi Troubleshooting &amp; Rescue Mission.</li>
                </ul>
            </div>
        </div>

        <div class="cover-footer">
            <div>
                <strong>Edisi Revisi Total Kurikulum MazeBot EduKit</strong><br>
                Lengkap dengan Kode Balok Visual, LKS Siswa, &amp; Panduan Troubleshooting Guru
            </div>
            <div style="text-align: right;">
                <strong>Kode Dokumen:</strong> EDU-MB-SD-2026<br>
                <strong>Total Modul:</strong> 16 Pertemuan (M-01 – M-16)
            </div>
        </div>
    </div>

    <!-- FRONTMATTER: SOP & TOC -->
    <div class="page-break">
        <div class="section-header">
            <h1>Panduan Umum, SOP Keselamatan &amp; Daftar Isi</h1>
            <p>Buku Pegangan Terpadu Guru &amp; Siswa — Tingkat Sekolah Dasar (Kelas 4–6)</p>
        </div>

        <div class="alert alert-danger">
            <span class="alert-title">⚠️ PROSEDUR OPERASIONAL STANDAR (SOP) KESELAMATAN BATERAI 18650 (KHUSUS GURU)</span>
            <ol style="padding-left: 18px; margin-top: 4px;">
                <li><strong>Holder Tertutup Baut:</strong> Sel baterai Lithium-Ion 18650 pada unit MazeBot SD wajib dipasang di dalam <em>battery enclosure</em> tertutup yang dikunci menggunakan baut pengaman.</li>
                <li><strong>Otoritas Guru/Instruktur:</strong> Siswa SD <strong>DILARANG KERAS</strong> membuka penutup baterai, melepas sel 18650, atau menghubungkan baterai ke charger eksternal. Seluruh proses charging dan pergantian baterai dilakukan oleh Guru di luar jam pemakaian siswa.</li>
                <li><strong>Inspeksi Pra-Kelas:</strong> Sebelum membagikan robot ke meja kelompok, Guru memastikan saklar pada posisi OFF, kabel motor tidak terkelupas, dan stiker identitas Wi-Fi (SSID &amp; Password) terbaca jelas.</li>
            </ol>
        </div>

        <h3 class="sub-heading">📋 Daftar Isi Kurikulum Tingkat SD (M-01 s/d M-16)</h3>
        <table class="toc-table">
            <thead>
                <tr>
                    <th style="width: 10%;">Kode</th>
                    <th style="width: 48%;">Topik Materi Modul</th>
                    <th style="width: 20%;">Alokasi Waktu</th>
                    <th style="width: 22%;">Platform Utama</th>
                </tr>
            </thead>
            <tbody>
                {toc_rows}
            </tbody>
        </table>
    </div>

    <!-- ALL 16 MODULES -->
    {modules_html}

</body>
</html>
"""
    out_path = os.path.join(os.path.dirname(__file__), "Modul_Ajar_MazeBot_SD.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated SD HTML at: {out_path}")

if __name__ == "__main__":
    generate_sd_html()
