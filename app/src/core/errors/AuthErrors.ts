import { HttpStatus } from "@nestjs/common";
import { DomainError } from "./DomainErrors";

export class UserNotFoundError extends DomainError{
    constructor() {
        super({
            message: 'User not found',
            statusCode: HttpStatus.NOT_FOUND
        });
    }
}

export class UnauthorizedError extends DomainError{
    constructor() {
        super({
            message: 'Unauthorized error',
            statusCode: HttpStatus.UNAUTHORIZED
        });
    }
}

export class LoginCredentialsDidNotMatchError extends DomainError{
    constructor() {
        super({
            message: 'Login credentials did not match',
            statusCode: HttpStatus.CONFLICT
        });
    }
}

export class UserAlreadyExistsError extends DomainError{
    constructor() {
        super({
            message: 'User already exists',
            statusCode: HttpStatus.CONFLICT
        });
    }
}



