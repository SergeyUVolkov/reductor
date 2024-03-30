# -*- coding: utf-8 -*-

from Database.database import DataBase


class Model:

    def __init__(self):
        self.db = DataBase()

    def insert(self, model_name: str, brand_id: int):
        """
        Загрузка данных в таблицу моделей.
        :param model_name: Название модели
        :param brand_id: ID бренда из БД
        """
        model_name = model_name.lower().strip()
        if not self.select_id(model_name=model_name, brand_id=brand_id):
            sql = 'INSERT INTO models (name, brand_id) VALUES (%s, %s) ON CONFLICT (name, brand_id) DO NOTHING;'
            param = (model_name, brand_id)
            self.db.execute(sql=sql, parameters=param, commit=True)

    def select_id(self, model_name: str, brand_id: int):
        model_name = model_name.lower().strip()
        sql = 'SELECT id FROM models WHERE name=%s and brand_id=%s;'
        param = (model_name, brand_id)
        response = self.db.execute(sql=sql, parameters=param, fetchall=True)
        return response

    def select_name(self, model_id: int, brand_id: int):
        sql = 'SELECT name FROM models WHERE id=%s and brand_id=%s;'
        param = (model_id, brand_id)
        response = self.db.execute(sql=sql, parameters=param, fetchall=True)
        return response

if __name__ == '__main__':
    print('test')
