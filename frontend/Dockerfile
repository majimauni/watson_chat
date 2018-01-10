FROM node:6

WORKDIR /src

ADD package.json /

RUN cp /package.json ./ && npm install && rm -rf ../.npm

CMD ["npm", "run", "dev"]


