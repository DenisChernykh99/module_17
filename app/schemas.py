from pydantic import BaseModel, Field
from typing import Optional
# Импортировали модели и инструменты для их настройки


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(CreateUser):  # Наследуем атрибуты, переопределяя username на None
    username: Optional[str] = Field(default=None, exclude=True)  # И исключаем его из сериализации с помощью exclude


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(CreateTask):
    ...
