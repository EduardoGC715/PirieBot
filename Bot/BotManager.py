from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from Database.DBManager import DBManager
from Bot.IKKeyboard import IKKeyboard
from Bot.IKButtons import IKButtons

bot = Client("PirieBot")
keyboards_factory = IKKeyboard()
buttons_factory = IKButtons()
database = DBManager()

aux_buttons = {
    "main": ["Menú Principal", {
        "Consultas de Cursos": "menu queries"
    }
             ],
    "queries": ["Menú de Consultas", {
        "Áreas": "areas 0 Áreas",
        "Profesores": "teachers 0 Profesores"
    }
                ]
}


def menu(client, update, t_kbsize, t_data):
    if t_data[0] == "menu":
        buttons = buttons_factory.create_buttons(aux_buttons[t_data[1]][1])
        title = aux_buttons[t_data[1]][0]
        keyboard = keyboards_factory.create_keyboard(buttons, t_kbsize)
        reply_markup = InlineKeyboardMarkup(keyboard)
        client.send_message(chat_id=update.from_user.id, text=title, reply_markup=reply_markup)
    else:
        query = database.select(t_data[0], t_data[1], t_data[2])
        if isinstance(query, str):
            title = query
            client.send_message(chat_id=update.from_user.id, text=title)
            client.send_message(chat_id=update.from_user.id, text=title)
        else:
            buttons = buttons_factory.create_buttons(query[1])
            title = query[0]
            keyboard = keyboards_factory.create_keyboard(buttons, t_kbsize)
            reply_markup = InlineKeyboardMarkup(keyboard)
            client.send_message(chat_id=update.from_user.id, text=title, reply_markup=reply_markup)


@bot.on_callback_query()
def callback_handler(client: Client, callback_query: CallbackQuery):
    # Check the callback data and call the corresponding function
    data = callback_query.data.split()
    menu(client, callback_query, 2, data)


@bot.on_message(filters.command("menu"))
def open_menu_handler(client, update):
    # can add more functions to new buttons here
    menu(client, update, 2, ["menu", "main"])


@bot.on_message(filters.text & filters.private)
def talk(client, update):
    if update.text.lower() == "gloriana quirós":
        menu(client, update, 2, ["tcourses", "1", "Cursos"])


def run_bot():
    bot.run()
