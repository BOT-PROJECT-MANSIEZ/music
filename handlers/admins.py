from asyncio.queues import QueueEmpty
from cache.admins import set
from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic
import traceback
import os
import sys
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import filters, emoji
from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from config import que, admins as a


@Client.on_message(filters.command('reload'))
async def update_admin(client, message):
    global a
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    new_ads = []
    for u in admins:
        new_ads.append(u.user.id)
    a[message.chat.id] = new_ads
    await message.reply_text('✅ Daftar admin berhasil diperbarui di **{}**'.format(message.chat.title))


@Client.on_message(command("jeda") & other_filters)
@errors
@authorized_users_only
async def jeda(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("❗ Tidak ada yang diputar!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("▶️ Jeda!")
        
        
@Client.on_message(
    filters.command("clear")
)
@errors
async def clear(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("**✅ Admin list =** Cache admin berhasil disegarkan!")
        

@Client.on_message(command("lanjut") & other_filters)
@errors
@authorized_users_only
async def lanjut(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("❗ Tidak ada yang dijeda!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("⏸ Melanjutkan!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak ada yang ditayangkan!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌ Menghentikan siaran!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak ada yang dapat dilewati!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("➡️ Lewati sebuah lagu!")
        
        
   
