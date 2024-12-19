import openai
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

openai.api_key = ""

# Telegram Bot tokeni
TELEGRAM_BOT_TOKEN = ""

# Aiogram bot va dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.reply("Salom! Men ChatGPT botman. Menga savollaringizni yozing.")

@dp.message()
async def handle_message(message: Message):
    user_message = message.text
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Yangi model nomi
            messages=[
                {"role": "system", "content": "Siz foydalanuvchiga yordam beradigan bot siz."},
                {"role": "user", "content": user_message},
            ],
        )
    bot_reply = response['choices'][0]['message']['content']
    await message.reply(bot_reply)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
