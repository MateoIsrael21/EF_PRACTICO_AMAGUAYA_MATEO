import axios from 'axios';
import { OptimizacionRequest, OptimizacionResponse, ApiError } from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const optimizacionService = {
  async optimizar(data: OptimizacionRequest): Promise<OptimizacionResponse> {
    try {
      const response = await api.post<OptimizacionResponse>('/optimizar', data);
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        const errorData = error.response?.data as ApiError;
        throw new Error(errorData?.error || 'Error en la optimización');
      }
      throw new Error('Error de conexión');
    }
  },

  async healthCheck(): Promise<{ status: string; service: string; version: string }> {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      throw new Error('Servicio no disponible');
    }
  },
};
