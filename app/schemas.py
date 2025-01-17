from pydantic import BaseModel, Field
from typing import Optional


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(CreateUser):
    username: Optional[str] = Field(default=None, exclude=True)


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(CreateTask):
    ...
