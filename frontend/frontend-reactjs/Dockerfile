# FROM node:alpine

# WORKDIR '/app'
# COPY package.json .
# RUN npm install
# COPY . .
# CMD ["npm","start"]

FROM node:alpine

WORKDIR '/app'
COPY build .
RUN npm install -g serve
CMD ["serve","-s","build"]

