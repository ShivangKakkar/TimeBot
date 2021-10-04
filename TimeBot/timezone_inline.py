from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from TimeBot import TimeTeller
from Data import Data

time_filter = filters.create(lambda _, __, query: query.query.lower() not in ["", "gmt", "unix", "time"])


# Inline Mode for GMT
@Client.on_inline_query(time_filter)
async def answer(_, inline_query):
    time_zone = inline_query.query
    string = TimeTeller.particular(time_zone)
    if string.startswith("**Unknown"):
        await inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title=f"Unknown TimeZone - {time_zone}",
                    input_message_content=InputTextMessageContent(string),
                    description=f"Timezone {time_zone} doesn't exist. Tap to know how to fix this.",
                    thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg",
                ),
                InlineQueryResultArticle(
                    title=f"How to use this bot ?",
                    input_message_content=InputTextMessageContent(Data.HELP, parse_mode="Markdown"),
                    description=f"Tap to know how to use me properly.",
                    thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg",
                )
            ],
            cache_time=1,
        )
    else:
        await inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title=f"{time_zone}'s Time",
                    input_message_content=InputTextMessageContent(string),
                    description=f"Tap to know {time_zone}'s time to current chat",
                    thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg"
                )
            ],
            cache_time=1,
        )
