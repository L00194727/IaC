:: Batch file to demonstrate conditional branching 
:: By: Edmund Connolly
:: Initial file: 20 OCT 25
:: Filename: Demo7.bat

@echo off
cls
title Edmund's Find a File
echo *******************************************
echo This batch file will do stuff
echo This is for demonstration purposes only.
echo *******************************************

SET ospath=C:\Windows\
SET filename=explorer.exe

If exist %ospath%%filename% (
	echo %filename% exists
) else (
	echo No file named %filename%
) 