import { Module } from '@nestjs/common';
import { HttpEventsModule } from './infra/http/http-events.module';
import { ConfigsModule } from './infra/commons/configs/config.module';

@Module({
  imports: [
    HttpEventsModule,
    ConfigsModule,
  ],
})
export class AppModule {}
