# User/Infrastructure/GraphQL/query.py

import strawberry
from fastapi import HTTPException

@strawberry.type
class Query:
    @strawberry.field
    def secure_data(self, info) -> str:
        user = info.context.get("user")
        if not user:
            raise HTTPException(status_code=401, detail="No autorizado")
        return f"Hola {user['username']}, este es un dato seguro."
