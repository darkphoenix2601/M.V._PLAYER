from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.Akshi import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/38ca11b0fb33d6d9cf472.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━
🖤 ʜᴇʏ,
      ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
┏━━━━━━━━━━━━━━┓
┣★ᴄʀᴇᴀᴛᴏʀ: [VOID](t.me/voidxtoxic)
┗━━━━━━━━━━━━━━┛
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/VOIDXTOXIC) ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Add Void To Your Gc •", url="https://t.me/void_group_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "✗ ᴄʀᴇᴀᴛᴏʀ ✗", url="https://t.me/voidxtoxic"
                    ),
                    InlineKeyboardButton(
                        "✗ sᴜᴘᴘᴏʀᴛ ✗", url="https://t.me/horimiya_family"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "✗ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​ ✗", url="https://t.me/horimiya_family"
                    )]
            ]
       ),
    )

@Client.on_message(command(["ping", "repo", "voidvc", "alive"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZIiVngACSppiDZZGd6IPFA0TnEuOM3EqFbRxVQACCQMAArU72FSskU3O5FiqcyME")
    await message.reply_text(
        text=f"""» ɪ ᴀᴍ ᴀʟɪᴠᴇ ree !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✗ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✗", url="https://t.me/voidxtoxic")
                  ],[
                    InlineKeyboardButton(
                        "✗ sᴜᴘᴘᴏʀᴛ ✗", url="https://t.me/horimiya_family"
                    ),
                    InlineKeyboardButton(
                        "✗ sᴏᴜʀᴄᴇ ✗", url="https://t.me/horimiya_family"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "✗ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ​​ ✗", url="https://t.me/void_group_bot?startgroup=true"
                    )]
            ]
        ),
    )

