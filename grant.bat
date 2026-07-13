@echo off
icacls "C:\one\paperclip-company" /grant:r paperclipuser:(OI)(CI)F /T /Q
echo ICACLS_DONE=%ERRORLEVEL%
