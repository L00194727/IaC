:: Batch file to take arguments at runtime 
:: By: Edmund Connolly
:: Initial file: 20 OCT 25
:: Filename: Demo6.bat

@echo off
cls
title Edmund's user prompt test
echo *******************************************
echo Welcome 
echo This batch file will do stuff
echo This is for demonstration purposes only.
echo *******************************************

set /p NAME=What is your name?
echo Your name is %NAME%