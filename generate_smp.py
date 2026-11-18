import os
import html as html_lib

def get_smp_modules():
    return [
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
            "theory": """
                <p>Pada tingkat SMP, kita mempelajari MazeBot sebagai sebuah sistem tertanam (<em>Embedded System</em>) yang terdiri dari tiga blok fungsi utama: <strong>Input (Sensor)</strong>, <strong>Proses (Mikrokontroler ESP32)</strong>, dan <strong>Output (Driver Motor DRV8833 &amp; Roda)</strong>. Kita tidak perlu merakit komponen mikro di dalam keping PCB, melainkan memahami bagaimana antarmodul saling berkomunikasi melalui pin GPIO (<em>General Purpose Input/Output</em>).</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Nama Modul</th><th>Kategori</th><th>Pin GPIO ESP32</th><th>Fungsi Teknis pada MazeBot</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>ESP32 DevKit V1</strong></td><td>Pemroses Utama</td><td>32-bit Dual Core</td><td>Mengeksekusi program C++, mengolah sinyal sensor, dan memancarkan Wi-Fi.</td></tr>
                        <tr><td><strong>Driver DRV8833</strong></td><td>Output Aktuator</td><td>IN1:25, IN2:26, IN3:27, IN4:14</td><td>Memperkuat arus listrik dari ESP32 untuk memutar 2 motor DC Gearbox TT.</td></tr>
                        <tr><td><strong>3x HC-SR04</strong></td><td>Input Jarak</td><td>Kiri(32,35), Depan(33,34), Kanan(18,19)</td><td>Mengukur jarak dinding labirin dalam satuan sentimeter menggunakan gelombang ultrasonik.</td></tr>
                        <tr><td><strong>TCRT5000</strong></td><td>Input Garis</td><td>DO: GPIO 4</td><td>Mendeteksi kontras warna hitam pada garis Finish di permukaan lantai.</td></tr>
                    </tbody>
                </table>
            """,
            "safety": "Pastikan polaritas baterai 18650 tidak terbalik dan jangan pernah menghubungkan pin VCC (5V/3.3V) langsung ke pin GND karena akan menyebabkan hubung singkat (short circuit).",
            "steps": [
                "Amati papan utama MazeBot dan identifikasi letak modul ESP32, modul merah/biru DRV8833, ketiga sensor ultrasonik, dan sensor TCRT5000 di bawah sasis.",
                "Hubungkan ESP32 ke komputer menggunakan kabel data Micro-USB / USB-C yang mendukung transfer data.",
                "Buka aplikasi Arduino IDE, pilih Board <strong>DOIT ESP32 DEVKIT V1</strong> dan Port COM yang sesuai.",
                "Unggah kode diagnostik M-01 di bawah ini untuk memastikan lampu indikator internal (GPIO 2) menyala dan pesan serial tampil di layar komputer."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-01: Diagnostik Sistem & Identifikasi Pinout MazeBot SMP
// =========================================================================
#define PIN_LED     2
#define PIN_FINISH  4

void setup() {
  Serial.begin(115200);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_FINISH, INPUT);

  Serial.println("==========================================");
  Serial.println("  SISTEM MAZEBOT EDUKIT SMP - AKTIF!      ");
  Serial.println("  Otak: ESP32 | Driver: DRV8833           ");
  Serial.println("==========================================");
}

void loop() {
  digitalWrite(PIN_LED, HIGH);
  Serial.println("[STATUS] Sistem Normal - Siap Menerima Instruksi...");
  delay(1000);
  
  digitalWrite(PIN_LED, LOW);
  delay(1000);
}""",
            "lks": """
                <p><strong>Lembar Identifikasi Modul Hardware MazeBot:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Komponen yang Diperiksa</th><th>Pin GPIO yang Terhubung</th><th>Mengapa ESP32 Butuh Modul Driver DRV8833?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Motor Kiri (Maju &amp; Mundur)</td><td>GPIO ..... &amp; GPIO .....</td><td rowspan="3">Jelaskan: Karena arus dari pin GPIO ESP32 terlalu kecil (~40mA) sehingga tidak kuat memutar motor DC secara langsung tanpa penguat arus DRV8833.</td></tr>
                        <tr><td>2</td><td>Motor Kanan (Maju &amp; Mundur)</td><td>GPIO ..... &amp; GPIO .....</td></tr>
                        <tr><td>3</td><td>Sensor Garis Bawah (TCRT5000)</td><td>GPIO .....</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika Port COM tidak muncul di Arduino IDE, pastikan kabel USB yang dipakai bukan kabel 'charge-only' dan driver CP210x / CH340 sudah terinstal di komputer lab."
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
            "theory": """
                <p>Di tingkat SD kita menyusun balok puzzle visual. Tahukah kamu bahwa di balik setiap balok warna-warni tersebut sebenarnya tersimpan baris kode bahasa <strong>C++</strong>? Pada modul jembatan ini, kita membuka jendela <strong>Side-by-Side (Berdampingan)</strong> untuk melihat terjemahan langsung dari balok ke teks C++:</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Balok Visual (Blockly)</th><th>Terjemahan Sintaks C++ (Arduino IDE)</th><th>Aturan Penting Sintaks</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>[Saat Program Dimulai]</code></td><td><code>void setup() { ... }</code></td><td>Dijalankan 1 kali saja saat robot baru menyala.</td></tr>
                        <tr><td><code>[Ulangi Selamanya]</code></td><td><code>void loop() { ... }</code></td><td>Diulang terus-menerus selama robot menyala.</td></tr>
                        <tr><td><code>[Tunggu 1 detik]</code></td><td><code>delay(1000);</code></td><td>1 detik = 1000 milidetik (ms). Wajib diakhiri titik koma <code>;</code></td></tr>
                        <tr><td><code>[Jika (Jarak &lt; 10) Maka]</code></td><td><code>if (jarak &lt; 10) { ... }</code></td><td>Syarat ditulis di dalam <code>( )</code>, aksi di dalam <code>{ }</code>.</td></tr>
                    </tbody>
                </table>
            """,
            "safety": "Perhatikan penulisan huruf besar dan kecil pada kode C++. Menulis 'digitalwrite' (huruf w kecil) akan menghasilkan pesan error karena yang benar adalah 'digitalWrite' (huruf W besar).",
            "steps": [
                "Buka mode <strong>Side-by-Side Block-to-C++ Viewer</strong> pada aplikasi MazeBot.",
                "Tarik balok <strong>[Nyalakan LED]</strong> dan <strong>[Tunggu 0.5 detik]</strong> ke kanvas kiri, lalu amati kode C++ yang muncul otomatis di panel kanan.",
                "Salin kode C++ tersebut ke Arduino IDE, lalu coba ubah angka <code>delay(500);</code> menjadi <code>delay(200);</code> langsung pada teks kodenya.",
                "Klik tombol <strong>Verify (Centang)</strong> di Arduino IDE untuk mengecek apakah ada tanda titik koma (<code>;</code>) yang terlupa."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-02: Side-by-Side Translation (Dari Balok Visual ke C++ Murni)
// =========================================================================
#define PIN_LED 2

// [BALOK: Saat Program Dimulai]
void setup() {
  pinMode(PIN_LED, OUTPUT); // Mengatur pin GPIO 2 sebagai keluaran
}

// [BALOK: Ulangi Selamanya]
void loop() {
  // [BALOK: Lampu Indikator NYALA]
  digitalWrite(PIN_LED, HIGH);
  
  // [BALOK: Tunggu 0.5 Detik (500 milidetik)]
  delay(500);
  
  // [BALOK: Lampu Indikator MATI]
  digitalWrite(PIN_LED, LOW);
  
  // [BALOK: Tunggu 0.5 Detik (500 milidetik)]
  delay(500);
}""",
            "lks": """
                <p><strong>Latihan Terjemahan Balok ke C++:</strong> Tuliskan baris kode C++ yang setara dengan balok berikut!</p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Instruksi Balok Visual</th><th>Tuliskan Kode C++ yang Benar</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Tunggu selama 2.5 detik</td><td><code>delay(..........);</code></td></tr>
                        <tr><td>2</td><td>Nyalakan lampu pada PIN_LED</td><td><code>digitalWrite(.........., ..........);</code></td></tr>
                        <tr><td>3</td><td>Jika jarak kurang dari 15 cm</td><td><code>if (....................) {</code></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika muncul error 'expected ; before } token', tunjukkan kepada siswa nomor baris yang berwarna merah di Arduino IDE—itu tandanya baris tepat di atasnya lupa diberi titik koma (;)."
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
            "theory": """
                <p>Dalam pemrograman C++, <strong>Variabel</strong> adalah sebuah kotak penyimpanan di dalam memori otak ESP32 yang diberi nama. Misalnya, daripada mengetik angka kecepatan berulang-ulang di banyak baris, kita cukup membuat variabel <code>int kecepatan = 180;</code>.</p>
                <ul>
                    <li><strong><code>int</code> (Integer):</strong> Menyimpan angka bulat tanpa koma (contoh: <code>int kecepatan = 150;</code>, <code>int hitungan = 1;</code>).</li>
                    <li><strong><code>float</code> (Floating Point):</strong> Menyimpan angka desimal berkoma (contoh: <code>float jarakCm = 12.45;</code>).</li>
                    <li><strong>Serial Monitor:</strong> Jendela komunikasi teks antara robot dan layar komputer melalui kabel USB dengan kecepatan baca <code>115200</code> baud.</li>
                </ul>
            """,
            "safety": "Pastikan angka baudrate di pojok kanan bawah jendela Serial Monitor diatur ke '115200 baud' (sama dengan angka di dalam Serial.begin) agar teks yang muncul tidak berupa simbol acak.",
            "steps": [
                "Ketikkan kode program M-03 di bawah ini pada lembar kerja baru (Sketch) di Arduino IDE.",
                "Perhatikan pendeklarasian variabel <code>int kecepatanMotor</code> dan <code>float batasJarakAman</code> di bagian atas program.",
                "Unggah program ke ESP32, lalu buka <strong>Tools &rarr; Serial Monitor</strong> (atau klik ikon kaca pembesar di pojok kanan atas).",
                "Amati bagaimana nilai variabel <code>hitunganDetik</code> bertambah 1 setiap detiknya di layar!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-03: Struktur C++ (Setup, Loop, Variabel int/float, & Serial Print)
// =========================================================================

// Deklarasi Variabel Global
int kecepatanMotor = 160;       // Bilangan bulat (0 - 255)
float batasJarakAman = 12.5;    // Bilangan desimal (cm)
int hitunganDetik = 0;          // Variabel penghitung waktu

void setup() {
  Serial.begin(115200); // Memulai komunikasi serial ke PC
  Serial.println("--- INISIALISASI VARIABEL MAZEBOT ---");
  
  Serial.print("Kecepatan Awal Motor (PWM): ");
  Serial.println(kecepatanMotor);
  
  Serial.print("Batas Jarak Aman Dinding : ");
  Serial.print(batasJarakAman);
  Serial.println(" cm");
  Serial.println("-------------------------------------");
}

void loop() {
  hitunganDetik = hitunganDetik + 1;
  
  Serial.print("Detik ke-");
  Serial.print(hitunganDetik);
  Serial.println(" -> Robot aktif memantau sensor.");
  
  delay(1000); // Jeda 1000 ms (1 detik)
}""",
            "lks": """
                <p><strong>Eksperimen Variabel &amp; Tipe Data:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Eksperimen Kode</th><th>Hasil yang Muncul di Serial Monitor</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Simpan angka <code>15.75</code> ke dalam variabel bertipe <code>int</code></td><td>Angka di belakang koma menjadi: ....................</td></tr>
                        <tr><td>2</td><td>Simpan angka <code>15.75</code> ke dalam variabel bertipe <code>float</code></td><td>Angka yang tampil adalah: ..........................</td></tr>
                        <tr><td>3</td><td>Apa bedanya <code>Serial.print()</code> dengan <code>Serial.println()</code>?</td><td><code>println</code> membuat: .................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika tidak ada teks yang muncul di Serial Monitor setelah upload selesai, tekan tombol kecil bertuliskan 'EN' atau 'RST' (Reset) pada papan ESP32 untuk mengulang fungsi void setup() dari awal."
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
            "theory": """
                <p>Jika setiap kali ingin maju kita harus menulis 4 baris perintah pin motor di dalam <code>void loop()</code>, kode program kita akan menjadi sangat panjang dan membingungkan! Solusinya adalah <strong>Pemrograman Modular (Function)</strong>: kita membungkus perintah pin motor ke dalam fungsi bernama <code>maju(int spd)</code>, <code>belokKanan(int spd)</code>, dan <code>berhenti()</code>.</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Nama Fungsi</th><th>Motor Kiri (IN1:25, IN2:26)</th><th>Motor Kanan (IN3:27, IN4:14)</th><th>Gerakan Fisik Robot</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>maju(spd)</code></td><td>IN1 = <code>spd</code>, IN2 = <code>0</code></td><td>IN3 = <code>spd</code>, IN4 = <code>0</code></td><td>Melaju lurus ke depan</td></tr>
                        <tr><td><code>mundur(spd)</code></td><td>IN1 = <code>0</code>, IN2 = <code>spd</code></td><td>IN3 = <code>0</code>, IN4 = <code>spd</code></td><td>Melaju lurus ke belakang</td></tr>
                        <tr><td><code>belokKiri(spd)</code></td><td>IN1 = <code>0</code>, IN2 = <code>spd</code> (Mundur)</td><td>IN3 = <code>spd</code>, IN4 = <code>0</code> (Maju)</td><td>Berputar poros ke kiri (Pivot Left)</td></tr>
                        <tr><td><code>belokKanan(spd)</code></td><td>IN1 = <code>spd</code>, IN2 = <code>0</code> (Maju)</td><td>IN3 = <code>0</code>, IN4 = <code>spd</code> (Mundur)</td><td>Berputar poros ke kanan (Pivot Right)</td></tr>
                        <tr><td><code>berhenti()</code></td><td>IN1 = <code>0</code>, IN2 = <code>0</code></td><td>IN3 = <code>0</code>, IN4 = <code>0</code></td><td>Kedua roda berhenti</td></tr>
                    </tbody>
                </table>
            """,
            "safety": "Saat pertama kali mengunggah kode motor, angkat sedikit bodi robot (atau letakkan di atas kotak kecil sehingga roda menggantung) untuk memastikan arah putar roda sudah benar sebelum ditaruh di lantai.",
            "steps": [
                "Ketikkan deklarasi pin motor DRV8833 dan kelima fungsi modular gerak seperti pada kode M-04 di bawah.",
                "Perhatikan betapa bersih dan singkatnya isi <code>void loop()</code> karena kita cukup memanggil nama fungsinya saja!",
                "Uji di lantai kelas dan sesuaikan nilai parameter <code>delay(...)</code> pada saat memanggil <code>belokKanan(160)</code> hingga sudut putarannya tepat 90 derajat."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-04: Fungsi Modular Gerak Robot dengan Driver DRV8833 (PWM 0-255)
// =========================================================================
#define IN1_KIRI_MAJU    25
#define IN2_KIRI_MUNDUR  26
#define IN3_KANAN_MAJU   27
#define IN4_KANAN_MUNDUR 14

// --- FUNGSI MODULAR GERAK MOTOR ---
void maju(int spd) {
  analogWrite(IN1_KIRI_MAJU, spd);   analogWrite(IN2_KIRI_MUNDUR, 0);
  analogWrite(IN3_KANAN_MAJU, spd);  analogWrite(IN4_KANAN_MUNDUR, 0);
}

void mundur(int spd) {
  analogWrite(IN1_KIRI_MAJU, 0);     analogWrite(IN2_KIRI_MUNDUR, spd);
  analogWrite(IN3_KANAN_MAJU, 0);    analogWrite(IN4_KANAN_MUNDUR, spd);
}

void belokKiri(int spd) {
  analogWrite(IN1_KIRI_MAJU, 0);     analogWrite(IN2_KIRI_MUNDUR, spd);
  analogWrite(IN3_KANAN_MAJU, spd);  analogWrite(IN4_KANAN_MUNDUR, 0);
}

void belokKanan(int spd) {
  analogWrite(IN1_KIRI_MAJU, spd);   analogWrite(IN2_KIRI_MUNDUR, 0);
  analogWrite(IN3_KANAN_MAJU, 0);    analogWrite(IN4_KANAN_MUNDUR, spd);
}

void berhenti() {
  analogWrite(IN1_KIRI_MAJU, 0);     analogWrite(IN2_KIRI_MUNDUR, 0);
  analogWrite(IN3_KANAN_MAJU, 0);    analogWrite(IN4_KANAN_MUNDUR, 0);
}

void setup() {
  pinMode(IN1_KIRI_MAJU, OUTPUT);    pinMode(IN2_KIRI_MUNDUR, OUTPUT);
  pinMode(IN3_KANAN_MAJU, OUTPUT);   pinMode(IN4_KANAN_MUNDUR, OUTPUT);
  berhenti();
  delay(2000); // Jeda aman 2 detik sebelum bergerak
}

void loop() {
  maju(160);       delay(1500); // Maju selama 1.5 detik
  berhenti();      delay(500);
  belokKanan(160); delay(450);  // Belok Kanan 90 derajat
  berhenti();      delay(500);
  maju(160);       delay(1500);
  berhenti();
  while(true); // Berhenti selamanya setelah 1 siklus selesai
}""",
            "lks": """
                <p><strong>Uji Fungsi Modular &amp; Kalibrasi Waktu Belok:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Nama Fungsi yang Dipanggil</th><th>Nilai PWM (0–255)</th><th>Nilai <code>delay(ms)</code> yang Diuji</th><th>Hasil Gerakan Fisik Robot</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>maju(160)</code></td><td>160</td><td>1500 ms</td><td>Maju lurus sejauh ......... cm</td></tr>
                        <tr><td><code>belokKanan(160)</code></td><td>160</td><td>....... ms (Cari yang pas 90&deg;)</td><td>Berputar tepat 90&deg; ke kanan</td></tr>
                        <tr><td><code>belokKiri(160)</code></td><td>160</td><td>....... ms (Cari yang pas 90&deg;)</td><td>Berputar tepat 90&deg; ke kiri</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika saat dipanggil fungsi maju() salah satu roda justru berputar mundur, tukar definisi nomor pin IN1 dan IN2 (atau IN3 dan IN4) di bagian #define paling atas program."
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
            "theory": """
                <p>Materi ini terintegrasi langsung dengan pelajaran <strong>IPA Fisika Kelas 8 (Gelombang dan Bunyi)</strong>! Sensor HC-SR04 bekerja dengan memancarkan gelombang ultrasonik berfrekuensi <strong>40 kHz</strong> dari pin <strong>TRIG</strong>, lalu menghitung berapa mikrodetik (&mu;s) waktu yang dibutuhkan sampai pantulan suaranya diterima kembali oleh pin <strong>ECHO</strong>.</p>
                <div class="formula-box">
                    Rumus Fisika Pantulan Bunyi: &nbsp;&nbsp; <i>s</i> = (<i>v</i> &times; <i>t</i>) / 2 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Jarak (cm) = (Durasi &mu;s &times; 0.034) / 2
                </div>
                <p><strong>Mengapa harus dibagi 2?</strong> Karena waktu <i>t</i> yang diukur oleh sensor adalah waktu perjalanan gelombang bunyi <em>Pergi (dari robot ke dinding)</em> ditambah waktu <em>Pulang (dari dinding kembali ke robot)</em>. Padahal jarak robot ke dinding hanyalah separuh dari lintasan bolak-balik tersebut!</p>
            """,
            "safety": "Perhatikan bahwa pin ECHO sensor depan terhubung ke GPIO 34 pada ESP32. Pin GPIO 34 dan 35 pada ESP32 adalah pin khusus INPUT-ONLY, sehingga tidak boleh diatur sebagai OUTPUT.",
            "steps": [
                "Siapkan penggaris 30 cm dan sebuah papan/buku tebal sebagai bidang pantul di depan sensor depan robot.",
                "Ketikkan fungsi perhitungan fisika ultrasonik pada kode M-05 di bawah ini.",
                "Unggah program dan buka Serial Monitor. Bandingkan nilai durasi mikrodetik (&mu;s) dan hasil konversi sentimeter (cm) dengan ukuran penggaris asli!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-05: Fisika Gelombang Bunyi pada Sensor Ultrasonik (s = v * t / 2)
// =========================================================================
#define TRIG_DEPAN 33
#define ECHO_DEPAN 34

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_DEPAN, OUTPUT);
  pinMode(ECHO_DEPAN, INPUT);
}

void loop() {
  // 1. Berikan pulsa pemicu (Trigger) selama 10 mikrodetik
  digitalWrite(TRIG_DEPAN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_DEPAN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_DEPAN, LOW);

  // 2. Ukur waktu tempuh gelombang pergi-pulang (t) dalam mikrodetik (us)
  long durasiMikrodetik = pulseIn(ECHO_DEPAN, HIGH, 30000); // Timeout 30.000 us

  // 3. Terapkan Rumus Fisika: s = (v * t) / 2  dengan v = 0.034 cm/us
  float jarakCm = (durasiMikrodetik * 0.034) / 2.0;

  // 4. Tampilkan hasil ke Serial Monitor
  Serial.print("Waktu Pantul (t): ");
  Serial.print(durasiMikrodetik);
  Serial.print(" us  |  Jarak Hitung (s): ");
  Serial.print(jarakCm);
  Serial.println(" cm");

  delay(300);
}""",
            "lks": """
                <p><strong>Lembar Kerja Eksperimen Fisika Bunyi (IPA &times; Robotika):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Jarak Sebenarnya (Penggaris)</th><th>Durasi Pantul <i>t</i> (&mu;s) di Serial Monitor</th><th>Perhitungan Manual (<i>t</i> &times; 0.034) / 2</th><th>Bacaan Sensor Robot (cm)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>10 cm</td><td>.............. &mu;s</td><td>.............. cm</td><td>.............. cm</td></tr>
                        <tr><td>20 cm</td><td>.............. &mu;s</td><td>.............. cm</td><td>.............. cm</td></tr>
                        <tr><td>30 cm</td><td>.............. &mu;s</td><td>.............. cm</td><td>.............. cm</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Selalu sertakan parameter ke-3 berupa angka timeout 30000 pada pulseIn(ECHO, HIGH, 30000) agar jika tidak ada penghalang di depan robot, program tidak macet menunggu pantulan suara terlalu lama."
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
            "theory": """
                <p>MazeBot memiliki 3 sensor ultrasonik yang menghadap ke <strong>Kiri</strong>, <strong>Depan</strong>, dan <strong>Kanan</strong>. Apa yang terjadi jika ketiga sensor memancarkan gelombang bunyi secara bersamaan di dalam lorong labirin yang sempit? Pantulan suara dari sensor Kiri bisa memantul ke dinding lalu masuk ke telinga sensor Depan! Gangguan tabrakan gema ini disebut <strong>Crosstalk</strong>.</p>
                <p>Untuk mencegahnya, kita membaca ketiga sensor <strong>secara bergantian (sekuensial)</strong> dengan memberikan jeda hening singkat (<code>delay(20)</code> milidetik) supaya gema sensor sebelumnya hilang terlebih dahulu sebelum sensor berikutnya berbunyi.</p>
            """,
            "safety": "Pastikan kabel jumper atau soket ketiga sensor ultrasonik terpasang kencang dan tidak menghalangi putaran roda kiri maupun roda kanan.",
            "steps": [
                "Perhatikan bagaimana kita membuat satu fungsi pintar <code>float bacaUltrasonik(int trig, int echo)</code> yang mengembalikan nilai <code>return jarak;</code>.",
                "Di dalam <code>void loop()</code>, panggil fungsi tersebut berurutan untuk sensor Kiri, jeda 20 ms, sensor Depan, jeda 20 ms, lalu sensor Kanan.",
                "Letakkan robot di dalam lorong kardus dan amati ketiga nilai jarak secara langsung pada Serial Monitor!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-06: Pembacaan 3 Sensor Sekuensial dengan Jeda Aman Anti-Crosstalk
// =========================================================================
#define TRIG_KIRI   32
#define ECHO_KIRI   35
#define TRIG_DEPAN  33
#define ECHO_DEPAN  34
#define TRIG_KANAN  18
#define ECHO_KANAN  19

// Fungsi Reusable untuk membaca sensor ultrasonik mana saja
float bacaUltrasonik(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long durasi = pulseIn(echoPin, HIGH, 25000); // Timeout 25 ms (~4 meter)
  if (durasi == 0) return 999.0; // Jika ruang kosong jauh (tidak ada pantulan)
  return (durasi * 0.034) / 2.0;
}

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_KIRI, OUTPUT);   pinMode(ECHO_KIRI, INPUT);
  pinMode(TRIG_DEPAN, OUTPUT);  pinMode(ECHO_DEPAN, INPUT);
  pinMode(TRIG_KANAN, OUTPUT);  pinMode(ECHO_KANAN, INPUT);
}

void loop() {
  float jarakKiri = bacaUltrasonik(TRIG_KIRI, ECHO_KIRI);
  delay(20); // Jeda Anti-Crosstalk agar gema suara kiri reda
  
  float jarakDepan = bacaUltrasonik(TRIG_DEPAN, ECHO_DEPAN);
  delay(20); // Jeda Anti-Crosstalk agar gema suara depan reda
  
  float jarakKanan = bacaUltrasonik(TRIG_KANAN, ECHO_KANAN);
  delay(20);

  Serial.print("[RADAR] Kiri: ");  Serial.print(jarakKiri, 1);
  Serial.print(" cm | Depan: ");   Serial.print(jarakDepan, 1);
  Serial.print(" cm | Kanan: ");   Serial.print(jarakKanan, 1);
  Serial.println(" cm");

  delay(200);
}""",
            "lks": """
                <p><strong>Tabel Pemetaan Radar 3 Arah di Berbagai Posisi Labirin:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Posisi Robot di Labirin</th><th>Bacaan Sensor Kiri (cm)</th><th>Bacaan Sensor Depan (cm)</th><th>Bacaan Sensor Kanan (cm)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Di tengah lorong lurus</td><td>.......... cm</td><td>.......... cm</td><td>.......... cm</td></tr>
                        <tr><td>Menghadap tikungan siku kiri</td><td>.......... cm</td><td>.......... cm</td><td>.......... cm</td></tr>
                        <tr><td>Di ujung jalan buntu (Dead-End)</td><td>.......... cm</td><td>.......... cm</td><td>.......... cm</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Perhatikan baris 'if (durasi == 0) return 999.0;' pada kode! Baris ini sangat penting karena saat di depan robot tidak ada dinding sama sekali, pulseIn menghasilkan angka 0. Jika tidak diubah menjadi 999.0 cm, robot akan mengira di depannya ada dinding menempel (0 cm)!"
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
            "theory": """
                <p>Ketika robot berada di persimpangan yang memiliki lebih dari satu jalur terbuka (misalnya Kiri terbuka dan Depan juga terbuka), robot tidak mungkin membelah diri menjadi dua! Oleh karena itu, kita menggunakan struktur <strong>Percabangan Berjenjang (<code>if - else if - else</code>)</strong> untuk memberikan urutan prioritas berpikir kepada robot:</p>
                <ol>
                    <li><code>if (jarakDepan &gt; 15)</code> &rarr; Prioritas 1: Jika depan kosong, maju lurus!</li>
                    <li><code>else if (jarakKiri &gt; 15)</code> &rarr; Prioritas 2: Jika depan tertutup tapi kiri terbuka, belok kiri!</li>
                    <li><code>else if (jarakKanan &gt; 15)</code> &rarr; Prioritas 3: Jika depan dan kiri tertutup tapi kanan terbuka, belok kanan!</li>
                    <li><code>else</code> &rarr; Pilihan Terakhir: Jika semua tertutup, berhenti!</li>
                </ol>
            """,
            "safety": "Uji logika percabangan terlebih dahulu melalui teks di Serial Monitor sebelum mengaktifkan motor agar siswa benar-benar paham alur pengambilan keputusan robot.",
            "steps": [
                "Gabungkan kode pembacaan 3 sensor (M-06) dengan blok logika <code>if - else if - else</code> seperti pada kode M-07.",
                "Gunakan dua buah buku sebagai dinding buatan untuk menutup sensor depan, kiri, atau kanan secara bergantian.",
                "Amati keputusan yang dicetak oleh robot di Serial Monitor, lalu aktifkan pemanggilan fungsi motornya!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-07: Logika Percabangan Majemuk (IF - ELSE IF - ELSE)
// =========================================================================
// (Gunakan definisi pin & fungsi bacaUltrasonik dari Modul M-06)
#define BATAS_TERBUKA 15.0 // Jarak > 15 cm dianggap jalan terbuka/kosong

void evaluasiKeputusan(float kiri, float depan, float kanan) {
  if (depan > BATAS_TERBUKA) {
    Serial.println("KEPUTUSAN: Jalan Depan Kosong -> MAJU LURUS");
    // maju(150);
  } 
  else if (kiri > BATAS_TERBUKA) {
    Serial.println("KEPUTUSAN: Depan Tertutup, Kiri Terbuka -> BELOK KIRI");
    // belokKiri(160); delay(450);
  } 
  else if (kanan > BATAS_TERBUKA) {
    Serial.println("KEPUTUSAN: Depan & Kiri Tertutup, Kanan Terbuka -> BELOK KANAN");
    // belokKanan(160); delay(450);
  } 
  else {
    Serial.println("KEPUTUSAN: Semua Arah Tertutup -> JALAN BUNTU (STOP)");
    // berhenti();
  }
}""",
            "lks": """
                <p><strong>Uji Meja Kebenaran Logika (Truth Table) Percabangan:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Kasus</th><th>Nilai Kiri</th><th>Nilai Depan</th><th>Nilai Kanan</th><th>Keputusan Mana yang Diambil oleh Kode M-07?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>8 cm</td><td>45 cm</td><td>9 cm</td><td>........................................................</td></tr>
                        <tr><td>2</td><td>35 cm</td><td>7 cm</td><td>40 cm</td><td>........................................................</td></tr>
                        <tr><td>3</td><td>6 cm</td><td>8 cm</td><td>30 cm</td><td>........................................................</td></tr>
                        <tr><td>4</td><td>7 cm</td><td>6 cm</td><td>8 cm</td><td>........................................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Perhatikan Kasus nomor 2 pada LKS (Kiri=35 cm, Depan=7 cm, Kanan=40 cm): karena 'else if (kiri > 15)' ditulis lebih dulu di atas 'else if (kanan > 15)', maka robot pasti memilih BELOK KIRI!"
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
            "theory": """
                <p>Pada <strong>Ujian Tengah Semester (Proyek Mini 2)</strong> ini, setiap kelompok diuji pada arena <strong>Persimpangan Huruf T (T-Junction)</strong>. Robot diletakkan di lorong tengah menuju pertigaan T. Penguji (Guru) akan menutup salah satu cabang pertigaan (Kiri atau Kanan) secara acak menggunakan papan penghalang.</p>
                <p>Begitu robot mendeteksi dinding pertigaan di depannya, robot harus berhenti sejenak, memindai jarak Kiri dan Kanan, lalu <strong>memilih berbelok ke sisi yang terbuka lebar</strong> tanpa menyentuh dinding!</p>
            """,
            "safety": "Pastikan kecepatan maju tidak terlalu kencang (gunakan PWM sekitar 140–160) agar robot sempat berhenti dan memindai pertigaan sebelum hidungnya menabrak dinding depan.",
            "steps": [
                "Tulis dan lengkapi program utuh Proyek Mini 2 di bawah ini pada Arduino IDE.",
                "Unggah ke MazeBot dan lakukan uji coba mandiri di meja kelompok.",
                "Majulah ke arena ujian Persimpangan T. Guru akan melakukan 2 kali pengujian: Skenario A (Cabang Kiri ditutup) dan Skenario B (Cabang Kanan ditutup)."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-08: UTS PROYEK MINI 2 - Uji Refleks Radar di Persimpangan T
// =========================================================================
#define IN1 25
#define IN2 26
#define IN3 27
#define IN4 14
#define TRIG_KIRI  32
#define ECHO_KIRI  35
#define TRIG_DEPAN 33
#define ECHO_DEPAN 34
#define TRIG_KANAN 18
#define ECHO_KANAN 19

float bacaSensor(int trig, int echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10);
  digitalWrite(trig, LOW);
  long d = pulseIn(echo, HIGH, 25000);
  return (d == 0) ? 999.0 : (d * 0.034) / 2.0;
}

void gerak(int kiriMaju, int kiriMundur, int kananMaju, int kananMundur) {
  analogWrite(IN1, kiriMaju);  analogWrite(IN2, kiriMundur);
  analogWrite(IN3, kananMaju); analogWrite(IN4, kananMundur);
}

void setup() {
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  pinMode(TRIG_KIRI, OUTPUT);  pinMode(ECHO_KIRI, INPUT);
  pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT);
  pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT);
  gerak(0, 0, 0, 0);
  delay(2000);
}

void loop() {
  float depan = bacaSensor(TRIG_DEPAN, ECHO_DEPAN);
  delay(20);

  if (depan > 14.0) {
    gerak(150, 0, 150, 0); // Maju lurus selama depan aman
  } else {
    gerak(0, 0, 0, 0);     // Berhenti di mulut Persimpangan T
    delay(300);            // Beri waktu stabil untuk memindai kiri & kanan
    
    float kiri  = bacaSensor(TRIG_KIRI, ECHO_KIRI);   delay(20);
    float kanan = bacaSensor(TRIG_KANAN, ECHO_KANAN); delay(20);

    if (kiri > kanan && kiri > 18.0) {
      gerak(0, 160, 160, 0); delay(450); // Belok Kiri 90 derajat
    } else if (kanan > 18.0) {
      gerak(160, 0, 0, 160); delay(450); // Belok Kanan 90 derajat
    }
    gerak(0, 0, 0, 0); delay(200);
  }
}""",
            "lks": """
                <p><strong>Lembar Penilaian Ujian Tengah Semester (Proyek Mini 2 - SMP):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Pengujian</th><th>Kondisi Pertigaan T</th><th>Respon yang Diharapkan</th><th>Hasil Uji (Berhasil / Gagal)</th><th>Skor (Maks 50)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Uji 1</td><td>Sisi Kanan Ditutup, Kiri Terbuka</td><td>Berhenti di T &rarr; Belok Kiri &rarr; Maju</td><td>Berhasil / Gagal</td><td>....... / 50</td></tr>
                        <tr><td>Uji 2</td><td>Sisi Kiri Ditutup, Kanan Terbuka</td><td>Berhenti di T &rarr; Belok Kanan &rarr; Maju</td><td>Berhasil / Gagal</td><td>....... / 50</td></tr>
                        <tr><td colspan="4"><strong>TOTAL NILAI UTS PRAKTIKUM SMP</strong></td><td><strong>....... / 100</strong></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Perhatikan kondisi 'if (kiri > kanan && kiri > 18.0)': membandingkan 'kiri > kanan' memastikan robot memilih lorong yang paling lapang di pertigaan T!"
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
            "theory": """
                <p>Pada MazeBot EduKit, sensor <strong>TCRT5000</strong> yang dipasang di kolong depan dikhususkan murni sebagai <strong>Detektor Garis Finish</strong> (bukan pendeteksi persimpangan). Modul ini dilengkapi IC komparator yang mengeluarkan logika digital pada pin <strong>DO (Digital Output - GPIO 4)</strong>:</p>
                <ul>
                    <li><strong>Lantai Putih (Memantulkan Inframerah):</strong> Pin DO bernilai <code>LOW (0)</code>.</li>
                    <li><strong>Garis Lakban Hitam (Menyerap Inframerah):</strong> Pin DO bernilai <code>HIGH (1)</code>.</li>
                </ul>
                <p>Saat bernilai <code>HIGH</code>, program akan mengubah variabel status <code>bool misiSelesai = true;</code> sehingga robot menghentikan seluruh roda dan keluar dari siklus penjelajahan.</p>
            """,
            "safety": "Kalibrasi trimpot (potensiometer biru) pada modul TCRT5000 menggunakan obeng plus kecil hanya bila sensitivitas cahaya ruangan berubah drastis.",
            "steps": [
                "Unggah kode M-09 di bawah ini untuk menguji penguncian status Finish.",
                "Letakkan robot di lantai putih; robot akan berjalan maju perlahan.",
                "Hadang jalur depan robot dengan lakban hitam yang ditempel di lantai. Pastikan begitu sensor TCRT5000 melewati lakban hitam, robot langsung berhenti permanen!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-09: Sensor Inframerah TCRT5000 sebagai Pengunci Garis Finish
// =========================================================================
#define PIN_FINISH 4
#define PIN_LED    2
#define IN1 25
#define IN2 26
#define IN3 27
#define IN4 14

bool misiSelesai = false; // Flag pengunci status finish

void berhentiTotal() {
  analogWrite(IN1, 0); analogWrite(IN2, 0);
  analogWrite(IN3, 0); analogWrite(IN4, 0);
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_FINISH, INPUT);
  pinMode(PIN_LED, OUTPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  delay(2000);
}

void loop() {
  // Jika sudah menyentuh finish, kunci robot dalam keadaan diam!
  if (misiSelesai == true) {
    berhentiTotal();
    return; // Langsung keluar dari loop()
  }

  int statusGaris = digitalRead(PIN_FINISH);

  if (statusGaris == HIGH) { // HIGH = Mendeteksi Garis Hitam Finish
    berhentiTotal();
    digitalWrite(PIN_LED, HIGH);
    misiSelesai = true; // Kunci flag agar tidak jalan lagi
    Serial.println("GARIS FINISH TERDETEKSI! Navigasi Dihentikan.");
  } else {
    // Selama masih lantai putih (LOW), terus melaju
    analogWrite(IN1, 145); analogWrite(IN2, 0);
    analogWrite(IN3, 145); analogWrite(IN4, 0);
  }
}""",
            "lks": """
                <p><strong>Tabel Pengujian Sensor Garis TCRT5000:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Permukaan Lantai</th><th>Nilai <code>digitalRead(PIN_FINISH)</code></th><th>Nilai Variabel <code>misiSelesai</code></th><th>Kondisi Motor Roda</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Keramik Putih</td><td><code>LOW (0)</code> / <code>HIGH (1)</code></td><td><code>false</code> / <code>true</code></td><td>Berputar / Berhenti</td></tr>
                        <tr><td>Garis Lakban Hitam</td><td><code>LOW (0)</code> / <code>HIGH (1)</code></td><td><code>false</code> / <code>true</code></td><td>Berputar / Berhenti</td></tr>
                        <tr><td>Diangkat kembali ke Putih setelah Finish</td><td><code>LOW (0)</code></td><td>Tetap <code>true</code> (Terkunci)</td><td>Tetap Berhenti</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Beberapa modul TCRT5000 di pasaran memiliki logika terbalik (LOW saat hitam). Jika demikian, cukup ubah syarat 'if (statusGaris == HIGH)' menjadi 'if (statusGaris == LOW)'."
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
            "theory": """
                <p>Bagaimana seorang penjelajah bisa dijamin keluar dari labirin yang rumit tanpa peta? Dalam ilmu komputer dan matematika topologi, terdapat algoritma klasik bernama <strong>Wall-Follower: Left-Hand Rule (Aturan Tangan Kiri)</strong>. Bayangkan kamu berjalan di dalam labirin sambil terus menyentuhkan tangan kirimu ke dinding sebelah kiri tanpa pernah melepaskannya!</p>
                <p>Jika diterjemahkan menjadi aturan algoritma prioritas untuk MazeBot setiap kali menemui persimpangan:</p>
                <ol>
                    <li><strong>Prioritas 1 (Cek Kiri):</strong> Apakah dinding di sebelah KIRI terbuka? Jika YA &rarr; <strong>Wajib Belok Kiri!</strong></li>
                    <li><strong>Prioritas 2 (Cek Depan):</strong> Jika kiri tertutup, apakah DEPAN terbuka? Jika YA &rarr; <strong>Maju Lurus!</strong></li>
                    <li><strong>Prioritas 3 (Cek Kanan):</strong> Jika kiri dan depan tertutup, apakah KANAN terbuka? Jika YA &rarr; <strong>Belok Kanan!</strong></li>
                    <li><strong>Prioritas 4 (Buntu):</strong> Jika Kiri, Depan, dan Kanan semuanya tertutup dinding &rarr; <strong>Putar Balik 180&deg; (U-Turn)!</strong></li>
                </ol>
            """,
            "safety": "Pada sesi ini siswa fokus merancang flowchart dan simulasi algoritma menggunakan pion robot di atas peta labirin sebelum memprogram gerakan fisik.",
            "steps": [
                "Perhatikan gambar peta labirin yang memiliki 2 jalan buntu dan 1 jalur keluar menuju Finish.",
                "Gunakan penghapus atau miniatur robot, lalu gerakkan mengikuti aturan ketat <em>Left-Hand Rule</em> (selalu utamakan belok kiri setiap ada bukaan kiri).",
                "Tandai rute yang dilalui dengan pensil dan buktikan bahwa meskipun sempat masuk ke jalan buntu, aturan ini selalu berhasil membawa robot keluar ke garis Finish!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-10: Pseudocode & Kerangka Logika Algoritma Left-Hand Rule
// =========================================================================

void algoritmaLeftHandRule(float jarakKiri, float jarakDepan, float jarakKanan) {
  const float AMBANG_BUKAAN = 18.0; // Lorong dianggap terbuka jika > 18 cm
  const float AMBANG_DEPAN  = 13.0; // Batas aman depan sebelum menabrak

  // PRIORITAS 1: Cek apakah ada bukaan belokan di sebelah KIRI
  if (jarakKiri > AMBANG_BUKAAN) {
    Serial.println("[LHR] Bukaan Kiri Terdeteksi -> Ambil Belok KIRI!");
    // Maju sedikit ke tengah simpang -> Belok Kiri 90 -> Maju masuk lorong baru
  }
  // PRIORITAS 2: Jika Kiri tertutup dinding, cek apakah DEPAN bebas
  else if (jarakDepan > AMBANG_DEPAN) {
    Serial.println("[LHR] Kiri Dinding, Depan Bebas -> MAJU LURUS!");
  }
  // PRIORITAS 3: Jika Kiri & Depan tertutup, cek apakah KANAN terbuka
  else if (jarakKanan > AMBANG_BUKAAN) {
    Serial.println("[LHR] Kiri & Depan Tertutup -> Ambil Belok KANAN!");
  }
  // PRIORITAS 4: Ketiga arah tertutup (Jalan Buntu / Dead-End)
  else {
    Serial.println("[LHR] JALAN BUNTU! -> Eksekusi Putar Balik 180 Derajat!");
  }
}""",
            "lks": """
                <p><strong>Uji Pemahaman Algoritma Left-Hand Rule:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Kondisi Persimpangan yang Dihadapi Robot</th><th>Bukaan yang Tersedia</th><th>Keputusan Robot (Left-Hand Rule)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Simpang Empat (Crossroad +)</td><td>Kiri, Depan, dan Kanan Terbuka</td><td>Harus memilih: ..........................</td></tr>
                        <tr><td>Simpang Tiga Kiri</td><td>Kiri dan Depan Terbuka</td><td>Harus memilih: ..........................</td></tr>
                        <tr><td>Simpang Tiga Kanan</td><td>Depan dan Kanan Terbuka (Kiri Dinding)</td><td>Harus memilih: ..........................</td></tr>
                        <tr><td>Ujung Lorong Buntu</td><td>Tidak ada yang terbuka</td><td>Harus memilih: ..........................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Pastikan siswa memahami bahwa pada Simpang Tiga Kanan (Depan & Kanan terbuka, sedangkan Kiri tertutup dinding), robot memilih MAJU LURUS (bukan belok kanan) karena Prioritas 2 adalah Depan!"
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
            "theory": """
                <p>Saat mengimplementasikan <em>Left-Hand Rule</em> ke robot nyata, ada satu trik mekanik yang sangat penting: ketika sensor samping kiri pertama kali melihat celah lorong terbuka (<code>jarakKiri &gt; 20 cm</code>), posisi roda robot sebenarnya baru berada di <em>bibir awal</em> persimpangan!</p>
                <p>Jika robot langsung berputar di tempat saat itu juga, bagian belakang robot akan menyangkut di sudut dinding. Oleh karena itu, sebelum mengeksekusi <code>belokKiri()</code>, robot harus: (1) <strong>Maju sedikit (~250 ms)</strong> agar badan robot pas di tengah simpang, (2) <strong>Belok Kiri 90&deg;</strong>, lalu (3) <strong>Maju masuk ke lorong baru (~400 ms)</strong> agar keluar dari area simpang.</p>
            """,
            "safety": "Awasi gerakan robot di persimpangan. Siapkan tangan di dekat saklar jika sudut belok belum terkalibrasi sehingga robot menyerempet dinding.",
            "steps": [
                "Ketik dan unggah program implementasi Left-Hand Rule Dasar (M-11) di bawah ini.",
                "Perhatikan blok <code>if (kiri &gt; 20.0)</code> yang menyertakan dorongan maju sebelum dan sesudah berputar.",
                "Uji robot di arena labirin dan amati bagaimana robot secara konsisten mengambil belokan kiri setiap kali menemukan lorong di sebelah kirinya!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-11: Implementasi Navigasi Left-Hand Rule Dasar di C++
// =========================================================================
#define IN1 25
#define IN2 26
#define IN3 27
#define IN4 14
#define TRIG_KIRI  32
#define ECHO_KIRI  35
#define TRIG_DEPAN 33
#define ECHO_DEPAN 34
#define TRIG_KANAN 18
#define ECHO_KANAN 19

float bacaJarak(int trig, int echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10);
  digitalWrite(trig, LOW);
  long d = pulseIn(echo, HIGH, 25000);
  return (d == 0) ? 999.0 : (d * 0.034) / 2.0;
}

void setMotor(int L1, int L2, int R1, int R2) {
  analogWrite(IN1, L1); analogWrite(IN2, L2);
  analogWrite(IN3, R1); analogWrite(IN4, R2);
}

void setup() {
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  pinMode(TRIG_KIRI, OUTPUT);  pinMode(ECHO_KIRI, INPUT);
  pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT);
  pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT);
  setMotor(0, 0, 0, 0);
  delay(2000);
}

void loop() {
  float kiri  = bacaJarak(TRIG_KIRI, ECHO_KIRI);   delay(15);
  float depan = bacaJarak(TRIG_DEPAN, ECHO_DEPAN); delay(15);
  float kanan = bacaJarak(TRIG_KANAN, ECHO_KANAN); delay(15);

  if (kiri > 20.0) {
    // PRIORITAS 1: Kiri Terbuka -> Maju sedikit ke tengah simpang, Belok Kiri, Masuk lorong
    setMotor(145, 0, 145, 0); delay(250);
    setMotor(0, 0, 0, 0);     delay(150);
    setMotor(0, 160, 160, 0); delay(440); // Belok Kiri 90 derajat
    setMotor(0, 0, 0, 0);     delay(150);
    setMotor(145, 0, 145, 0); delay(400); // Masuk ke lorong baru
  }
  else if (depan > 12.0) {
    // PRIORITAS 2: Depan Bebas -> Maju Lurus
    setMotor(145, 0, 145, 0);
  }
  else if (kanan > 20.0) {
    // PRIORITAS 3: Belok Kanan
    setMotor(0, 0, 0, 0);     delay(150);
    setMotor(160, 0, 0, 160); delay(440); // Belok Kanan 90 derajat
    setMotor(0, 0, 0, 0);     delay(150);
  }
  else {
    // PRIORITAS 4: Buntu -> Berhenti / Putar Balik
    setMotor(160, 0, 0, 160); delay(880); // Putar 180 derajat
    setMotor(0, 0, 0, 0);     delay(200);
  }
}""",
            "lks": """
                <p><strong>Eksperimen Alignment Persimpangan:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Parameter Waktu (ms)</th><th>Jika Angka Terlalu Kecil</th><th>Jika Angka Terlalu Besar</th><th>Nilai Optimal Kelompokmu</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Delay Maju Sebelum Belok Kiri (250 ms)</td><td>Belok terlalu cepat (nyangkut sudut kiri)</td><td>Kelewatan mulut simpang</td><td>.......... ms</td></tr>
                        <tr><td>Delay Masuk Lorong Baru (400 ms)</td><td>Belok kiri dua kali di simpang yang sama</td><td>Menabrak dinding depan lorong baru</td><td>.......... ms</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika setelah belok kiri robot langsung belok kiri lagi (berputar-putar di tempat), tambah durasi 'Masuk ke lorong baru' dari 400 ms menjadi 500–600 ms agar sensor kiri sudah masuk diapit dinding lorong baru."
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
            "theory": """
                <p>Saat robot berjalan di lorong panjang, sedikit saja posisi awalnya miring 2&deg;, lama-kelamaan robot akan menabrak dinding samping! Agar robot tetap berada di tengah lorong, kita menggunakan sensor ultrasonik samping kiri untuk menjaga <strong>Wall Offset (Jarak Ideal ke Dinding Kiri = 5 s/d 8 cm)</strong>:</p>
                <ul>
                    <li>Jika <code>jarakKiri &lt; 5.0 cm</code> (Terlalu mepet ke dinding kiri!) &rarr; Kurangi kecepatan roda kanan sedikit agar robot miring menjauh ke kanan.</li>
                    <li>Jika <code>jarakKiri &gt; 8.0 cm</code> dan <code>&lt; 18.0 cm</code> (Terlalu jauh dari dinding kiri!) &rarr; Kurangi kecepatan roda kiri sedikit agar robot kembali mendekat ke tengah.</li>
                    <li>Jika <code>jarakKiri</code> berada di antara 5.0 – 8.0 cm &rarr; Kedua roda melaju dengan kecepatan sama (Lurus).</li>
                </ul>
            """,
            "safety": "Koreksi kecepatan PWM untuk menjaga dinding cukup berbeda 20–30 poin PWM saja (misal 150 dan 125) agar gerakan robot tetap mulus dan tidak bergoyang patah-patah (zig-zag kasar).",
            "steps": [
                "Buat fungsi <code>majuSusurDindingKiri(float jarakKiri)</code> seperti pada kode M-12 di bawah.",
                "Letakkan robot dengan posisi sengaja agak miring di awal lorong lurus sepanjang 1,5 meter.",
                "Jalankan robot dan amati bagaimana robot memperbaiki posisinya sendiri agar sejajar dengan dinding kiri pada jarak ~6 cm!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-12: Penjaga Jarak Sisi Dinding (Wall Offset 5 - 8 cm)
// =========================================================================
// Menggantikan perintah maju biasa saat menyusuri lorong lurus

void majuSusurDindingKiri(float jarakKiri) {
  int spdDasar = 150;
  int koreksi  = 28; // Selisih PWM untuk membelokkan halus ke tengah lorong

  if (jarakKiri < 5.0) {
    // Terlalu dekat dinding kiri (< 5 cm) -> Arahkan halus ke KANAN
    // Roda Kiri lebih cepat, Roda Kanan diperlambat
    setMotor(spdDasar, 0, spdDasar - koreksi, 0);
  } 
  else if (jarakKiri > 8.0 && jarakKiri < 18.0) {
    // Terlalu jauh dari dinding kiri (8 - 18 cm) -> Arahkan halus ke KIRI
    // Roda Kiri diperlambat, Roda Kanan lebih cepat
    setMotor(spdDasar - koreksi, 0, spdDasar, 0);
  } 
  else {
    // Jarak sudah pas di zona ideal (5.0 s/d 8.0 cm) -> Lurus Stabil
    setMotor(spdDasar, 0, spdDasar, 0);
  }
}""",
            "lks": """
                <p><strong>Eksperimen Tuning Nilai Koreksi Wall Offset:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Nilai Variabel <code>koreksi</code></th><th>Perilaku Gerak Robot di Lorong Panjang 1.5 Meter</th><th>Apakah Menyentuh Dinding?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>koreksi = 10</code> (Terlalu kecil)</td><td>.........................................................</td><td>Ya / Tidak</td></tr>
                        <tr><td><code>koreksi = 28</code> (Sedang/Ideal)</td><td>.........................................................</td><td>Ya / Tidak</td></tr>
                        <tr><td><code>koreksi = 70</code> (Terlalu besar)</td><td>.........................................................</td><td>Ya / Tidak (Bergoyang zig-zag)</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Mengapa syarat kedua memiliki batas '&& jarakKiri < 18.0'? Karena jika jarakKiri > 18.0 cm, itu artinya dinding kiri hilang (ada persimpangan belokan kiri), bukan sekadar bergeser di lorong!"
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
            "theory": """
                <p>Saat mengikuti <em>Left-Hand Rule</em>, robot pasti akan sesekali masuk ke <strong>Lorong Buntu (Dead-End)</strong> di mana dinding menutup bagian Depan, Kiri, dan Kanan sekaligus. Di dalam kantong jalan buntu yang sempit (lebar ~20–25 cm), memutar badan 180&deg; membutuhkan trik khusus agar bumper robot tidak menyangkut di dinding samping:</p>
                <ol>
                    <li>Jika <code>jarakDepan &lt; 8 cm</code> (terlalu mepet dinding ujung), <strong>mundur sedikit (~200 ms)</strong>.</li>
                    <li>Bandingkan ruang samping: jika <code>jarakKanan &gt;= jarakKiri</code>, berputarlah 180&deg; ke arah Kanan (begitu pula sebaliknya) agar hidung robot melewati sisi yang lebih longgar!</li>
                </ol>
            """,
            "safety": "Pastikan kabel baterai atau kabel sensor tidak menjuntai keluar dari sasis belakang robot agar tidak menyangkut di sudut lorong saat berputar 180 derajat.",
            "steps": [
                "Buat sebuah lorong buntu (huruf U terbalik) menggunakan 3 papan dinding kardus.",
                "Tambahkan fungsi <code>manuverPutarBalik(float kiri, float depan, float kanan)</code> ke dalam program robotmu.",
                "Lepaskan robot masuk ke lorong buntu tersebut dan setel durasi <code>delay(...)</code> putar 180&deg; hingga robot keluar lurus kembali!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-13: Penanganan Jalan Buntu Cerdas (Smart Dead-End U-Turn 180)
// =========================================================================

void manuverPutarBalik(float kiri, float depan, float kanan) {
  // 1. Berhenti sejenak
  setMotor(0, 0, 0, 0);
  delay(200);

  // 2. Jika hidung robot terlalu dekat ke dinding depan (< 8 cm), mundur sedikit
  if (depan < 8.0) {
    setMotor(0, 145, 0, 145);
    delay(220);
    setMotor(0, 0, 0, 0);
    delay(150);
  }

  // 3. Putar 180 derajat ke arah sisi samping yang lebih lega ruangnya
  int durasi180 = 860; // Kalibrasi sesuai lantai (sekitar 2x waktu belok 90)
  if (kanan >= kiri) {
    // Putar Balik lewat Kanan
    setMotor(165, 0, 0, 165);
    delay(durasi180);
  } else {
    // Putar Balik lewat Kiri
    setMotor(0, 165, 165, 0);
    delay(durasi180);
  }

  // 4. Berhenti stabil sebelum lanjut maju keluar lorong buntu
  setMotor(0, 0, 0, 0);
  delay(200);
}""",
            "lks": """
                <p><strong>Lembar Kalibrasi Manuver Dead-End 180&deg;:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Percobaan</th><th>Nilai <code>durasi180 (ms)</code></th><th>Sudut Putar yang Dihasilkan</th><th>Apakah Bodi Menyenggol Dinding Buntu?</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>800 ms</td><td>Kurang dari 180&deg; / Pas / Lebih</td><td>Ya / Tidak</td></tr>
                        <tr><td>2</td><td>860 ms</td><td>Kurang dari 180&deg; / Pas / Lebih</td><td>Ya / Tidak</td></tr>
                        <tr><td>3</td><td>....... ms (Nilai Terbaik)</td><td>Tepat 180&deg; (Lurus Keluar)</td><td>Tidak Menyenggol</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika saat berputar 180 derajat bagian belakang robot menyentuh dinding ujung buntu, itu tandanya robot berhenti terlalu dekat dengan dinding depan. Naikkan batas jarak berhenti depan dari 11 cm menjadi 13–14 cm."
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
            "theory": """
                <p>Motor kuning DC Gearbox TT yang digunakan pada robot edukasi tidak memiliki sensor penghitung putaran roda (<em>no encoder</em>). Akibat toleransi pabrik pada kumparan tembaga dan roda gigi plastik di dalamnya, ketika kita memberi nilai PWM yang sama (misal Kiri = 150, Kanan = 150), salah satu roda hampir pasti berputar sedikit lebih cepat!</p>
                <p>Untuk mengatasinya secara perangkat lunak, kita menambahkan konstanta kompensasi (<strong>Wheel Trim Offset</strong>) di bagian atas kode program kita, misalnya:</p>
                <div class="formula-box">
                    PWM_KIRI = baseSpeed + OFFSET_KIRI &nbsp;&nbsp;|&nbsp;&nbsp; PWM_KANAN = baseSpeed + OFFSET_KANAN
                </div>
            """,
            "safety": "Lakukan kalibrasi dengan kondisi baterai yang sudah terisi penuh agar nilai offset dan durasi belok akurat saat dipakai berlomba.",
            "steps": [
                "Letakkan robot di atas garis sambungan keramik lurus sepanjang 2 meter.",
                "Jalankan fungsi maju lurus selama 3 detik dengan <code>OFFSET_KIRI = 0</code> dan <code>OFFSET_KANAN = 0</code>.",
                "Jika robot melenceng ke Kanan (berarti roda Kiri lebih kencang), beri nilai <code>OFFSET_KANAN = +6</code> (atau <code>OFFSET_KIRI = -6</code>) lalu uji kembali hingga robot melaju lurus tepat di atas garis keramik!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-14: Parameter Kalibrasi Master (Wheel Trim & Turn Timing)
// =========================================================================

// --- UBAH KEEMPAT ANGKA KALIBRASI INI SESUAI KARAKTER ROBOT KELOMPOKMU ---
const int BASE_SPEED    = 145; // Kecepatan dasar jelajah (0-255)
const int OFFSET_KIRI   = 0;   // Tambahan/pengurangan PWM Roda Kiri (-20 s/d +20)
const int OFFSET_KANAN  = 6;   // Tambahan/pengurangan PWM Roda Kanan (-20 s/d +20)
const int DELAY_BELOK90 = 435; // Durasi milidetik putar tepat 90 derajat
const int DELAY_PUTAR180= 865; // Durasi milidetik putar balik 180 derajat

void majuTerkalibrasi(int koreksiDinding) {
  int pwmKiri  = BASE_SPEED + OFFSET_KIRI  + koreksiDinding;
  int pwmKanan = BASE_SPEED + OFFSET_KANAN - koreksiDinding;
  
  // Batasi agar nilai PWM tetap berada di rentang aman 0 - 255
  pwmKiri  = constrain(pwmKiri, 0, 255);
  pwmKanan = constrain(pwmKanan, 0, 255);

  setMotor(pwmKiri, 0, pwmKanan, 0);
}""",
            "lks": """
                <p><strong>Lembar Sertifikasi Kalibrasi Unit MazeBot SMP:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Parameter Konstanta</th><th>Nilai Awal (Default)</th><th>Hasil Kalibrasi Final Kelompok</th><th>Bukti Uji Fisik</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>OFFSET_KIRI</code></td><td>0</td><td>..................</td><td rowspan="2">Simpangan lurus 2 meter &lt; 3 cm</td></tr>
                        <tr><td><code>OFFSET_KANAN</code></td><td>0</td><td>..................</td></tr>
                        <tr><td><code>DELAY_BELOK90</code></td><td>450 ms</td><td>.................. ms</td><td>Sudut siku 90&deg; presisi</td></tr>
                        <tr><td><code>DELAY_PUTAR180</code></td><td>900 ms</td><td>.................. ms</td><td>Berbalik arah 180&deg; presisi</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Periksa juga apakah ban karet terpasang lurus pada velg kuning motor TT. Ban yang miring atau bergesekan dengan baut sasis adalah penyebab utama robot melenceng!"
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
            "theory": """
                <p>Bagaimana robot bisa menghitung sendiri berapa detik waktu yang ia butuhkan dari titik Start sampai menginjak Garis Finish? ESP32 memiliki fungsi pencatat waktu internal bernama <strong><code>millis()</code></strong> yang menghitung jumlah milidetik sejak robot dinyalakan.</p>
                <div class="formula-box">
                    Waktu Tempuh (Detik) = (millis() Saat Menyentuh Finish &minus; millis() Saat Start) / 1000.0
                </div>
                <p>Dengan mencatat <code>waktuStart = millis();</code> di akhir <code>setup()</code>, begitu sensor TCRT5000 mendeteksi garis hitam Finish, robot langsung menghitung dan mengirimkan catatan waktu resminya ke Serial Monitor / Web Dashboard!</p>
            """,
            "safety": "Pastikan seluruh dinding labirin terpasang sesuai peta standar kompetisi dan garis lakban hitam di titik Finish menempel rata di lantai.",
            "steps": [
                "Masukkan angka-angka hasil kalibrasi M-14 ke dalam kode integrasi penuh M-15 di bawah ini.",
                "Letakkan robot di titik Start labirin dan nyalakan saklar daya.",
                "Catat waktu tempuh yang berhasil dicapai robot dan identifikasi titik tikungan mana yang masih bisa diperhalus gerakannya!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-15: Integrasi Stopwatch Otomatis (millis) & Uji Labirin Lengkap
// =========================================================================
unsigned long waktuStart  = 0;
unsigned long waktuFinish = 0;
bool sudahFinish = false;

// Dipanggil di baris paling akhir void setup() tepat sebelum robot mulai jalan:
void mulaiStopwatch() {
  waktuStart = millis();
  Serial.println("[STOPWATCH] Waktu Dimulai! Robot Memasuki Labirin...");
}

// Dipanggil di dalam void loop() saat sensor TCRT5000 mendeteksi garis hitam:
void cekGarisFinishDanCatatWaktu(int pinFinish) {
  if (!sudahFinish && digitalRead(pinFinish) == HIGH) {
    setMotor(0, 0, 0, 0); // Rem darurat
    waktuFinish = millis();
    sudahFinish = true;

    float totalDetik = (waktuFinish - waktuStart) / 1000.0;
    Serial.println("==========================================");
    Serial.println("GARIS FINISH TERCAPAI!");
    Serial.print("Waktu Tempuh Resmi: ");
    Serial.print(totalDetik, 2);
    Serial.println(" detik");
    Serial.println("==========================================");
  }
}""",
            "lks": """
                <p><strong>Jurnal Uji Coba Labirin Lengkap (Simulasi Pra-Kompetisi):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Uji Coba</th><th>Apakah Berhasil Keluar dari Jalan Buntu?</th><th>Berhenti di Garis Finish?</th><th>Catatan Waktu Stopwatch (Detik)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Trial 1</td><td>Ya / Tidak</td><td>Ya / Tidak</td><td>.............. detik</td></tr>
                        <tr><td>Trial 2</td><td>Ya / Tidak</td><td>Ya / Tidak</td><td>.............. detik</td></tr>
                        <tr><td>Trial 3</td><td>Ya / Tidak</td><td>Ya / Tidak</td><td>.............. detik</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika sensor TCRT5000 tidak sengaja terpicu di tengah jalan karena sambungan nat keramik lantai yang berwarna gelap, atur sedikit trimpot TCRT5000 agar hanya merespon warna hitam pekat lakban."
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
            "theory": """
                <p>Selamat datang di puncak kurikulum tingkat SMP: <strong>Kompetisi Maze Solver Otonom SMP</strong>! Setiap tim akan menurunkan robot MazeBot terbaiknya untuk menaklukkan labirin resmi yang memiliki cabang pengecoh (jalan buntu), tikungan siku, dan lorong lurus hingga berhenti presisi di atas garis Finish hitam.</p>
                <p>Di bawah ini adalah <strong>Kode Master Lengkap (Full Production Code SMP)</strong> yang merangkum seluruh modul M-01 hingga M-15 dan siap digunakan dalam perlombaan!</p>
            """,
            "safety": "Selama putaran resmi kompetisi berlangsung, anggota tim tidak diperkenankan menyentuh robot kecuali meminta 'Retry' (ulang dari titik Start dengan waktu yang terus berjalan).",
            "steps": [
                "Pastikan nilai konstanta kalibrasi (<code>OFFSET_KIRI</code>, <code>OFFSET_KANAN</code>, <code>DELAY_BELOK90</code>, <code>DELAY_PUTAR180</code>) pada Kode Master M-16 sudah diisi sesuai robot timmu.",
                "Unggah kode ke robot dan lakukan pemeriksaan akhir baterai serta kebersihan roda karet.",
                "Saat dipanggil oleh Juri, letakkan robot di belakang garis Start dan nyalakan saklar saat peluit dibunyikan!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-16: MASTER CODE KOMPETISI MAZE SOLVER OTONOM SMP (FULL C++)
// =========================================================================
#define IN1 25
#define IN2 26
#define IN3 27
#define IN4 14
#define TRIG_KIRI  32
#define ECHO_KIRI  35
#define TRIG_DEPAN 33
#define ECHO_DEPAN 34
#define TRIG_KANAN 18
#define ECHO_KANAN 19
#define PIN_FINISH 4
#define PIN_LED    2

// --- PARAMETER KALIBRASI TIM ---
const int BASE_SPD       = 148;
const int OFFSET_KIRI    = 0;
const int OFFSET_KANAN   = 5;
const int DELAY_BELOK90  = 435;
const int DELAY_PUTAR180 = 865;

unsigned long startTime = 0;
bool finished = false;

float getDist(int trig, int echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10);
  digitalWrite(trig, LOW);
  long d = pulseIn(echo, HIGH, 25000);
  return (d == 0) ? 999.0 : (d * 0.034) / 2.0;
}

void drive(int L1, int L2, int R1, int R2) {
  analogWrite(IN1, constrain(L1, 0, 255)); analogWrite(IN2, constrain(L2, 0, 255));
  analogWrite(IN3, constrain(R1, 0, 255)); analogWrite(IN4, constrain(R2, 0, 255));
}

void setup() {
  Serial.begin(115200);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  pinMode(TRIG_KIRI, OUTPUT);  pinMode(ECHO_KIRI, INPUT);
  pinMode(TRIG_DEPAN, OUTPUT); pinMode(ECHO_DEPAN, INPUT);
  pinMode(TRIG_KANAN, OUTPUT); pinMode(ECHO_KANAN, INPUT);
  pinMode(PIN_FINISH, INPUT);  pinMode(PIN_LED, OUTPUT);
  drive(0, 0, 0, 0);
  delay(2000); // Jeda siap start
  startTime = millis();
}

void loop() {
  if (finished) { drive(0, 0, 0, 0); return; }

  // 1. Cek Garis Finish Hitam (TCRT5000)
  if (digitalRead(PIN_FINISH) == HIGH) {
    drive(0, 0, 0, 0);
    digitalWrite(PIN_LED, HIGH);
    finished = true;
    Serial.print("FINISH! Waktu: ");
    Serial.print((millis() - startTime) / 1000.0, 2);
    Serial.println(" dtk");
    return;
  }

  // 2. Baca 3 Sensor Ultrasonik dengan Jeda Anti-Crosstalk
  float kiri  = getDist(TRIG_KIRI, ECHO_KIRI);   delay(15);
  float depan = getDist(TRIG_DEPAN, ECHO_DEPAN); delay(15);
  float kanan = getDist(TRIG_KANAN, ECHO_KANAN); delay(15);

  // 3. Algoritma Navigasi Left-Hand Rule + Wall Offset
  if (kiri > 20.0) {
    drive(BASE_SPD + OFFSET_KIRI, 0, BASE_SPD + OFFSET_KANAN, 0); delay(240);
    drive(0, 0, 0, 0); delay(120);
    drive(0, 160, 160, 0); delay(DELAY_BELOK90);
    drive(0, 0, 0, 0); delay(120);
    drive(BASE_SPD + OFFSET_KIRI, 0, BASE_SPD + OFFSET_KANAN, 0); delay(380);
  }
  else if (depan > 12.0) {
    int kor = 0;
    if (kiri < 5.0) kor = 25;
    else if (kiri > 8.0 && kiri < 18.0) kor = -25;
    drive(BASE_SPD + OFFSET_KIRI + kor, 0, BASE_SPD + OFFSET_KANAN - kor, 0);
  }
  else if (kanan > 20.0) {
    drive(0, 0, 0, 0); delay(120);
    drive(160, 0, 0, 160); delay(DELAY_BELOK90);
    drive(0, 0, 0, 0); delay(120);
  }
  else {
    if (depan < 8.0) { drive(0, 145, 0, 145); delay(200); }
    drive(0, 0, 0, 0); delay(120);
    if (kanan >= kiri) drive(165, 0, 0, 165);
    else drive(0, 165, 165, 0);
    delay(DELAY_PUTAR180);
    drive(0, 0, 0, 0); delay(150);
  }
}""",
            "lks": """
                <p><strong>Rubrik Penilaian Resmi Kompetisi Maze Solver Otonom SMP:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Kriteria Penilaian</th><th>Bobot</th><th>Indikator Capaian</th><th>Skor Tim (0–100)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>1. Penguasaan Kode C++ &amp; Kalibrasi</strong></td><td>25%</td><td>Kode terstruktur modular, parameter kalibrasi dipahami</td><td>.............</td></tr>
                        <tr><td><strong>2. Navigasi Persimpangan &amp; Jalan Buntu</strong></td><td>30%</td><td>Berhasil keluar dari jebakan jalan buntu (Left-Hand Rule)</td><td>.............</td></tr>
                        <tr><td><strong>3. Ketepatan Berhenti di Garis Finish</strong></td><td>25%</td><td>Sensor TCRT5000 mengunci penghentian tepat di garis hitam</td><td>.............</td></tr>
                        <tr><td><strong>4. Waktu Tempuh &amp; Minim Tabrakan</strong></td><td>20%</td><td>Menyelesaikan labirin dengan cepat &amp; minim sentuhan dinding</td><td>.............</td></tr>
                        <tr><td colspan="3"><strong>TOTAL NILAI AKHIR SEMESTER (TINGKAT SMP)</strong></td><td><strong>............. / 100</strong></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Berikan penghargaan khusus untuk kategori 'Best Code Architecture', 'Fastest Time', dan 'Most Smooth Wall-Follower' agar seluruh siswa termotivasi!"
        }
    ]

def generate_smp_html():
    modules = get_smp_modules()
    toc_rows = ""
    for m in modules:
        toc_rows += f"""
        <tr>
            <td class="toc-code">{m['code']}</td>
            <td><strong>{m['title']}</strong></td>
            <td>{m['duration']}</td>
            <td>Arduino C++ / ESP32</td>
        </tr>
        """

    modules_html = ""
    for m in modules:
        objectives_li = "".join([f"<li>{obj}</li>" for obj in m["objectives"]])
        steps_li = "".join([f'<li><span class="step-num">{i+1}</span>{s}</li>' for i, s in enumerate(m["steps"])])
        escaped_code = html_lib.escape(m["cpp_code"])

        modules_html += f"""
        <div class="module-page" id="{m['code']}">
            <div class="module-banner">
                <div class="module-banner-left">
                    <span class="mod-code">MODUL {m['code']} &bull; KURIKULUM SMP (KELAS 8–9)</span>
                    <h2>{m['title']}</h2>
                </div>
                <div class="module-banner-right">
                    <div><strong>Alokasi:</strong> {m['duration']}</div>
                    <div><strong>Fase:</strong> {m['phase']}</div>
                    <div><strong>Bahasa:</strong> C++ Arduino</div>
                </div>
            </div>

            <div class="card">
                <h3>🎯 Target Kemampuan &amp; Capaian Pembelajaran</h3>
                <ul>{objectives_li}</ul>
            </div>

            <div class="alert alert-info">
                <span class="alert-title">⚡ Standar Keselamatan Laboratorium &amp; Perangkat Keras</span>
                {m['safety']}
            </div>

            <h3 class="sub-heading">📖 A. Konsep Kunci &amp; Landasan Teori (STEM / Fisika / Komputasi)</h3>
            {m['theory']}

            <h3 class="sub-heading">🛠️ B. Prosedur Praktikum &amp; Eksperimen</h3>
            <ul class="steps-list">
                {steps_li}
            </ul>

            <h3 class="sub-heading">💻 C. Kode Program Lengkap (Arduino C++ ESP32)</h3>
            <div class="code-box">
                <div class="code-header">
                    <span>📄 MazeBot_{m['code']}_SMP.ino</span>
                    <span>Board: DOIT ESP32 DEVKIT V1 | Baud: 115200</span>
                </div>
                <pre>{escaped_code}</pre>
            </div>

            <div class="lks-box">
                <div class="lks-header">
                    <span>📝 D. Lembar Kerja Siswa (LKS) — {m['code']}</span>
                    <span>Kelompok / Kelas: ..............................</span>
                </div>
                {m['lks']}
            </div>

            <div class="alert alert-warning">
                <span class="alert-title">🔧 Panduan Guru: Troubleshooting &amp; Catatan Kalibrasi</span>
                {m['troubleshooting']}
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Modul Ajar MazeBot EduKit - Tingkat SMP (Kelas 8-9)</title>
    <link rel="stylesheet" href="css/modul_style.css">
</head>
<body class="theme-smp">

    <!-- COVER PAGE -->
    <div class="cover-page">
        <div>
            <span class="cover-badge">Kurikulum Robotika &amp; Pemrograman STEM Nasional</span>
            <div class="cover-title">MODUL AJAR &amp; PRAKTIKUM<br>MAZEBOT EDUKIT</div>
            <div class="cover-subtitle">📙 TINGKAT SMP (Target: Kelas 8–9)<br>"Logika Pemrograman C++ &amp; Navigasi Robot Otonom"</div>
            <div class="cover-divider"></div>

            <div class="cover-highlights">
                <h3>Spesifikasi Pedagogis &amp; Teknis Hardware SMP</h3>
                <ul>
                    <li><strong>Transisi Mulus (Hybrid Block-to-Text):</strong> Dilengkapi modul jembatan Side-by-Side Code Viewer sebelum masuk ke pemrograman C++ di Arduino IDE.</li>
                    <li><strong>Integrasi Kurikulum IPA Fisika Kelas 8:</strong> Implementasi rumus pemantulan gelombang bunyi (<em>s = v &times; t / 2</em> dengan cepat rambat bunyi 340 m/s) secara nyata pada sensor ultrasonik.</li>
                    <li><strong>Arsitektur Hardware Modular:</strong> Fokus pada fungsi modul ESP32, Driver DRV8833, 3x Sensor Ultrasonik HC-SR04 (Anti-Crosstalk), dan Sensor Garis TCRT5000.</li>
                    <li><strong>Algoritma Wall-Follower &amp; Kalibrasi Nyata:</strong> Mencakup <em>Left-Hand Rule</em>, <em>Wall Offset</em>, <em>Dead-End U-Turn</em>, serta sesi khusus kompensasi deviasi motor DC TT.</li>
                </ul>
            </div>
        </div>

        <div class="cover-footer">
            <div>
                <strong>Edisi Revisi Total Kurikulum MazeBot EduKit</strong><br>
                Lengkap dengan Source Code Arduino C++, LKS Eksperimen, &amp; Rubrik Kompetisi
            </div>
            <div style="text-align: right;">
                <strong>Kode Dokumen:</strong> EDU-MB-SMP-2026<br>
                <strong>Total Modul:</strong> 16 Pertemuan (M-01 – M-16)
            </div>
        </div>
    </div>

    <!-- FRONTMATTER: PINOUT & TOC -->
    <div class="page-break">
        <div class="section-header">
            <h1>Standar Pemetaan Pinout Hardware &amp; Daftar Isi</h1>
            <p>Buku Pegangan Terpadu Guru &amp; Siswa — Tingkat Sekolah Menengah Pertama (Kelas 8–9)</p>
        </div>

        <h3 class="sub-heading">🔌 Tabel Standar Pemetaan Pin (Pinout) MazeBot EduKit ESP32</h3>
        <table class="std-table">
            <thead>
                <tr>
                    <th>Modul Perangkat Keras</th>
                    <th>Nama Pin Modul</th>
                    <th>Pin GPIO ESP32</th>
                    <th>Keterangan Arah &amp; Fungsi</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Driver Motor DRV8833</strong></td><td>IN1, IN2 (Motor Kiri)</td><td>GPIO 25, GPIO 26</td><td>OUTPUT PWM (0–255) Penggerak Roda Kiri</td></tr>
                <tr><td><strong>Driver Motor DRV8833</strong></td><td>IN3, IN4 (Motor Kanan)</td><td>GPIO 27, GPIO 14</td><td>OUTPUT PWM (0–255) Penggerak Roda Kanan</td></tr>
                <tr><td><strong>Ultrasonik KIRI</strong></td><td>TRIG / ECHO</td><td>GPIO 32 / GPIO 35</td><td>OUTPUT Trigger / INPUT Echo Sisi Kiri</td></tr>
                <tr><td><strong>Ultrasonik DEPAN</strong></td><td>TRIG / ECHO</td><td>GPIO 33 / GPIO 34</td><td>OUTPUT Trigger / INPUT Echo Sisi Depan</td></tr>
                <tr><td><strong>Ultrasonik KANAN</strong></td><td>TRIG / ECHO</td><td>GPIO 18 / GPIO 19</td><td>OUTPUT Trigger / INPUT Echo Sisi Kanan</td></tr>
                <tr><td><strong>Sensor Garis TCRT5000</strong></td><td>DO (Digital Out)</td><td>GPIO 4</td><td>INPUT Digital Detektor Garis Finish Hitam</td></tr>
                <tr><td><strong>Indikator Internal</strong></td><td>LED Built-in</td><td>GPIO 2</td><td>OUTPUT Indikator Status Robot</td></tr>
            </tbody>
        </table>

        <h3 class="sub-heading">📋 Daftar Isi Kurikulum Tingkat SMP (M-01 s/d M-16)</h3>
        <table class="toc-table">
            <thead>
                <tr>
                    <th style="width: 10%;">Kode</th>
                    <th style="width: 50%;">Topik Materi Modul</th>
                    <th style="width: 18%;">Alokasi Waktu</th>
                    <th style="width: 22%;">Fokus Kompetensi</th>
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
    out_path = os.path.join(os.path.dirname(__file__), "Modul_Ajar_MazeBot_SMP.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated SMP HTML at: {out_path}")

if __name__ == "__main__":
    generate_smp_html()
