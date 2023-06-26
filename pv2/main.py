from defs import getUrl, getcards, phone
from pyrogram import Client, filters
import asyncio
import os, sys
import re
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 20393133
API_HASH = 'c0b5c0973efd3a3f702695e2edf3b8b6'
SEND_ID = -1001943074057
client = Client('session', api_id=API_ID, api_hash=API_HASH)
ccs = []
chats = [
    '@HQ_cc_Live',
]

with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue


@client.on_message(filters.chat(chats) & filters.text)
async def my_event_handler(client, message):
    if message.reply_markup:
        text = message.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = message.text
    cards = getcards(text)
    if not cards:
        return
    cc, mes, ano, cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    extra = cc[0:0 + 12]
    bin = requests.get(f'https://bins.antipublic.cc/bins/{cc[:6]}')
    if not bin:
        return
    bin_json = bin.json()
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}"
    # print(f'{cc}|{mes}|{ano}|{cvv}')
    print(f'{cc}|{mes}|{ano}|{cvv} - Aprovada [a+]')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')
    await client.send_photo(
        chat_id=SEND_ID,
        photo='heart4youu.jpg',
        caption=f""">_「 𝑆𝑐𝑟𝑎𝑝𝑒𝑟 @Was_FaReS ↯  」 _<
━━━━━━━━━━━━━━━━━ 
ꑭ < ʙɪɴ ⌯ {cc[:6]} | {bin_json['country_flag']}
ꑭ < ᴄᴀʀᴅ ⌯ `{cc}|{mes}|{ano}|{cvv}`↯ 
🥀« ɪɴғᴏ ⌯  {bin_json['type']} ↯ 
🥀« ᴛʏᴘᴇ ⌯ {bin_json['brand']}↯ 
🥀« ʙᴀɴᴋ ⌯ {bin_json['bank']} ↯ 
🥀« ᴄᴏᴜɴᴛʀʏ ⌯ {bin_json['country_name']} | {bin_json['country_flag']} ↯ 
🥀 « 𝐸𝑥𝑡𝑟𝑎 ⌯
ꑭ <  ⤷ `{extra}xxxx|{mes}|{ano}|{cvv}` ↯ 
━━━━━━━━━━━━━━━━━
🥀 « 𝐶𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦 ⌯「 @CRKSOO_CC ↯ 」
🥀 « 𝑂𝑤𝑛𝑒𝑟 ⌯「 @Was_FaReS ↯ 」
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Developer", url="https://t.me/Was_FaReS")],
                [InlineKeyboardButton("Channel", url="https://t.me/CRKSOO_CC")],
            ]
        )
    )


@client.on_message(filters.outgoing & filters.regex(r'.lives'))
async def my_event_handler(client, message):
    await message.reply_document(document='cards.txt')
    await asyncio.sleep(15)


client.start()
client.run()
