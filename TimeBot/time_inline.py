from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from TimeBot import TimeTeller
from Data import Data

empty_filter = filters.create(lambda _, __, query: query.query.lower() in ["", "time"])


# Inline Mode
@Client.on_inline_query(empty_filter)
async def answer(_, inline_query):
	string = TimeTeller.india()
	if inline_query.query == "time":
		await inline_query.answer(
			results=[
				InlineQueryResultArticle(
					title=f"Time at Present",
					input_message_content=InputTextMessageContent(string),
					description="Tap to send time to current chat",
					thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg",
				)
			],
			cache_time=1,
		)
	elif inline_query.query == "":
		await inline_query.answer(
			results=[
				InlineQueryResultArticle(
					title=f"Time at Present",
					input_message_content=InputTextMessageContent(string),
					description="Tap to send time to current chat",
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
