color 04
title BlackLeakz PYUIC6 GUI Converter


echo CONVERTING UI FILE FROM SRC-PATH: "C:\Users\black\Development\WPA-BRUTEFORCE\GUI\mainwindow\form.ui"
ECHO TO C:\Users\black\Development\WPA-BRUTEFORCE\GUI\mainwindow\mainwindow.py


pyuic6 -o mainwindow.py C:\Users\black\Development\WPA-BRUTEFORCE\GUI\mainwindow\form.ui

ECHO COPIN CONVERTED FILE TO APPLICATION FOLDER NOW!!!


XCOPY /E /H /J C:\Users\black\Development\WPA-BRUTEFORCE\GUI\mainwindow\mainwindow.py C:\Users\black\Development\WPA-BRUTEFORCE\application

dir "C:\Users\black\Development\WPA-BRUTEFORCE\application\mainwindow.py"

