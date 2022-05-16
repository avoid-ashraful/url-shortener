FROM node:lts-alpine as build-stage

WORKDIR /app/frontend

COPY frontend/package*.json  /app/frontend

ENV NODE_ENV=development

RUN npm install

COPY .  /app/frontend


CMD ["npm", "run", "serve"]
