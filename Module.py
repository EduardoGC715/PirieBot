class Module:

    def __init__(self):
        self.m_area = ""
        self.m_teacher = ""
        self.m_courses = []
        self.m_groups = {}

    def set_module(self, t_area, t_teacher, t_courses, t_groups):
        self.m_area = t_area
        self.m_teacher = t_teacher
        self.m_courses = t_courses
        self.m_groups = t_groups

    # gets

    def get_area(self):
        return self.m_area

    def get_teacher(self):
        return self.m_teacher

    def get_courses(self):
        return self.m_courses

    def get_groups(self):
        return self.m_groups

    # sets

    def set_area(self, t_area):
        self.m_area = t_area

    def set_name(self, t_teacher):
        self.m_teacher = t_teacher

    def set_courses(self, t_courses):
        self.m_courses = t_courses

    def set_groups(self, t_groups):
        self.m_groups = t_groups
