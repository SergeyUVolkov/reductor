# -*- coding: utf-8 -*-
from Database.database import DataBase


class Messenger:
    """
    Класс работы с месенджерами.
    """
    def __init__(self, name_messenger='vk'):
        self.db = DataBase()
        self.name = name_messenger

    def create(self):
        result = self.read()
        if not result:
            sql = 'INSERT INTO messengers (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;'
            param = ('vk',)
            self.db.execute(sql=sql, parameters=param, commit=True)
            result = self.read()
        return result

    def read(self, name=None):
        if not name:
            name = self.name
        sql = 'SELECT id FROM messengers WHERE name=%s;'
        param = (name,)
        result = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return result

    def update(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    msgr = Messenger()
    print(msgr.create())
