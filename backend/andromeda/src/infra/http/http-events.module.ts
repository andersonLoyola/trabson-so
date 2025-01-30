import { Module } from '@nestjs/common';
import { AuthController } from './auth/auth.controller';
import { CreateUserUseCase } from '@root/src/use-cases/auth/create-user';
import { LoginUseCase } from '@root/src/use-cases/auth/login';
import { RepositoriesModule } from '@root/src/repositories/repositories.module';
import { TodoListController } from './todo-list/todo-list.controller';
import { CreateTodoListUseCase } from '@root/src/use-cases/todo-list/create-todo-list';
import { ServicesModule } from '@root/src/services/services.module';


@Module({
	imports: [RepositoriesModule, ServicesModule],
	providers: [
		CreateTodoListUseCase,
		CreateUserUseCase,
		LoginUseCase,
	],
	controllers: [AuthController, TodoListController],
})
export class HttpEventsModule {}
