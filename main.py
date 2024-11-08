from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.webhook_info import WebhookInfo

bot = Bot('7540206805:AAFh6UTmOo1bhVubKip49shMsqiPyfftAIQ')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Otktrity web sranicu', web_app= WebhookInfo(url='C:/phyton/start/tgbot_webp/p.html')))
    await message.answer("privet", reply_markup=markup)

 





executor.start_polling(dp)