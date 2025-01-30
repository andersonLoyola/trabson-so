import { registerAs } from '@nestjs/config';

export enum ConfigKey {
	Jwt = 'Jwt',
}

const Jwt = registerAs(ConfigKey.Jwt, () => ({
	jwtSecret: process.env.JWT_SECRET,
	expireTime: process.env.JWT_EXPIRE_TIME,
}));

export const configurations = [
	Jwt
];
