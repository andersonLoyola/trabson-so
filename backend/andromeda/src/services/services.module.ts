import { Module, Global } from '@nestjs/common';
import { PrismaService } from './prisma.service';
import { JWTService } from './jwt.service';
import { ConfigModule } from '@nestjs/config';

@Global()
@Module({
  exports: [PrismaService, JWTService],
  providers: [PrismaService, JWTService],
})
export class ServicesModule {}