import * as jwt from 'jsonwebtoken';
import { ConfigService } from '@nestjs/config';
import { Injectable } from '@nestjs/common';

export class DecodedToken {
    id: string;
    username: string;
}

@Injectable()
export class JWTService {
    private secret: string;
    private expireTime: number

    constructor(
        private readonly configService: ConfigService
    ) {
        this.secret = this.configService.getOrThrow<string>('Jwt.jwtSecret');
        this.expireTime = this.configService.getOrThrow<number>('Jwt.expireTime');
    }

    public generateToken(payload: object, ): string {
        return jwt.sign(payload, this.secret, { expiresIn: this.expireTime });
    }

    public verifyToken(token: string): DecodedToken {
        try {
            return jwt.verify(token, this.secret) as DecodedToken;
        } catch (error) {
            throw new Error('Invalid token');
        }
    }
}