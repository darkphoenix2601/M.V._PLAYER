import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Doreamon_music")
ALIVE_NAME = getenv("ALIVE_NAME", "Akshi")
BOT_USERNAME = getenv("BOT_USERNAME", "Miss_Akshi2_0_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Miss_Akshi")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Darkphoenix_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Miss_Akshi_updates")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a7ca957dfc07340df2d3f.mp4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/darkphoenix2601/video_stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e623eef8d0095ae8de786.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/03b1f7fe0bbbde39db832.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/fc45bf199525bd137d675.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/35649978e8135b03287fe.png")
