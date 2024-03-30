# -*- coding: utf-8 -*-

from Database.database import DataBase


class DeviceType:
    """
    Класс типа оборудования
    """

    def __init__(self):
        self.db = DataBase()

    def insert(self, device_type_name: str):
        """
        Загрузка данных в таблицу брендов.
        :param device_type_name: Название типа оборудования
        """
        device_type_name = device_type_name.lower().strip()
        if not self.select_id(device_type_name=device_type_name):
            sql = 'INSERT INTO devices_type (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;'
            param = (device_type_name,)
            self.db.execute(sql=sql, parameters=param, commit=True)

    def select_id(self, device_type_name: str):
        """
        Выборка ID типа оборудования
        :param device_type_name: Название типа оборудования
        :return:
        """
        device_type_name = device_type_name.lower().strip()
        sql = 'SELECT id FROM devices_type WHERE name=%s;'
        param = (device_type_name,)
        response = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return response

    def select_name(self, device_type_id: int):
        """
        Получение названия типа оборудования
        :param device_type_id: ID типа оборудования
        :return:
        """
        sql = 'SELECT name FROM devices_type WHERE id=%s;'
        param = (device_type_id,)
        response = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return response


if __name__ == '__main__':
    print('test')
