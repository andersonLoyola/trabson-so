import { Module } from '@nestjs/common';
import { UsersRepository } from './users.repository';
import { PrismaModule } from '../services/prisma.module';


@Module({
    imports: [PrismaModule],
    providers: [
        UsersRepository,
    ],
})
export class Repositories {}
