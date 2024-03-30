# -*- coding: utf-8 -*-


from Database.database import DataBase


class GroupType:
    """
    Класс типа оборудования
    """

    def __init__(self):
        self.db = DataBase()

    def insert(self, group_devices_type_name: str):
        """
        Загрузка данных в таблицу групповых типов.
        :param group_devices_type_name: Название типа группы оборудования
        """
        group_devices_type_name = group_devices_type_name.lower().strip()
        if not self.select_id(group_devices_type_name=group_devices_type_name):
            sql = 'INSERT INTO groups_devices_type (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;'
            param = (group_devices_type_name,)
            self.db.execute(sql=sql, parameters=param, commit=True)

    def select_id(self, group_devices_type_name: str):
        """
        Выборка ID типа группы оборудования
        :param group_devices_type_name: Название типа группы оборудования
        :return:
        """
        group_devices_type_name = group_devices_type_name.lower().strip()
        sql = 'SELECT id FROM groups_devices_type WHERE name=%s;'
        param = (group_devices_type_name,)
        response = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return response

    def select_name(self, group_devices_type_id: int):
        """
        Получение названия типа группы оборудования
        :param group_devices_type_id: ID типа группы оборудования
        :return:
        """
        sql = 'SELECT name FROM groups_type WHERE id=%s;'
        param = (group_devices_type_id,)
        response = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return response


if __name__ == '__main__':
    print('test')
