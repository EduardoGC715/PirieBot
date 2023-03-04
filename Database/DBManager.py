import pyodbc


class DBManager:
    def __init__(self):
        self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\Database\Data\CC_data_finished.accdb;')
        self.cursor = self.conn.cursor()

    def select_area(self, area):
        self.cursor.execute('select course_name from courses where area_id='+str(area))
        for row in self.cursor.fetchall():
            print(row)
