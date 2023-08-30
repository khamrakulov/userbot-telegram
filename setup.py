from pyrogram import Client
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

app.run()