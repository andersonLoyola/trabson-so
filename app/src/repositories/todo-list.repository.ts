import { Injectable } from "@nestjs/common";
import { PrismaService } from "../services/prisma.service";

export enum TodoStatus {
    PENDING = 'PENDING',
    IN_PROGRESS = 'IN_PROGRESS',
    COMPLETED = 'COMPLETED'
}

export class TodoItem {
    title: string;
    description?: string;
}

@Injectable()
export class TodoListRepository {
    constructor (
        private readonly client: PrismaService
    ) {}

    public createTodoList = async (
        ownerId: string,
        listTitle: string,
        listDescription: string = '',
    ) => {
        return this.client.todoLists.create({
            data: {
                title: listTitle,
                description: listDescription,
                owner: {
                    connect: {
                        id: ownerId
                    }
                },
            },
            select: {
                id: true
            }
        })
    }

    public createTodoItem = async (
        listId: string,
        itemTitle: string,
        itemDescription: string = '',
    ) => {
        await this.client.todoItem.create({
            data: {
                title: itemTitle,
                Description: itemDescription,
                list: {
                    connect: {
                        id: listId
                    }
                }
            }
        })
    }

    public updateTodoListStatus = async (
        listId: string,
        status: TodoStatus
    ) => {
        await this.client.todoLists.update({
            where: {
                id: listId
            },
            data: {
                status: status,
            }
        })
    }

    public updateTodoItemStatus = async (
        listId: string,
        todoItemId: string,
        status: TodoStatus,
    ) => {
        await this.client.todoItem.update({
            where: {
                listId,    
                id: todoItemId,
            },
            data: {
                status: status
            }
        })
    }

    public findTodoListById = async (
        listId: string
    ) => {
        return this.client.todoLists.findFirst({
            where: {
                id: listId
            },
            include: {
                owner: {
                  select: {
                    id: true
                  }
                },
                TodoItem: {
                    select: {
                        id: true
                    }
                }
            }
        })
    }

}