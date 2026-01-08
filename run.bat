@echo off
cd /d "C:\Users\RCS\Desktop\ssm"

echo Activating virtual environment...
call venv\Scripts\activate

echo Running app.py...
python app.py

echo.
echo App stopped. Press any key to exit.
pause
