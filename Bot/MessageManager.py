import re
from Database.DataManager import DataManager


class MessageManager:
    def __init__(self):
        self.message = "gloriana quiros"
        self.reply = ""
        self.dm = DataManager()
        self.patterns = [
            # patterns for areas
            (r'\bArtes\sMusicales\b', self.dm.get_courses_per_area("AMU")),
            (r'\bArtes\sManuales\b', self.dm.get_courses_per_area("AMA")),
            (r'\bArtes\sVisuales\b', self.dm.get_courses_per_area("AVI")),
            (r'\bArte\sy\sSalud\b', self.dm.get_courses_per_area("ASA")),
            (r'\bCapacitaci[oó]n\b', self.dm.get_courses_per_area("CAP")),
            (r'\bArtes\sEsc[eé]nicas\b', self.dm.get_courses_per_area("AES")),
            # patterns for teachers
            (r'\bGloriana\sQuir[oó]s\b', self.dm.get_teacher("GQ")),
            (r'\bDavid\sRodr[ií]guez\b', self.dm.get_teacher("DR")),
            (r'\bAna\sGuill[eé]n\b', self.dm.get_teacher("AG")),
            (r'\bPamela\sAlvarado\b', self.dm.get_teacher("PA")),
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
