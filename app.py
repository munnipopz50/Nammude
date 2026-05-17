from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "render_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private)
async def echo(client, message):
    await message.reply_text(f"Hello {message.from_user.first_name}!")

print("Bot Started...")
app.run()
