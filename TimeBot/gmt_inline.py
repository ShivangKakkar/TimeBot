from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from TimeBot import TimeTeller

gmt_filter = filters.create(lambda _, __, query: query.query.lower() == "gmt")


# Inline Mode for GMT
@Client.on_inline_query(gmt_filter)
async def answer(_, inline_query):
	gmt = TimeTeller.gmt()
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"GMT Time at Present",
				input_message_content=InputTextMessageContent(gmt),
				description="Tap to send gmt time to current chat",
				thumb_url="https://telegra.ph/file/b29908ccae574846c264a.jpg",
			)
		],
		cache_time=1,
	)
