:: Batch file to display success or failure 
:: By: Edmund Connolly
:: Initial file: 20 Oct 25
:: Filename: Demo9.bat

@echo off
cls
title Edmund's Error level tester v.2
echo *******************************************
echo This batch file will do stuff
echo This is for demonstration purposes only.
echo *******************************************

SET ospath=C:\Windows\
SET filename1=explorer.exe
SET filename2=DoesNotExist.exe
copy %ospath%%filename1% %TEMP% && echo Copy of %filename1% worked!
echo.
echo.
copy %ospath%%filename2% %TEMP% || echo Copy of %filename2% failed!