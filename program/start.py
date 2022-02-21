from datetime import datetime
from sys import version_info
from time import time

from config import (
    alive_img,
    alive_name,
    bot_name,
    bot_username,
    group_support,
    owner_name,
    updates_channel,
)
from program import __version__
from driver.akshi import user
from driver.filters import command, other_filters
from pyrogram import client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import inlinekeyboardbutton, inlinekeyboardmarkup, message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


start_time = datetime.utcnow()
start_time_iso = start_time.replace(microsecond=0).isoformat()
time_duration_units = (
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
    for unit, div in time_duration_units:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@client.on_message(
    command(["start", f"start@{bot_username}"]) & filters.private & ~filters.edited
)
async def text_(client: client, message: message):
    await message.reply_text(
        f"""✨ **welcome {message.from_user.mention()} !**\n
💭 [{bot_name}](https://t.me/{bot_username}) **allows you to play music and video on groups through the new telegram's video chats!!**
💡 **find out all the bot's commands and how they work by clicking on the » 📚  commands button!**
🔖 **to know how to use this bot, please click on the » ❓ basic guide button!**
"""
   ,
        reply_markup=inlinekeyboardmarkup(
            [
                [
                    inlinekeyboardbutton(
                        "➕ 📍 add me to your group 📍 ➕",
                        url=f"https://t.me/{bot_username}?startgroup=true",
                    )
                ],
                
                [
                    inlinekeyboardbutton("commands 📚", callback_data="cbcmds"),
                    inlinekeyboardbutton("donate ❤️", url=f"https://t.me/{owner_name}"),
                ],
                [
                    inlinekeyboardbutton(
                        "official group 💖", url=f"https://t.me/{group_support}"
                    ),
                    inlinekeyboardbutton(
                        " official channel 😎", url=f"https://t.me/{updates_channel}"
                    ),
                ],
                [
                    inlinekeyboardbutton(
                        "🔹 source code 🔹", url="https://github.com/pragulofficial/music-bot"
                    )
                ],
            ]
        ),
        disable_web_page_preview=true,
    )
@client.on_message(
    command(["alive", f"alive@{bot_username}"]) & filters.private & ~filters.edited
)
async def alive(client: client, message: message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - start_time).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = inlinekeyboardmarkup(
        [
            [
                inlinekeyboardbutton("✨ group", url=f"https://t.me/{group_support}"),
                inlinekeyboardbutton(
                    "📣 channel", url=f"https://t.me/{updates_channel}"
                ),
            ]
        ]
    )

    alive = f"**hello {message.from_user.mention()}, i'm {bot_name}**\n\n✨ bot is working normally\n🍀 my master: [{alive_name}](https://t.me/{owner_name})\n✨ bot version: `v{__version__}`\n🍀 pyrogram version: `{pyrover}`\n✨ python version: `{__python_version__}`\n🍀 pytgcalls version: `{pytover.__version__}`\n✨ uptime status: `{uptime}`\n\n**thanks for adding me here, for playing video & music on your group's video chat** ❤"

    await message.reply_photo(
        photo=f"{alive_img}",
        caption=alive,
        reply_markup=keyboard,
    )


@client.on_message(command(["ping", f"ng@{bot_username}"]) & ~filters.edited)
async def ping(client: client, message: message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `pong!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@client.on_message(command(["uptime", f"uptime@{bot_username}"]) & ~filters.edited)
async def get_uptime(client: client, message: message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - start_time).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{start_time_iso}`"
    )


@client.on_message(filters.new_chat_members)
async def new_chat(c: client, m: message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **thanks for adding me to the group !**\n"
                "**promote me as administrator of the group, otherwise i will not be able to work properly**\n\n"
                "**once done, type** /reload\n\n"
                "**new to szrosebot, touch the below button to for quick setup guide**",
                reply_markup=inlinekeyboardmarkup(
                    [
                        [
                            inlinekeyboardbutton("quick setup guide", url="https://t.me/miss_akshi_updates/16")
                        ]
                    ]
                )
            )
