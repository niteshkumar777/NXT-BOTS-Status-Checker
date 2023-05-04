from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
TIME_ZONE = getenv("TIME_ZONE")
BOT_LIST = list(getenv("BOT_LIST").split())
CHANNEL_ID = getenv("CHANNEL_ID")
MESSAGE_ID = int(getenv("MESSAGE_ID"))
BOT_ADMIN_IDS = list(getenv("BOT_ADMIN_IDS"))
GRP_ID = getenv("GRP_ID")
