import React from 'react';
import { OptimizacionResponse } from '../types';
import './ResultsDisplay.css';

interface ResultsDisplayProps {
  resultado: OptimizacionResponse;
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ resultado }) => {
  return (
    <div className="results-container">
      <h2>Resultados de la Optimización</h2>
      
      <div className="results-card">
        <div className="result-section">
          <h3>Proyectos Seleccionados</h3>
          {resultado.seleccionados.length > 0 ? (
            <div className="selected-projects">
              {resultado.seleccionados.map((proyecto, index) => (
                <span key={index} className="project-tag">
                  {proyecto}
                </span>
              ))}
            </div>
          ) : (
            <p className="no-projects">No se seleccionaron proyectos</p>
          )}
        </div>

        <div className="result-section">
          <h3>Resumen Financiero</h3>
          <div className="financial-summary">
            <div className="summary-item">
              <label>Ganancia Total:</label>
              <span className="value gain">${resultado.ganancia_total.toLocaleString()}</span>
            </div>
            <div className="summary-item">
              <label>Costo Total:</label>
              <span className="value cost">${resultado.peso_total.toLocaleString()}</span>
            </div>
            <div className="summary-item">
              <label>ROI:</label>
              <span className={`value ${resultado.peso_total > 0 ? 'roi' : 'neutral'}`}>
                {resultado.peso_total > 0 
                  ? `${((resultado.ganancia_total / resultado.peso_total) * 100).toFixed(2)}%`
                  : 'N/A'
                }
              </span>
            </div>
          </div>
        </div>

        <div className="result-section">
          <h3>Análisis de Eficiencia</h3>
          <div className="efficiency-analysis">
            <div className="efficiency-item">
              <label>Proyectos Evaluados:</label>
              <span className="value">{resultado.seleccionados.length}</span>
            </div>
            <div className="efficiency-item">
              <label>Capacidad Utilizada:</label>
              <span className="value">
                {resultado.peso_total > 0 ? `${((resultado.peso_total / 10000) * 100).toFixed(1)}%` : '0%'}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultsDisplay;
