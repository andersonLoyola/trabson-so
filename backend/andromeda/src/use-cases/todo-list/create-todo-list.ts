import { Injectable } from "@nestjs/common";
import { UserNotFoundError } from "@root/src/core/errors/AuthErrors";
import { TodoListRepository } from "@root/src/repositories/todo-list.repository";
import { UsersRepository } from "@root/src/repositories/users.repository";
import { JWTService } from "@root/src/services/jwt.service";

@Injectable()
export class CreateTodoListUseCase {
    constructor (
        private readonly tokenService: JWTService,
        private readonly usersRepository: UsersRepository,
        private readonly todoListRepository: TodoListRepository
    ) {}

    public async execute(usertoken: string, listName: string, listDescription?: string) {
        const decodedToken = this.tokenService.verifyToken(usertoken)
        const foundUser = await this.usersRepository.findByUsername(decodedToken?.username)
        if (!foundUser) {
            throw new UserNotFoundError();
        }
        await this.todoListRepository.createTodoList(foundUser.id, listName, listDescription)
        return {
            message: 'Todolist created successfully'
        }
    }

}