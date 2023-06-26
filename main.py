from defs import getUrl, getcards, phone
from flask import Flask
import telethon
import asyncio
import os, sys
import re
import requests
from telethon import TelegramClient, events
import random_address
from random_address import real_random_address
import names
from datetime import datetime
import time
import random
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

API_ID = 20393133
API_HASH = 'c0b5c0973efd3a3f702695e2edf3b8b6'
SEND_ID = -1001943074057
client = TelegramClient('session', API_ID, API_HASH)
ccs = []
chats = [
   '@VegetaScrap',
    '@RevyDrops',
    '@TechzillaCheckerChat',
     '@secretgroup01',
      '@xfoxa',
    '@ritagroupOfc',
    '@AssociatonBinners1',
    '@accerroreschecker',
    '@ChatA2Assiad',
    '@Kurumichat',
     '@Venexchk',
     '@BinsHellChat',
     '@ScrapperLala',
     '@Hackezdroperr',
     '@deltaforcevips',
    '@anyascrapperchat',
    '@antichinasLBGT',
    '@TechzillaCheckerChat',
    '@ritagroupOfc',
    '@kurumichks',
    '@RemChatChk',
    '@secretgroup01',
    '@SitesCCSChat',
    '@team_pain_bins',
    '@ScrapperLala',
    '@IsagiChkLibre',
    '@accerroreschecker',
    '@botsakuraa',
    '@ccdropperchat',
    '@OficialScorpionsGrupo',
    '@dropsliveschat',
    '@webninjachatz',
    '@antichinasLBGT',
    '@cyberpirateschats',
    '@SpaceHackingG',
    '@THE_CARD_DROP',
    
  
]
with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue


@client.on(events.NewMessage(chats=chats, func=lambda x: getattr(x, 'text')))
async def my_event_handler(m):
    if m.reply_markup:
        text = m.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = m.text
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
    #print(f'{cc}|{mes}|{ano}|{cvv}')
    print(f'{cc}|{mes}|{ano}|{cvv} - Aprovada [a+]')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')
    await client.send_message(
        PeerChannel(SEND_ID),
        f""">_「 𝑆𝑐𝑟𝑎𝑝𝑒𝑟 @Was_FaReS ↯  」 _<
━━━━━━━━━━━━━━━━━ 
ꑭ < 𝒃𝒊𝒏 ⌯ {cc[:6]} | {bin_json['country_flag']}
ꑭ < 𝐶𝑎𝑟𝑑 ⌯ `{cc}|{mes}|{ano}|{cvv}`↯ 
🥀« 𝐼𝑛𝑓𝑜 ⌯  {bin_json['type']} ↯ 
🥀« 𝑇𝑦𝑝𝑒 ⌯ {bin_json['brand']}↯ 
🥀« 𝐵𝑎𝑛𝑘 ⌯ {bin_json['bank']} ↯ 
🥀« 𝑪𝑜𝑢𝑛𝑡𝑟𝑦 ⌯ {bin_json['country_name']} | {bin_json['country_flag']} ↯ 
🥀 « 𝐸𝑥𝑡𝑟𝑎 ⌯
ꑭ <  ⤷ `{extra}xxxx|{mes}|{ano}|{cvv}` ↯ 
━━━━━━━━━━━━━━━━━
🥀 « 𝐶𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦 ⌯「 @CRKSOO_CC ↯ 」
🥀 « 𝑂𝑤𝑛𝑒𝑟 ⌯「 @Was_FaReS ↯ 」
""",file = 'scra.jpg')


@client.on(events.NewMessage(outgoing=True, pattern=re.compile(r'.lives')))
async def my_event_handler(m):
    # emt = await client.get_entity(1582775844)
    # print(telethon.utils.get_input_channel(emt))
    # print(telethon.utils.resolve_id(emt))
    await m.reply(file='cards.txt')
    time.sleep(15)


client.start()
client.run_until_disconnected()
