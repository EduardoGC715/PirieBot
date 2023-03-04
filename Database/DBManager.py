import pyodbc


class DBManager:
    def __init__(self):
        self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\Data\CC_data_finished.accdb;')
        self.cursor = self.conn.cursor()

    '''
    Access du dreckiges Stück scheiße 
    '''

    def select(self):
        self.cursor.execute('select * from courses where course_id=(select course_id from groups where course_id=5)')
        for row in self.cursor.fetchall():
            print(row)

dbmanager = DBManager()
dbmanager.select()
