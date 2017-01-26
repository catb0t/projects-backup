@echo off
cls && color 08

rem .... the following line creates a [DEL] [ASCII 8] [Backspace] character to use later
rem .... All this to remove [:]
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (set "DEL=%%a")

echo.

<nul set /p="("
call :PainText 09 "BLUE is cold"    && <nul set /p=")  ("
call :PainText 02 "GREEN is earth"  && <nul set /p=")  ("
call :PainText F0 "BLACK is night"  && <nul set /p=")"
echo.
<nul set /p="("
call :PainText 04 "RED is blood"    && <nul set /p=")  ("
call :PainText 0e "YELLOW is pee"   && <nul set /p=")  ("
call :PainText 0F "WHITE all colors"&& <nul set /p=")"

goto :end

:PainText
<nul set /p "=%DEL%" > "%~2"
findstr /v /a:%1 /R "+" "%~2" nul
del "%~2" > nul
goto :eof

:end
echo.
pause