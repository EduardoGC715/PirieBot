import openpyxl
import os


class DBManager:
    def __init__(self):
        # opening the workbook with the data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # navigate to the data directory and open the file
        file_path = os.path.join(current_dir, "Data/database.xlsx")
        self.wb = openpyxl.load_workbook(file_path, read_only=True)

    def style_row(self, t_row, t_itr):
        sms = ""
        # (10, 3, 'creciendo con el arte 1', None)
        sms += str(self.wb["Áreas"]["A" + str(t_itr)].value)
        return sms

    def select(self, t_method, t_code, t_ws):
        itr = 0
        ws = self.wb[t_ws]
        button_dict = {}
        text = ""

        if t_method == "areas":
            text = "Áreas"
            for row in ws.values:
                itr += 1
                button_dict[str(row[0])] = "acourses " + str(itr) + " Cursos"

        elif t_method == "teachers":
            text = "Profesores"
            for row in ws.values:
                itr += 1
                if itr > 19:
                    break
                button_dict[str(row[1])] = "tcourses " + str(itr) + " Cursos"

        elif t_method == "acourses":
            text = str(self.wb["Áreas"]["A" + t_code].value)
            for row in ws.values:
                if t_code == str(row[1]):
                    itr += 1
                    button_dict[str(row[2])] = "groups " + str(itr) + " Grupos"

        elif t_method == "tcourses":
            text = str(self.wb["Profesores"]["B" + t_code].value)
            for row in ws.values:
                if t_code == str(row[0]):
                    itr += 1
                    button_dict[str(row[2])] = "groups " + str(itr) + " Grupos"

        elif t_method == "groups":
            text = str(self.wb["Cursos"]["C" + t_code].value)
            button_dict[0] = 0
            for row in ws.values:
                if t_code == str(row[0]):
                    itr += 1
            return text

        to_return = [text, button_dict]
        return to_return
