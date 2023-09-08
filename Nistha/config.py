import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "29405343"))
API_HASH = getenv("API_HASH", "21cf17b612d3e12d02a8af0bef657759")
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
OWNER_USERNAME = getenv("OWNER_USERNAME")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5709622852").split()))
aiohttpsession = aiohttp.ClientSession()
