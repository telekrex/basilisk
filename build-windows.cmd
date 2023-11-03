@echo off
echo locating source
cd source
echo compiling...
python -m PyInstaller --onefile basilisk.py
echo moving to release folder
move %~dp0\source\dist\basilisk.exe %~dp0\release\Windows
echo done
pause