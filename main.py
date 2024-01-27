import os

from pyrogram import Client, filters
from pyrogram.types import Message

# Укажите токен вашего бота
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Укажите ID вашего канала, куда будут отправляться сообщения
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Массив ключевых слов
KEYWORDS = ['perevod', 'перевод', 'perevodchik', 'tarjimon', 'tarjima', 'kerak', 'kere', 'kk', 'керак', 'кере', 'kk', 'переводчик', 'таржимон', 'таржима', 'нужен', 'ищем']

# Создаем клиент Pyrogram
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH)

# Функция для отправки сообщения на канал
async def send_to_channel(original_message: Message, user):
    user_mention = f"@{user.username}" if user.username else user.first_name
    message_link = f"https://t.me/{original_message.chat.username}/{original_message.id}"
    text = (f"🔎 Найдено сообщение с ключевым словом в группе **{original_message.chat.title}**s!\n\n"
            f"👤 Пользователь: [{user_mention}](tg://user?id={user.id})\n"
            f"📝 Текст сообщения: **{original_message.text}**\n")
    if original_message.chat.username != None:
        text += (f"🔸 Ссылка на сообщение: {message_link}")

    await app.send_message(CHANNEL_ID, text, disable_web_page_preview=True)


# Функция-обработчик для проверки каждого сообщения
@app.on_message(filters.group & ~filters.me)
async def check_message(client, message):
    for keyword in KEYWORDS:
        if keyword.lower() in message.text.lower():
            messageInfo = await app.get_messages(message.chat.id, message.id)
            await app.send_message(CHANNEL_ID, messageInfo, disable_web_page_preview=True)
            # await app.send_message(CHANNEL_ID, message, disable_web_page_preview=True)
            await send_to_channel(message, message.from_user)
            break

# Запускаем бота
app.run()