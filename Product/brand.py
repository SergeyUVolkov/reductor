# -*- coding: utf-8 -*-

from Database.database import DataBase


class Brand:

    def __init__(self):
        self.db = DataBase()

    def insert(self, brand_name: str):
        """
        Загрузка данных в таблицу брендов.
        :param brand_name: Название Бренда
        """
        brand_name = brand_name.lower().strip()
        if not self.select_id(brand_name=brand_name):
            sql = 'INSERT INTO brands (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;'
            param = (brand_name,)
            self.db.execute(sql=sql, parameters=param, commit=True)

    def select_id(self, brand_name: str):
        brand_name = brand_name.lower().strip()
        sql = 'SELECT id FROM brands WHERE name=%s;'
        param = (brand_name,)
        response = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return response

    def select_name(self, brand_id: int):
        sql = 'SELECT name FROM brands WHERE id=%s;'
        param = (brand_id,)
        response = self.db.execute(sql=sql, parameters=param, fetchone=True)
        return response


if __name__ == '__main__':
    print('test')
