@echo off
for %%i in (*.pdf) do (
	pdftitle -p %%i -c && echo Successfully || (echo %%i) && echo Failed
	)