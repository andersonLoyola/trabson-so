import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { configurations } from '@infra/commons/configs/config.service';

@Module({
	imports: [
		ConfigModule.forRoot({
			load: [...configurations],
			isGlobal: true,
			cache: true,
		}),
	],
})
export class ConfigsModule {}
