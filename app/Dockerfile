FROM node:22

WORKDIR /usr/src/app
COPY . .
RUN npm install
RUN npx prisma db push
RUN npx prisma migrate deploy
EXPOSE 3000
CMD ["npm", "start"]