# app/main.py
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema

app = FastAPI()

# Creamos un router GraphQL
graphql_app = GraphQLRouter(schema)

# Montamos el endpoint /graphql
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
