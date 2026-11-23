@echo off
setlocal
cd /d "%~dp0"
if not exist .venv (
  echo Creating Python virtual environment...
  py -3 -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Starting RoboMentor AI...
python -m streamlit run app.py
pause
