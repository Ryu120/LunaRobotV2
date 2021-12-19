import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/b5106f8f3b2a0b4c340ef.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**I am the Ghost of Uchiha!** \n\n"
  LUNA += "🔴 **I'm Working Properly** \n\n"
  LUNA += "🔴 **My Master : [𝚁 𝚢 𝚞](https://t.me/Ryu_God)** \n\n"
  LUNA += f"🔴 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/MadaraXRoBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/komisansupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  Madara = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/Komisansupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
