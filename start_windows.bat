@echo off
title MazeBot EduKit — Learning Portal Server
cd /d "%~dp0"

echo ==============================================================
echo   MEMULAI SERVER MAZEBOT EDUKIT LEARNING PORTAL...
echo ==============================================================

where python >nul 2>nul
if %errorlevel%==0 (
    python server.py
    goto :eof
)

where py >nul 2>nul
if %errorlevel%==0 (
    py server.py
    goto :eof
)

where npx >nul 2>nul
if %errorlevel%==0 (
    echo [INFO] Python tidak ditemukan, menggunakan Node.js npx serve...
    npx --yes serve -l 8080 .
    goto :eof
)

echo [INFO] Membuka index.html secara langsung di browser default...
start "" "%~dp0index.html"
