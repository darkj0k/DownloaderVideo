import asyncio
from os import getenv
from Routes import Route1
from aiogram import Bot, Dispatcher
from aiogram.fsm.scene import SceneRegistry
from Routes.Route1 import YouTubeDownloadScene


class Base:
    import logging
    logging.getLogger(__name__)
    logging.basicConfig(filename="Log.log", level=logging.DEBUG, filemode='a', encoding='utf-8',
                        format="%(asctime)s : %(name)s - %(module)s.%(funcName)s : %(levelname)s ---- %(message)s")


class App(Base):
    import dotenv
    env = dotenv.load_dotenv('.env')
    Token = getenv('TOKEN')
    bot = Bot(Token)

    def create_dispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.include_routers(Route1.router)
        scene_registry = SceneRegistry(dispatcher)
        scene_registry.add(YouTubeDownloadScene)

        return dispatcher, self.bot


async def start_bot():
    dp, bot = App().create_dispatcher()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
