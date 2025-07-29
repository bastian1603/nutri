FROM node:22

WORKDIR /app

COPY ./fe/package*.json /app/

WORKDIR /app
RUN npm install



EXPOSE 5173
CMD ["npm", "run", "dev"]