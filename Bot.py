from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

TOKEN = "8911200848:AAHLhoQb_qTurzik46fdY_39LnDQpy119Tg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Товары")],
        [KeyboardButton(text="💰 Оплата")],
        [KeyboardButton(text="📞 Поддержка")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🛍 Добро пожаловать в магазин!",
        reply_markup=menu
    )

@dp.message()
async def buttons(message: types.Message):
    if message.text == "🛒 Товары":
        await message.answer("📦 Пока товаров нет")

    elif message.text == "💰 Оплата":
        await message.answer("💳 Оплата скоро будет")

    elif message.text == "📞 Поддержка":
        await message.answer("@твойдс")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
