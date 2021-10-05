from fastapi import FastAPI
from routers import users, authors

app = FastAPI()


app.include_router(users.router)
app.include_router(authors.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
