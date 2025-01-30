// filepath: /C:/Users/loyol/Documents/trabson-so/backend/andromeda/src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify';
import fastifyCookie from 'fastify-cookie';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

async function bootstrap() {
  const app = await NestFactory.create<NestFastifyApplication>(
    AppModule,
    new FastifyAdapter(),
  );

  app.register(fastifyCookie, {
    secret: 'secret-secretness', 
  });

  const config = new DocumentBuilder()
    .setTitle('API Documentation')
    .setDescription('The API description')
    .setVersion('1.0')
    .addTag('auth')
    .addTag('todo')
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  await app.listen(3000);
}
bootstrap();