import openpyxl


class DBManager:
    def __init__(self):
        # opening the workbook with the data
        self.wb = openpyxl.load_workbook('../Database/Data/database.xlsx', read_only=True)

    def style_row(self, t_row, t_type):
        sms = "Area: "
        if t_type == ("acourses" or "tcourses"):
            # (10, 3, 'creciendo con el arte 1', None)
            sms += str(self.wb["areas"]["A" + str(t_row[1])].value)
            print(sms)

    def select(self, t_method, t_code, t_ws):
        itr = 1
        ws = self.wb[t_ws]
        button_dict = {}

        if t_method == "areas":
            for row in ws.values:
                itr += 1
                button_dict[str(row[0])] = "acourses " + str(itr) + " Cursos"

        elif t_method == "teachers":
            for row in ws.values:
                itr += 1
                button_dict[str(row[1])] = "tcourses " + str(itr) +" Cursos"

        elif t_method == "acourses":
            for row in ws.values:
                if t_code == str(row[1]):
                    itr += 1
                    button_dict[str(row[2])] = "groups " + str(itr) + " Grupos"

        elif t_method == "tcourses":
            for row in ws.values:
                if t_code == str(row[0]):
                    itr += 1
                    button_dict[str(row[2])] = "groups " + str(itr) + " Grupos"

        elif t_method == "groups":
            for row in ws.values:
                if t_code == str(row[0]):
                    return

        return button_dict
