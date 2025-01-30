import { Optional } from '@nestjs/common';
import { ApiProperty } from '@nestjs/swagger';
import {
    IsString,
    MaxLength,
    MinLength,
    IsNotEmpty,
} from 'class-validator'

export class TodoAttachment {
    attachmentName: string;
    attachmentType: string;
    attachmentSize: number;
}

export class CreateTodoItemDTO {
    title: string;
    description?: string;
    attachment?: TodoAttachment
}

export class CreateTodoListDTO {
    @IsString()
    @IsNotEmpty()
    @MinLength(6)
    @MaxLength(60)
    @ApiProperty({ description: 'The name of the todo-list' })
    title: string;

    @IsString()
    @MinLength(6)
    @MaxLength(30)
    @ApiProperty({ description: 'The description of the todo-list' })
    description?: string;

    // @Optional()
    // @ApiProperty({ description: 'The i qtems of the todo-list', type: [CreateTodoItemDTO] })
    // todoItems?: CreateTodoItemDTO[];
}

export class UpdateTodoItemStatusDTO {
    ownerId: string;
    status: string;
    todoItemId: string;
    todoListId: string;
}

export class UpdateTodoListStatusDTO {
    ownerId: string;
    todoListId: string;
}