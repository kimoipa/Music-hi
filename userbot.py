import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بـنـك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم اعادة تشغيل ميوزك ماس **")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر","اوامر الاغاني"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
- هلا ياطيب  {m.from_user.mention} ✫
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
قائمـة اوامر سـورس ماس مـيـوزك. ✫
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
- أوامر المستخدمين: 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​✫
• {HNDLR}تشغيل
 اسم الاغنيه | رابط يوتيوب | الرد على ملف مقطع صوتي ​​​​•
 - لتشغيل مقطع صوتي في المكالمه
                                     ​​​​​​​​​​​​​✫
• {HNDLR}فيديو
 عنوان الفيديو | رابط يوتيوب | الرد على الفيديو ​​​​•
 - لتشغيل فيديو في المكالمة
                                     ​​​​​​​​​​​✫
• {HNDLR}القائمة
  - لعرض قائمة التشغيل الحالية
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}بنك
 - لعرض سرعه النت للبوت
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}الاوامر
 - لعرض اوامر سورس ميوزك ماس 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
- أوامر المشرفين  : 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}كمل
 - لمواصلة تشغيل المقطع الصوتي أو الفيديو المتوقف
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}وقف
 - لإيقاف تشغيل المقطع الصوتي أو مقطع فيديو مؤقتًا
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}عدي
 - لتخطي المقطع الصوتي أو الفيديو الحالي وتشغيل ما بعده
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}انهاء
 - لإنهاء التشغيل
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
قناة السورس : @e1r_1
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["السورس", "الريبو", "سورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>❤️ هلو {m.from_user.mention}!
      ✪ 🆂︎ سورس ميوزك 🅼︎ ماس ✪

 سورس ماس افضل السورسات على تليجرام تنصيبات مجانيه تابع قناتنا في الاسفل.

»  
• [قناة السورس](https://t.me/e1r_1)
• [كروب الدعم](https://t.me/e1r_2)


»  ✪ مبرمج السورس ✪
 • 
» [𝐒𝐈𝐅 𝐂𝐎𝐁𝐑𝐀](https://t.me/e1r_6) 
 
 </b>
"""
    await m.reply(REPO, disable_web_page_preview=True)
