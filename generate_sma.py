import os
import html as html_lib

def get_sma_modules():
    return [
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
            "theory": """
                <p>Pada tingkat SMA/SMK, fokus utama pembelajaran adalah <strong>Algoritma Komputasi Navigasi, Struktur Data Array, dan Optimasi Jalur Terpendek (Shortest Path)</strong>. Oleh sebab itu, fungsi komunikasi Wi-Fi SoftAP dan WebSocket Web Server telah dibungkus di dalam pustaka siap pakai <code>MazeBotStarter.h</code>.</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Fungsi Starter API</th><th>Nilai Kembalian / Parameter</th><th>Deskripsi Fungsi</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>bot.begin("MazeBot-SMA-01")</code></td><td><code>void</code> (SSID String)</td><td>Menginisialisasi pin GPIO, PWM DRV8833, sensor, dan Wi-Fi Web Server.</td></tr>
                        <tr><td><code>bot.readLeft() / Front() / Right()</code></td><td><code>float</code> (cm)</td><td>Membaca jarak 3 sensor ultrasonik dengan proteksi anti-crosstalk otomatis.</td></tr>
                        <tr><td><code>bot.isFinishLine()</code></td><td><code>bool</code> (true/false)</td><td>Membaca sensor bawah TCRT5000 (<code>true</code> jika mendeteksi garis hitam Finish).</td></tr>
                        <tr><td><code>bot.drive(pwmKiri, pwmKanan)</code></td><td><code>int</code> (-255 s/d 255)</td><td>Menggerakkan motor kiri &amp; kanan (nilai negatif = putar mundur).</td></tr>
                    </tbody>
                </table>
            """,
            "safety": "Pastikan prasyarat dasar C++ (variabel, fungsi, percabangan) telah dikuasai dan pustaka MazeBotStarter.h berada di dalam satu folder yang sama dengan file .ino utama.",
            "steps": [
                "Buka folder <code>MazeBot_SMA_Starter</code> pada Arduino IDE dan amati deklarasi fungsi pada tab <code>MazeBotStarter.h</code>.",
                "Panggil fungsi inisialisasi <code>bot.begin(\"MazeBot-SMA-01\");</code> di dalam <code>void setup()</code>.",
                "Unggah kode M-01 dan pastikan nilai ketiga sensor jarak serta status garis finish tampil akurat di Serial Monitor."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-01: Arsitektur Starter Code Platform MazeBot SMA/SMK
// =========================================================================
#include "MazeBotStarter.h"

MazeBotCore bot;

void setup() {
  Serial.begin(115200);
  bot.begin("MazeBot-SMA-01"); // Inisialisasi Hardware & Pre-built Web Server
  Serial.println("[SYSTEM] Starter Platform MazeBot SMA Siap!");
}

void loop() {
  bot.updateWeb(); // Menjaga komunikasi background Web Dashboard

  float L = bot.readLeft();
  float F = bot.readFront();
  float R = bot.readRight();
  bool fin = bot.isFinishLine();

  Serial.printf("L: %.1f cm | F: %.1f cm | R: %.1f cm | Finish: %s\\n",
                L, F, R, fin ? "HITAM (YA)" : "PUTIH (TIDAK)");
  delay(200);
}""",
            "lks": """
                <p><strong>Lembar Eksplorasi API Starter Code:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>Perintah yang Diinginkan</th><th>Pemanggilan Fungsi API <code>bot</code> yang Tepat</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Maju lurus dengan PWM 150 di kedua roda</td><td><code>bot.drive(........, ........);</code></td></tr>
                        <tr><td>2</td><td>Berputar poros ke kanan (Pivot Right) dengan PWM 160</td><td><code>bot.drive(........, ........);</code></td></tr>
                        <tr><td>3</td><td>Berhenti mengunci roda</td><td><code>bot.drive(........, ........);</code></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Dengan nilai parameter negatif pada bot.drive(160, -160), fungsi secara otomatis mengaktifkan pin mundur pada DRV8833 untuk roda kanan."
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
            "theory": """
                <p>Pada tingkat SMP, koreksi dinding hanya menggunakan sistem biner (jika terlalu dekat koreksi sekian, jika terlalu jauh koreksi sekian). Di tingkat SMA/SMK, kita menerapkan <strong>Closed-Loop Proportional Correction</strong> berbasis umpan balik sensor ultrasonik samping:</p>
                <div class="formula-box">
                    error = TARGET_DINDING &minus; jarakKiri &nbsp;&nbsp;|&nbsp;&nbsp; koreksiPWM = constrain(Kp &times; error, &minus;MAX_CORR, +MAX_CORR)
                </div>
                <p>Semakin besar penyimpangan posisi robot dari jarak target (6.5 cm), semakin kuat pula koreksi setir yang diberikan. Sebaliknya, jika penyimpangan hanya 0.5 cm, koreksi PWM yang diberikan sangat lembut sehingga robot meluncur mulus di tengah lorong!</p>
            """,
            "safety": "Batasi nilai koreksi maksimum (MAX_CORR) sekitar 35–40 PWM agar salah satu roda tidak berhenti mendadak saat melaju di lorong lurus.",
            "steps": [
                "Implementasikan fungsi <code>majuClosedLoop(float jarakKiri)</code> dengan konstanta <code>TARGET_WALL = 6.5</code> cm dan <code>Kp = 8.0</code>.",
                "Hanya aktifkan koreksi dinding ketika dinding kiri benar-benar ada (<code>jarakKiri &lt; 15.0 cm</code>). Jika dinding kiri hilang (persimpangan), matikan koreksi (<code>koreksi = 0</code>).",
                "Uji pada lorong lurus sepanjang 2 meter dan amati kemulusan lintasan dibanding metode biner."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-02: Closed-Loop Proportional Wall Correction
// =========================================================================
const float TARGET_WALL = 6.5;  // Jarak ideal dari dinding kiri (cm)
const float KP_WALL     = 8.0;  // Konstanta penguat proporsional
const int   BASE_PWM    = 150;  // Kecepatan dasar
const int   MAX_CORR    = 35;   // Batas maksimum koreksi PWM

void majuClosedLoop(float jarakKiri) {
  int koreksi = 0;

  // Hanya lakukan koreksi jika dinding samping kiri terdeteksi (< 15 cm)
  if (jarakKiri < 15.0) {
    float error = TARGET_WALL - jarakKiri; // Positif jika terlalu dekat dinding kiri
    koreksi = (int)(KP_WALL * error);
    koreksi = constrain(koreksi, -MAX_CORR, MAX_CORR);
  }

  // Jika terlalu dekat kiri (error > 0), roda kiri dipercepat & kanan diperlambat
  int pwmKiri  = BASE_PWM + koreksi;
  int pwmKanan = BASE_PWM - koreksi;

  bot.drive(pwmKiri, pwmKanan);
}""",
            "lks": """
                <p><strong>Analisis Perhitungan Closed-Loop Correction (Target = 6.5 cm, Kp = 8.0):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Jarak Kiri Aktual</th><th>Nilai <code>error (6.5 - aktual)</code></th><th>Nilai <code>koreksi (Kp &times; error)</code></th><th>PWM Kiri &amp; Kanan (Base 150)</th><th>Arah Koreksi Robot</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>4.5 cm (Terlalu dekat)</td><td>+2.0 cm</td><td>+16</td><td>Kiri: 166 | Kanan: 134</td><td>Menjauh ke Kanan</td></tr>
                        <tr><td>6.5 cm (Tepat di target)</td><td>0.0 cm</td><td>0</td><td>Kiri: 150 | Kanan: 150</td><td>Lurus Sempurna</td></tr>
                        <tr><td>9.0 cm (Agak menjauh)</td><td>-2.5 cm</td><td>-20</td><td>Kiri: 130 | Kanan: 170</td><td>Mendekat ke Kiri</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika robot terlihat bergoyang kiri-kanan terus menerus (osilasi), turunkan nilai KP_WALL dari 8.0 menjadi 5.0 atau 6.0."
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
            "theory": """
                <p>Sesuai arsitektur perangkat keras MazeBot EduKit, deteksi persimpangan dilakukan <strong>100% menggunakan kombinasi 3x Sensor Ultrasonik</strong> (sedangkan sensor TCRT5000 dikhususkan murni untuk Garis Finish). Sebuah sisi dinyatakan <strong>Terbuka (Open)</strong> apabila jarak ultrasonik melebihi ambang <code>OPEN_THRES = 16.0 cm</code>:</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Status Kiri (&gt;16cm)</th><th>Status Depan (&gt;14cm)</th><th>Status Kanan (&gt;16cm)</th><th>Klasifikasi Persimpangan</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Tertutup</td><td>Terbuka</td><td>Tertutup</td><td><code>CORRIDOR</code> (Lorong Lurus Biasa)</td></tr>
                        <tr><td>Terbuka</td><td>Tertutup</td><td>Tertutup</td><td><code>LEFT_CORNER</code> (Tikungan/Simpang Kiri)</td></tr>
                        <tr><td>Tertutup</td><td>Tertutup</td><td>Terbuka</td><td><code>RIGHT_CORNER</code> (Tikungan/Simpang Kanan)</td></tr>
                        <tr><td>Terbuka</td><td>Terbuka</td><td>Tertutup</td><td><code>T_LEFT</code> (Simpang Tiga Cabang Kiri-Depan)</td></tr>
                        <tr><td>Tertutup</td><td>Terbuka</td><td>Terbuka</td><td><code>T_RIGHT</code> (Simpang Tiga Cabang Depan-Kanan)</td></tr>
                        <tr><td>Terbuka</td><td>Tertutup</td><td>Terbuka</td><td><code>T_JUNCTION</code> (Pertigaan Huruf T)</td></tr>
                        <tr><td>Terbuka</td><td>Terbuka</td><td>Terbuka</td><td><code>CROSSROAD</code> (Simpang Empat +)</td></tr>
                        <tr><td>Tertutup</td><td>Tertutup</td><td>Tertutup</td><td><code>DEAD_END</code> (Jalan Buntu)</td></tr>
                    </tbody>
                </table>
            """,
            "safety": "Pastikan ambang jarak bukaan samping (16.0 cm) disesuaikan dengan lebar lorong labirin sekolah (umumnya lebar lorong standar adalah 20–25 cm).",
            "steps": [
                "Ketikkan fungsi klasifikasi <code>klasifikasiSimpang(float L, float F, float R)</code> pada Arduino IDE.",
                "Tempatkan robot secara manual di 5 titik berbeda di dalam labirin (lorong lurus, tikungan L, pertigaan T, perempatan +, dan jalan buntu).",
                "Catat hasil klasifikasi yang dicetak pada Serial Monitor dan pastikan akurasinya 100% tepat!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-03: Klasifikasi Persimpangan Berbasis 3x Sensor Ultrasonik
// =========================================================================
const float SIDE_OPEN_THRES  = 16.0; // Sisi kiri/kanan terbuka jika > 16 cm
const float FRONT_OPEN_THRES = 14.0; // Sisi depan terbuka jika > 14 cm

String klasifikasiSimpang(float L, float F, float R) {
  bool openL = (L > SIDE_OPEN_THRES);
  bool openF = (F > FRONT_OPEN_THRES);
  bool openR = (R > SIDE_OPEN_THRES);

  if (openL && openF && openR)  return "CROSSROAD (+)";
  if (openL && !openF && openR) return "T_JUNCTION (T)";
  if (openL && openF && !openR) return "T_LEFT (Simpang Kiri-Lurus)";
  if (!openL && openF && openR) return "T_RIGHT (Simpang Lurus-Kanan)";
  if (openL && !openF && !openR) return "LEFT_TURN (Belokan Kiri)";
  if (!openL && !openF && openR) return "RIGHT_TURN (Belokan Kanan)";
  if (!openL && !openF && !openR) return "DEAD_END (Jalan Buntu)";
  return "CORRIDOR (Lorong Lurus)";
}""",
            "lks": """
                <p><strong>Verifikasi Klasifikasi Persimpangan Ultrasonik:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Lokasi Uji Robot</th><th>Bacaan (L, F, R) cm</th><th>Status Boolean (openL, openF, openR)</th><th>Output Klasifikasi</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Pertigaan T</td><td>L:.... | F:.... | R:....</td><td>( true , false , true )</td><td>............................</td></tr>
                        <tr><td>Simpang Kiri-Lurus</td><td>L:.... | F:.... | R:....</td><td>( ..... , ..... , ..... )</td><td>............................</td></tr>
                        <tr><td>Jalan Buntu</td><td>L:.... | F:.... | R:....</td><td>( ..... , ..... , ..... )</td><td>............................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Saat robot baru saja mendekati bibir simpang, sensor samping mungkin membaca nilai peralihan. Modul M-04 berikutnya akan membahas cara menstabilkan pembacaan tepat di titik tengah simpang!"
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
            "theory": """
                <p>Mengapa robot sering salah mengambil keputusan jika langsung berbelok saat melaju kencang? Karena ketika sensor kiri baru menyentuh tepi bukaan simpang, sensor kanan mungkin belum sejajar dengan bukaan kanan! Solusi rekayasa perangkat lunaknya adalah <strong>Intersection State Stabilization</strong>:</p>
                <ol>
                    <li><strong>Trigger Awal:</strong> Saat berada di lorong, jika <code>L &gt; 16 cm</code> ATAU <code>R &gt; 16 cm</code> ATAU <code>F &lt; 13 cm</code>, tandai bahwa robot memasuki <em>Zona Persimpangan</em>.</li>
                    <li><strong>Centering &amp; Stop:</strong> Maju perlahan selama <code>220 ms</code> (jika depan masih longgar) agar sumbu roda tepat berada di pusat persimpangan, lalu <strong>Berhenti Penuh selama 150 ms</strong>.</li>
                    <li><strong>Stable Re-Scan:</strong> Dalam keadaan diam di pusat simpang, baca ulang ketiga sensor (Kiri, Depan, Kanan) untuk menghasilkan keputusan yang 100% akurat!</li>
                </ol>
            """,
            "safety": "Pastikan dorongan maju centering (220 ms) hanya dijalankan apabila jarak depan masih > 11 cm agar robot tidak menabrak dinding depan pertigaan T.",
            "steps": [
                "Implementasikan fungsi <code>ambilKeputusanSimpangStabil()</code> seperti pada kode M-04 di bawah.",
                "Uji robot melewati pertigaan T dan perempatan (+). Perhatikan bagaimana robot berhenti sejenak dengan anggun di tengah simpang sebelum berbelok!",
                "Bandingkan kestabilan belokannya dengan gerakan tanpa jeda berhenti."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-04: Intersection State (Stop, Stabilize, Re-Scan, & Execute)
// =========================================================================

char ambilKeputusanSimpangStabil() {
  // 1. Jika terdeteksi bukaan samping dan depan masih aman, maju ke pusat simpang
  float fAwal = bot.readFront();
  if (fAwal > 12.0) {
    bot.drive(140, 140);
    delay(220); // Centering roda di tengah persimpangan
  }

  // 2. Berhenti sejenak agar getaran bodi hilang & pembacaan ultrasonik stabil
  bot.drive(0, 0);
  delay(150);

  // 3. Re-Scan 3 sensor dalam posisi robot diam sempurna
  float L = bot.readLeft();
  float F = bot.readFront();
  float R = bot.readRight();

  // 4. Evaluasi keputusan berdasarkan aturan Left-Hand Rule:
  if (L > 16.0) {
    bot.turnLeft90();
    bot.drive(145, 145); delay(350); // Keluar dari zona simpang
    return 'L'; // Left
  }
  else if (F > 13.0) {
    bot.drive(145, 145); delay(350); // Lurus melewati simpang
    return 'S'; // Straight
  }
  else if (R > 16.0) {
    bot.turnRight90();
    bot.drive(145, 145); delay(350);
    return 'R'; // Right
  }
  else {
    bot.turnAround180();
    return 'U'; // U-Turn (Buntu)
  }
}""",
            "lks": """
                <p><strong>Analisis State Persimpangan Stabil:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Tahapan State</th><th>Aksi Fisik Robot</th><th>Tujuan Teknis</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1. Centering (220 ms)</td><td>Maju ke tengah simpang</td><td>Agar poros roda tepat di tengah jalur belokan</td></tr>
                        <tr><td>2. Stop &amp; Re-Scan (150 ms)</td><td>Berhenti &amp; baca ulang 3 sensor</td><td>..........................................................</td></tr>
                        <tr><td>3. Step-Out (350 ms)</td><td>Maju masuk ke lorong baru</td><td>..........................................................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Perhatikan bahwa fungsi ambilKeputusanSimpangStabil() mengembalikan satu karakter ('L', 'S', 'R', atau 'U'). Karakter inilah yang nantinya akan kita simpan ke dalam Array pada Modul M-09!"
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
            "theory": """
                <p>Dalam arsitektur perangkat lunak MazeBot SMA/SMK, sensor bawah <strong>TCRT5000</strong> berperan sebagai pemicu transisi fase utama. Ketika <code>bot.isFinishLine() == true</code> terdeteksi saat penjelajahan:</p>
                <ol>
                    <li>Robot langsung menghentikan kedua motor (<code>bot.drive(0, 0)</code>).</li>
                    <li>State sistem berpindah dari <code>STATE_EXPLORE</code> menjadi <code>STATE_FINISH_COMPUTE</code>.</li>
                    <li>Otak ESP32 langsung mengeksekusi algoritma pemangkasan jalan buntu (<em>Path Simplification</em>) dan bersiap untuk fase <em>Speed Run</em>!</li>
                </ol>
            """,
            "safety": "Pengecekan bot.isFinishLine() wajib diletakkan di baris paling atas di dalam void loop() agar memiliki prioritas interupsi tertinggi dibanding pembacaan ultrasonik.",
            "steps": [
                "Buat struktur <code>enum RobotState { STATE_EXPLORE, STATE_FINISH_COMPUTE, STATE_DONE };</code>.",
                "Pasang pengecekan <code>if (bot.isFinishLine())</code> di awal state <code>STATE_EXPLORE</code>.",
                "Uji transisi state tersebut dengan menjalankan robot melewati satu persimpangan menuju lakban hitam Finish."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-05: State Machine Utama & Trigger Garis Finish TCRT5000
// =========================================================================
enum RobotState {
  STATE_EXPLORE,
  STATE_FINISH_COMPUTE,
  STATE_DONE
};

RobotState currentState = STATE_EXPLORE;

void loop() {
  bot.updateWeb();

  switch (currentState) {
    case STATE_EXPLORE:
      // Prioritas Tertinggi: Cek apakah sensor bawah TCRT5000 menyentuh Garis Finish
      if (bot.isFinishLine()) {
        bot.drive(0, 0);
        Serial.println("[FINISH] Garis Hitam Terdeteksi! Memulai Komputasi Rute...");
        currentState = STATE_FINISH_COMPUTE;
        break;
      }
      // Lanjutkan navigasi lorong & persimpangan
      jalankanNavigasiEksplorasi();
      break;

    case STATE_FINISH_COMPUTE:
      // Panggil mesin pemangkas jalan buntu (akan dilengkapi di M-12)
      pangkasRuteJalanBuntu();
      currentState = STATE_DONE;
      break;

    case STATE_DONE:
      bot.drive(0, 0); // Siap diangkat kembali ke garis Start untuk Speed Run
      break;
  }
}""",
            "lks": """
                <p><strong>Diagram Alir Transisi State (Finite State Machine Sederhana):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>State Saat Ini</th><th>Pemicu (Trigger Event)</th><th>State Berikutnya</th><th>Aksi Robot</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>STATE_EXPLORE</code></td><td><code>bot.isFinishLine() == false</code></td><td>Tetap <code>STATE_EXPLORE</code></td><td>Menyusuri labirin</td></tr>
                        <tr><td><code>STATE_EXPLORE</code></td><td><code>bot.isFinishLine() == true</code></td><td><code>STATE_FINISH_COMPUTE</code></td><td>Rem motor &amp; hitung rute</td></tr>
                        <tr><td><code>STATE_FINISH_COMPUTE</code></td><td>Komputasi array selesai</td><td><code>STATE_DONE</code></td><td>Tampilkan rute optimal</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Pastikan lakban hitam Finish dipasang melintang penuh selebar lorong labirin (20–25 cm) agar dari sudut mana pun robot masuk ke kotak Finish, sensor TCRT5000 pasti melintasinya."
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
            "theory": """
                <p>Saat robot bergerak di dalam labirin, kabel USB tentu sudah dilepas sehingga kita tidak bisa melihat Serial Monitor melalui kabel! Sebagai gantinya, Starter Platform menyediakan API <strong>WebSocket Telemetry</strong>: <code>bot.sendTelemetry(L, F, R, status)</code>.</p>
                <p>Agar pengiriman paket Wi-Fi tidak menghambat respons motor, kita tidak memanggil fungsi ini di setiap milidetik, melainkan menggunakan <strong>Non-Blocking Timer (<code>millis() - lastTel &gt;= 200</code>)</strong> sehingga data dikirim cukup 5 kali per detik.</p>
            """,
            "safety": "Hindari penggunaan delay() panjang saat mengirim telemetri; gunakan pola perbandingan millis() seperti pada contoh kode di bawah.",
            "steps": [
                "Hubungkan laptop/HP ke Wi-Fi robot dan buka halaman Web Dashboard (<code>http://192.168.4.1</code>).",
                "Tambahkan blok pengiriman telemetri berkala menggunakan <code>millis()</code> di dalam program navigasimu.",
                "Jalankan robot di labirin dan amati grafik jarak Kiri, Depan, Kanan serta teks keputusan persimpangan yang berubah secara langsung di layar browser!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-06: Integrasi Telemetri Web Dashboard dengan Non-Blocking Timer
// =========================================================================
unsigned long lastTelemetryTime = 0;

void kirimTelemetriBerkala(float L, float F, float R, String status) {
  // Kirim data ke Web Dashboard setiap 200 milidetik (5 Hz) tanpa delay()
  if (millis() - lastTelemetryTime >= 200) {
    lastTelemetryTime = millis();
    bot.sendTelemetry(L, F, R, status);
  }
}

// Contoh pemakaian di dalam loop navigasi:
void loop() {
  bot.updateWeb();
  float L = bot.readLeft();
  float F = bot.readFront();
  float R = bot.readRight();

  String tipe = klasifikasiSimpang(L, F, R);
  kirimTelemetriBerkala(L, F, R, tipe);
}""",
            "lks": """
                <p><strong>Pengamatan Telemetri Nirkabel Web Dashboard:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Posisi Fisik Robot di Arena</th><th>Nilai (L / F / R) di Web</th><th>Teks Status di Web Dashboard</th><th>Delay Tampilan (Real-time?)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Di Lorong Lurus</td><td>.... / .... / .... cm</td><td><code>CORRIDOR (Lorong Lurus)</code></td><td>Real-time (&lt; 0.2 dtk)</td></tr>
                        <tr><td>Di Persimpangan T</td><td>.... / .... / .... cm</td><td><code>T_JUNCTION (T)</code></td><td>Real-time (&lt; 0.2 dtk)</td></tr>
                        <tr><td>Di Atas Garis Hitam</td><td>.... / .... / .... cm</td><td><code>FINISH LINE REACHED!</code></td><td>Real-time (&lt; 0.2 dtk)</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Selain mengirim berkala setiap 200 ms, panggil juga bot.sendTelemetry() secara langsung tepat ketika robot mengambil keputusan belok di persimpangan agar momen belokan langsung tercatat di log web."
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
            "theory": """
                <p>Jika kita menyimpan angka kalibrasi hanya pada variabel biasa di RAM, setiap kali baterai dilepas atau saklar dimatikan, perubahan nilai tuning dari Web Dashboard akan hilang kembali ke angka awal! ESP32 menyediakan fitur <strong>NVS (Non-Volatile Storage)</strong> melalui library resmi <code>&lt;Preferences.h&gt;</code> yang menyimpan data di memori Flash layaknya <em>harddisk</em> kecil:</p>
                <ul>
                    <li><code>prefs.begin("mazebot_cfg", false);</code> &rarr; Membuka ruang penyimpanan bernama <code>"mazebot_cfg"</code>.</li>
                    <li><code>prefs.putInt("turn90", 435);</code> &rarr; Menyimpan angka <code>435</code> secara permanen ke Flash.</li>
                    <li><code>prefs.getInt("turn90", 440);</code> &rarr; Membaca angka dari Flash (jika belum pernah disimpan, gunakan angka default <code>440</code>).</li>
                </ul>
            """,
            "safety": "Jangan memanggil fungsi prefs.putInt() di dalam void loop() yang berulang ribuan kali per detik karena memori Flash memiliki batas usia tulis (~100.000 kali tulis). Panggil putInt() hanya saat tombol 'Simpan Kalibrasi' ditekan!",
            "steps": [
                "Sertakan header <code>#include &lt;Preferences.h&gt;</code> di bagian atas program.",
                "Buat fungsi <code>muatKalibrasiDariFlash()</code> yang dipanggil di dalam <code>void setup()</code>.",
                "Ubah nilai kalibrasi, matikan saklar baterai robot selama 10 detik, lalu nyalakan kembali dan buktikan bahwa nilai kalibrasi tetap tersimpan!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-07: Penyimpanan Parameter Kalibrasi Permanen dengan Preferences.h
// =========================================================================
#include <Preferences.h>

Preferences prefs;

int   calBaseSpeed  = 150;
int   calTurn90Ms   = 440;
float calTargetWall = 6.5;

void muatKalibrasiDariFlash() {
  prefs.begin("mazebot_cfg", true); // Mode Read-Only (true)
  calBaseSpeed  = prefs.getInt("baseSpd", 150);
  calTurn90Ms   = prefs.getInt("turn90",  440);
  calTargetWall = prefs.getFloat("wallCm", 6.5);
  prefs.end();

  Serial.printf("[NVS] Kalibrasi Dimuat -> Spd:%d | Turn90:%d ms | Wall:%.1f cm\\n",
                calBaseSpeed, calTurn90Ms, calTargetWall);
}

void simpanKalibrasiKeFlash(int spdBaru, int turnBaru, float wallBaru) {
  prefs.begin("mazebot_cfg", false); // Mode Read-Write (false)
  prefs.putInt("baseSpd", spdBaru);
  prefs.putInt("turn90",  turnBaru);
  prefs.putFloat("wallCm", wallBaru);
  prefs.end();

  calBaseSpeed = spdBaru; calTurn90Ms = turnBaru; calTargetWall = wallBaru;
  Serial.println("[NVS] Parameter Kalibrasi Berhasil Disimpan Permanen ke Flash!");
}""",
            "lks": """
                <p><strong>Uji Ketahanan Memori Non-Volatile Storage (NVS):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Key NVS</th><th>Nilai Default Awal</th><th>Nilai Baru yang Disimpan</th><th>Nilai Saat Robot Dimatikan &amp; Dinyalakan Lagi</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>"baseSpd"</code></td><td>150</td><td>158</td><td>.................. (Tetap Tersimpan!)</td></tr>
                        <tr><td><code>"turn90"</code></td><td>440</td><td>425</td><td>.................. (Tetap Tersimpan!)</td></tr>
                        <tr><td><code>"wallCm"</code></td><td>6.5</td><td>6.0</td><td>.................. (Tetap Tersimpan!)</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Nama key pada Preferences.h maksimal terdiri dari 15 karakter (contoh: 'baseSpd', 'turn90'). Jangan gunakan nama key yang terlalu panjang."
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
            "theory": """
                <p>Pada <strong>Ujian Tengah Semester (Proyek Mini 3)</strong> tingkat SMA/SMK, robot diuji melintasi jalur labirin yang memuat <strong>3 jenis persimpangan berurutan</strong> (misalnya: Simpang Tiga Kiri &rarr; Jalan Buntu &rarr; Pertigaan T &rarr; Garis Finish). Setiap kali robot berhenti sejenak di pusat persimpangan, robot wajib mengirimkan jenis persimpangan dan arah belokan yang diambil ke layar Web Dashboard penguji!</p>
            """,
            "safety": "Pastikan parameter NVS telah disesuaikan untuk permukaan lantai arena ujian sebelum giliran tim dipanggil.",
            "steps": [
                "Integrasikan modul M-01 s/d M-07 ke dalam program Proyek Mini 3 di bawah ini.",
                "Buka Web Dashboard pada laptop Juri/Guru untuk memantau kiriman telemetri langsung dari robot timmu.",
                "Lepaskan robot dari kotak Start dan biarkan robot menavigasi ketiga persimpangan hingga berhenti di garis Finish."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-08: UTS PROYEK MINI 3 - Navigasi Persimpangan & Telemetri Web
// =========================================================================
#include "MazeBotStarter.h"
#include <Preferences.h>

MazeBotCore bot;
int simpangKe = 0;

void setup() {
  Serial.begin(115200);
  bot.begin("MazeBot-SMA-UTS");
  delay(2000);
}

void loop() {
  bot.updateWeb();

  if (bot.isFinishLine()) {
    bot.drive(0, 0);
    bot.sendTelemetry(0, 0, 0, "FINISH TERCAPAI! Total Simpang: " + String(simpangKe));
    while (true) { bot.updateWeb(); delay(100); }
  }

  float L = bot.readLeft();
  float F = bot.readFront();
  float R = bot.readRight();

  // Cek apakah memasuki persimpangan atau jalan buntu
  if (L > 16.0 || R > 16.0 || F < 13.0) {
    simpangKe++;
    String jenis = klasifikasiSimpang(L, F, R);
    char aksi = ambilKeputusanSimpangStabil(); // Fungsi dari M-04
    
    String logMsg = "Simpang #" + String(simpangKe) + ": " + jenis + " -> Aksi: " + String(aksi);
    bot.sendTelemetry(L, F, R, logMsg);
  } else {
    majuClosedLoop(L); // Fungsi dari M-02
  }
}""",
            "lks": """
                <p><strong>Lembar Penilaian UTS Proyek Mini 3 (Tingkat SMA/SMK):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Titik Uji</th><th>Jenis Persimpangan Aktual</th><th>Log Telemetri yang Muncul di Web</th><th>Ketepatan Manuver Fisik</th><th>Skor (0–25)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Simpang #1</td><td>........................</td><td>.......................................</td><td>Tepat / Menyenggol</td><td>.......</td></tr>
                        <tr><td>Simpang #2</td><td>........................</td><td>.......................................</td><td>Tepat / Menyenggol</td><td>.......</td></tr>
                        <tr><td>Simpang #3</td><td>........................</td><td>.......................................</td><td>Tepat / Menyenggol</td><td>.......</td></tr>
                        <tr><td>Garis Finish</td><td>Lakban Hitam TCRT5000</td><td><code>FINISH TERCAPAI!</code></td><td>Berhenti Tepat</td><td>.......</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Pastikan fungsi Step-Out (maju 350 ms setelah belok di simpang) berjalan tuntas agar satu persimpangan yang sama tidak terhitung dua kali (double counting)."
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
            "theory": """
                <p>Agar robot bisa mengingat jalan yang pernah ia lalui, robot membutuhkan struktur data <strong>Array of Characters (<code>char rawPath[100]</code>)</strong>. Setiap kali robot melewati sebuah persimpangan (atau jalan buntu), kita menyisipkan 1 huruf simbol keputusan ke urutan indeks berikutnya:</p>
                <ul>
                    <li><code>'L'</code> (<em>Left</em>): Belok Kiri 90&deg; di persimpangan.</li>
                    <li><code>'R'</code> (<em>Right</em>): Belok Kanan 90&deg; di persimpangan.</li>
                    <li><code>'S'</code> (<em>Straight</em>): Memilih jalan Lurus melewati persimpangan.</li>
                    <li><code>'U'</code> (<em>U-Turn</em>): Berputar balik 180&deg; karena menemui jalan buntu.</li>
                </ul>
                <p>Contoh: Jika robot belok kiri, lalu masuk jalan buntu (putar balik), lalu belok kiri lagi, dan terakhir jalan lurus, maka isi array <code>rawPath</code> adalah: <strong><code>['L', 'U', 'L', 'S']</code></strong> dengan <code>pathLength = 4</code>.</p>
            """,
            "safety": "Selalu periksa batas ukuran array (if (pathLength < MAX_PATH - 1)) sebelum menyimpan elemen baru agar tidak terjadi Buffer Overflow di memori ESP32.",
            "steps": [
                "Deklarasikan <code>const int MAX_PATH = 100;</code>, <code>char rawPath[MAX_PATH];</code>, dan <code>int pathLength = 0;</code>.",
                "Buat fungsi <code>rekamLangkah(char aksi)</code> yang menyimpan karakter ke <code>rawPath[pathLength]</code> lalu menaikkan nilai <code>pathLength++</code>.",
                "Simulasikan penambahan beberapa langkah di <code>void setup()</code> dan tampilkan hasilnya di Serial Monitor!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-09: Struktur Data Array of Chars untuk Perekaman Jejak Labirin
// =========================================================================
const int MAX_PATH = 100;
char rawPath[MAX_PATH]; // Array penyimpan riwayat belokan
int  pathLength = 0;    // Jumlah langkah yang sudah terekam

void resetMemoriJejak() {
  pathLength = 0;
  rawPath[0] = '\\0'; // Null-terminator penanda akhir string C
}

void rekamLangkah(char aksi) {
  if (pathLength < (MAX_PATH - 1)) {
    rawPath[pathLength] = aksi;
    pathLength++;
    rawPath[pathLength] = '\\0'; // Jaga agar selalu valid sebagai C-String
    
    Serial.print("[MEMORY] Langkah Ditambahkan: ");
    Serial.print(aksi);
    Serial.print(" | Jejak Saat Ini (");
    Serial.print(pathLength);
    Serial.print("): ");
    Serial.println(rawPath);
  }
}

void setup() {
  Serial.begin(115200);
  resetMemoriJejak();
  
  // Simulasi robot melewati 5 titik persimpangan/buntu:
  rekamLangkah('L'); // Simpang 1: Belok Kiri
  rekamLangkah('U'); // Buntu: Putar Balik 180
  rekamLangkah('L'); // Kembali ke Simpang 1: Belok Kiri (yang berarti lurus dari arah awal)
  rekamLangkah('R'); // Simpang 2: Belok Kanan
  rekamLangkah('S'); // Simpang 3: Lurus menuju Finish
}

void loop() {}""",
            "lks": """
                <p><strong>Latihan Representasi Array Jejak Perjalanan:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Indeks Array</th><th><code>rawPath[0]</code></th><th><code>rawPath[1]</code></th><th><code>rawPath[2]</code></th><th><code>rawPath[3]</code></th><th><code>rawPath[4]</code></th><th><code>rawPath[5]</code></th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Isi Karakter</strong></td><td><code>'S'</code></td><td><code>'L'</code></td><td><code>'U'</code></td><td><code>'L'</code></td><td><code>'R'</code></td><td><code>'\\0'</code></td></tr>
                    </tbody>
                </table>
                <p>Pertanyaan: Berapakah nilai variabel <code>pathLength</code> pada tabel di atas? Jawab: <strong>.......</strong></p>
            """,
            "troubleshooting": "Menambahkan karakter null-terminator '\\0' setiap kali habis mengisi elemen baru sangat memudahkan kita karena array char tersebut bisa langsung dicetak dengan Serial.println(rawPath)!"
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
            "theory": """
                <p>Pada <strong>Fase Eksplorasi (Mapping Run)</strong>, robot berjalan menyusuri labirin untuk pertama kalinya menggunakan aturan <em>Left-Hand Rule</em>. Setiap kali robot mengeksekusi keputusan pada persimpangan atau jalan buntu, hasil karakter dari fungsi <code>char aksi = ambilKeputusanSimpangStabil();</code> langsung dimasukkan ke dalam fungsi <code>rekamLangkah(aksi);</code>.</p>
                <p>Begitu sensor bawah TCRT5000 menyentuh garis Finish hitam, robot berhenti dan menampilkan seluruh riwayat jejak penjelajahannya (misalnya: <code>"SLULSRULLR"</code>) ke layar Web Dashboard!</p>
            """,
            "safety": "Pastikan memori jejak di-reset (resetMemoriJejak()) setiap kali robot memulai Mapping Run baru dari garis Start.",
            "steps": [
                "Siapkan arena labirin yang memiliki minimal 1 cabang jalan buntu (Dead-End).",
                "Unggah kode Mapping Run M-10 ke robot dan jalankan dari titik Start.",
                "Ikuti perjalanan robot dan catat secara manual huruf keputusan di setiap simpang, lalu cocokkan catatan manualmu dengan string <code>rawPath</code> yang dikirim robot ke Web Dashboard saat menyentuh Finish!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-10: Fase Eksplorasi (Mapping Run) + Perekaman Array Otomatis
// =========================================================================

void jalankanMappingRun() {
  // 1. Cek apakah sudah sampai di Garis Finish (TCRT5000)
  if (bot.isFinishLine()) {
    bot.drive(0, 0);
    String pesanFinish = "MAPPING SELESAI! Raw Path: " + String(rawPath);
    bot.sendTelemetry(0, 0, 0, pesanFinish);
    Serial.println(pesanFinish);
    currentState = STATE_FINISH_COMPUTE;
    return;
  }

  // 2. Baca ketiga sensor ultrasonik
  float L = bot.readLeft();
  float F = bot.readFront();
  float R = bot.readRight();

  // 3. Jika mendeteksi persimpangan (bukaan kiri/kanan) atau jalan buntu/dinding depan
  if (L > 16.0 || R > 16.0 || F < 13.0) {
    char aksiDiambil = ambilKeputusanSimpangStabil();
    rekamLangkah(aksiDiambil); // Simpan 'L', 'R', 'S', atau 'U' ke dalam rawPath[]
    
    bot.sendTelemetry(L, F, R, "Recorded: " + String(rawPath));
  } 
  else {
    // Selama di lorong lurus biasa, gunakan koreksi dinding proporsional
    majuClosedLoop(L);
  }
}""",
            "lks": """
                <p><strong>Verifikasi Rekaman Mapping Run vs Pengamatan Manual:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Urutan Node</th><th>Kondisi Simpang di Labirin</th><th>Aksi Fisik Robot</th><th>Huruf yang Tercatat di <code>rawPath</code></th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Node 1</td><td>Simpang Tiga (Belok Kiri ke Jalan Buntu)</td><td>Belok Kiri</td><td><code>'L'</code></td></tr>
                        <tr><td>Node 2</td><td>Ujung Jalan Buntu</td><td>Putar Balik 180&deg;</td><td><code>'U'</code></td></tr>
                        <tr><td>Node 3</td><td>Kembali ke Simpang Tiga Awal</td><td>Belok Kiri</td><td><code>'L'</code></td></tr>
                        <tr><td>Node 4</td><td>Simpang Berikutnya Menuju Finish</td><td>.....................</td><td><code>'...'</code></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Perhatikan Node 1, 2, dan 3 pada tabel LKS di atas: ketiganya membentuk pola 'L' -> 'U' -> 'L'. Pada modul M-11 berikutnya, kita akan mempelajari bagaimana memangkas ketiga langkah sia-sia tersebut menjadi 1 langkah 'S' (Lurus)!"
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
            "theory": """
                <p>Setiap kali di dalam rekaman perjalanan terdapat huruf <strong><code>'U'</code> (Putar Balik)</strong>, itu adalah bukti pasti bahwa robot baru saja tersesat masuk ke dalam <strong>Jalan Buntu</strong>! Tiga langkah berurutan <code>[Aksi Masuk] + 'U' + [Aksi Keluar]</code> sebenarnya dapat digantikan (direduksi) menjadi <strong>1 langkah langsung</strong> seandainya robot tidak masuk ke jalan buntu tersebut:</p>
                <table class="std-table">
                    <thead>
                        <tr><th>Pola 3 Karakter (Tersesat ke Buntu)</th><th>Makna Gerakan Fisik Asli</th><th>Hasil Reduksi (1 Karakter)</th><th>Makna Gerakan Baru (Tanpa Tersesat)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong><code>L + U + L</code></strong></td><td>Belok Kiri (-90&deg;), Putar Balik (+180&deg;), Belok Kiri (-90&deg;)</td><td><strong><code>S</code></strong></td><td>Langsung <strong>Lurus (Straight 0&deg;)</strong> melewati simpang!</td></tr>
                        <tr><td><strong><code>L + U + S</code></strong></td><td>Belok Kiri (-90&deg;), Putar Balik (+180&deg;), Jalan Lurus (0&deg;)</td><td><strong><code>R</code></strong></td><td>Langsung <strong>Belok Kanan (+90&deg;)</strong>!</td></tr>
                        <tr><td><strong><code>S + U + L</code></strong></td><td>Jalan Lurus (0&deg;), Putar Balik (+180&deg;), Belok Kiri (-90&deg;)</td><td><strong><code>R</code></strong></td><td>Langsung <strong>Belok Kanan (+90&deg;)</strong>!</td></tr>
                        <tr><td><strong><code>L + U + R</code></strong></td><td>Belok Kiri (-90&deg;), Putar Balik (+180&deg;), Belok Kanan (+90&deg;)</td><td><strong><code>U</code></strong></td><td>Simpang itu sendiri buntu &rarr; <strong>Putar Balik (U)</strong></td></tr>
                        <tr><td><strong><code>S + U + S</code></strong></td><td>Jalan Lurus (0&deg;), Putar Balik (+180&deg;), Jalan Lurus (0&deg;)</td><td><strong><code>U</code></strong></td><td>Simpang itu sendiri buntu &rarr; <strong>Putar Balik (U)</strong></td></tr>
                    </tbody>
                </table>
                <div class="formula-box">
                    Contoh Bertingkat: &nbsp; L L U L U L R &nbsp;&rarr;&nbsp; L (L U L) U L R &nbsp;&rarr;&nbsp; L S U L R &nbsp;&rarr;&nbsp; L (S U L) R &nbsp;&rarr;&nbsp; L R (Rute Terpendek!)
                </div>
            """,
            "safety": "Pahami penjumlahan sudutnya: Kiri = -90 derajat, Kanan = +90 derajat, Lurus = 0 derajat, Putar Balik = +180 derajat. Contoh: L + U + S = -90 + 180 + 0 = +90 derajat (sama dengan Belok Kanan 'R')!",
            "steps": [
                "Pelajari rumus penjumlahan sudut rotasi mengapa 3 langkah yang mengapit huruf <code>U</code> selalu ekuivalen dengan 1 langkah tunggal.",
                "Ambil kertas kerja LKS dan selesaikan latihan pemangkasan string jejak labirin secara bertahap sampai tidak ada lagi huruf <code>U</code> yang tersisa!",
                "Tuliskan fungsi pencocokan pola <code>char aturanReduksiBuntu(char sebelum, char sesudah)</code> di C++."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-11: Aturan Substitusi Reduksi Jalan Buntu (Dead-End Rules)
// =========================================================================

// Mengembalikan karakter tunggal pengganti pola [sebelum] + 'U' + [sesudah]
char aturanReduksiBuntu(char sebelum, char sesudah) {
  if (sebelum == 'L' && sesudah == 'L') return 'S'; // L + U + L = S
  if (sebelum == 'L' && sesudah == 'S') return 'R'; // L + U + S = R
  if (sebelum == 'L' && sesudah == 'R') return 'U'; // L + U + R = U
  if (sebelum == 'S' && sesudah == 'L') return 'R'; // S + U + L = R
  if (sebelum == 'S' && sesudah == 'S') return 'U'; // S + U + S = U
  if (sebelum == 'R' && sesudah == 'L') return 'U'; // R + U + L = U
  return '?'; // Pola tidak valid
}""",
            "lks": """
                <p><strong>Latihan Komputasi Manual Reduksi Rute Labirin:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>No</th><th>String Jejak Eksplorasi Mentah (<code>rawPath</code>)</th><th>Tahap Pemangkasan 1</th><th>Hasil Akhir Rute Terpendek (<code>optPath</code>)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td><code>S L U L R</code></td><td><code>S (L U L) R</code> &rarr; ............</td><td>........................</td></tr>
                        <tr><td>2</td><td><code>L U S R L U L</code></td><td><code>(L U S) R (L U L)</code> &rarr; ............</td><td>........................</td></tr>
                        <tr><td>3</td><td><code>S L L U L U S L</code></td><td><code>S L (L U L) U S L</code> &rarr; <code>S L S U S L</code> &rarr; ...</td><td>........................</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Pada soal nomor 3, setelah LUL diubah menjadi S, muncul huruf U berikutnya yang membentuk pola baru! Itulah sebabnya algoritma pemangkasan harus dijalankan di dalam perulangan while sampai seluruh huruf 'U' habis."
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
            "theory": """
                <p>Bagaimana cara paling elegan menulis algoritma pemangkas array di C++? Ketika kita menemukan huruf <code>'U'</code> pada indeks <code>i</code> (yaitu <code>optPath[i] == 'U'</code>), kita mengganti elemen di kirinya (<code>optPath[i-1]</code>) dengan hasil substitusi <code>substitusiBuntu(optPath[i-1], optPath[i+1])</code>, lalu <strong>menggeser seluruh elemen setelahnya maju sebanyak 2 kotak ke kiri</strong> (mengurangi panjang array sebanyak 2)!</p>
                <p>Proses pencarian ini diulang di dalam <code>while (masihAdaU)</code> sampai tidak ada lagi huruf <code>'U'</code> di dalam array <code>optPath</code>.</p>
            """,
            "safety": "Pastikan indeks pencarian dimulai dari i = 1 hingga i < optLength - 1 agar akses optPath[i-1] dan optPath[i+1] selalu berada di dalam batas memori array yang sah.",
            "steps": [
                "Ketikkan kode lengkap <strong>Path Simplification Engine</strong> (M-12) di bawah ini pada Arduino IDE.",
                "Unggah ke ESP32 dan buka Serial Monitor.",
                "Amati bagaimana string mentah sepanjang 13 langkah seperti <code>\"SLLULUSLRULLS\"</code> dipangkas dalam waktu kurang dari 1 milidetik menjadi rute terpendek yang bersih dari jalan buntu!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-12: Path Simplification Engine (Algoritma Pemangkas Array C++)
// =========================================================================
char rawPath[100] = "SLLULUSLRULLS"; // Contoh jejak mentah hasil Mapping Run
char optPath[100];                   // Array hasil optimasi rute terpendek
int  optLength = 0;

char substitusiBuntu(char A, char B) {
  if (A == 'L' && B == 'L') return 'S';
  if (A == 'L' && B == 'S') return 'R';
  if (A == 'L' && B == 'R') return 'U';
  if (A == 'S' && B == 'L') return 'R';
  if (A == 'S' && B == 'S') return 'U';
  if (A == 'R' && B == 'L') return 'U';
  return 'U';
}

void pangkasRuteJalanBuntu() {
  // 1. Salin isi rawPath ke optPath agar rawPath asli tetap tersimpan untuk laporan
  strcpy(optPath, rawPath);
  optLength = strlen(optPath);

  bool masihAdaU = true;
  int tahap = 1;

  while (masihAdaU) {
    masihAdaU = false;
    for (int i = 1; i < optLength - 1; i++) {
      if (optPath[i] == 'U') {
        char pengganti = substitusiBuntu(optPath[i - 1], optPath[i + 1]);
        optPath[i - 1] = pengganti; // Ganti 3 huruf (i-1, i, i+1) dengan 1 huruf

        // Geser sisa array di sebelah kanan maju 2 langkah ke kiri
        for (int j = i; j < optLength - 2; j++) {
          optPath[j] = optPath[j + 2];
        }
        optLength -= 2;
        optPath[optLength] = '\\0';

        Serial.printf("  [Tahap %d] Reduksi -> %s (Panjang: %d)\\n", tahap++, optPath, optLength);
        masihAdaU = true;
        break; // Mulai scan ulang dari depan untuk menangani nested U-turn
      }
    }
  }
}

void setup() {
  Serial.begin(115200);
  Serial.print("Jejak Mentah (Raw Path)      : "); Serial.println(rawPath);
  pangkasRuteJalanBuntu();
  Serial.print("Rute Terpendek (Optimized)   : "); Serial.println(optPath);
}

void loop() {}""",
            "lks": """
                <p><strong>Hasil Eksekusi Path Simplification Engine di ESP32:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Input <code>rawPath</code></th><th>Panjang Awal</th><th>Output <code>optPath</code> di Serial Monitor</th><th>Panjang Akhir</th><th>Persentase Penghematan Langkah</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><code>"SLLULUSLRULLS"</code></td><td>13 langkah</td><td>..............................</td><td>..... langkah</td><td>.......... % lebih singkat</td></tr>
                        <tr><td><code>"LULSLULR"</code></td><td>8 langkah</td><td>..............................</td><td>..... langkah</td><td>.......... % lebih singkat</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Mengapa kita menyalin rawPath ke optPath menggunakan strcpy(optPath, rawPath)? Supaya di Web Dashboard kita bisa menampilkan perbandingan 'Before (Raw Path)' dan 'After (Optimized Path)' secara berdampingan!"
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
            "theory": """
                <p>Setelah robot menyentuh garis Finish pada akhir <em>Mapping Run</em> dan menjalankan fungsi <code>pangkasRuteJalanBuntu()</code>, siswa perlu memverifikasi secara visual apakah rute terpendek yang dihitung oleh otak ESP32 sudah sesuai dengan bentuk fisik labirin.</p>
                <p>Starter API menyediakan fungsi <strong><code>bot.sendRouteSummary(rawPath, optPath, exploreTimeSec)</code></strong> yang langsung menampilkan kartu perbandingan <em>Exploration Path vs Shortest Path</em> pada layar Web Dashboard!</p>
            """,
            "safety": "Saat robot berada pada state selesai eksplorasi (STATE_DONE), pastikan motor terkunci penuh (PWM 0) sembari siswa menganalisis data di layar web dan memindahkan robot kembali ke titik Start.",
            "steps": [
                "Panggil fungsi <code>bot.sendRouteSummary(rawPath, optPath, detikExplore);</code> tepat setelah fungsi <code>pangkasRuteJalanBuntu()</code> selesai dieksekusi.",
                "Amati panel <strong>Path Reduction Visualizer</strong> pada Web Dashboard.",
                "Verifikasi bahwa setiap pola jalan buntu (yang berwarna merah di layar web) telah berubah menjadi langkah langsung (berwarna hijau)."
            ],
            "cpp_code": """// =========================================================================
// MODUL M-13: Pengiriman & Visualisasi Perbandingan Rute ke Web Dashboard
// =========================================================================

void tampilkanAnalisisRuteKeWeb(unsigned long waktuExploreMs) {
  // 1. Jalankan mesin pemangkas jalan buntu
  pangkasRuteJalanBuntu();

  // 2. Hitung metrik efisiensi
  int langkahAwal  = strlen(rawPath);
  int langkahAkhir = strlen(optPath);
  int langkahHemat = langkahAwal - langkahAkhir;
  float detikExplore = waktuExploreMs / 1000.0;

  // 3. Kirim ke kartu visualisasi Web Dashboard melalui Starter API
  bot.sendRouteSummary(rawPath, optPath, detikExplore);

  // 4. Kirim pesan ringkasan ke log telemetri
  String info = "RAW: " + String(rawPath) + " (" + String(langkahAwal) + ") -> " +
                "OPT: " + String(optPath) + " (" + String(langkahAkhir) + ") | " +
                "Hemat: " + String(langkahHemat) + " simpang!";
  bot.sendTelemetry(0, 0, 0, info);
}""",
            "lks": """
                <p><strong>Lembar Analisis Data Telemetri Reduksi Rute:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Metrik Evaluasi</th><th>Data pada Web Dashboard</th><th>Analisis Siswa</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>String <code>rawPath</code> (Explore Run)</td><td><code>....................................</code></td><td>Jumlah masuk jalan buntu (huruf U): .... kali</td></tr>
                        <tr><td>String <code>optPath</code> (Optimized)</td><td><code>....................................</code></td><td>Seluruh huruf U berhasil dieliminasi? Ya / Tidak</td></tr>
                        <tr><td>Waktu Tempuh Explore Run</td><td>................ detik</td><td>Prediksi waktu Speed Run: &lt; ............ detik</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Jika tampilan di browser belum memperbarui string optPath, pastikan fungsi bot.updateWeb() tetap dipanggil di dalam perulangan tunggu STATE_DONE."
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
            "theory": """
                <p>Inilah momen paling memukau dalam robotika labirin otonom: <strong>Fase Eksekusi Jalur Tercepat (Speed Run)</strong>! Setelah robot diangkat dari garis Finish dan diletakkan kembali di garis Start, kita menekan tombol <strong>[START SPEED RUN]</strong> di Web Dashboard (atau tombol fisik di robot).</p>
                <p>Pada mode <em>Speed Run</em>, ketika robot mendeteksi persimpangan ke-<code>stepIndex</code>, robot tidak lagi menebak-nebak dengan <em>Left-Hand Rule</em>, melainkan <strong>langsung mengeksekusi instruksi dari memori <code>optPath[stepIndex]</code></strong>:</p>
                <ul>
                    <li>Jika <code>optPath[stepIndex] == 'L'</code> &rarr; Langsung eksekusi Belok Kiri!</li>
                    <li>Jika <code>optPath[stepIndex] == 'R'</code> &rarr; Langsung eksekusi Belok Kanan!</li>
                    <li>Jika <code>optPath[stepIndex] == 'S'</code> &rarr; Langsung melaju Lurus melewati simpang tanpa ragu!</li>
                </ul>
            """,
            "safety": "Saat menaikkan kecepatan untuk Speed Run (misal dari PWM 145 ke 160), pastikan nilai DELAY_BELOK90 disesuaikan sedikit karena putaran motor yang lebih cepat membutuhkan durasi belok yang sedikit lebih singkat.",
            "steps": [
                "Tambahkan variabel <code>int stepIndex = 0;</code> sebagai penunjuk langkah saat Speed Run.",
                "Implementasikan fungsi <code>jalankanSpeedRun()</code> seperti pada kode M-14 di bawah.",
                "Jalankan robot dari Explore Run, biarkan ia memangkas rute di Finish, lalu pindahkan ke Start dan jalankan Speed Run! Bandingkan waktu tempuh keduanya!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-14: Eksekusi Jalur Terpendek (Speed Run Mode) Berbasis Array optPath
// =========================================================================
int stepIndex = 0; // Indeks pembacaan array optPath[] saat Speed Run

void mulaiSpeedRunDariStart() {
  stepIndex = 0;
  bot.sendTelemetry(0, 0, 0, "SPEED RUN DIMULAI! Mengikuti Rute: " + String(optPath));
}

void jalankanSpeedRun() {
  // 1. Cek apakah sudah menyentuh Garis Finish Hitam (TCRT5000)
  if (bot.isFinishLine()) {
    bot.drive(0, 0);
    bot.sendTelemetry(0, 0, 0, "SPEED RUN FINISH! Rute Terpendek Tuntas!");
    currentState = STATE_DONE;
    return;
  }

  float L = bot.readLeft();
  float F = bot.readFront();
  float R = bot.readRight();

  // 2. Jika mendeteksi persimpangan (bukaan kiri/kanan atau dinding depan)
  if (L > 16.0 || R > 16.0 || F < 13.0) {
    // Maju sedikit ke titik pusat simpang
    if (F > 12.0) { bot.drive(150, 150); delay(200); }
    bot.drive(0, 0); delay(100);

    // Baca instruksi matang dari array optPath pada indeks stepIndex!
    char perintah = optPath[stepIndex];
    if (stepIndex < optLength) stepIndex++;

    bot.sendTelemetry(L, F, R, "SpeedRun Step #" + String(stepIndex) + " -> " + String(perintah));

    if (perintah == 'L') {
      bot.turnLeft90();
      bot.drive(155, 155); delay(350);
    } else if (perintah == 'R') {
      bot.turnRight90();
      bot.drive(155, 155); delay(350);
    } else if (perintah == 'S') {
      bot.drive(160, 160); delay(380); // Lurus cepat melewati mulut simpang!
    }
  } 
  else {
    // Di lorong lurus, gunakan Closed-Loop Wall Correction
    majuClosedLoop(L);
  }
}""",
            "lks": """
                <p><strong>Tabel Perbandingan Performa Explore Run vs Speed Run:</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Parameter Perbandingan</th><th>Fase 1: Explore Run (Left-Hand Rule)</th><th>Fase 2: Speed Run (Array <code>optPath</code>)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Rute yang Ditempuh</td><td><code>rawPath = ....................</code></td><td><code>optPath = ....................</code></td></tr>
                        <tr><td>Jumlah Masuk Jalan Buntu</td><td>......... kali</td><td><strong>0 kali (Bebas Jalan Buntu!)</strong></td></tr>
                        <tr><td>Catatan Waktu Stopwatch</td><td>................ detik</td><td>................ detik</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Perhatikan saat perintah == 'S' (Lurus melewati persimpangan): kita tidak perlu berhenti lama di simpang, cukup melaju lurus selama 380 ms sampai mulut cabang kiri/kanan terlewati!"
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
            "theory": """
                <p>Dalam standar industri robotika otonom (seperti AGV di pabrik), setiap robot wajib memiliki dua lapis sistem pengaman (<strong>Failsafe</strong>):</p>
                <ol>
                    <li><strong>Wireless Emergency Stop (E-Stop):</strong> Tombol merah besar di layar Web Dashboard yang jika ditekan oleh operator, langsung memutus sinyal PWM motor (<code>bot.drive(0,0)</code>) dan mengunci state ke <code>STATE_ESTOP</code>.</li>
                    <li><strong>Stuck / Slip Watchdog:</strong> Jika bodi robot tidak sengaja menyangkut di sudut dinding sehingga roda terus berputar selip di tempat (<code>jarakDepan &lt; 4.5 cm</code> terus-menerus selama &gt; 2000 ms), sistem Watchdog otomatis menghentikan motor atau melakukan manuver mundur pembebasan diri (<em>Auto-Recovery</em>) agar motor DC dan driver DRV8833 tidak panas/terbakar!</li>
                </ol>
            """,
            "safety": "Jangan pernah membiarkan motor DC tertahan (stall) dalam kondisi diberi tegangan PWM tinggi lebih dari 3 detik karena arus stall dapat merusak gigi gearbox dan menguras baterai 18650.",
            "steps": [
                "Tambahkan fungsi <code>cekSistemFailsafe(float jarakDepan)</code> di baris paling awal <code>void loop()</code>.",
                "Uji tombol <strong>[E-STOP DARURAT]</strong> pada layar Web Dashboard saat robot sedang melaju.",
                "Simulasikan kondisi tersangkut dengan menahan penghalang tepat 3 cm di depan robot selama 2 detik; pastikan Watchdog aktif memundurkan/menghentikan robot!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-15: Sistem Pengaman E-Stop Nirkabel & Stuck Watchdog Timer
// =========================================================================
unsigned long stuckTimerStart = 0;
bool isStuckMonitoring = false;

bool cekSistemFailsafe(float jarakDepan) {
  // 1. Cek Tombol Emergency Stop (E-Stop) dari Web Dashboard
  if (bot.isEmergencyStop()) {
    bot.drive(0, 0);
    bot.sendTelemetry(0, jarakDepan, 0, "E-STOP AKTIF! Motor Dikunci oleh Operator.");
    return true; // Mengindikasikan interupsi darurat aktif
  }

  // 2. Stuck Watchdog: Deteksi jika robot nyangkut dinding depan (< 4.5 cm) > 2 detik
  if (jarakDepan < 4.5) {
    if (!isStuckMonitoring) {
      isStuckMonitoring = true;
      stuckTimerStart = millis();
    } else if (millis() - stuckTimerStart > 2000) {
      // Robot terbukti tersangkut selama 2 detik! Lakukan Auto-Recovery atau Stop:
      bot.drive(0, 0);
      bot.sendTelemetry(0, jarakDepan, 0, "WATCHDOG: Robot Tersangkut! Melakukan Mundur Bebas...");
      bot.drive(-145, -145); delay(350); // Mundur pembebasan diri
      bot.drive(0, 0);       delay(200);
      isStuckMonitoring = false;
      return true;
    }
  } else {
    isStuckMonitoring = false; // Reset timer jika jarak depan aman
  }

  return false; // Sistem aman, lanjutkan navigasi normal
}""",
            "lks": """
                <p><strong>Lembar Pengujian Sistem Keamanan (Failsafe &amp; Watchdog):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Skenario Pengujian</th><th>Kondisi Pemicu</th><th>Respon Failsafe Robot</th><th>Status Kelulusan Uji</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Uji E-Stop Nirkabel</td><td>Tombol E-Stop di Web ditekan</td><td>Motor berhenti dalam &lt; 0.1 detik</td><td>Lulus / Gagal</td></tr>
                        <tr><td>Uji Stuck Watchdog</td><td>Dinding ditahan 3 cm di depan &gt; 2 dtk</td><td>Peringatan Web &amp; Mundur Otomatis</td><td>Lulus / Gagal</td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Fitur Auto-Recovery (mundur 350 ms saat tersangkut) sangat berguna di dalam kompetisi karena menyelamatkan robot yang menyerempet dinding tanpa perlu disentuh tangan (bebas penalti retry)!"
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
            "theory": """
                <p>Selamat datang di puncak kurikulum tingkat SMA/SMK: <strong>Capstone Project — Autonomous Maze Grand Prix</strong>! Setiap tim dievaluasi dalam 3 tahapan berkesinambungan:</p>
                <ol>
                    <li><strong>Tahap 1 — Explore Run (Mapping):</strong> Robot dilepas dari Start, memetakan labirin menggunakan <em>Left-Hand Rule</em>, mencatat setiap persimpangan ke dalam <code>rawPath[]</code>, dan berhenti tepat di atas garis Finish hitam (TCRT5000).</li>
                    <li><strong>Tahap 2 — Data Analysis (Web Verification):</strong> Di garis Finish, robot otomatis menjalankan <em>Path Simplification Engine</em> dan mengirimkan <code>rawPath</code> vs <code>optPath</code> ke Web Dashboard. Siswa memverifikasi hasil pemangkasan rute di hadapan Juri.</li>
                    <li><strong>Tahap 3 — Speed Run (Shortest Path Execution):</strong> Robot ditaruh kembali di garis Start, beralih ke mode <em>Speed Run</em>, dan melintasi rute terpendek <code>optPath[]</code> tanpa sekalipun berbelok ke jalan buntu!</li>
                </ol>
            """,
            "safety": "Pastikan tombol E-Stop di Web Dashboard selalu siap siaga di layar operator tim selama pelaksanaan Explore Run maupun Speed Run.",
            "steps": [
                "Unggah <strong>Kode Master Capstone M-16</strong> di bawah ini ke unit MazeBot timmu.",
                "Lakukan Tahap 1 (Explore Run) dari garis Start hingga robot berhenti di garis Finish.",
                "Tunjukkan layar Web Dashboard kepada Juri untuk memverifikasi hasil reduksi array (Tahap 2).",
                "Pindahkan robot kembali ke garis Start, tekan tombol mode <strong>Speed Run</strong> di Web Dashboard, dan catat rekor waktu tercepat timmu (Tahap 3)!"
            ],
            "cpp_code": """// =========================================================================
// MODUL M-16: MASTER CODE CAPSTONE SMA/SMK - AUTONOMOUS MAZE GRAND PRIX
// =========================================================================
#include "MazeBotStarter.h"
#include <Preferences.h>

MazeBotCore bot;
Preferences prefs;

enum Mode { MODE_EXPLORE, MODE_WAIT_SPEEDRUN, MODE_SPEEDRUN, MODE_FINISHED };
Mode currentMode = MODE_EXPLORE;

char rawPath[100];
char optPath[100];
int  rawLen = 0, optLen = 0, stepIdx = 0;
unsigned long startTime = 0;

char reduceRule(char A, char B) {
  if (A == 'L' && B == 'L') return 'S';
  if (A == 'L' && B == 'S') return 'R';
  if (A == 'L' && B == 'R') return 'U';
  if (A == 'S' && B == 'L') return 'R';
  if (A == 'S' && B == 'S') return 'U';
  return 'U';
}

void simplifyPath() {
  strcpy(optPath, rawPath);
  optLen = strlen(optPath);
  bool changed = true;
  while (changed) {
    changed = false;
    for (int i = 1; i < optLen - 1; i++) {
      if (optPath[i] == 'U') {
        optPath[i - 1] = reduceRule(optPath[i - 1], optPath[i + 1]);
        for (int j = i; j < optLen - 2; j++) optPath[j] = optPath[j + 2];
        optLen -= 2;
        optPath[optLen] = '\\0';
        changed = true;
        break;
      }
    }
  }
}

void setup() {
  Serial.begin(115200);
  bot.begin("MazeBot-SMA-GP");
  rawPath[0] = '\\0'; optPath[0] = '\\0';
  delay(2000);
  startTime = millis();
}

void loop() {
  bot.updateWeb();
  float L = bot.readLeft(), F = bot.readFront(), R = bot.readRight();
  if (cekSistemFailsafe(F)) return;

  if (currentMode == MODE_EXPLORE) {
    if (bot.isFinishLine()) {
      bot.drive(0, 0);
      float expSec = (millis() - startTime) / 1000.0;
      simplifyPath();
      bot.sendRouteSummary(rawPath, optPath, expSec);
      currentMode = MODE_WAIT_SPEEDRUN;
      return;
    }
    if (L > 16.0 || R > 16.0 || F < 13.0) {
      char act = ambilKeputusanSimpangStabil();
      if (rawLen < 98) { rawPath[rawLen++] = act; rawPath[rawLen] = '\\0'; }
      bot.sendTelemetry(L, F, R, "Explore Rec: " + String(rawPath));
    } else {
      majuClosedLoop(L);
    }
  }
  else if (currentMode == MODE_WAIT_SPEEDRUN) {
    bot.drive(0, 0);
    if (bot.isSpeedRunRequested()) {
      stepIdx = 0;
      startTime = millis();
      currentMode = MODE_SPEEDRUN;
    }
  }
  else if (currentMode == MODE_SPEEDRUN) {
    if (bot.isFinishLine()) {
      bot.drive(0, 0);
      float spdSec = (millis() - startTime) / 1000.0;
      bot.sendTelemetry(0, 0, 0, "GRAND PRIX TUNTAS! SpeedRun: " + String(spdSec, 2) + " dtk");
      currentMode = MODE_FINISHED;
      return;
    }
    if (L > 16.0 || R > 16.0 || F < 13.0) {
      if (F > 12.0) { bot.drive(150, 150); delay(200); }
      bot.drive(0, 0); delay(100);
      char cmd = (stepIdx < optLen) ? optPath[stepIdx++] : 'S';
      if (cmd == 'L') { bot.turnLeft90(); bot.drive(155, 155); delay(350); }
      else if (cmd == 'R') { bot.turnRight90(); bot.drive(155, 155); delay(350); }
      else { bot.drive(160, 160); delay(380); }
    } else {
      majuClosedLoop(L);
    }
  }
}""",
            "lks": """
                <p><strong>Lembar Penilaian Akhir Capstone Project (Autonomous Maze Grand Prix - SMA/SMK):</strong></p>
                <table class="std-table">
                    <thead>
                        <tr><th>Tahapan &amp; Komponen Evaluasi</th><th>Bobot</th><th>Indikator Keberhasilan</th><th>Skor Tim (0–100)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>1. Tahap 1: Explore Run &amp; Perekaman Array</strong></td><td>30%</td><td>Menyelesaikan eksplorasi ke garis Finish &amp; mencatat <code>rawPath</code> akurat</td><td>.............</td></tr>
                        <tr><td><strong>2. Tahap 2: Reduksi Jalan Buntu &amp; Telemetri</strong></td><td>30%</td><td>Algoritma pemangkasan menghasilkan <code>optPath</code> bebas huruf 'U' di Web</td><td>.............</td></tr>
                        <tr><td><strong>3. Tahap 3: Eksekusi Speed Run Terpendek</strong></td><td>25%</td><td>Menuntaskan rute terpendek tanpa masuk ke jalan buntu</td><td>.............</td></tr>
                        <tr><td><strong>4. Kestabilan Closed-Loop &amp; Failsafe</strong></td><td>15%</td><td>Koreksi dinding halus, NVS berfungsi, &amp; proteksi E-Stop/Watchdog aktif</td><td>.............</td></tr>
                        <tr><td colspan="3"><strong>TOTAL NILAI CAPSTONE PROJECT (TINGKAT SMA/SMK)</strong></td><td><strong>............. / 100</strong></td></tr>
                    </tbody>
                </table>
            """,
            "troubleshooting": "Selamat! Dengan tuntasnya Modul M-16 ini, siswa telah menguasai konsep struktur data, finite state machine, algoritma optimasi graf/rute sederhana, dan sistem kontrol tertanam berbasis sensor."
        }
    ]

def generate_sma_html():
    modules = get_sma_modules()
    toc_rows = ""
    for m in modules:
        toc_rows += f"""
        <tr>
            <td class="toc-code">{m['code']}</td>
            <td><strong>{m['title']}</strong></td>
            <td>{m['duration']}</td>
            <td>C++ Array &amp; Shortest Path</td>
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
                    <span class="mod-code">MODUL {m['code']} &bull; KURIKULUM SMA/SMK (KELAS X–XII)</span>
                    <h2>{m['title']}</h2>
                </div>
                <div class="module-banner-right">
                    <div><strong>Alokasi:</strong> {m['duration']}</div>
                    <div><strong>Fase:</strong> {m['phase']}</div>
                    <div><strong>Fokus:</strong> Algoritma &amp; Array</div>
                </div>
            </div>

            <div class="card">
                <h3>🎯 Target Kemampuan &amp; Capaian Pembelajaran</h3>
                <ul>{objectives_li}</ul>
            </div>

            <div class="alert alert-info">
                <span class="alert-title">⚙️ Catatan Sistem &amp; Rekayasa Perangkat Lunak</span>
                {m['safety']}
            </div>

            <h3 class="sub-heading">📖 A. Konsep Kunci &amp; Landasan Algoritma Komputasi</h3>
            {m['theory']}

            <h3 class="sub-heading">🛠️ B. Prosedur Implementasi &amp; Praktikum</h3>
            <ul class="steps-list">
                {steps_li}
            </ul>

            <h3 class="sub-heading">💻 C. Kode Program Lengkap (C++ ESP32 Starter Platform)</h3>
            <div class="code-box">
                <div class="code-header">
                    <span>📄 MazeBot_{m['code']}_SMA.ino</span>
                    <span>Platform: ESP32 + MazeBotStarter.h | C++17</span>
                </div>
                <pre>{escaped_code}</pre>
            </div>

            <div class="lks-box">
                <div class="lks-header">
                    <span>📝 D. Lembar Kerja Siswa (LKS) — {m['code']}</span>
                    <span>Tim / Kelas: ..............................</span>
                </div>
                {m['lks']}
            </div>

            <div class="alert alert-warning">
                <span class="alert-title">🔧 Panduan Guru / Instruktur: Catatan Teknis &amp; Debugging</span>
                {m['troubleshooting']}
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Modul Ajar MazeBot EduKit - Tingkat SMA/SMK (Kelas X-XII)</title>
    <link rel="stylesheet" href="css/modul_style.css">
</head>
<body class="theme-sma">

    <!-- COVER PAGE -->
    <div class="cover-page">
        <div>
            <span class="cover-badge">Kurikulum Robotika &amp; Komputasi Algoritma STEM Nasional</span>
            <div class="cover-title">MODUL AJAR &amp; PRAKTIKUM<br>MAZEBOT EDUKIT</div>
            <div class="cover-subtitle">📕 TINGKAT SMA / SMK (Target: Kelas X–XII)<br>"Algoritma Komputasi Navigasi &amp; Reduksi Rute Labirin"</div>
            <div class="cover-divider"></div>

            <div class="cover-highlights">
                <h3>Spesifikasi Pedagogis &amp; Rekayasa Sistem SMA/SMK</h3>
                <ul>
                    <li><strong>Prasyarat Terukur:</strong> Telah menyelesaikan kurikulum robotika SMP atau menguasai dasar C++ (variabel, fungsi, array, percabangan).</li>
                    <li><strong>Bebas Beban Heavy Networking:</strong> Web Dashboard &amp; WebSocket disediakan sebagai <em>Pre-Built Starter Library</em> (<code>MazeBotStarter.h</code>); siswa fokus 100% pada logika telemetri &amp; algoritma navigasi.</li>
                    <li><strong>Deteksi Persimpangan Murni 3x Sensor Ultrasonik:</strong> Klasifikasi T-Junction, Crossroad, Corner, &amp; Dead-End berbasis bukaan ultrasonik; sensor TCRT5000 dikhususkan murni sebagai Detektor Garis Finish.</li>
                    <li><strong>Closed-Loop Threshold Correction &amp; Dead-End Elimination:</strong> Mencakup koreksi dinding proporsional dan algoritma pemangkasan array (<em>L+U+L=S, L+U+S=R</em>) untuk <em>Speed Run</em>.</li>
                </ul>
            </div>
        </div>

        <div class="cover-footer">
            <div>
                <strong>Edisi Revisi Total Kurikulum MazeBot EduKit</strong><br>
                Lengkap dengan Source Code C++, Path Simplification Engine, &amp; Capstone Project
            </div>
            <div style="text-align: right;">
                <strong>Kode Dokumen:</strong> EDU-MB-SMA-2026<br>
                <strong>Total Modul:</strong> 16 Pertemuan (M-01 – M-16)
            </div>
        </div>
    </div>

    <!-- FRONTMATTER: ARCHITECTURE & TOC -->
    <div class="page-break">
        <div class="section-header">
            <h1>Arsitektur Starter Platform &amp; Daftar Isi</h1>
            <p>Buku Pegangan Terpadu Guru &amp; Siswa — Tingkat SMA / SMK (Kelas X–XII)</p>
        </div>

        <div class="alert alert-success">
            <span class="alert-title">✅ PENYESUAIAN KURIKULUM REALISTIS (HARDWARE &amp; ALGORITMA)</span>
            <ul style="padding-left: 18px; margin-top: 4px;">
                <li><strong>Tanpa Klaim Odometry Motor TT:</strong> Mengingat motor DC Gearbox TT tidak memiliki rotary encoder, koreksi lintasan menggunakan <em>Closed-Loop Threshold/Proportional Correction</em> berbasis bacaan riil sensor ultrasonik samping.</li>
                <li><strong>Pemisahan Peran Sensor Secara Tegas:</strong> 3x Sensor Ultrasonik menangani seluruh deteksi dinding dan klasifikasi persimpangan, sedangkan 1x Sensor Inframerah TCRT5000 di bagian bawah dikhususkan murni sebagai pemicu Garis Finish.</li>
                <li><strong>Pre-Built Web Dashboard API:</strong> Siswa cukup memanggil <code>bot.sendTelemetry()</code> dan <code>bot.sendRouteSummary()</code> tanpa perlu memprogram raw FreeRTOS task atau LittleFS server dari nol.</li>
            </ul>
        </div>

        <h3 class="sub-heading">📋 Daftar Isi Kurikulum Tingkat SMA/SMK (M-01 s/d M-16)</h3>
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
    out_path = os.path.join(os.path.dirname(__file__), "Modul_Ajar_MazeBot_SMA_SMK.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated SMA HTML at: {out_path}")

if __name__ == "__main__":
    generate_sma_html()
