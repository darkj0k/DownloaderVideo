import aiogram.fsm.scene
from aiogram.filters import Command
from aiogram.types import Message, Document
from aiogram.handlers import MessageHandler, BaseHandler
from aiogram.dispatcher import router
from aiogram.fsm.scene import Scene, ScenesManager, SceneRegistry, on
from aiogram.fsm.state import State


class YouTubeDownloadScene(Scene, state='YouTube'):
    @on.message.enter()
    async def on_enter(self, message: Message):
        await message.answer('Привет я пидор')


router = router.Router(name=__name__)
router.message.register(YouTubeDownloadScene.as_handler(), Command('/YouTube'))
