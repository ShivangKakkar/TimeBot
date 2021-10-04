from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from datetime import datetime
from TimeBot.unix import what

unix_filter = filters.create(lambda _, __, query: query.query.lower() == "unix")


# Inline Mode for Unix
@Client.on_inline_query(unix_filter)
async def answer(_, inline_query):
	unixtime = int(datetime.utcnow().timestamp())
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"Unix Time at Present",
				input_message_content=InputTextMessageContent(f"**UNIX TIME** :- `{unixtime}`"),
				description="Tap to send unix time to current chat",
				thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg",
			),
			InlineQueryResultArticle(
				title=f"What is Unix Time ?",
				input_message_content=InputTextMessageContent(what),
				description="Tap to know what is unix time",
				thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg",
			)
		],
		cache_time=1,
	)
