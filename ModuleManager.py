import json
import Module


class ModuleManager:
    def __init__(self):
        self.curr_module = None

    def create_module(self):
        # blah
        return True

    def save_curr_module(self):
        with open('Data/data.json', 'r') as f:
            loaded_data = json.load(f)

        loaded_data[self.curr_module.get_name()] = self.curr_module

        with open('Data/data.json', 'w') as f:
            json.dump(loaded_data, f)

    def select_module(self, t_name):
        with open('Data/data.json', 'r') as f:
            loaded_data = json.load(f)

        self.curr_module = loaded_data[t_name]

    def get_curr_module_area(self):
        if self.curr_module is not None:
            return self.curr_module.get_area()

    def get_curr_module_teacher(self):
        if self.curr_module is not None:
            return self.curr_module.get_teacher()

    def get_curr_module_courses(self):
        if self.curr_module is not None:
            return self.curr_module.get_courses()

    def get_curr_module_groups(self):
        if self.curr_module is not None:
            return self.curr_module.get_groups()
