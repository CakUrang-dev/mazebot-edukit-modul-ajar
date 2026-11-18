#!/usr/bin/env python3
"""
MazeBot EduKit — Portable Web Server (Cross-Platform PC & Cloud Server)
Dapat dijalankan langsung tanpa library tambahan (Zero-Dependency Standard Library).
"""
import os
import sys
import socket
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MazeBotHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS and proper caching headers for PDFs & static assets
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def main():
    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("HOST", "0.0.0.0")
    no_browser = "--no-browser" in sys.argv or os.environ.get("CI") or os.environ.get("DOCKER_CONTAINER")

    for i, arg in enumerate(sys.argv):
        if arg in ("-p", "--port") and i + 1 < len(sys.argv):
            port = int(sys.argv[i + 1])

    local_ip = get_local_ip()
    server = ThreadingHTTPServer((host, port), MazeBotHandler)

    print("=" * 62)
    print("  MAZEBOT EDUKIT — LEARNING PORTAL & VIRTUAL LAB SERVER")
    print("=" * 62)
    print(f"  [LOKAL PC]     : http://localhost:{port}")
    print(f"  [JARINGAN LAN] : http://{local_ip}:{port}")
    print("  [TEKAN CTRL+C UNTUK MENGHENTIKAN SERVER]")
    print("=" * 62)

    if not no_browser:
        try:
            webbrowser.open(f"http://localhost:{port}")
        except Exception:
            pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Server dihentikan.")
        server.server_close()

if __name__ == "__main__":
    main()
