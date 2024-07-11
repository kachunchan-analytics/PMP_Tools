@echo off
cd /d "C:\Users\Andy\Desktop\python_work_github\PMP_GITHUB\PMP_Tools"
rem cd /d %cd%
python change_TXT_to_PY.py
git add . 
git commit -m "Updated new tools for PMP"
git push