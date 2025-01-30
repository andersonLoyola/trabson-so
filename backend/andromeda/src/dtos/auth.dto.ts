import { ApiProperty } from '@nestjs/swagger';
import {
    IsString,
    MaxLength,
    MinLength,
    IsNotEmpty,
} from 'class-validator'

export class CreateUserDTO {
    @IsString()
    @IsNotEmpty()
    @MinLength(6)
    @MaxLength(30)
    @ApiProperty({ description: 'The username of the user' })
    username: string;

    @IsString()
    @IsNotEmpty()
    @MinLength(16)
    @MaxLength(30) 
    @ApiProperty({ description: 'The password of the user' })
    password: string;
}

export class LoginDTO {
    @IsString()
    @IsNotEmpty()
    @MinLength(6)
    @MaxLength(30)
    @ApiProperty({ description: 'The username of the user' })
    username: string;

    @IsString()
    @IsNotEmpty()
    @MinLength(16)
    @MaxLength(30)
    @ApiProperty({ description: 'The password of the user' })
    password: string;
}

