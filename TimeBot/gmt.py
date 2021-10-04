from pyrogram import Client, filters
from TimeBot import TimeTeller


@Client.on_message(filters.command("gmt"))
async def gmt_time(_, msg):
    time = TimeTeller.gmt()
    await msg.reply(time, quote=True)
