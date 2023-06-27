from pyrogram.types import InlineKeyboardButton

def add_button(message):
    button = InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", user_id=1057412250)
    if message.reply_markup:
        message.reply_markup.inline_keyboard.append([button])
    else:
        message.reply_markup = InlineKeyboardMarkup([[button]])
