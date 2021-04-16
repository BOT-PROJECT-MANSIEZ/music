from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAx0CVs_uIgACAZJgeHSF8wXX0u4SBXgcBufDpcqeNwACaQEAAhAabSLT-dGKr5wzrR8E")
    await message.reply_text(
        f"""**Hey, saya {bn} 🎵

Saya adalah bot VC group telegram. 

Add saya ke group untuk memulai hal seru!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/KlikDisiniUntukBergabung"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="t.me/PoocongOnlen"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add saya ke group ➕", url="https://t.me/MusicIndonesiaBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Saya sudah siap, klik /cara untuk melihat penggunaan ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="t.me/PoocongOnlen")
                ]
            ]
        )
   )


