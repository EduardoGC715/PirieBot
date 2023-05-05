import re
from Database.DataManager import DataManager


class MessageManager:
    def __init__(self):
        self.message = "gloriana quiros"
        self.reply = ""
        self.dm = DataManager()
        self.patterns = [
            # patterns for areas
            (r'\bArtes\sMusicales\b', "AMU"),
            (r'\bArtes\sManuales\b', "AMA"),
            (r'\bArtes\sVisuales\b', "AVI"),
            (r'\bArte\sy\sSalud\b', "ASA"),
            (r'\bCapacitaci[oó]n\b', "CAP"),
            (r'\bArtes\sEsc[eé]nicas\b', "AES"),
            # patterns for teachers
            (r'\bGloriana\sQuir[oó]s\b', "GQ"),
            (r'\bDavid\sRodr[ií]guez\b', "DR"),
            (r'\bAna\sGuill[eé]n\b', "AG"),
            (r'\bPamela\sAlvarado\b', "PA"),
            # patterns for courses
            (r"Quilting|Quilting\sPrincipiantes", "QP"),
            (r'Lesco\s[I1]', "LI"),
            (r'Lesco\s(?:II|2)', "LII"),
            (r'Lesco\s[V5]', "LV"),


        ]

    def regex_match(self):
        for pattern, action in self.patterns:
            matches = re.findall(pattern, self.message, re.IGNORECASE)
            if matches:
                print(action)

    def set_message(self, t_message):
        self.message = t_message

    def get_message(self):
        return self.message

    def set_reply(self, t_reply):
        self.reply = t_reply

    def get_reply(self):
        return self.reply


cm = MessageManager()
cm.regex_match()
