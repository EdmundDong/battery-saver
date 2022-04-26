@echo off
title Battery Saver
cls
:loop
echo %date:~12,2%-%date:~4,2%-%date:~7,2% %time:~0,8% ^| Watchdog Started
call conda activate battery-saver
python battery_saver.py
echo ***************************************************************
echo %date:~12,2%-%date:~4,2%-%date:~7,2% %time:~0,8% ^| WARNING: Program closed or crashed, restarting.
echo ***************************************************************
goto loop