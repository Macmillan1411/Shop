from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

user_router = Router()

@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer("Welcome to the shop!")
