@echo off
echo.
echo ========================================
echo   ClaveGen - Compilador a EXE
echo ========================================
echo.

REM Verificar que Python esté instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no encontrado. Por favor instala Python primero.
    pause
    exit /b 1
)

echo ✅ Python encontrado

REM Instalar dependencias si es necesario
echo 📦 Verificando dependencias...
pip install -r requirements.txt

echo.
echo 🔧 Iniciando compilación con PyInstaller...
echo.

REM Compilar con PyInstaller usando especificación personalizada
pyinstaller ClaveGen_custom.spec --distpath=dist --clean

if errorlevel 1 (
    echo.
    echo ❌ Error durante la compilación
    pause
    exit /b 1
)

echo.
echo ✅ ¡Compilación exitosa!
echo 📁 El archivo ejecutable se encuentra en: dist\ClaveGen.exe
echo.

REM Verificar que el archivo existe
if exist "dist\ClaveGen.exe" (
    echo 🎉 El archivo ClaveGen.exe ha sido creado correctamente
    echo.
    echo ¿Quieres abrir la carpeta dist? (S/N)
    set /p choice=
    if /i "%choice%"=="S" start explorer dist
) else (
    echo ❌ No se pudo encontrar el archivo ejecutable
)

echo.
pause 