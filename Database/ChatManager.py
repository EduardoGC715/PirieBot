import re
from DataManager import DataManager


class ChatManager:
    def __init__(self):
        self.message = "David Rodriguez"
        self.reply = ""
        self.dm = DataManager()
        self.patterns = [
            (r'\bGloriana\sQuir[oó]s\b', self.dm.get_teacher("GQ")),
            (r'\bDavid\sRodr[ií]guez\b', self.dm.get_teacher("DR")),
            (r'\bAna\sGuill[eé]n\b', self.dm.get_teacher("AG")),
            (r'\bPamela\sAlvarado\b', self.dm.get_teacher("PA"))
        ]

    def regex_match(self):
        for pattern, action in self.patterns:
            matches = re.findall(pattern, self.message, re.IGNORECASE)
            if matches:
                print(action)


cm = ChatManager()
cm.regex_match()
