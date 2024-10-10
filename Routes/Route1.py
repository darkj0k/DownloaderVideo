from abc import ABC
from typing import Any

import aiogram.fsm.scene
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, Document
from aiogram.handlers import MessageHandler, BaseHandler
from aiogram.dispatcher import router
from aiogram.fsm.scene import Scene, ScenesManager, SceneRegistry, on
from aiogram.fsm.state import State
from Texts import Router1


class YouTubeDownloadScene(Scene, state='YouTube'):
    @on.message.enter()
    async def on_enter(self, message: Message):
        await message.answer('Привет ты зашел на ютуб')


router = router.Router(name=__name__)
router.message.register(YouTubeDownloadScene.as_handler(), Command('YouTube'))


@router.message(CommandStart())
class GeneralHandler(BaseHandler[Message]):
    async def handle(self) -> Any:
        await self.event.answer(Router1.Greetings)
