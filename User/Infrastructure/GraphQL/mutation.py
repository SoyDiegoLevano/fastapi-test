# User/Infrastructure/GraphQL/mutation.py

import strawberry
from fastapi import HTTPException
from User.Application.Login.LoginUserHandler import login_user
from User.Application.Create.CreateUserHandler import create_user
from User.Infrastructure.Persistence.postgres_user_repository import PostgresUserRepository

user_repo = PostgresUserRepository()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def login(self, username: str, password: str) -> str:
        try:
            return login_user(username, password, user_repo)
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))

    @strawberry.mutation
    def register(self, username: str, password: str) -> str:
        try:
            return create_user(username, password, user_repo)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
