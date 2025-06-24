import os
import subprocess
import sys

def build_exe():
    """Script para compilar ClaveGen.py en un archivo ejecutable"""
    
    print("🔧 Iniciando proceso de compilación de ClaveGen...")
    
    # Verificar que PyInstaller esté instalado
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado")
    except ImportError:
        print("❌ PyInstaller no encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Usar archivo de especificación personalizado que incluye todas las dependencias
    pyinstaller_cmd = [
        "pyinstaller",
        "ClaveGen_custom.spec",         # Usar especificación personalizada
        "--distpath=dist",              # Carpeta de salida
        "--clean"                       # Limpiar archivos temporales
    ]
    
    print("🚀 Ejecutando PyInstaller...")
    print(f"Comando: {' '.join(pyinstaller_cmd)}")
    
    try:
        result = subprocess.run(pyinstaller_cmd, check=True, capture_output=True, text=True)
        print("✅ Compilación exitosa!")
        print(f"📁 El archivo ejecutable se encuentra en: dist/ClaveGen.exe")
        
        # Verificar que el archivo se creó
        exe_path = "dist/ClaveGen.exe"
        if os.path.exists(exe_path):
            size = os.path.getsize(exe_path) / (1024 * 1024)  # Tamaño en MB
            print(f"📊 Tamaño del ejecutable: {size:.2f} MB")
        
    except subprocess.CalledProcessError as e:
        print("❌ Error durante la compilación:")
        print(e.stderr)
        return False
    
    return True

if __name__ == "__main__":
    success = build_exe()
    if success:
        print("\n🎉 ¡Compilación completada exitosamente!")
        print("📋 Puedes encontrar tu ejecutable en la carpeta 'dist'")
        input("Presiona Enter para continuar...")
    else:
        print("\n💥 Hubo errores durante la compilación")
        input("Presiona Enter para continuar...") 