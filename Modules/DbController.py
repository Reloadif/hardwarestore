from mysql.connector import connect

from .TableContext import TableContext

# Класс владеющий подключением к БД

class DbController():
    def __init__(self, username, password):
        self.connection = connect(
            host="localhost",
            user=username,
            password=password,
            database="hardware_store",
        )

        self.cursor = self.connection.cursor()
        self.tableContext = TableContext()
        self.currentReply = None

    def select(self):
        self.cursor.execute(self.tableContext.requestSelect)
        self.currentReply = self.cursor.fetchall()

    def insert(self, parameters):
        self.cursor.execute(self.tableContext.requestInsert, parameters)
        self.connection.commit()

    def delete(self, parameter):
        self.cursor.execute(self.tableContext.requestDelete, (parameter,))
        self.connection.commit()
    
    def customSelectWithParameter(self, parameter):
        self.cursor.execute(self.tableContext.requestSelect, (parameter,))
        self.currentReply = self.cursor.fetchall()

    def close(self, commit = True):
        if commit: self.commit()
        self.connection.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

ControllerDataBase = None