import { Module } from '@nestjs/common';
import { UsersRepository } from './users.repository';
import { ServicesModule } from '../services/services.module';
import { TodoListRepository } from './todo-list.repository';


@Module({
    imports: [ServicesModule],
    providers: [
        UsersRepository,
        TodoListRepository,
    ],
    exports: [UsersRepository, TodoListRepository]
})
export class RepositoriesModule {}
