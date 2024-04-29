# Код для aiogram

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import URLInputFile
from aiogram.filters.command import Command
from aiogram.utils.media_group import MediaGroupBuilder

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
        [types.KeyboardButton(text="авы пейсажи")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какие авы тебе нужны?", reply_markup=keyboard)

@dp.message(F.text.lower() == "аниме авы")
async def anime(message: types.Message):
    album_builder = MediaGroupBuilder(
        caption="Nagi"
    )
    album_builder.add_photo(
        media="https://sun9-36.userapi.com/impg/I92509_rGuHEzXtMdUj7n4QkvknqQjTs5_6aZw/BqsfGSgtM7M.jpg?size=807x807&quality=95&sign=480ba4b41fb1b52463dad59824e91d84&c_uniq_tag=7RoPF8K4XPyTNIOQtPjxIvnKLMCtrHsIf8JlLiyaJVo&type=album"
    )
    album_builder.add_photo(
        media="https://sun9-58.userapi.com/impg/sSw0dryaqfcInJexDJF5ZTzgmneFJprl4sZC1A/1FtX-OTHBGA.jpg?size=604x604&quality=95&sign=f496138830f36653679d08ee5d1f7dad&c_uniq_tag=jyleerp0idroxQwi4utQ7SQn-9vZ89RlFErG5ZdVWCc&type=album"
    )
    album_builder.add_photo(
        media="https://sun9-5.userapi.com/impg/jUK2JauHnmbvHob3jjqKUvaKErxtrbewaZpRXw/OkbCatokNrQ.jpg?size=564x564&quality=96&sign=4534908337962315a19ce6f171aa527a&type=album"
    )
    album_builder.add_photo(
        media="https://sun9-61.userapi.com/impg/-zkwN1GOCg1KrkBPt1aANpdnlmr07d8FeJo68g/dP2uTojnsUQ.jpg?size=564x564&quality=96&sign=db14b4ed21c24212f21bcd7eaeb1f761&c_uniq_tag=C69sbY0EXSEHJ_A3VEjZslyB_dTvXG2Ojv-5glHXTxw&type=album"
    )
    await message.answer_media_group(
        media=album_builder.build())
    
    album_builder = MediaGroupBuilder(
            caption="Gojo"
    )
    album_builder.add_photo(
        media="https://mixmag.io/wp-content/pics4/prew/1674798706_2-2.jpg"
    )
    album_builder.add_photo(
        media="https://static31.tgcnt.ru/posts/_0/ec/eca94baa2e5e1b013a92e1f6010f68ae.jpg"
    )
    album_builder.add_photo(
        media="https://static29.tgcnt.ru/posts/_0/06/06f607c3d960e561bf21dfee8c9b3a87.jpg"
    )
    album_builder.add_photo(
        media="https://static31.tgcnt.ru/posts/_0/b7/b7dab3f63e9f80c60957ed26120260cb.jpg"
    )
    await message.answer_media_group(
        media=album_builder.build())



    image_from_url = URLInputFile("")
    result = await message.answer_photo(image_from_url, caption = "test")                                        


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())