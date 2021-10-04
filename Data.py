from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I am a Time Teller bot and I can show time of different places in different ways (Not Wakanda :P).

Use below buttons to learn more !

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
Use below commands to use me. I can be used everywhere including here, groups, channels and even inline mode so that you can use me in groups where I'm not present.

**Available Commands** :-
/time - `Time at present (defaults to India).`
/time any_time_zone - `Time of that time zone at present.`
/timezones - `List all timezones.`
/search <continent/country/city> - `Search for timezone(s) for that continent/country/city.`
/gmt - `GMT time at present.`
/unixtime - `Unix Time at present. Same around the globe.`
/unix - `What is unix time?`
/about - `About this bot and source code.`
/help - `This Message.`
/start - `Check if bot is alive.`

**Inline Mode** :-
Format :- "`@TimeTellerBot <pass some text>`"
Use above format to use inline mode as follows:
- Pass no text or pass "time" to get current time.
- Pass any timezone to get that timezone's current time.
- Pass "gmt" to get current GMT time.
- Pass "unix" as text to get current unix time or learn 'What is unix ?'
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to show time of different places in different ways. by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/TimeBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
