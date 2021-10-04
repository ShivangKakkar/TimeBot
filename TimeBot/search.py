import pytz
from pyrogram import Client, filters


@Client.on_message(filters.command(["search"]))
async def search(_, msg):
    if len(msg.command) == 1:
        pass
    elif len(msg.command) == 2:
        location = (msg.command[1]).capitalize()
        tz = []
        for line in pytz.all_timezones:
            # try:
            line1 = line.split("/")
            line1.append(line)
            # except:
            #     words = [line]
            if location in line1:
                tz.append(line)
        if len(tz) > 0:
            if len(tz) == 1:
                string = f"**Timezone Found** : `{tz[0]}`"
            else:
                string = "**Timezones Found** \n\n"
                n = 0
                for t in tz:
                    n += 1
                    string += f"{n})  `{t}`\n"
            await msg.reply(string, quote=True)
        else:
            await msg.reply("No Such Timezone Found.", quote=True)
