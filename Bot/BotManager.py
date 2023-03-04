from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Database.DBManager import DBManager


bot = Client("PirieBot")
db = DBManager


def main_menu(client, update):
    keyboard = [
        [
            InlineKeyboardButton("Áreas", callback_data="area_menu")
        ],
        [
            InlineKeyboardButton("Profesores", callback_data="teacher_menu")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    client.send_message(chat_id=update.from_user.id, text="Menú principal", reply_markup=reply_markup)


def area_menu(client, update):
    # Create the inline keyboard markup
    keyboard = [[InlineKeyboardButton("Atrás", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message with the inline keyboard markup
    client.send_message(chat_id=update.from_user.id, text="Áreas", reply_markup=reply_markup)


def teacher_menu(client, update):
    # Create the inline keyboard markup
    keyboard = [[InlineKeyboardButton("Atrás", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message with the inline keyboard markup
    client.send_message(chat_id=update.from_user.id, text="Profesores", reply_markup=reply_markup)


@bot.on_callback_query()
def callback_handler(client: Client, callback_query: CallbackQuery):
    # Check the callback data and call the corresponding function
    if callback_query.data == "area_menu":
        area_menu(client, callback_query)

    elif callback_query.data == "teacher_menu":
        teacher_menu(client, callback_query)

    elif callback_query.data == "main_menu":
        main_menu(client, callback_query)


@bot.on_message(filters.command("menu"))
def open_menu_handler(client, update):
    main_menu(client, update)


@bot.on_message(filters.text & filters.private)
def talk(client, update):
    if update.text.lower() == "hola":
        update.reply(update.text)




bot.run()
