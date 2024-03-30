# -*- coding: utf-8 -*-
from Database.database import DataBase
from Messenger.messenger import Messenger


class User:
    """
    Обработка событий связанных с пользователем.
    """
    def __init__(self, user_id_vk):
        self.user_id_vk = user_id_vk
        self.db = DataBase()
        self.messenger = Messenger()

    def create(self):
        if not self.select_id():
            sql = 'INSERT INTO users (user_id_messenger, messenger_id) VALUES (%s, %s) ' \
                  'ON CONFLICT (user_id_messenger, messenger_id) DO NOTHING;'
            param = (self.user_id_vk, self.messenger.read())
            self.db.execute(sql=sql, parameters=param, commit=True)

    def select_id(self):
        """
        Получение ID пользователя в БД
        :return: list
        """
        sql = 'SELECT id FROM users WHERE user_id_messenger=%s AND messenger_id=%s;'
        param = (self.user_id_vk, self.messenger.read())
        result = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return result

    def checking_access_rules(self):
        """
        Получение прав доступа юзера.
        :return: list rules
        """
        self.create()
        user_id = self.select_id()[0]
        sql = 'SELECT rules_list_id FROM users WHERE id=%s;'
        param = (user_id,)
        result = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return result


if __name__ == '__main__':
    user = User(user_id_vk=12563)

    print(user.checking_access_rules())
