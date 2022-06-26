from io import BytesIO
from traceback import format_exc

import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ

from config import HNDLR
from MusicAndVideo.helpers.merrors import capture_err

ARQ_API_KEY = "HMPXNS-BDPCCB-UJKRPU-OQADHG-ARQ"
aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)


async def quotify(messages: list):
    response = await arq.quotly(messages)
    if not response.ok:
        return [False, response.result]
    sticker = response.result
    sticker = BytesIO(sticker)
    sticker.name = "sticker.webp"
    return [True, sticker]


def getArg(message: Message) -> str:
    arg = message.text.strip().split(None, 1)[1].strip()
    return arg


def isArgInt(message: Message) -> bool:
    count = getArg(message)
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]


@Client.on_message(filters.command(["q", "quote"], prefixes=f"{HNDLR}"))
@capture_err
async def quotly_func(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Rᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ǫᴜᴏᴛᴇ ɪᴛ")
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Rᴇᴘʟʏ ᴍᴇssᴀɢᴇs ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴛᴇxᴛ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴇxᴛ ᴍᴇssᴀɢᴇs"
        )
    m = await message.reply_text("`Cʀᴇᴀᴛɪɴɢ ᴀ ᴍᴇssᴀɢᴇ ǫᴜᴏᴛᴇ...`")
    if len(message.command) < 2:
        messages = [message.reply_to_message]

    elif len(message.command) == 2:
        arg = isArgInt(message)
        if arg[0]:
            if arg[1] < 2 or arg[1] > 10:
                return await m.edit("Aʀɢᴜᴍᴇɴᴛs ᴍᴜsᴛ ʙᴇ ʙᴇᴛᴡᴇᴇɴ 2-10.")
            count = arg[1]
            messages = await client.get_messages(
                message.chat.id,
                [
                    i
                    for i in range(
                        message.reply_to_message.message_id,
                        message.reply_to_message.message_id + count,
                    )
                ],
                replies=0,
            )
        else:
            if getArg(message) != "r":
                return await m.edit("**sᴏʀʀʏ**`")
            reply_message = await client.get_messages(
                message.chat.id,
                message.reply_to_message.message_id,
                replies=1,
            )
            messages = [reply_message]
    else:
        await m.edit("**ᴇʀʀᴏʀ**")
        return
    try:
        sticker = await quotify(messages)
        if not sticker[0]:
            await message.reply_text(sticker[1])
            return await m.delete()
        sticker = sticker[1]
        await message.reply_sticker(sticker)
        await m.delete()
        sticker.close()
    except Exception as e:
        await m.edit(
            "Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴡʜɪʟᴇ ǫᴜᴏᴛɪɴɢ ᴛʜᴇ ᴍᴇssᴀɢᴇ, ᴄᴀɴ ʏᴏᴜ"
            + " ᴛʜɪs ᴇʀʀᴏʀ  ᴜsᴜᴀʟʟʏ ᴏᴄᴄᴜʀs ᴡʜᴇɴ ᴛʜᴇʀᴇ ɪs "
            + " ᴀ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴀɪɴɪɴɢ sᴏᴍᴇᴛʜɪɴɢ sᴏᴍᴇᴛʜɪɴɢ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴛᴇxᴛ."
        )
        e = format_exc()
        print(e)
