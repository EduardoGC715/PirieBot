from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery

from Database.DBManager import DBManager

from IKKeyboard import IKKeyboard
from IKButtons import IKButtons

bot = Client("PirieBot")
keyboards_factory = IKKeyboard()
buttons_factory = IKButtons()
database = DBManager()


def main_menu(client, update):
    buttons = buttons_factory.create_buttons(
        {"Áreas": "areas 0 Áreas",
         "Profesores": "teachers 0 Profesores"}
    )
    keyboard = keyboards_factory.create_keyboard(buttons, 3)
    reply_markup = InlineKeyboardMarkup(keyboard)
    client.send_message(chat_id=update.from_user.id, text="Menú principal", reply_markup=reply_markup)


def menu(client, update, t_kbsize, t_data):
    buttons = buttons_factory.create_buttons(database.select(t_data[0], t_data[1], t_data[2]))
    keyboard = keyboards_factory.create_keyboard(buttons, t_kbsize)
    reply_markup = InlineKeyboardMarkup(keyboard)
    client.send_message(chat_id=update.from_user.id, text=t_data[2], reply_markup=reply_markup)


@bot.on_callback_query()
def callback_handler(client: Client, callback_query: CallbackQuery):
    # Check the callback data and call the corresponding function
    menu(client, callback_query, 2, callback_query.data.split())


@bot.on_message(filters.command("menu"))
def open_menu_handler(client, update):
    main_menu(client, update)


@bot.on_message(filters.text & filters.private)
def talk(client, update):
    if update.text.lower() == "gloriana quirós":
        menu(client, update, 2, ["tcourses", "1", "Cursos"])


bot.run()
