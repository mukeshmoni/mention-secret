import asyncio
import importlib
import logging
import time

from Abg import patch  # type : ignore
from pyrogram import Client
from pyrogram.enums import ParseMode

from config import config

# Enable logging

logging.basicconfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("Tagslogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
OWNER_ID = config.OWNER_ID
StartTime = time.time()


class Abishnoi(Client):
    def __init__(self):
        super().__init__(
            "Abishnoi",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


Abishnoi = Abishnoi()
