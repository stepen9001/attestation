@echo off
set fullname=.\run.exe
set prog=run.exe
 
:begin
tasklist /fi "IMAGENAME eq %prog%"|>nul find "%prog%"||start "" "%fullname%"
>nul ping 127.1 -n 2
goto :begin