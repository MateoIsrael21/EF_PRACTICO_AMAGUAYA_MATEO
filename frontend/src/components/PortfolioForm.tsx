import React, { useState } from 'react';
import { Objeto } from '../types';
import './PortfolioForm.css';

interface PortfolioFormProps {
  onOptimizar: (capacidad: number, objetos: Objeto[]) => void;
  loading: boolean;
}

const PortfolioForm: React.FC<PortfolioFormProps> = ({ onOptimizar, loading }) => {
  const [capacidad, setCapacidad] = useState<number>(10000);
  const [objetos, setObjetos] = useState<Objeto[]>([
    { nombre: 'A', peso: 2000, ganancia: 1500 },
    { nombre: 'B', peso: 4000, ganancia: 3500 },
    { nombre: 'C', peso: 5000, ganancia: 4000 },
    { nombre: 'D', peso: 3000, ganancia: 2500 }
  ]);

  const agregarObjeto = () => {
    const nuevoObjeto: Objeto = {
      nombre: `Proyecto_${objetos.length + 1}`,
      peso: 0,
      ganancia: 0
    };
    setObjetos([...objetos, nuevoObjeto]);
  };

  const eliminarObjeto = (index: number) => {
    if (objetos.length > 1) {
      const nuevosObjetos = objetos.filter((_, i) => i !== index);
      setObjetos(nuevosObjetos);
    }
  };

  const actualizarObjeto = (index: number, campo: keyof Objeto, valor: string | number) => {
    const nuevosObjetos = [...objetos];
    nuevosObjetos[index] = {
      ...nuevosObjetos[index],
      [campo]: campo === 'nombre' ? valor : Number(valor)
    };
    setObjetos(nuevosObjetos);
  };

  const limpiarFormulario = () => {
    setCapacidad(10000);
    setObjetos([
      { nombre: 'A', peso: 2000, ganancia: 1500 },
      { nombre: 'B', peso: 4000, ganancia: 3500 },
      { nombre: 'C', peso: 5000, ganancia: 4000 },
      { nombre: 'D', peso: 3000, ganancia: 2500 }
    ]);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onOptimizar(capacidad, objetos);
  };

  return (
    <div className="portfolio-form-container">
      <h2>Configuración del Portafolio</h2>
      
      <form onSubmit={handleSubmit} className="portfolio-form">
        <div className="form-group">
          <label htmlFor="capacidad">Capacidad Presupuestaria (USD):</label>
          <input
            type="number"
            id="capacidad"
            value={capacidad}
            onChange={(e) => setCapacidad(Number(e.target.value))}
            min="1"
            required
            className="form-control"
          />
        </div>

        <div className="form-group">
          <label>Proyectos de Inversión:</label>
          <div className="objetos-container">
            {objetos.map((objeto, index) => (
              <div key={index} className="objeto-item">
                <div className="objeto-header">
                  <h4>Proyecto {index + 1}</h4>
                  {objetos.length > 1 && (
                    <button
                      type="button"
                      onClick={() => eliminarObjeto(index)}
                      className="btn-eliminar"
                    >
                      ✕
                    </button>
                  )}
                </div>
                
                <div className="objeto-fields">
                  <div className="field-group">
                    <label>Nombre:</label>
                    <input
                      type="text"
                      value={objeto.nombre}
                      onChange={(e) => actualizarObjeto(index, 'nombre', e.target.value)}
                      required
                      className="form-control"
                    />
                  </div>
                  
                  <div className="field-group">
                    <label>Costo (USD):</label>
                    <input
                      type="number"
                      value={objeto.peso}
                      onChange={(e) => actualizarObjeto(index, 'peso', e.target.value)}
                      min="1"
                      required
                      className="form-control"
                    />
                  </div>
                  
                  <div className="field-group">
                    <label>Ganancia Esperada (USD):</label>
                    <input
                      type="number"
                      value={objeto.ganancia}
                      onChange={(e) => actualizarObjeto(index, 'ganancia', e.target.value)}
                      min="0"
                      required
                      className="form-control"
                    />
                  </div>
                </div>
              </div>
            ))}
          </div>
          
          <button
            type="button"
            onClick={agregarObjeto}
            className="btn-agregar"
          >
            + Agregar Proyecto
          </button>
        </div>

        <div className="form-actions">
          <button
            type="submit"
            disabled={loading}
            className="btn-calcular"
          >
            {loading ? 'Calculando...' : 'Calcular Optimización'}
          </button>
          
          <button
            type="button"
            onClick={limpiarFormulario}
            className="btn-limpiar"
          >
            Limpiar
          </button>
        </div>
      </form>
    </div>
  );
};

export default PortfolioForm;
