from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAx0CVs_uIgACAZJgeHSF8wXX0u4SBXgcBufDpcqeNwACaQEAAhAabSLT-dGKr5wzrR8E")
    await message.reply_text(
        f"""**Hey, saya {bn} π΅

Saya adalah bot VC group telegram. 

Add saya ke group untuk memulai hal seru!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π¬ Group", url="https://t.me/TheLittleMusic"
                    ),
                    InlineKeyboardButton(
                        "Pemilikπ€", url="https://t.me/Pocongonlen"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π DONATE π", url="https://link.dana.id/qr/3777ro50"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Saya sudah siap, ketik / cara untuk melihat penggunaan β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Channel", url="t.me/PoocongOnlen")
                ]
            ]
        )
   )


