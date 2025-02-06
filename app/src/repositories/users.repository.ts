import { Injectable } from "@nestjs/common";
import { PrismaService } from "../services/prisma.service";

@Injectable()
export class UsersRepository {
    constructor(
        private readonly databaseService: PrismaService
    ) {}

    async createUser(username: string, password: string) {
        await this.databaseService.users.create({
            data: {
                username,
                password
            }
        })
    }

    async findByUsername(username: string) {
        return this.databaseService.users.findFirst({
            where: {
                username: {
                    equals: username
                }
            }
        })
    }
}