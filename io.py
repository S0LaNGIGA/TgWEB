from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot("Your telegram token")
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть веб страницу", web_app=WebAppInfo(url="Your link to the site")))
    await message.answer("Привет, заходи в наше приложение!", reply_markup=markup)

@dp.message_handler(content_types=["web_app_data"])
async def get_data(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Имя: {res["name"]}\nEmail: {res["email"]}\nТелефон: {res["phone"]}')


executor.start_polling(dp)

