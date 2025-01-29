import { Module } from '@nestjs/common';
import { AuthController } from './auth/auth.controller';


@Module({
	providers: [
	
	],
	controllers: [AuthController],
})
export class HttpEventsModule {}
