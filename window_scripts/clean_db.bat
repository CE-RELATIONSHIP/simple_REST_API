@echo off
setlocal

:: Define directories to delete
set "DIRS=db\dev db\test"

:: Loop through directories and remove them
for %%D in (%DIRS%) do (
    if exist "%%D" (
        echo Removing directory: %%D
        rmdir /s /q "%%D"
    ) else (
        echo Directory %%D does not exist.
    )
)

echo Cleanup completed.
endlocal
