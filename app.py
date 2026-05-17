from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("1778836"))
API_HASH = os.environ.get("7bcf61fcd32b8652cd5876b02dcf57ae")
BOT_TOKEN = os.environ.get("2108094040:AAGtt-AtXwPcqqmJ7I7SycZqIt-Y-CazV3s")

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
