from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Apakah kamu ingin mencari Video YouTube?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Iya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Engga ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
