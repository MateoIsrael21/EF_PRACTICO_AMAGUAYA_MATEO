export interface Objeto {
  nombre: string;
  peso: number;
  ganancia: number;
}

export interface OptimizacionRequest {
  capacidad: number;
  objetos: Objeto[];
}

export interface OptimizacionResponse {
  seleccionados: string[];
  ganancia_total: number;
  peso_total: number;
}

export interface ApiError {
  error: string;
  details?: string;
}
