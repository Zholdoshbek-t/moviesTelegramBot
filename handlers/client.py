import json
import urllib.request

from aiogram import types, Dispatcher

import keyBoard.keyboard
from bot_instance import bot


async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello : {message.from_user.full_name}',
                           reply_markup=keyBoard.keyboard.keyboard_start)


async def parser_cinematica_film(message: types.Message):
    with urllib.request.urlopen("https://cinematica.kg/api/v1/movies/today") as url:
        data = json.load(url)

        posts = 0

        for i in data["list"]:
            ageRest = i["age_restriction"]
            if ageRest == "":
                ageRest = "0+"

            baseUrl = "https://cinematica.kg"

            await bot.send_message(message.chat.id,
                                   "Имя: " + i["name"] + " возраст " + ageRest + "\n" +
                                   "Настигает с: " + i["date_start"] + " по: " + i["date_end"])

            if i["file_poster_vertical"][-3:] != "jpg":
                await bot.send_message(message.chat.id, baseUrl + i["file_poster_vertical"])
            else:
                await bot.send_photo(message.chat.id, baseUrl + i["file_poster_vertical"])

            posts += 1

            if posts == 10:
                break


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(parser_cinematica_film, commands=['movies'])
