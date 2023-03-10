@echo off

call %~dp0TGbot\venv\Scripts\activate

cd %~dp0TGbot

set TOKEN=

python tgbot.py

pause