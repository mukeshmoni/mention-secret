from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
TOKEN = getenv("TOKEN", "6213183796:AAH3zyr14_ZmJaVry5CoSBoBYjphcMAON3A")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", "6649395836"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/bot_testing_groups")

DEV_USERS = set(int(x) for x in getenv("DEV_USERS", "5854691181").split())
LOGGER_ID = getenv("LOGGER_ID", "-1001668749714")
