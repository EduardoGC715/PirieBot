import openpyxl
import os

from Bot.IKKeyboard import IKKeyboard
from Bot.IKButtons import IKButtons
from pyrogram.types import InlineKeyboardMarkup


class DBManager:
    def __init__(self):
        # opening the workbook with the data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # navigate to the data directory and open the file
        file_path = os.path.join(current_dir, "Data/database.xlsx")
        self.wb = openpyxl.load_workbook(file_path, read_only=True)
        # factories for keyboards and buttons
        self.keyboards_factory = IKKeyboard()
        self.buttons_factory = IKButtons()

    def query_to_reply(self, t_menu, t_code, t_ws):
        itr = 0
        try:
            ws = self.wb[t_ws]
        except KeyError:
            ws = None
        button_dict = {}
        text = ""

        if t_menu == "main":
            text = "Menú Principal"
            button_dict = {"Consultas de Cursos": "queries 0 None"}

        elif t_menu == "queries":
            text = "Menú de Consultas"
            button_dict = {"Áreas": "areas 0 Áreas",
                           "Profesores": "teachers 0 Profesores"
                           }

        elif t_menu == "areas":
            text = "Áreas"
            for row in ws.values:
                itr += 1
                button_dict[str(row[0])] = "area_courses " + str(itr) + " Cursos"

        elif t_menu == "teachers":
            text = "Profesores"
            for row in ws.values:
                itr += 1
                if itr > 19:
                    break
                button_dict[str(row[1])] = "teacher_courses " + str(itr) + " Cursos"

        elif t_menu == "area_courses":
            text = str(self.wb["Áreas"]["A" + t_code].value)
            for row in ws.values:
                itr += 1
                if t_code == str(row[1]):
                    button_dict[str(row[2])] = "groups " + str(itr) + " Grupos"

        elif t_menu == "teacher_courses":
            text = str(self.wb["Profesores"]["B" + t_code].value)
            for row in ws.values:
                itr += 1
                if t_code == str(row[0]):
                    button_dict[str(row[2])] = "groups " + str(itr) + " Grupos"

        elif t_menu == "groups":
            text = str(self.wb["Cursos"]["C" + t_code].value) + "\nGrupos disponibles:\n"
            button_dict[0] = 0
            for row in ws.values:
                itr += 1
                if t_code == str(row[0]) and row[7] == 1:
                    text = (text + "\nModalidad: " + str(row[1]) + "\nPrecio: " + str(row[2]) + "\nHorario: " +
                            str(row[3]) + "\nRequisitos: " + str(row[4]) + "\nDuración: " + str(row[5]) +
                            "\nAula: " + str(row[6]) + "\n"
                            )

        reply_data = [text, button_dict]
        return reply_data

    def reply_maker(self, t_data):
        # t_data = [t_menu, t_code, t_ws]

        query = self.query_to_reply(t_data[0], t_data[1], t_data[2])
        if any(query[1]):
            message = query[0]
            buttons = self.buttons_factory.create_buttons(query[1])
            keyboard = self.keyboards_factory.create_keyboard(buttons, 2)
            markup = InlineKeyboardMarkup(keyboard)
            reply = [message, markup]
        else:
            message = query[0]
            reply = [message, 0]

        return reply
