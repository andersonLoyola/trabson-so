import { Injectable } from "@nestjs/common";
import { LoginCredentialsDidNotMatchError, UserNotFoundError } from "@root/src/core/errors/AuthErrors";
import { UsersRepository } from "@root/src/repositories/users.repository";
import { JWTService } from "@root/src/services/jwt.service";
import * as bcrypt from 'bcrypt';

@Injectable()
export class LoginUseCase {
    constructor (
        private readonly usersRepository: UsersRepository,
        private readonly jwtService: JWTService
    ) {}

    public execute = async (username: string, password: string) => {
        const foundUser = await this.usersRepository.findByUsername(username);
        if (!foundUser) {
            throw new UserNotFoundError()
        }
        const result = await bcrypt.compare(password, foundUser.password);
        if (!result) {
            throw new LoginCredentialsDidNotMatchError()
        }

        const generatedToken = this.jwtService.generateToken({
            id: foundUser.id,
            username: foundUser.username,
        });

        return {
            authToken: generatedToken
        }
    }
}