# Telegram Bot Hujjati
  
![TgBot](https://celebrated-pudding-07af2f.netlify.app/images/ai.jpg)
)
   
        
## Umumiy ma'lumot  
  
ChatGPT — bu OpenAI tomonidan yaratilgan ilg‘or sun’iy intellekt modeli bo‘lib, inson tiliga yaqin matnlarni tushunish va yaratish qobiliyatiga ega. U foydalanuvchilarga turli sohalarda yordam ko‘rsatish uchun mo‘ljallangan va savollarga javob berish, tushuntirishlar berish, matn yozish, dasturlashda yordam ko‘rsatish kabi vazifalarni bajaradi.


**Atrof-muhitni sozlash**:
    Quyidagi parametrlarni qo'shing:

    ```
    TELEGRAM_BOT_TOKEN
    openai.api_key

    ```

### Buyruqlar

#### `/start`

```python
@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.reply("Salom! Men ChatGPT botman. Menga savollaringizni yozing.")  # noqa
```


## Asosiy kod
### Botni ishga tushirish uchun asosiy kod:

```main
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

```
## Owner:
### Bu bot Responsibility team tomonidan qilingan,
### Coders: @IbragimovIcciv, @Miraziz888
