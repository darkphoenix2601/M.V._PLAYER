import asyncio
from pytgcalls import idle
from driver.Akshi import call_py, bot

async def start_bot():
    print("[Akshi]: STARTING BOT CLIENT")
    await bot.start()
    print("[Akshi]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    print("[Akshi]: STOPPING BOT & USERBOT")
    await bot.stop()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

