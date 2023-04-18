from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from Database.DBManager import DBManager

bot = Client("PirieBot")

database = DBManager()


def send_message(client, update, t_reply):
    if t_reply[1] != 0:
        client.send_message(chat_id=update.from_user.id, text=t_reply[0], reply_markup=t_reply[1])
    else:
        client.send_message(chat_id=update.from_user.id, text=t_reply[0])


@bot.on_callback_query()
def callback_handler(client: Client, callback_query: CallbackQuery):
    # Check the callback data and send it to the DBManager
    data = callback_query.data.split()
    reply = database.reply_maker(data)
    send_message(client, callback_query, reply)


@bot.on_message(filters.command("menu"))
def open_menu_handler(client, update):
    # Check command and send it to the DBManager
    reply = database.reply_maker(["main", "0", "None"])
    send_message(client, update, reply)


@bot.on_message(filters.text & filters.private)
def message_handler(client, update):
    # Check message and send it to the DBManager
    reply = database.reply_maker(["main", "0", "None"])
    send_message(client, update, reply)


def run_bot():
    # function to run bot
    bot.run()
