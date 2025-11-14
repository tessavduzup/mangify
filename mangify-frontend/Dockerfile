FROM python:3.12.4-slim-bookworm

WORKDIR /mangify-frontend

COPY . /mangify-frontend

RUN apt update 
RUN apt install -y build-essential curl gcc g++ make
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt install -y nodejs
RUN npm install

ENTRYPOINT ["npm", "run", "dev"]
