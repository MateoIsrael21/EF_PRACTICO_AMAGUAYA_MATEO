#!/usr/bin/env python3
"""
Script para ejecutar las pruebas del microservicio de optimización de portafolio.
"""

import subprocess
import sys
import os

def run_tests():
    """Ejecuta las pruebas del backend."""
    print("🚀 Ejecutando pruebas del microservicio...")
    print("=" * 50)
    
    # Cambiar al directorio del backend
    backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
    os.chdir(backend_dir)
    
    try:
        # Ejecutar pytest con cobertura
        result = subprocess.run([
            'python', '-m', 'pytest', 
            'tests/', 
            '-v', 
            '--cov=app', 
            '--cov-report=term-missing',
            '--cov-report=html'
        ], capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.stderr:
            print("Errores:", result.stderr)
        
        if result.returncode == 0:
            print("\n✅ Todas las pruebas pasaron exitosamente!")
        else:
            print("\n❌ Algunas pruebas fallaron.")
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando las pruebas: {e}")
        return False
    
    return True

def run_manual_tests():
    """Ejecuta pruebas manuales de los casos del enunciado."""
    print("\n🧪 Ejecutando pruebas manuales de casos del enunciado...")
    print("=" * 50)
    
    import requests
    import json
    
    base_url = "http://localhost:5000"
    
    # Caso 1: Caso básico
    print("\n📊 Caso 1: Caso básico")
    data1 = {
        "capacidad": 10000,
        "objetos": [
            {"nombre": "A", "peso": 2000, "ganancia": 1500},
            {"nombre": "B", "peso": 4000, "ganancia": 3500},
            {"nombre": "C", "peso": 5000, "ganancia": 4000},
            {"nombre": "D", "peso": 3000, "ganancia": 2500}
        ]
    }
    
    try:
        response = requests.post(f"{base_url}/optimizar", json=data1)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Resultado: {result}")
            expected = {"B", "C"}
            actual = set(result["seleccionados"])
            if actual == expected:
                print(f"✅ Caso 1 correcto: {actual} == {expected}")
            else:
                print(f"❌ Caso 1 incorrecto: {actual} != {expected}")
        else:
            print(f"❌ Error en caso 1: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en caso 1: {e}")
    
    # Caso 2: Caso de éxito 1
    print("\n📊 Caso 2: Caso de éxito 1")
    data2 = {
        "capacidad": 10000,
        "objetos": [
            {"nombre": "Fondo_A", "peso": 2000, "ganancia": 1500},
            {"nombre": "Fondo_B", "peso": 4000, "ganancia": 3500},
            {"nombre": "Fondo_C", "peso": 5000, "ganancia": 4000},
            {"nombre": "Fondo_D", "peso": 3000, "ganancia": 2500},
            {"nombre": "Fondo_E", "peso": 1500, "ganancia": 1800}
        ]
    }
    
    try:
        response = requests.post(f"{base_url}/optimizar", json=data2)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Resultado: {result}")
            expected = {"Fondo_B", "Fondo_C", "Fondo_E"}
            actual = set(result["seleccionados"])
            if actual == expected:
                print(f"✅ Caso 2 correcto: {actual} == {expected}")
            else:
                print(f"❌ Caso 2 incorrecto: {actual} != {expected}")
        else:
            print(f"❌ Error en caso 2: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en caso 2: {e}")

if __name__ == "__main__":
    print("🧪 Ejecutando pruebas del microservicio de optimización de portafolio")
    print("=" * 60)
    
    # Verificar si el servidor está corriendo
    try:
        import requests
        response = requests.get("http://localhost:5000/health", timeout=5)
        if response.status_code == 200:
            print("✅ Servidor backend está corriendo")
        else:
            print("❌ Servidor backend no responde correctamente")
            sys.exit(1)
    except Exception as e:
        print(f"❌ No se puede conectar al servidor backend: {e}")
        print("💡 Asegúrate de que el servidor esté corriendo en http://localhost:5000")
        sys.exit(1)
    
    # Ejecutar pruebas unitarias
    if run_tests():
        print("\n" + "=" * 60)
        # Ejecutar pruebas manuales
        run_manual_tests()
        print("\n🎉 Proceso de pruebas completado!")
    else:
        print("\n❌ Las pruebas unitarias fallaron. Revisa los errores arriba.")
        sys.exit(1)
