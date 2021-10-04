from pyrogram import Client, filters
from TimeBot import TimeTeller


# By Default Indian Time
@Client.on_message(filters.command("time"))
async def default_time(_, msg):
    if len(msg.command) == 1:
        time = TimeTeller.india()
        await msg.reply(time, quote=True)
    elif len(msg.command) == 2:
        time_zone = msg.command[1]
        time = TimeTeller.particular(time_zone)
        await msg.reply(time, quote=True)
    else:
        await msg.reply(
            "**Incorrect Time Zone** \n\nTime Zones are of only one word with format 'country/city' \n\nPlease Check all timezones by sending /timezones",
            quote=True)
