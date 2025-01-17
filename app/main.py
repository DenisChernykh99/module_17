from fastapi import FastAPI
from routers.user import router1
from routers.task import router

app = FastAPI()


@app.get("/")
async def main_page():
    return {"message": "Welcome to Taskmanager"}

app.include_router(router1)
app.include_router(router)
