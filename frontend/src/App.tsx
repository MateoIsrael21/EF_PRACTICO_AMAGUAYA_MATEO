import React, { useState } from 'react';
import './App.css';
import PortfolioForm from './components/PortfolioForm';
import ResultsDisplay from './components/ResultsDisplay';
import { Objeto, OptimizacionResponse } from './types';

function App() {
  const [resultado, setResultado] = useState<OptimizacionResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleOptimizacion = async (capacidad: number, objetos: Objeto[]) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('/optimizar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ capacidad, objetos }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Error en la optimización');
      }

      const data = await response.json();
      setResultado(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error desconocido');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Optimización de Portafolio de Inversiones</h1>
        <p>Universidad de las Fuerzas Armadas ESPE - Arquitectura de Software</p>
      </header>
      
      <main className="App-main">
        <PortfolioForm onOptimizar={handleOptimizacion} loading={loading} />
        
        {error && (
          <div className="error-message">
            <h3>Error:</h3>
            <p>{error}</p>
          </div>
        )}
        
        {resultado && <ResultsDisplay resultado={resultado} />}
      </main>
    </div>
  );
}

export default App;
