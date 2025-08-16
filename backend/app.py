from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def knapsack_dynamic_programming(capacidad, objetos):
    """
    Implementa el algoritmo de programación dinámica para el problema de la mochila.
    
    Args:
        capacidad (int): Capacidad máxima de la mochila
        objetos (list): Lista de objetos con nombre, peso y ganancia
    
    Returns:
        tuple: (seleccionados, ganancia_total, peso_total)
    """
    n = len(objetos)
    
    # Crear tabla de programación dinámica
    # dp[i][w] = máxima ganancia usando los primeros i objetos con capacidad w
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla dp
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            # No incluir el objeto i
            dp[i][w] = dp[i-1][w]
            
            # Incluir el objeto i si es posible
            if objetos[i-1]['peso'] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - objetos[i-1]['peso']] + objetos[i-1]['ganancia'])
    
    # Reconstruir la solución
    seleccionados = []
    ganancia_total = dp[n][capacidad]
    peso_total = 0
    
    w = capacidad
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            seleccionados.append(objetos[i-1]['nombre'])
            peso_total += objetos[i-1]['peso']
            w -= objetos[i-1]['peso']
    
    return seleccionados[::-1], ganancia_total, peso_total

def validar_entrada(data):
    """
    Valida los datos de entrada del request.
    
    Args:
        data (dict): Datos del request JSON
    
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    # Verificar que los campos requeridos existan
    if 'capacidad' not in data:
        return False, "Campo 'capacidad' es requerido"
    
    if 'objetos' not in data:
        return False, "Campo 'objetos' es requerido"
    
    # Validar capacidad
    capacidad = data['capacidad']
    if not isinstance(capacidad, (int, float)) or capacidad <= 0:
        return False, "La capacidad debe ser un número positivo"
    
    # Validar objetos
    objetos = data['objetos']
    if not isinstance(objetos, list) or len(objetos) == 0:
        return False, "Los objetos deben ser una lista no vacía"
    
    for i, obj in enumerate(objetos):
        if not isinstance(obj, dict):
            return False, f"El objeto {i} debe ser un diccionario"
        
        # Verificar campos requeridos del objeto
        if 'nombre' not in obj:
            return False, f"El objeto {i} debe tener un campo 'nombre'"
        
        if 'peso' not in obj:
            return False, f"El objeto {i} debe tener un campo 'peso'"
        
        if 'ganancia' not in obj:
            return False, f"El objeto {i} debe tener un campo 'ganancia'"
        
        # Validar tipos y valores
        if not isinstance(obj['peso'], (int, float)) or obj['peso'] <= 0:
            return False, f"El peso del objeto {i} debe ser un número positivo"
        
        if not isinstance(obj['ganancia'], (int, float)) or obj['ganancia'] < 0:
            return False, f"La ganancia del objeto {i} debe ser un número no negativo"
    
    return True, ""

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar el estado del servicio."""
    return jsonify({
        "status": "healthy",
        "service": "Portfolio Optimization Service",
        "version": "1.0.0"
    })

@app.route('/optimizar', methods=['POST'])
def optimizar():
    """
    Endpoint principal para optimizar la selección de proyectos de inversión.
    
    Returns:
        JSON: Resultado de la optimización o error
    """
    try:
        # Obtener datos del request
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "Datos JSON requeridos"
            }), 400
        
        # Validar entrada
        es_valido, mensaje_error = validar_entrada(data)
        if not es_valido:
            return jsonify({
                "error": mensaje_error
            }), 400
        
        capacidad = int(data['capacidad'])
        objetos = data['objetos']
        
        logger.info(f"Optimizando portafolio con capacidad {capacidad} y {len(objetos)} objetos")
        
        # Ejecutar algoritmo de optimización
        seleccionados, ganancia_total, peso_total = knapsack_dynamic_programming(capacidad, objetos)
        
        # Preparar respuesta
        resultado = {
            "seleccionados": seleccionados,
            "ganancia_total": ganancia_total,
            "peso_total": peso_total
        }
        
        logger.info(f"Optimización completada: {len(seleccionados)} proyectos seleccionados")
        
        return jsonify(resultado)
        
    except Exception as e:
        logger.error(f"Error en optimización: {str(e)}")
        return jsonify({
            "error": "Error interno del servidor",
            "details": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Manejo de rutas no encontradas."""
    return jsonify({
        "error": "Endpoint no encontrado"
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Manejo de métodos HTTP no permitidos."""
    return jsonify({
        "error": "Método HTTP no permitido"
    }), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
