@echo off
set fullname=.\RUN.exe
set prog=RUN.exe
 
:begin
tasklist /fi "IMAGENAME eq %prog%"|>nul find "%prog%"||start "" "%fullname%"
>nul ping 127.1 -n 2
goto :begin