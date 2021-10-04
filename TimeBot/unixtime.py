from datetime import datetime
from pyrogram import Client, filters


@Client.on_message(filters.command(["unixtime"]))
async def unix_time(_, msg):
    unixtime = int(datetime.utcnow().timestamp())
    await msg.reply(f"**UNIX TIME** :- `{unixtime}`", quote=True)
