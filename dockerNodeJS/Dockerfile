# Uso de node, version ligera y estable
FROM node:12.22.1-alpine3.11

WORKDIR /app

# Copiamos nuestros packages (importante)
COPY package*.json ./

# Se da por sentado que ya se tiene instalado Node
RUN npm install

# Copiar todo al directorio de trabajo
COPY . .

# Start
CMD ["npm", "start"]