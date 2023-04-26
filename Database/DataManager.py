import json


class DataManager:
    def __init__(self):
        with open('Data/data.json', 'r') as data_file:
            # Load the JSON data
            self.data = json.load(data_file)

    def refresh_data(self):
        with open('Data/data.json', 'r') as data_file:
            # Load the JSON data
            self.data = json.load(data_file)

    def get_areas(self):
        areas = self.data["areas"]
        for area in areas:
            print([area, areas[area]])

    def get_teachers(self):
        teachers = self.data["teachers"]
        for teacher in teachers:
            print([teacher, teachers[teacher]])

    def get_teachers_per_area(self, t_area):
        teachers_list = self.data["areas"][t_area][1]
        teachers = self.data["teachers"]
        for teacher in teachers_list:
                print([teacher, teachers[teacher]])


dm = DataManager()
dm.get_areas()
print("")
dm.get_teachers()
print("")
dm.get_teachers_per_area("AMU")
print("")
