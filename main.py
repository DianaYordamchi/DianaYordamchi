import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = '7814032384:AAHnTMvAoHfyHVyojan0k0OBeWuOzqwxaiY'
ADMIN_ID = 932283822  # Abdulmajidning Telegram ID raqami

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Salom, men DianaAssistant 🤖\n\nSMM kurslari haqida qiziqyapsizmi? Unda keling tanishamiz! \nIsmingizni va telefon raqamingizni yozib qoldiring, men esa siz haqingizdagi ma’lumotni menejerimizga uzataman. 😊")

@dp.message_handler(lambda message: True)
async def handle_info(message: types.Message):
    user_info = f"🆕 Yangi foydalanuvchi\n\n👤 Ismi: {message.from_user.full_name}\n📝 Xabar: {message.text}\n🆔 Username: @{message.from_user.username if message.from_user.username else 'yo‘q'}"

    await bot.send_message(ADMIN_ID, user_info)
    await message.reply("Rahmat! Ma’lumotlaringizni oldik. Tez orada siz bilan menejerimiz bog‘lanadi. 👩‍💼\nAgar boshqa savollaringiz bo‘lsa, yozaverishingiz mumkin.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
