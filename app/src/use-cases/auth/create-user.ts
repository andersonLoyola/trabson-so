import { Injectable } from "@nestjs/common";
import { UserAlreadyExistsError } from "@root/src/core/errors/AuthErrors";
import { UsersRepository } from "@root/src/repositories/users.repository";
import * as bcrypt from 'bcrypt';

@Injectable()
export class CreateUserUseCase {
    constructor (
        private readonly usersRepository: UsersRepository
    ) {}

    public execute = async (username: string, password: string) => {
        const foundUser = await this.usersRepository.findByUsername(username);
        if (foundUser) {
           throw new UserAlreadyExistsError()
        }
        const hashedPassword = await bcrypt.hash(password, 10);
        await this.usersRepository.createUser(username, hashedPassword);
        return {
            message: 'user created sucessfully'
        }
    }
}