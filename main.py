from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, PeerIdInvalid

# Configuration
API_ID = 12345678 #CHANGE WITH YOUR API_ID
API_HASH = "YOUR_API_HASH" #CHANGE WITH YOUR API_HASH
BOT_TOKEN = "YOUR_BOT_TOKEN" #CHANGE WITH YOUR BOT TOKEN
CHANNEL_ID = -100 # REPLACE WITH YOUR CHANNEL ID
CHANNEL_URL = "https://t.me/HyperBotChannel"  # REPLACE WITH YOUR FORCE CHANNEL URL

app = Client(
    "force_join_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.forwarded)
async def forwarded_message_handler(client, message):
    watermark = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌟 Bot Repository URL", url="https://github.com/farhanachyar")]
    ])

    if message.forward_from_chat:

        chat_id = message.forward_from_chat.id
        chat_title = message.forward_from_chat.title
        chat_type = message.forward_from_chat.type
        chat_username = message.forward_from_chat.username

        info_text = f"**Forwarded Chat Information**\n\n"
        info_text += f"• **Chat ID:** `{chat_id}`\n"
        info_text += f"• **Title:** {chat_title}\n"
        info_text += f"• **Type:** {chat_type}\n"
        
        if chat_username:
            info_text += f"• **Username:** @{chat_username}\n"
            info_text += f"• **Link:** https://t.me/{chat_username}"
        
        await message.reply(info_text, reply_markup=watermark)
        
    elif message.forward_from:
        user_id = message.forward_from.id
        user_name = f"{message.forward_from.first_name} {message.forward_from.last_name or ''}"
        username = message.forward_from.username

        info_text = f"**Forwarded User Information**\n\n"
        info_text += f"• **User ID:** `{user_id}`\n"
        info_text += f"• **Name:** {user_name}\n"
        
        if username:
            info_text += f"• **Username:** @{username}"

        await message.reply(info_text, reply_markup=watermark)
        
    else:
        await message.reply(
            "ℹ️ Cannot find original sender information from the forwarded message.\n"
            "This may happen if the original sender has privacy settings that restrict it.",
            reply_markup=watermark
        )

@app.on_message(filters.private & ~filters.bot, group=0)
async def check_channel_member(client, message):
    user_id = message.from_user.id
    
    try:
        member = await client.get_chat_member(CHANNEL_ID, user_id)
        await message.continue_propagation()
        
    except (UserNotParticipant, PeerIdInvalid):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔔 Join Channel", url=CHANNEL_URL)],
            [InlineKeyboardButton("🌟 Bot Repository URL", url="https://github.com/Farhanachyar/Force-Join-Channel-Telegram-Bot")]
        ])

        await message.reply(
            "⚠️ To use this bot, you must join our channel first.\n\n"
            "Please click the button below to join, then try using the bot again.",
            reply_markup=keyboard
        )
        return

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    watermark = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌟 Bot Repository URL", url="https://github.com/Farhanachyar/Force-Join-Channel-Telegram-Bot")]
    ])
    
    await message.reply(
        f"👋 Hello {message.from_user.mention}!\n\n"
        "Welcome to our bot. You have joined our channel, "
        "so you can use all the features of this bot.",
        reply_markup=watermark
    )

@app.on_message(filters.command("help") & filters.private)
async def help_command(client, message):
    watermark = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌟 Bot Repository URL", url="https://github.com/Farhanachyar/Force-Join-Channel-Telegram-Bot")]
    ])
    
    await message.reply(
        "📚 Bot Help\n\n"
        "Available commands:\n"
        "• /start - Start the bot\n"
        "• /help - Display help\n"
        "• /info - Display user information",
        reply_markup=watermark
    )

@app.on_message(filters.command("info") & filters.private)
async def info_command(client, message):
    watermark = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌟 Bot Repository URL", url="https://github.com/Farhanachyar/Force-Join-Channel-Telegram-Bot")]
    ])
    
    user = message.from_user
    await message.reply(
        f"👤 **User Information**\n\n"
        f"• **ID:** `{user.id}`\n"
        f"• **Name:** {user.first_name} {user.last_name or ''}\n"
        f"• **Username:** @{user.username or 'None'}",
        reply_markup=watermark
    )

if __name__ == "__main__":
    print("Bot has been started...")
    print("==================================")
    print("🌟 Bot by @farhanachyar on GitHub")
    print("https://github.com/farhanachyar")
    print("🌟 Bot Repository URL")
    print("https://github.com/Farhanachyar/Force-Join-Channel-Telegram-Bot")
    print("==================================")
    app.run()
