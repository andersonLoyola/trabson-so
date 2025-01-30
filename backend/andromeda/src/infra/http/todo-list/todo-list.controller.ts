import { Body, Controller, Post, Res, UsePipes, ValidationPipe } from "@nestjs/common";
import { ApiCookieAuth, ApiOperation, ApiResponse, ApiTags } from "@nestjs/swagger";
import { Cookies } from "@root/src/core/decorators/cookies.decorator";
import { CreateTodoListDTO } from "@root/src/dtos/todolist.dto";
import { CreateTodoListUseCase } from "@root/src/use-cases/todo-list/create-todo-list";
import { FastifyReply } from "fastify";

@ApiTags('todo')
@Controller('v1')
@ApiCookieAuth('auth_token')
export class TodoListController {

    constructor(
        private readonly createTodoListUsecase: CreateTodoListUseCase,
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
            createTodoListDTO.description
        );
        return res.send(result)
    }

}