from pyrogram import Client, filters, types
from pyrogram.handlers import UserStatusHandler
import os

SENDER_ID = os.getenv("SENDER_ID")
CLIENT_NAME = os.getenv("CLIENT_NAME")
app = Client(CLIENT_NAME)

@app.on_message(filters.me != True and filters.private and types.Dialog)
async def message_handler(Client, message):
    await message.forward(SENDER_ID)


# async def user_status_handler(status, user, Client):
#     print(user)
#
# app.add_handler(UserStatusHandler(user_status_handler))

app.run()