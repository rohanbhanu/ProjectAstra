@echo off

start cmd /k "py -m uvicorn backend.app:app --reload"

timeout /t 2 > nul

start cmd /k "py -m streamlit run frontend/app.py"