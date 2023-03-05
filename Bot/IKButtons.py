from pyrogram.types import InlineKeyboardButton


class IKButtons:
    def create_buttons(self, t_buttons_data):
        button_list = []
        for data in t_buttons_data:
            button = InlineKeyboardButton(data, callback_data=t_buttons_data[data])
            button_list.append(button)
        return button_list