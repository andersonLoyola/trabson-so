import { DomainError } from "./DomainErrors";

export class TodoListNotFoundError extends DomainError {
    constructor() {
        super({
            message: 'TodoList not found',
            statusCode: 404
        })
    }
}