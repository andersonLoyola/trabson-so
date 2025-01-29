import { PrismaService } from "../services/prisma.service";

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

    async getUser(username: string) {
        return this.databaseService.users.findFirst({
            where: {
                username: {
                    equals: username
                }
            }
        })
    }
}