import { Optional } from '@nestjs/common';
import { ApiProperty } from '@nestjs/swagger';
import {
    IsString,
    MaxLength,
    MinLength,
    IsNotEmpty,
} from 'class-validator'
import { TodoItem, TodoStatus } from '../repositories/todo-list.repository';
import { Type } from 'class-transformer';

export class TodoAttachment {
    attachmentName: string;
    attachmentType: string;
    attachmentSize: number;
}

export class CreateTodoItemDTO {
    @IsString()
    @IsNotEmpty()
    @MinLength(6)
    @MaxLength(60)
    title: string;

    @IsString()
    @Optional()
    @MinLength(6)
    @MaxLength(60)
    description?: string;
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

    @Optional()
    @Type(() => TodoItem)
    @ApiProperty({
        description: 'The items of the todo-list', 
        type: () => [TodoItem]
    })
    todoItems?: TodoItem[];
}

export class UpdateTodoItemStatusDTO {
    @IsNotEmpty()
    @ApiProperty({ description: 'The status of the todo item', enum: TodoStatus })
    status: TodoStatus;
}

export class UpdateTodoListStatusDTO {
    @IsString()
    @IsNotEmpty()
    @MinLength(6)
    @MaxLength(60)
    ownerId: string;

    @IsNotEmpty()
    @ApiProperty({ description: 'The status of the todo item', enum: TodoStatus })
    status: TodoStatus;
}