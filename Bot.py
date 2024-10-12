import asyncio
from os import getenv
from Routes import Route1
from aiogram import Bot, Dispatcher
import Base


class App(Base.Base):
    import dotenv
    env = dotenv.load_dotenv('.env')
    Token = getenv('TOKEN')
    bot = Bot(Token)

    def create_dispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.include_routers(Route1.router)

        return dispatcher, self.bot


async def start_bot():
    dp, bot = App().create_dispatcher()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
