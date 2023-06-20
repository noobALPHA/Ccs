from telethon.sync import TelegramClient, events

api_id = 0000000
api_hash = 'hash'
done = 0
total_cc_count = sum(1 for line in open('cc.txt'))

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage(from_users='SDBB_Bot'))
@client.on(events.MessageEdited(from_users='SDBB_Bot'))
async def handle_message(event):
    global done
    if 'wait' in event.message.text or 'Waiting' in event.message.text:
        return
       
    done += 1
    print(event.message.text.replace("`", ""))
    print()
    
    if done == total_cc_count:
        client.disconnect()

async def send_message_to_bot(cc):
    await client.send_message('SDBB_Bot', f'/vbv {cc}')

async def main():
    with open('cc.txt', 'r') as file:
        for line in file:
            cc = line.strip()
            await send_message_to_bot(cc)
            if done == total_cc_count:
                break

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
