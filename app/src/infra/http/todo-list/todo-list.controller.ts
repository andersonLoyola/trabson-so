import { Body, Controller, Param, Patch, Post, Res, UsePipes, ValidationPipe } from "@nestjs/common";
import { ApiCookieAuth, ApiOperation, ApiParam, ApiResponse, ApiTags } from "@nestjs/swagger";
import { Cookies } from "@root/src/core/decorators/cookies.decorator";
import { CreateTodoItemDTO, CreateTodoListDTO, UpdateTodoItemStatusDTO } from "@root/src/dtos/todolist.dto";
import { CreateTodoItemUseCase } from "@root/src/use-cases/todo-list/create-todo-item";
import { CreateTodoListUseCase } from "@root/src/use-cases/todo-list/create-todo-list";
import { UpdateTodoItemStatusUseCase } from "@root/src/use-cases/todo-list/update-todo-item";
import { FastifyReply } from "fastify";

@ApiTags('todo')
@Controller('v1')
@ApiCookieAuth('auth_token')
export class TodoListController {

    constructor(
        private readonly createTodoListUsecase: CreateTodoListUseCase,
        private readonly updateTodoItemStatusUseCase: UpdateTodoItemStatusUseCase,
        private readonly createTodoItemUseCase: CreateTodoItemUseCase,
    ){}

    @Post('/create-todo-list')
    @UsePipes(new ValidationPipe({whitelist: true}))
    @ApiOperation({ summary: 'Create a new todo list' })
    @ApiResponse({ status: 201, description: 'The todo-list has been successfully created.' })
    @ApiResponse({ status: 400, description: 'Bad Request.' })  
    public async createTodoList(
        @Cookies('authToken') authToken: string,
        @Body() createTodoListDTO: CreateTodoListDTO, 
        @Res() res: FastifyReply
    ) {
        const result = await this.createTodoListUsecase.execute(
            authToken, 
            createTodoListDTO.title, 
            createTodoListDTO.description,
            createTodoListDTO.todoItems
        );
        return res.send(result)
    }
    
    @Patch('/:list_id/:item_id')
    @UsePipes(new ValidationPipe({whitelist: true}))
    @ApiOperation({ summary: 'update a todo item status' })
    @ApiResponse({ status: 200, description: 'The todo item status was successfully updated.' })
    @ApiResponse({ status: 400, description: 'Bad Request.' })  
    @ApiParam({name: 'list_id', description: 'The todo list id'})
    @ApiParam({name: 'item_id', description: 'The todo item id'})
    public async updateTodoItemStatus(
        @Cookies('authToken') authToken: string,
        @Param('list_id') listId: string,
        @Param('item_id') itemId: string,
        @Body() updateTodoItemStatusDTO: UpdateTodoItemStatusDTO, 
        @Res() res: FastifyReply
    ) {
        const result = await this.updateTodoItemStatusUseCase.execute(
            authToken, 
            listId,
            itemId,
            updateTodoItemStatusDTO.status
        );
        return res.send(result)
    }
    
    @Post('/:listid')
    @UsePipes(new ValidationPipe({whitelist: true}))
    @ApiOperation({ summary: 'Create a new todo item' })
    @ApiResponse({ status: 200, description: 'The todo item status was successfully updated.' })
    @ApiResponse({ status: 400, description: 'Bad Request.' })  
    @ApiParam({name: 'listid', description: 'The todo list id'})
    @ApiParam({name: 'item_id', description: 'The todo item id'})
    public async creatTodoItem(
        @Cookies('authToken') authToken: string,
        @Param('listid') listId: string,
        @Body() createTodoItemDTO: CreateTodoItemDTO, 
        @Res() res: FastifyReply
    ) {
        const result = await this.createTodoItemUseCase.execute(
            authToken, 
            listId,
            createTodoItemDTO.title,
            createTodoItemDTO.description
        );
        return res.send(result)
    }

}