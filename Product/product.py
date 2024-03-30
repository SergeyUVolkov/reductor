# -*- coding: utf-8 -*-

from Database.database import DataBase


class Product:

    def __init__(self):
        self.db = DataBase()

    def insert(self, product_name: str, full_name: str, brand_id: int, model_id: int,
               device_type_id: int, group_devices_type_id: int, stock: int = 0):
        """
        Загрузка данных в таблицу моделей.
        :param product_name: Название продукта
        :param full_name: Полное название продукта из файла источника данных
        :param brand_id: ID бренда из БД
        :param model_id: ID модели из БД
        :param device_type_id: ID типа оборудования из БД
        :param group_devices_type_id: ID типа группы оборудования из БД
        :param stock: Остаток товара на складе
        """
        product_name = product_name.lower().strip()
        sql = 'INSERT INTO products (name, full_name, brand_id, model_id, ' \
              'device_type_id, group_devices_type_id, stock) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s) ' \
              'ON CONFLICT (name, brand_id, model_id, device_type_id, group_devices_type_id) DO NOTHING RETURNING id;'
        param = (product_name, full_name, brand_id, model_id, device_type_id, group_devices_type_id, stock)
        response = self.db.execute(sql=sql, parameters=param, commit=True)
        return response

    def select_product(self, product_name: str = None, brand_id: int = None, model_id: int = None,
                       device_type_id: int = None, group_devices_type_id: int = None):
        sql = 'SELECT id, name, full_name, brand_id, model_id, ' \
              'device_type_id, group_devices_type_id, stock, price, date_update  FROM products'
        param = ()
        if product_name or brand_id or model_id or device_type_id or group_devices_type_id:
            sql += ' WHERE '

        row_query = {}
        if product_name:
            product_name = product_name.lower().strip()
            row_query['name'] = product_name
        if brand_id:
            row_query['brand_id'] = brand_id
        if model_id:
            row_query['model_id'] = model_id
        if device_type_id:
            row_query['device_type_id'] = device_type_id
        if group_devices_type_id:
            row_query['group_devices_type_id'] = group_devices_type_id

        step_param = 0
        tmp_param = ()
        for item in row_query:
            tmp_row = row_query[item]
            sql += item + '=%s'
            tmp_param += (tmp_row,)
            step_param += 1
            if len(row_query)-step_param > 0:
                sql += ' AND '

        param += tmp_param
        sql += ';'
        response = self.db.execute(sql=sql, parameters=param, fetchall=True)
        return response

    def update_stock(self, product_id: int, stock: int = 0, price=0.0):
        """
        Обновить остаток склада
        :param product_id:
        :param stock:
        :param price:
        :return:
        """
        sql = 'UPDATE products SET stock=%s, price=%s WHERE id=%s;'
        param = (stock, price, product_id)
        self.db.execute(sql=sql, parameters=param, commit=True)


if __name__ == '__main__':
    product = Product()
    # result = product.select_product(brand_id=3, model_id=1, device_type_id=3, group_devices_type_id=2)
    product.update_stock(product_id=1, stock=5, price=12.50)
    print('result')
