import { Injectable } from "@nestjs/common";
import { UnauthorizedError, UserNotFoundError } from "@root/src/core/errors/AuthErrors";
import { TodoListNotFoundError } from "@root/src/core/errors/TodoListErrors";
import { TodoListRepository, TodoStatus } from "@root/src/repositories/todo-list.repository";
import { UsersRepository } from "@root/src/repositories/users.repository";
import { JWTService } from "@root/src/services/jwt.service";

@Injectable()
export class CreateTodoItemUseCase {
    constructor (
        private readonly tokenService: JWTService,
        private readonly usersRepository: UsersRepository,
        private readonly todoListRepository: TodoListRepository
    ) {}

    public async execute(usertoken: string, listId: string, itemTitle: string, itemDescription?: string) {
        const decodedToken = this.tokenService.verifyToken(usertoken)
        const foundUser = await this.usersRepository.findByUsername(decodedToken?.username)
        if (!foundUser) {
            throw new UserNotFoundError();
        }
        const foundTodoList = await this.todoListRepository.findTodoListById(listId);
        if (!foundTodoList) {
            throw new TodoListNotFoundError();
        }

        if (foundTodoList.owner.id != decodedToken.id) {
            throw new UnauthorizedError();
        }

        await this.todoListRepository.createTodoItem(listId, itemTitle, itemDescription)
        return {
            message: 'todo item created successfully'
        }
    }

}