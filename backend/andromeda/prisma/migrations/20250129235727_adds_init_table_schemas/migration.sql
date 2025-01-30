-- CreateEnum
CREATE TYPE "Status" AS ENUM ('PENDING', 'IN_PROGRESS', 'COMPLETED');

-- CreateTable
CREATE TABLE "Users" (
    "id" TEXT NOT NULL,
    "username" VARCHAR(30) NOT NULL,
    "password" TEXT NOT NULL,

    CONSTRAINT "Users_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TodoLists" (
    "id" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "userId" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "status" "Status" NOT NULL DEFAULT 'PENDING',

    CONSTRAINT "TodoLists_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TodoItem" (
    "id" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "Description" TEXT NOT NULL,
    "listId" TEXT NOT NULL,
    "status" "Status" NOT NULL DEFAULT 'PENDING',

    CONSTRAINT "TodoItem_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Users_username_key" ON "Users"("username");

-- AddForeignKey
ALTER TABLE "TodoLists" ADD CONSTRAINT "TodoLists_userId_fkey" FOREIGN KEY ("userId") REFERENCES "Users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TodoItem" ADD CONSTRAINT "TodoItem_listId_fkey" FOREIGN KEY ("listId") REFERENCES "TodoLists"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
