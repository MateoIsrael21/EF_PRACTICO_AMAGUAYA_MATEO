FROM node:16-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar código de la aplicación
COPY . .

# Construir la aplicación
RUN npm run build

# Instalar servidor ligero para servir la aplicación
RUN npm install -g serve

# Exponer puerto
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["serve", "-s", "build", "-l", "3000"]
