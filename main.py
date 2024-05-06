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
        [types.KeyboardButton(text="пейсажи")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какие авы тебе нужны?", reply_markup=keyboard)

@dp.message(F.text.lower() == "аниме авы")
async def anime(message: types.Message):
    album_builder = MediaGroupBuilder(
        caption="Персонаж - Nagi        anime - Синяя_Тюрьма"
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
            caption="Персонаж - Gojo        anime - Магическая_Битва"
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
    
    album_builder = MediaGroupBuilder(
        caption="Персонаж - Rubi        anime - Звездное_Дитя"
    )
    album_builder.add_photo(
        media="https://i.pinimg.com/736x/3d/81/24/3d81248039f2d5c39fe079e4ec27e38b.jpg"
    )
    album_builder.add_photo(
        media="https://i.pinimg.com/736x/21/89/a0/2189a064debd282db31c64d000074774.jpg"
    )
    album_builder.add_photo(
        media="https://i.pinimg.com/736x/1b/c4/19/1bc419fb38ff634f22212dee0e852a58.jpg"
    )
    album_builder.add_photo(
        media="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0660f85d-8626-4dc5-aa7b-06f70664117d/dg3d4po-6a97bac0-34e5-4f25-84ee-619bf4ae7fb4.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA2NjBmODVkLTg2MjYtNGRjNS1hYTdiLTA2ZjcwNjY0MTE3ZFwvZGczZDRwby02YTk3YmFjMC0zNGU1LTRmMjUtODRlZS02MTliZjRhZTdmYjQuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Yt0ComFISA4cQNocA9fTn86kif0NGwJYRlAvxYp6Nrc"
    )
    await message.answer_media_group(
        media=album_builder.build())
    
@dp.message(F.text.lower() == "пейсажи")
async def art(message: types.Message):
    album_builder = MediaGroupBuilder(
        caption= "Пейсажи"
    )
    album_builder.add_photo(
    media="https://i.pinimg.com/originals/c9/51/47/c951479f3bba1d473801c03f993843c0.jpg"
        )

    album_builder.add_photo(
        media="https://i.pinimg.com/236x/78/0b/73/780b73fcabd1266f44c6127a2a0e467e.jpg"
        )

    album_builder.add_photo(
        media="https://i.pinimg.com/736x/c5/5f/af/c55faf1299da96b18e3aea9ddb3d44f8.jpg"
        )

    album_builder.add_photo(
        media="https://i.pinimg.com/736x/93/7a/3c/937a3c4f494fb100b8449fd7a87671ad.jpg"
        )
    
    await message.answer_media_group(
        media=album_builder.build())
    
    album_builder = MediaGroupBuilder(
        caption= "Пейсаж море"
    )

    album_builder.add_photo(
        media="https://i.pinimg.com/564x/53/5d/ed/535ded0607931f18bfc3d823739d4f84.jpg"
        )
    
    album_builder.add_photo(
        media="https://i.pinimg.com/564x/53/5d/ed/535ded0607931f18bfc3d823739d4f84.jpg"
        ) 

    album_builder.add_photo(
        media="https://i.pinimg.com/736x/1a/0c/5a/1a0c5a716be89dec7b9b3d01e43ad456.jpg"
        )
    
    album_builder.add_photo(
        media="https://i.pinimg.com/736x/83/5b/79/835b79162cf863539c49addb91ab8ce7.jpg"
        )
    
    await message.answer_media_group(
        media=album_builder.build())
    

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())