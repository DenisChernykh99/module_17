from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Импортируем и создаем объект движка для БД
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# Импортируем и создаем локальную сессию на основе движка
SessionLocal = sessionmaker(bind=engine)

# Импортируем и создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass
