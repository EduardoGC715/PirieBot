from pyrogram import Client, filters

app = Client("PirieBot")


@app.on_message(filters.text & filters.private)
async def talk(client, message):
    if message.text.lower() == "hola":
        await message.reply(message.text)


app.run()
