@echo off
echo 🚀 Iniciando Microservicio de Optimización de Portafolio
echo ==================================================

REM Verificar si Docker está instalado
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker no está instalado. Por favor instala Docker primero.
    pause
    exit /b 1
)

REM Verificar si Docker Compose está instalado
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Compose no está instalado. Por favor instala Docker Compose primero.
    pause
    exit /b 1
)

echo ✅ Docker y Docker Compose están instalados

REM Construir y ejecutar los servicios
echo 🔨 Construyendo y ejecutando servicios...
docker-compose up --build -d

REM Esperar un momento para que los servicios se inicien
echo ⏳ Esperando que los servicios se inicien...
timeout /t 10 /nobreak >nul

REM Verificar el estado de los servicios
echo 🔍 Verificando estado de los servicios...

REM Verificar backend
curl -s http://localhost:5000/health >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Backend está funcionando en http://localhost:5000
) else (
    echo ❌ Backend no está respondiendo
)

REM Verificar frontend
curl -s http://localhost:3000 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Frontend está funcionando en http://localhost:3000
) else (
    echo ❌ Frontend no está respondiendo
)

echo.
echo 🎉 ¡Servicios iniciados exitosamente!
echo.
echo 📱 Frontend: http://localhost:3000
echo 🔧 Backend API: http://localhost:5000
echo 📚 Documentación: http://localhost:5000/health
echo.
echo Para detener los servicios, ejecuta: docker-compose down
echo Para ver los logs, ejecuta: docker-compose logs -f
echo.
pause
