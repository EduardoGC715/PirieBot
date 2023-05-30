import json


class DataManager:
    def __init__(self):
        with open('../Database/Data/data.json', 'r') as data_file:
            self.data = json.load(data_file)

    def reload_data(self):
        with open('../Database/Data/data.json', 'r') as data_file:
            self.data = json.load(data_file)

    def get_areas(self):
        areas = self.data["areas"]
        result = []
        for area in areas:
            result.append(areas[area])
        return result

    def get_teacher(self, t_teacher):
        teachers = self.data["teachers"]
        return teachers[t_teacher]

    def get_teachers(self):
        teachers = self.data["teachers"]
        result = []
        for teacher in teachers:
            result.append(teachers[teacher])
        return result

    def get_course(self, t_course):
        courses = self.data["courses"]
        return courses[t_course]

    def get_courses_per_area(self, t_area):
        courses_list = self.data["areas"][t_area][1]
        courses = self.data["courses"]
        result = []
        for course in courses_list:
            result.append(courses[course])
        return result

    def get_courses_per_teachers(self, t_teacher):
        courses_list = self.data["teachers"][t_teacher][1]
        courses = self.data["courses"]
        result = []
        for course in courses_list:
            result.append(courses[course])
        return result

    def get_groups_per_course(self, t_course):
        groups = self.data["groups"][t_course]
        print(groups)
