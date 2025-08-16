#!/bin/bash

echo "🚀 Iniciando Microservicio de Optimización de Portafolio"
echo "=================================================="

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Por favor instala Docker primero."
    exit 1
fi

# Verificar si Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no está instalado. Por favor instala Docker Compose primero."
    exit 1
fi

echo "✅ Docker y Docker Compose están instalados"

# Construir y ejecutar los servicios
echo "🔨 Construyendo y ejecutando servicios..."
docker-compose up --build -d

# Esperar un momento para que los servicios se inicien
echo "⏳ Esperando que los servicios se inicien..."
sleep 10

# Verificar el estado de los servicios
echo "🔍 Verificando estado de los servicios..."

# Verificar backend
if curl -s http://localhost:5000/health > /dev/null; then
    echo "✅ Backend está funcionando en http://localhost:5000"
else
    echo "❌ Backend no está respondiendo"
fi

# Verificar frontend
if curl -s http://localhost:3000 > /dev/null; then
    echo "✅ Frontend está funcionando en http://localhost:3000"
else
    echo "❌ Frontend no está respondiendo"
fi

echo ""
echo "🎉 ¡Servicios iniciados exitosamente!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:5000"
echo "📚 Documentación: http://localhost:5000/health"
echo ""
echo "Para detener los servicios, ejecuta: docker-compose down"
echo "Para ver los logs, ejecuta: docker-compose logs -f"
