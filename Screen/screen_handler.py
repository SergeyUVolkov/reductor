# -*- coding: utf-8 -*-

from Database.database import DataBase


class ScreenHandler:
    """
    Класс по работе с состояниями экранов пользователя
    """

    def __init__(self, user_id_vk):
        self.db = DataBase()
        self.user_id_vk = user_id_vk

    def read(self):
        # {{9И,177},{9Б,177}}
        sql = 'SELECT step_screen FROM users WHERE user_id_messenger=%s;'
        param = (self.user_id_vk,)
        result = self.db.execute(sql=sql, parameters=param, fetchone=True)
        screen_list = ()
        print('screen_list= ', len(result[0]))
        if result:
            if result[0] is not None:
                for item in result[0]:
                    print('result[0]= ', item)
                    # screen_list += item
        return screen_list

    def update(self, screen_name):
        sql = 'UPDATE '


if __name__ == '__main__':
    scr_hdr = ScreenHandler(user_id_vk=12563)

    print(scr_hdr.read())
