import os
import re
import shutil
from playwright.sync_api import sync_playwright

from generate_sd import generate_sd_html, get_sd_modules
from generate_smp import generate_smp_html, get_smp_modules
from generate_sma import generate_sma_html, get_sma_modules
import html as html_lib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

def slugify(text):
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    return re.sub(r'[\s-]+', '_', text).strip('_')

def build_single_module_html(level_tag, theme_class, mod, is_sd=False):
    objectives_li = "".join([f"<li>{obj}</li>" for obj in mod["objectives"]])
    steps_li = "".join([f'<li><span class="step-num">{i+1}</span>{s}</li>' for i, s in enumerate(mod["steps"])])

    if is_sd:
        code_section = f"""
        <h3 class="sub-heading">💻 C. Susunan Balok Kode Visual &amp; Logika Program</h3>
        {mod['code_block']}
        """
        safety_class = "alert-danger"
        safety_title = "🛡️ SOP Keselamatan Kerja &amp; Baterai 18650 (Wajib Dipatuhi)"
    else:
        escaped_code = html_lib.escape(mod["cpp_code"])
        code_section = f"""
        <h3 class="sub-heading">💻 C. Kode Program Lengkap (Arduino C++ ESP32)</h3>
        <div class="code-box">
            <div class="code-header">
                <span>📄 MazeBot_{level_tag}_{mod['code']}.ino</span>
                <span>Platform: ESP32 | Baud: 115200</span>
            </div>
            <pre>{escaped_code}</pre>
        </div>
        """
        safety_class = "alert-info"
        safety_title = "⚡ Standar Keselamatan Laboratorium &amp; Perangkat Keras"

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{level_tag} {mod['code']} - {mod['title']}</title>
    <link rel="stylesheet" href="{os.path.join(BASE_DIR, 'css', 'modul_style.css').replace(os.sep, '/')}">
</head>
<body class="{theme_class}">
    <div id="{mod['code']}">
        <div class="module-banner">
            <div class="module-banner-left">
                <span class="mod-code">MODUL {mod['code']} &bull; TINGKAT {level_tag}</span>
                <h2>{mod['title']}</h2>
            </div>
            <div class="module-banner-right">
                <div><strong>Alokasi:</strong> {mod['duration']}</div>
                <div><strong>Fase:</strong> {mod['phase']}</div>
            </div>
        </div>

        <div class="card">
            <h3>🎯 Target Kemampuan &amp; Capaian Pembelajaran</h3>
            <ul>{objectives_li}</ul>
        </div>

        <div class="alert {safety_class}">
            <span class="alert-title">{safety_title}</span>
            {mod['safety']}
        </div>

        <h3 class="sub-heading">📖 A. Konsep Kunci &amp; Materi Pembelajaran</h3>
        {mod['theory']}

        <h3 class="sub-heading">🛠️ B. Langkah Kerja Praktikum</h3>
        <ul class="steps-list">
            {steps_li}
        </ul>

        {code_section}

        <div class="lks-box">
            <div class="lks-header">
                <span>📝 D. Lembar Kerja Siswa (LKS) — {mod['code']}</span>
                <span>Kelompok / Kelas: ..............................</span>
            </div>
            {mod['lks']}
        </div>

        <div class="alert alert-warning">
            <span class="alert-title">🔧 Panduan Guru: Troubleshooting &amp; Tips Kelas</span>
            {mod['troubleshooting']}
        </div>
    </div>
</body>
</html>"""

def render_pdf(page, html_path, pdf_path, footer_label):
    file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    page.goto(file_url, wait_until="networkidle")
    footer_template = f"""
    <div style="width: 100%; font-family: 'Segoe UI', Arial, sans-serif; font-size: 7.5pt; color: #64748b; padding: 0 15mm; display: flex; justify-content: space-between; align-items: center;">
        <span>Kurikulum Resmi MazeBot EduKit &bull; {footer_label}</span>
        <span>Halaman <span class="pageNumber"></span> dari <span class="totalPages"></span></span>
    </div>
    """
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        display_header_footer=True,
        header_template="<div></div>",
        footer_template=footer_template,
        margin={"top": "15mm", "bottom": "16mm", "left": "15mm", "right": "15mm"}
    )

def main():
    print("1. Generating complete HTML files...")
    generate_sd_html()
    generate_smp_html()
    generate_sma_html()

    per_kode_dir = os.path.join(BASE_DIR, "Modul_PDF_Per_Kode")
    for sub in ["SD", "SMP", "SMA_SMK"]:
        os.makedirs(os.path.join(per_kode_dir, sub), exist_ok=True)

    temp_html_dir = os.path.join(BASE_DIR, "_temp_html")
    os.makedirs(temp_html_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Render Full Books
        books = [
            ("Modul_Ajar_MazeBot_SD.html", "Modul_Ajar_MazeBot_SD.pdf", "Tingkat SD (Kelas 4–6) — M-01 s/d M-16"),
            ("Modul_Ajar_MazeBot_SMP.html", "Modul_Ajar_MazeBot_SMP.pdf", "Tingkat SMP (Kelas 8–9) — M-01 s/d M-16"),
            ("Modul_Ajar_MazeBot_SMA_SMK.html", "Modul_Ajar_MazeBot_SMA_SMK.pdf", "Tingkat SMA/SMK (Kelas X–XII) — M-01 s/d M-16"),
        ]

        for html_name, pdf_name, label in books:
            html_p = os.path.join(BASE_DIR, html_name)
            pdf_p = os.path.join(BASE_DIR, pdf_name)
            print(f"Rendering Full Book PDF: {pdf_name} ...")
            render_pdf(page, html_p, pdf_p, label)
            # Also copy to workspace root d:\Penelitian\
            shutil.copy2(pdf_p, os.path.join(ROOT_DIR, pdf_name))

        # Render Individual Module PDFs per Code (M-01 .. M-16)
        levels = [
            ("SD", "theme-sd", get_sd_modules(), True),
            ("SMP", "theme-smp", get_smp_modules(), False),
            ("SMA_SMK", "theme-sma", get_sma_modules(), False),
        ]

        for level_tag, theme_cls, mods, is_sd in levels:
            print(f"Rendering 16 individual module PDFs for {level_tag}...")
            for m in mods:
                single_html = build_single_module_html(level_tag, theme_cls, m, is_sd=is_sd)
                tmp_html_path = os.path.join(temp_html_dir, f"{level_tag}_{m['code']}.html")
                with open(tmp_html_path, "w", encoding="utf-8") as f:
                    f.write(single_html)

                safe_title = slugify(m["title"])[:40]
                out_pdf_name = f"{level_tag}_{m['code']}_{safe_title}.pdf"
                out_pdf_path = os.path.join(per_kode_dir, level_tag, out_pdf_name)
                render_pdf(page, tmp_html_path, out_pdf_path, f"{level_tag} — Modul {m['code']}: {m['title']}")

        browser.close()

    shutil.rmtree(temp_html_dir, ignore_errors=True)
    print("ALL PDFs GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
