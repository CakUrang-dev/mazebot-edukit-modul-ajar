import os
import re
import json
from generate_sd import get_sd_modules
from generate_smp import get_smp_modules
from generate_sma import get_sma_modules

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web")
os.makedirs(WEB_DIR, exist_ok=True)

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
        cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
        return cleaned
    elif isinstance(val, list):
        return [clean_emojis(x) for x in val]
    elif isinstance(val, dict):
        return {k: clean_emojis(v) for k, v in val.items()}
    return val

def slugify(text):
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    return re.sub(r'[\s-]+', '_', text).strip('_')

def prepare_dataset():
    sd_mods = clean_emojis(get_sd_modules())
    smp_mods = clean_emojis(get_smp_modules())
    sma_mods = clean_emojis(get_sma_modules())

    for m in sd_mods:
        safe_title = slugify(m["title"])[:40]
        m["pdf_url"] = f"Modul_PDF_Per_Kode/SD/SD_{m['code']}_{safe_title}.pdf"
        m["level"] = "SD"

    for m in smp_mods:
        safe_title = slugify(m["title"])[:40]
        m["pdf_url"] = f"Modul_PDF_Per_Kode/SMP/SMP_{m['code']}_{safe_title}.pdf"
        m["level"] = "SMP"

    for m in sma_mods:
        safe_title = slugify(m["title"])[:40]
        m["pdf_url"] = f"Modul_PDF_Per_Kode/SMA_SMK/SMA_SMK_{m['code']}_{safe_title}.pdf"
        m["level"] = "SMA"

    dataset = {
        "SD": {
            "id": "SD",
            "name": "Tingkat SD (Kelas 4–6)",
            "Badge": "TINGKAT SD",
            "tagline": "Petualangan Logika & Pengendali Robot Cilik",
            "platform": "Visual Block Programming (Blockly/Scratch) & Web Dashboard D-Pad",
            "sop": "Modul baterai 18650 berada di holder tertutup baut; pemasangan & pengisian daya 100% dilakukan oleh Guru/Instruktur.",
            "book_pdf": "Modul_Ajar_MazeBot_SD.pdf",
            "color": "#5CE1E6",
            "modules": sd_mods
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
            "modules": smp_mods
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
            "modules": sma_mods
        }
    }

    js_content = "window.MAZEBOT_DATA = " + json.dumps(dataset, ensure_ascii=False, indent=2) + ";\n"
    with open(os.path.join(WEB_DIR, "modules_data.js"), "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Generated clean emoji-free web/modules_data.js")

if __name__ == "__main__":
    prepare_dataset()
