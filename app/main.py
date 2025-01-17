from fastapi import FastAPI
from routers.user import router1
from routers.task import router

# Не забудь перейти в терминале в папку app(cd ...) для активации FastAPI
# python -m uvicorn main:app

app = FastAPI()


@app.get("/")
async def main_page():
    return {"message": "Welcome to Taskmanager"}

# Подключаем импортированные ранее роутеры
app.include_router(router1)
app.include_router(router)
