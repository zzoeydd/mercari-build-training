FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
COPY ./public /app/public
RUN npm install 
COPY . ./
RUN npm run build 
EXPOSE 3000
CMD ["npm", "start"]
