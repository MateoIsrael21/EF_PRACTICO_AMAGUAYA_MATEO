# Documentación de la API - Microservicio de Optimización de Portafolio

## Información General
- **Base URL**: `http://localhost:5000`
- **Versión**: 1.0.0
- **Formato de Respuesta**: JSON

## Endpoints

### 1. Health Check
**GET** `/health`

Verifica el estado del servicio.

**Respuesta Exitosa (200):**
```json
{
  "status": "healthy",
  "service": "Portfolio Optimization Service",
  "version": "1.0.0"
}
```

### 2. Optimizar Portafolio
**POST** `/optimizar`

Optimiza la selección de proyectos de inversión usando programación dinámica.

**Cuerpo de la Petición:**
```json
{
  "capacidad": 10000,
  "objetos": [
    {
      "nombre": "Proyecto_A",
      "peso": 2000,
      "ganancia": 1500
    },
    {
      "nombre": "Proyecto_B", 
      "peso": 4000,
      "ganancia": 3500
    }
  ]
}
```

**Parámetros:**
- `capacidad` (number, requerido): Capacidad presupuestaria total
- `objetos` (array, requerido): Lista de proyectos de inversión
  - `nombre` (string, requerido): Nombre del proyecto
  - `peso` (number, requerido): Costo del proyecto
  - `ganancia` (number, requerido): Ganancia esperada del proyecto

**Respuesta Exitosa (200):**
```json
{
  "seleccionados": ["Proyecto_B"],
  "ganancia_total": 3500,
  "peso_total": 4000
}
```

**Respuesta de Error (400):**
```json
{
  "error": "La capacidad debe ser un número positivo"
}
```

**Respuesta de Error (500):**
```json
{
  "error": "Error interno del servidor",
  "details": "Descripción del error"
}
```

## Códigos de Estado HTTP

- **200**: Operación exitosa
- **400**: Error en los datos de entrada
- **404**: Endpoint no encontrado
- **405**: Método HTTP no permitido
- **500**: Error interno del servidor

## Validaciones

### Capacidad
- Debe ser un número positivo
- No puede ser cero o negativo

### Objetos
- Debe ser una lista no vacía
- Cada objeto debe tener los campos: `nombre`, `peso`, `ganancia`
- `peso` debe ser un número positivo
- `ganancia` debe ser un número no negativo

## Algoritmo Utilizado

El microservicio implementa el algoritmo de **Programación Dinámica** para resolver el problema de la mochila (Knapsack Problem):

- **Complejidad Temporal**: O(n*W) donde n es el número de objetos y W es la capacidad
- **Complejidad Espacial**: O(n*W)
- **Garantía**: Siempre encuentra la solución óptima

## Ejemplos de Uso

### Ejemplo 1: Caso Básico
```bash
curl -X POST http://localhost:5000/optimizar \
  -H "Content-Type: application/json" \
  -d '{
    "capacidad": 10000,
    "objetos": [
      {"nombre": "A", "peso": 2000, "ganancia": 1500},
      {"nombre": "B", "peso": 4000, "ganancia": 3500},
      {"nombre": "C", "peso": 5000, "ganancia": 4000},
      {"nombre": "D", "peso": 3000, "ganancia": 2500}
    ]
  }'
```

### Ejemplo 2: Health Check
```bash
curl http://localhost:5000/health
```

## Casos de Prueba

### Caso de Éxito 1
- **Entrada**: Capacidad 10,000, 5 proyectos
- **Resultado Esperado**: ["Fondo_B", "Fondo_C", "Fondo_E"]
- **Ganancia Total**: 9,300

### Caso de Éxito 2
- **Entrada**: Capacidad 8,000, 5 proyectos
- **Resultado Esperado**: ["Acción_Y", "Acción_Z", "Bono_Q"]
- **Ganancia Total**: 6,200

### Caso de Éxito 3
- **Entrada**: Capacidad 5,000, 5 proyectos
- **Resultado Esperado**: ["Cripto_1", "Cripto_2", "ETF_2", "ETF_1"]
- **Ganancia Total**: 4,800

## Notas de Implementación

1. **CORS**: El servicio incluye soporte para CORS para permitir peticiones desde el frontend
2. **Logging**: Se registran todas las operaciones importantes para debugging
3. **Manejo de Errores**: Validación exhaustiva de entrada y manejo de excepciones
4. **Eficiencia**: Uso de programación dinámica para garantizar la solución óptima
