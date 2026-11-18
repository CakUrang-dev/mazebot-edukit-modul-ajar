import os
import re
import shutil
import html as html_lib
from playwright.sync_api import sync_playwright

from generate_sd import get_sd_modules
from generate_smp import get_smp_modules
from generate_sma import get_sma_modules

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# Regex to strip all Unicode emojis/pictographs for strict vector-icon consistency
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U00002600-\U000027BF"
    "\U0001FA00-\U0001FAFF"
    "\U00002300-\U000023FF"
    "\U00002B50-\U00002B55"
    "\U0000FE0F"
    "]+",
    flags=re.UNICODE,
)

def clean_emojis(val):
    if isinstance(val, str):
        cleaned = EMOJI_PATTERN.sub("", val)
        return cleaned.strip()
    elif isinstance(val, list):
        return [clean_emojis(x) for x in val]
    elif isinstance(val, dict):
        return {k: clean_emojis(v) for k, v in val.items()}
    return val

def slugify(text):
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    return re.sub(r'[\s-]+', '_', text).strip('_')

# Lucide Vector SVG Icons (stroke-width="2.5") wrapped in 2px solid black square box
SVGS = {
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "idea": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>',
    "alert": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>',
    "check": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "task": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>',
    "wrench": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
}

def doc_icon(name):
    return f'<span class="nb-doc-icon">{SVGS[name]}</span>'

def render_module_block(level_label, mod, is_sd=False, page_break=True):
    objectives_li = "".join([f"<li>{obj}</li>" for obj in mod["objectives"]])
    steps_li = "".join([f'<li><span class="step-num">{i+1}</span>{s}</li>' for i, s in enumerate(mod["steps"])])

    if is_sd:
        code_card = f"""
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-tujuan">
                <div class="nb-doc-card-title">{doc_icon("code")} <span>C. Susunan Balok Kode Visual &amp; Logika Program</span></div>
                <span class="nb-doc-card-tag">BLOCKLY VISUAL LOGIC</span>
            </div>
            <div class="nb-doc-card-body">
                {mod['code_block']}
            </div>
        </div>
        """
    else:
        escaped_code = html_lib.escape(mod["cpp_code"])
        code_card = f"""
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-tujuan">
                <div class="nb-doc-card-title">{doc_icon("code")} <span>C. Kode Program Lengkap (Arduino C++ ESP32)</span></div>
                <span class="nb-doc-card-tag">SOURCE CODE .INO</span>
            </div>
            <div class="nb-doc-card-body">
                <div class="code-box">
                    <div class="code-header">
                        <span>FILE: MazeBot_{mod['code']}.ino</span>
                        <span>BOARD: DOIT ESP32 DEVKIT V1 | BAUD: 115200</span>
                    </div>
                    <pre>{escaped_code}</pre>
                </div>
            </div>
        </div>
        """

    container_cls = "module-page" if page_break else ""
    return f"""
    <div class="{container_cls}" id="{mod['code']}">
        <!-- Header Judul Bab (#FFDE59, 3px solid #000, 6px 6px 0px #000) -->
        <div class="module-banner">
            <div class="module-banner-left">
                <span class="mod-code">BAB / MODUL {mod['code']} &bull; {level_label}</span>
                <h2>{mod['title']}</h2>
            </div>
            <div class="module-banner-right">
                <div>ESTIMASI: {mod['duration']}</div>
                <div>TARGET: {mod['phase']}</div>
            </div>
        </div>

        <!-- Callout 1: Tujuan Pembelajaran (#5CE1E6 Biru Langit) -->
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-tujuan">
                <div class="nb-doc-card-title">{doc_icon("check")} <span>Tujuan Pembelajaran &amp; Target Kemampuan</span></div>
                <span class="nb-doc-card-tag">CAPAIAN KOMPETENSI</span>
            </div>
            <div class="nb-doc-card-body">
                <ul>{objectives_li}</ul>
            </div>
        </div>

        <!-- Callout 2: SOP Keselamatan (#FFDE59 Kuning Cerah) -->
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-peringatan">
                <div class="nb-doc-card-title">{doc_icon("alert")} <span>SOP Keselamatan Kerja &amp; Perangkat Keras</span></div>
                <span class="nb-doc-card-tag">WAJIB DIPATUHI</span>
            </div>
            <div class="nb-doc-card-body">
                <p style="margin-bottom:0;">{mod['safety']}</p>
            </div>
        </div>

        <!-- Callout 3: Ringkasan / Poin Kunci & Materi (#7ED957 Hijau Lime) -->
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-kunci">
                <div class="nb-doc-card-title">{doc_icon("idea")} <span>A. Konsep Kunci, Ringkasan &amp; Materi Pembelajaran</span></div>
                <span class="nb-doc-card-tag">RINGKASAN &amp; POIN KUNCI</span>
            </div>
            <div class="nb-doc-card-body">
                {mod['theory']}
            </div>
        </div>

        <!-- Callout 4: Langkah Kerja Praktikum (#7ED957 Hijau Lime) -->
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-kunci">
                <div class="nb-doc-card-title">{doc_icon("book")} <span>B. Langkah Kerja Praktikum</span></div>
                <span class="nb-doc-card-tag">PROSEDUR EKSPERIMEN</span>
            </div>
            <div class="nb-doc-card-body">
                <ul class="steps-list">{steps_li}</ul>
            </div>
        </div>

        <!-- Callout 5: Kode Program / Balok Visual -->
        {code_card}

        <!-- Callout 6: Latihan / Tugas / LKS (#CB6CE6 Ungu Pastel) -->
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-latihan">
                <div class="nb-doc-card-title">{doc_icon("task")} <span>D. Latihan, Tugas &amp; Lembar Kerja Siswa (LKS) — {mod['code']}</span></div>
                <span class="nb-doc-card-tag">LATIHAN &amp; TUGAS</span>
            </div>
            <div class="nb-doc-card-body">
                {mod['lks']}
            </div>
        </div>

        <!-- Callout 7: Troubleshooting & Catatan Guru (#FFDE59) -->
        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-peringatan">
                <div class="nb-doc-card-title">{doc_icon("wrench")} <span>Panduan Troubleshooting &amp; Catatan Praktikum</span></div>
                <span class="nb-doc-card-tag">SOLUSI TEKNIS</span>
            </div>
            <div class="nb-doc-card-body">
                <p style="margin-bottom:0;">{mod['troubleshooting']}</p>
            </div>
        </div>
    </div>
    """

def build_full_book_html(level_id, level_title, subtitle, doc_code, highlights, frontmatter_extra, modules, is_sd=False):
    css_rel = "css/modul_style.css"
    toc_rows = "".join([
        f"""
        <tr>
            <td class="toc-code">{m['code']}</td>
            <td><strong>{m['title']}</strong></td>
            <td class="font-mono">{m['duration']}</td>
            <td class="font-mono">{m['phase']}</td>
        </tr>
        """
        for m in modules
    ])

    highlights_li = "".join([f"<li>{h}</li>" for h in highlights])
    modules_html = "".join([render_module_block(level_title, m, is_sd=is_sd, page_break=True) for m in modules])

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Modul Ajar MazeBot EduKit — {level_title}</title>
    <link rel="stylesheet" href="{css_rel}">
</head>
<body>

    <!-- SAMPUL NEO-BRUTALIST A4 -->
    <div class="cover-page">
        <div>
            <div class="cover-header-box">
                <span class="cover-badge">KURIKULUM ROBOTIKA &amp; PEMROGRAMAN STEM NASIONAL</span>
                <div class="cover-title">MODUL AJAR &amp; LKS<br>MAZEBOT EDUKIT</div>
                <div class="cover-subtitle">{level_title}<br>"{subtitle}"</div>
            </div>

            <div class="cover-highlights">
                <div class="cover-highlights-header">
                    {doc_icon("idea")}
                    <span>Spesifikasi Pedagogis &amp; Standar Teknis Kurikulum</span>
                </div>
                <ul>{highlights_li}</ul>
            </div>
        </div>

        <div class="cover-footer">
            <div>
                <strong>EDISI NEO-BRUTALIST SIAP CETAK (A4)</strong><br>
                Lengkap dengan Materi, Kode Program, LKS Siswa, &amp; Panduan Troubleshooting
            </div>
            <div style="text-align: right;">
                <strong>KODE:</strong> {doc_code}<br>
                <strong>TOTAL:</strong> 16 MODUL (M-01 – M-16)
            </div>
        </div>
    </div>

    <!-- DAFTAR ISI & PANDUAN UMUM -->
    <div class="page-break">
        <div class="section-header">
            <h1>Panduan Umum, Standar Sistem &amp; Daftar Isi</h1>
            <p>Buku Pegangan Terpadu Guru &amp; Siswa — {level_title}</p>
        </div>

        {frontmatter_extra}

        <div class="nb-doc-card">
            <div class="nb-doc-card-header header-tujuan">
                <div class="nb-doc-card-title">{doc_icon("book")} <span>Daftar Isi Kurikulum (M-01 s/d M-16)</span></div>
                <span class="nb-doc-card-tag">16 PERTEMUAN</span>
            </div>
            <div class="nb-doc-card-body">
                <table class="toc-table">
                    <thead>
                        <tr>
                            <th style="width: 11%;">Kode Bab</th>
                            <th style="width: 49%;">Topik Materi Modul</th>
                            <th style="width: 18%;">Estimasi Waktu</th>
                            <th style="width: 22%;">Target Fase</th>
                        </tr>
                    </thead>
                    <tbody>{toc_rows}</tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- SELURUH 16 MODUL -->
    {modules_html}

</body>
</html>"""

def build_single_module_html(level_title, mod, is_sd=False):
    css_abs = os.path.join(BASE_DIR, "css", "modul_style.css").replace(os.sep, "/")
    body_html = render_module_block(level_title, mod, is_sd=is_sd, page_break=False)
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{level_title} — {mod['code']}: {mod['title']}</title>
    <link rel="stylesheet" href="{css_abs}">
</head>
<body>
    {body_html}
</body>
</html>"""

def render_pdf(page, html_path, pdf_path, footer_label):
    file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    page.goto(file_url, wait_until="networkidle")
    footer_template = f"""
    <div style="width: 100%; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 7.5pt; font-weight: 700; color: #000000; padding: 0 15mm; display: flex; justify-content: space-between; align-items: center;">
        <span>MAZEBOT EDUKIT &bull; {footer_label}</span>
        <span>HALAMAN <span class="pageNumber"></span> / <span class="totalPages"></span></span>
    </div>
    """
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        display_header_footer=True,
        header_template="<div></div>",
        footer_template=footer_template,
        margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
    )

def main():
    sd_mods = clean_emojis(get_sd_modules())
    smp_mods = clean_emojis(get_smp_modules())
    sma_mods = clean_emojis(get_sma_modules())

    # 1. Generate 3 Full Book HTMLs (Neo-Brutalist A4)
    sd_front = f"""
    <div class="nb-doc-card">
        <div class="nb-doc-card-header header-peringatan">
            <div class="nb-doc-card-title">{doc_icon("alert")} <span>Prosedur Operasional Standar (SOP) Keselamatan Baterai 18650 (Khusus Guru)</span></div>
            <span class="nb-doc-card-tag">K3 LABORATORIUM SD</span>
        </div>
        <div class="nb-doc-card-body">
            <ol>
                <li><strong>Holder Tertutup Baut:</strong> Sel baterai Lithium-Ion 18650 pada unit MazeBot SD wajib dipasang di dalam <em>battery enclosure</em> tertutup yang dikunci menggunakan baut pengaman.</li>
                <li><strong>Otoritas Guru/Instruktur:</strong> Siswa SD <strong>DILARANG KERAS</strong> membuka penutup baterai, melepas sel 18650, atau menghubungkan baterai ke charger eksternal. Seluruh proses charging dan pergantian baterai dilakukan oleh Guru.</li>
                <li><strong>Inspeksi Pra-Kelas:</strong> Sebelum membagikan robot ke meja kelompok, Guru memastikan saklar pada posisi OFF, kabel motor tidak terkelupas, dan stiker identitas Wi-Fi (SSID &amp; Password) terbaca jelas.</li>
            </ol>
        </div>
    </div>
    """

    smp_front = f"""
    <div class="nb-doc-card">
        <div class="nb-doc-card-header header-kunci">
            <div class="nb-doc-card-title">{doc_icon("code")} <span>Tabel Standar Pemetaan Pin (Pinout) MazeBot EduKit ESP32</span></div>
            <span class="nb-doc-card-tag">REFERENSI GPIO</span>
        </div>
        <div class="nb-doc-card-body">
            <table class="std-table">
                <thead>
                    <tr><th>Modul Perangkat Keras</th><th>Nama Pin Modul</th><th>Pin GPIO ESP32</th><th>Keterangan Arah &amp; Fungsi</th></tr>
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
        </div>
    </div>
    """

    sma_front = f"""
    <div class="nb-doc-card">
        <div class="nb-doc-card-header header-kunci">
            <div class="nb-doc-card-title">{doc_icon("idea")} <span>Spesifikasi Arsitektur Starter Platform &amp; Algoritma SMA/SMK</span></div>
            <span class="nb-doc-card-tag">REKAYASA SISTEM</span>
        </div>
        <div class="nb-doc-card-body">
            <ul>
                <li><strong>Tanpa Klaim Odometry Motor TT:</strong> Mengingat motor DC Gearbox TT tidak memiliki rotary encoder, koreksi lintasan menggunakan <em>Closed-Loop Threshold/Proportional Correction</em> berbasis bacaan riil sensor ultrasonik samping.</li>
                <li><strong>Pemisahan Peran Sensor Secara Tegas:</strong> 3x Sensor Ultrasonik menangani seluruh deteksi dinding dan klasifikasi persimpangan, sedangkan 1x Sensor Inframerah TCRT5000 di bagian bawah dikhususkan murni sebagai pemicu Garis Finish.</li>
                <li><strong>Pre-Built Web Dashboard API:</strong> Siswa cukup memanggil <code>bot.sendTelemetry()</code> dan <code>bot.sendRouteSummary()</code> tanpa perlu memprogram raw FreeRTOS task atau LittleFS server dari nol.</li>
            </ul>
        </div>
    </div>
    """

    books_spec = [
        (
            "Modul_Ajar_MazeBot_SD.html",
            "Modul_Ajar_MazeBot_SD.pdf",
            "TINGKAT SD (KELAS 4–6)",
            "Petualangan Logika & Pengendali Robot Cilik",
            "EDU-MB-SD-2026",
            [
                "<strong>Platform Ramah Anak:</strong> Visual Block Programming (Blockly/Scratch) &amp; Web Dashboard D-Pad Interaktif.",
                "<strong>SOP Keselamatan Baterai 18650 (Guru Only):</strong> Baterai terkunci rapat di dalam holder tertutup baut; pemasangan dan pengisian daya 100% dilakukan oleh Guru.",
                "<strong>Pre-Configured Wi-Fi SoftAP:</strong> Setiap unit robot memiliki SSID &amp; Password unik tertera pada stiker bodi robot.",
                "<strong>16 Modul Terstruktur (M-01 s/d M-16):</strong> Lengkap dari pengenalan bagian robot, algoritma unplugged, kendali D-Pad, sensor ultrasonik, sensor garis TCRT5000, hingga Rescue Mission."
            ],
            sd_front,
            sd_mods,
            True
        ),
        (
            "Modul_Ajar_MazeBot_SMP.html",
            "Modul_Ajar_MazeBot_SMP.pdf",
            "TINGKAT SMP (KELAS 8–9)",
            "Logika Pemrograman C++ & Navigasi Robot Otonom",
            "EDU-MB-SMP-2026",
            [
                "<strong>Transisi Mulus (Hybrid Block-to-Text):</strong> Dilengkapi modul jembatan Side-by-Side Code Viewer sebelum masuk ke pemrograman C++ di Arduino IDE.",
                "<strong>Integrasi Kurikulum IPA Fisika Kelas 8:</strong> Implementasi rumus pemantulan gelombang bunyi (<em>s = v &times; t / 2</em> dengan cepat rambat bunyi 340 m/s) secara nyata pada sensor ultrasonik.",
                "<strong>Arsitektur Hardware Modular:</strong> Fokus pada fungsi modul ESP32, Driver DRV8833, 3x Sensor Ultrasonik HC-SR04 (Anti-Crosstalk), dan Sensor Garis TCRT5000.",
                "<strong>Algoritma Wall-Follower &amp; Kalibrasi Nyata:</strong> Mencakup <em>Left-Hand Rule</em>, <em>Wall Offset</em>, <em>Dead-End U-Turn</em>, serta sesi khusus kompensasi deviasi motor DC TT."
            ],
            smp_front,
            smp_mods,
            False
        ),
        (
            "Modul_Ajar_MazeBot_SMA_SMK.html",
            "Modul_Ajar_MazeBot_SMA_SMK.pdf",
            "TINGKAT SMA / SMK (KELAS X–XII)",
            "Algoritma Komputasi Navigasi & Reduksi Rute Labirin",
            "EDU-MB-SMA-2026",
            [
                "<strong>Prasyarat Terukur:</strong> Telah menyelesaikan kurikulum robotika SMP atau menguasai dasar C++ (variabel, fungsi, array, percabangan).",
                "<strong>Bebas Beban Heavy Networking:</strong> Web Dashboard &amp; WebSocket disediakan sebagai <em>Pre-Built Starter Library</em> (<code>MazeBotStarter.h</code>); siswa fokus 100% pada logika telemetri &amp; algoritma navigasi.",
                "<strong>Deteksi Persimpangan Murni 3x Sensor Ultrasonik:</strong> Klasifikasi T-Junction, Crossroad, Corner, &amp; Dead-End berbasis bukaan ultrasonik; sensor TCRT5000 dikhususkan murni sebagai Detektor Garis Finish.",
                "<strong>Closed-Loop Threshold Correction &amp; Dead-End Elimination:</strong> Mencakup koreksi dinding proporsional dan algoritma pemangkasan array (<em>L+U+L=S, L+U+S=R</em>) untuk <em>Speed Run</em>."
            ],
            sma_front,
            sma_mods,
            False
        )
    ]

    for html_name, pdf_name, lvl_title, sub, code, high, front, mods, is_sd in books_spec:
        html_str = build_full_book_html(code, lvl_title, sub, code, high, front, mods, is_sd=is_sd)
        with open(os.path.join(BASE_DIR, html_name), "w", encoding="utf-8") as f:
            f.write(html_str)
        print(f"Generated Neo-Brutalist A4 HTML: {html_name}")

    per_kode_dir = os.path.join(BASE_DIR, "Modul_PDF_Per_Kode")
    for sub in ["SD", "SMP", "SMA_SMK"]:
        os.makedirs(os.path.join(per_kode_dir, sub), exist_ok=True)

    temp_html_dir = os.path.join(BASE_DIR, "_temp_html")
    os.makedirs(temp_html_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Render 3 Full Books
        for html_name, pdf_name, lvl_title, *_ in books_spec:
            html_p = os.path.join(BASE_DIR, html_name)
            pdf_p = os.path.join(BASE_DIR, pdf_name)
            print(f"Rendering Full Book PDF: {pdf_name} ...")
            render_pdf(page, html_p, pdf_p, f"{lvl_title} — M-01 s/d M-16")
            shutil.copy2(pdf_p, os.path.join(ROOT_DIR, pdf_name))

        # Render 48 Individual Module PDFs
        levels = [
            ("SD", "TINGKAT SD (KELAS 4–6)", sd_mods, True),
            ("SMP", "TINGKAT SMP (KELAS 8–9)", smp_mods, False),
            ("SMA_SMK", "TINGKAT SMA/SMK (KELAS X–XII)", sma_mods, False),
        ]

        for level_tag, lvl_title, mods, is_sd in levels:
            print(f"Rendering 16 individual Neo-Brutalist module PDFs for {level_tag}...")
            for m in mods:
                single_html = build_single_module_html(lvl_title, m, is_sd=is_sd)
                tmp_html_path = os.path.join(temp_html_dir, f"{level_tag}_{m['code']}.html")
                with open(tmp_html_path, "w", encoding="utf-8") as f:
                    f.write(single_html)

                safe_title = slugify(m["title"])[:40]
                out_pdf_name = f"{level_tag}_{m['code']}_{safe_title}.pdf"
                out_pdf_path = os.path.join(per_kode_dir, level_tag, out_pdf_name)
                render_pdf(page, tmp_html_path, out_pdf_path, f"{level_tag} &bull; MODUL {m['code']}: {m['title']}")

        browser.close()

    shutil.rmtree(temp_html_dir, ignore_errors=True)
    print("ALL 51 NEO-BRUTALIST A4 PDFs GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
