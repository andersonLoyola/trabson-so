import { Body, Controller, Post, Res, UsePipes, ValidationPipe } from "@nestjs/common";
import { ApiOperation, ApiResponse, ApiTags } from "@nestjs/swagger";
import { CreateUserDTO, LoginDTO } from "@root/src/dtos/auth.dto";
import { CreateUserUseCase } from "@root/src/use-cases/auth/create-user";
import { LoginUseCase } from "@root/src/use-cases/auth/login";
import { FastifyReply } from "fastify";

@ApiTags('auth')
@Controller('v1')
export class AuthController {

    constructor(
        private readonly createUserUseCase: CreateUserUseCase,
        private readonly loginUseCase: LoginUseCase
    ){}

    @Post('/create-user')
    @UsePipes(new ValidationPipe({whitelist: true}))
    @ApiOperation({ summary: 'Create a new user' })
    @ApiResponse({ status: 201, description: 'The user has been successfully created.' })
    @ApiResponse({ status: 400, description: 'Bad Request.' })  
    public async createUser(@Body() createUserDTO: CreateUserDTO, @Res() res: FastifyReply) {
        const result =  await this.createUserUseCase.execute(createUserDTO.username, createUserDTO.password)
        return res.send(result)
    }
   
    @Post('/login')
    @UsePipes(new ValidationPipe({whitelist: true}))
    @ApiOperation({ summary: 'Login a user' })
    @ApiResponse({ status: 200, description: 'The user has been successfully logged in.' })
    @ApiResponse({ status: 400, description: 'Bad Request.' })
    public async login(@Body() createUserDTO: LoginDTO, @Res() res: FastifyReply) {
        const { authToken } =  await this.loginUseCase.execute(createUserDTO.username, createUserDTO.password)
        res.setCookie('authToken', authToken, {httpOnly: true})
        return res.send({message: 'User logged in successfully'})
    }    
}