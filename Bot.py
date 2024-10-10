from os import getenv
import importlib
from Routes import Route1
import aiogram
from aiogram import Bot, Dispatcher, Router
from aiogram.types import message, Document
import logging


class Base:
    import logging
    logging.getLogger(__name__)
    logging.basicConfig("Log.log", level=logging.DEBUG, filemode='a', encoding='utf-8',
                        format="%{asctime}s : %{name}s - %{module}s.%{funcName}s : %{levelname}s ---- ")


class App(Base):
    import dotenv
    env = dotenv.load_dotenv('.env')
    Token = getenv('TOKEN')
    bot = Bot(Token)

    @staticmethod
    def create_dispatcher():
        dispatcher = aiogram.Dispatcher()
        dispatcher.include_routers(Route1.router)

        return dispatcher

