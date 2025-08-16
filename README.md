# Microservicio de Optimización de Portafolio de Inversiones

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

## Descripción

Este proyecto implementa un **microservicio completo** que resuelve el problema de la mochila (knapsack problem) para optimizar la asignación de recursos en un portafolio de inversiones con restricción presupuestaria.

### Características Principales

**Algoritmo de Programación Dinámica** para optimización óptima
**API REST** con validación completa de datos
**Interfaz Web Moderna** con React/TypeScript
**Dockerización Completa** con docker-compose
**Suite de Pruebas** con 15+ casos de prueba
 **Documentación Completa** con ejemplos de uso



## Tecnologías Utilizadas

- **Backend**: Python 3.9+, Flask 2.3.3, Programación Dinámica
- **Frontend**: React 18.2.0, TypeScript 4.7.4, CSS3
- **Contenedores**: Docker, Docker Compose
- **Pruebas**: pytest, cobertura de código
- **Documentación**: Markdown, Postman Collection

## Instalación y Despliegue

### Instalación Rápida (Recomendado)

```bash
# 1. Clonar el repositorio
git clone https://github.com/USERNAME/portfolio-optimization-service.git
cd portfolio-optimization-service

# 2. Ejecutar con Docker (Windows)
start.bat

# O ejecutar con Docker (Linux/Mac)
chmod +x start.sh
./start.sh

# 3. ¡Listo! Abre http://localhost:3000
```

### Opción 1: Usando Docker Compose (Recomendado)
```bash
# Clonar el repositorio
git clone https://github.com/USERNAME/portfolio-optimization-service.git
cd portfolio-optimization-service

# Construir y ejecutar con Docker Compose
docker-compose up --build
```

### Opción 2: Desarrollo Local

#### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## API Endpoints

### POST /optimizar
Optimiza la selección de proyectos de inversión.

**Entrada:**
```json
{
  "capacidad": 10000,
  "objetos": [
    {"nombre": "A", "peso": 2000, "ganancia": 1500},
    {"nombre": "B", "peso": 4000, "ganancia": 3500},
    {"nombre": "C", "peso": 5000, "ganancia": 4000},
    {"nombre": "D", "peso": 3000, "ganancia": 2500}
  ]
}
```

**Salida:**
```json
{
  "seleccionados": ["B", "C"],
  "ganancia_total": 7500,
  "peso_total": 9000
}
```

## Casos de Prueba

### Caso 1: Caso Básico
- Capacidad: 10,000
- Resultado esperado: ["Fondo_B", "Fondo_C", "Fondo_E"]
- Ganancia total: 9,300

### Caso 2: Máximo Aprovechamiento
- Capacidad: 8,000
- Resultado esperado: ["Acción_Y", "Acción_Z", "Bono_Q"]
- Ganancia total: 6,200

### Caso 3: Proyectos de Bajo Costo
- Capacidad: 5,000
- Resultado esperado: ["Cripto_1", "Cripto_2", "ETF_2", "ETF_1"]
- Ganancia total: 4,800

## Características del Algoritmo
- Utiliza programación dinámica para garantizar la solución óptima
- Complejidad temporal: O(n*W) donde n es el número de objetos y W es la capacidad
- Complejidad espacial: O(n*W)

## Validaciones
- Capacidad debe ser un número positivo
- Todos los objetos deben tener nombre, peso y ganancia válidos
- Peso y ganancia deben ser números positivos
- Manejo de errores para datos inválidos

## 📊 Ejemplos de Uso

###  Caso de Prueba 1: Caso Básico
**Entrada:**
```json
{
  "capacidad": 10000,
  "objetos": [
    {"nombre": "A", "peso": 2000, "ganancia": 1500},
    {"nombre": "B", "peso": 4000, "ganancia": 3500},
    {"nombre": "C", "peso": 5000, "ganancia": 4000},
    {"nombre": "D", "peso": 3000, "ganancia": 2500}
  ]
}
```

**Salida Esperada:**
```json
{
  "seleccionados": ["B", "C"],
  "ganancia_total": 7500,
  "peso_total": 9000
}
```

###  Caso de Prueba 2: Máximo Aprovechamiento
**Entrada:**
```json
{
  "capacidad": 8000,
  "objetos": [
    {"nombre": "Acción_X", "peso": 1000, "ganancia": 800},
    {"nombre": "Acción_Y", "peso": 2500, "ganancia": 2200},
    {"nombre": "Acción_Z", "peso": 3000, "ganancia": 2800},
    {"nombre": "Bono_P", "peso": 4000, "ganancia": 3000},
    {"nombre": "Bono_Q", "peso": 1500, "ganancia": 1200}
  ]
}
```

**Salida Esperada:**
```json
{
  "seleccionados": ["Acción_Y", "Acción_Z", "Bono_Q"],
  "ganancia_total": 6200,
  "peso_total": 7000
}
```

## 🧪 Pruebas

```bash
# Ejecutar todas las pruebas
python run_tests.py

# O ejecutar pruebas del backend
cd backend
python -m pytest tests/ -v
```

