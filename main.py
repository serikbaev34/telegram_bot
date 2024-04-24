# Код для aiogram

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота. Вставьте сюда свой токен
bot = Bot(token="6981278189:AAFhhbvjNc6YNzhQz31JijZCalKAKYJx5OQ")

# Диспетчер
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Аниме авы")],
        [types.KeyboardButton(text="пейсажи")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какие авы тебе нужны?", reply_markup=keyboard)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())