from datetime import datetime
from sqlalchemy import DateTime, create_engine, Column, Text, Integer, BigInteger, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import ENUM
from enum import Enum, unique

from config import cfg

# Определение базового класса
Base = declarative_base()

# Определение класса User, который представляет таблицу в базе данных


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(32))
    firstname = Column(String(100))
    lastname= Column(String(100))
    last_activity = Column(DateTime)
    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, username='{self.username}', fullname='{self.firstname}{self.lastname}')>"



# Создание движка SQLAlchemy для MySQL
# Предполагается, что MySQL запущен на localhost и имеет базу данных 'testdb'
# с пользователем 'testuser' и паролем 'testpass'
engine = create_engine(
   f"mysql+pymysql://{cfg.tg_bot.user}:{cfg.tg_bot.password}@{cfg.tg_bot.host}:{cfg.tg_bot.port}/{cfg.tg_bot.db_name}")

# Привязка движка к базовому классу и создание таблиц
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# CRUD операции

# Создание (Create)


def create_user(name, telegram_id):
    new_user = User(name=name, telegram_id=telegram_id)
    session.add(new_user)
    session.commit()
    return new_user
# Чтение (Read)
def get_user(user_id):
    return session.query(User).get(user_id)

def get_all_users():
    return session.query(User).all()

# Обновление (Update)
def update_user_activiry_status(telegram_id):
    user = session.query(User).get(User.telegram_id == telegram_id)
    if not user:
        return None

    user.last_activity = datetime.now()
    session.commit()
    return user

# Удаление (Delete)


def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
