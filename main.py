import asyncio
from pyrogram import Client
from dotenv.main import load_dotenv
import os
load_dotenv()

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]

async def main():
    clientName = os.environ["client_name"]

    async with Client(clientName, api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

asyncio.run(main())