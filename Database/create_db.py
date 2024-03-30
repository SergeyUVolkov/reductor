# -*- coding: utf-8 -*-

import sys
from Database.database import DataBase

db = DataBase()


def create_table():
    """
    Создание таблиц БД
    :return:
    """

    # Создаем таблицу брендов
    sql = "CREATE TABLE IF NOT EXISTS brands(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL UNIQUE);"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу моделей
    sql = "CREATE TABLE IF NOT EXISTS models" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL, " \
          "brand_id int NOT NULL,"\
          "FOREIGN KEY (brand_id) REFERENCES brands (id) ON DELETE CASCADE"\
          ");"
    db.execute(sql=sql, commit=True)
    sql = 'CREATE UNIQUE INDEX IF NOT EXISTS brand_model ON models (name, brand_id);'
    db.execute(sql=sql, commit=True)

    # Создаем таблицу типов оборудования
    sql = "CREATE TABLE IF NOT EXISTS devices_type" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL UNIQUE "\
          ");"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу типов групп оборудования
    sql = "CREATE TABLE IF NOT EXISTS groups_devices_type" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL UNIQUE "\
          ");"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу хранения ссылок на отправляемые документы
    sql = "CREATE TABLE IF NOT EXISTS repo_file" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name_object text NOT NULL UNIQUE, "\
          "url_object text"\
          ");"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу продукции
    sql = "CREATE TABLE IF NOT EXISTS products" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL, " \
          "full_name text, " \
          "brand_id int NOT NULL, " \
          "model_id int NOT NULL, " \
          "device_type_id int NOT NULL, " \
          "group_devices_type_id int NOT NULL, " \
          "stock int DEFAULT 0," \
          "price money DEFAULT 0, " \
          "date_update timestamp DEFAULT CURRENT_TIMESTAMP," \
          "FOREIGN KEY (brand_id) REFERENCES brands (id) ON DELETE CASCADE, " \
          "FOREIGN KEY (model_id) REFERENCES models (id) ON DELETE CASCADE, " \
          "FOREIGN KEY (device_type_id) REFERENCES devices_type (id) ON DELETE CASCADE, " \
          "FOREIGN KEY (group_devices_type_id) REFERENCES groups_devices_type (id) ON DELETE CASCADE" \
          ");"
    db.execute(sql=sql, commit=True)
    sql = 'CREATE UNIQUE INDEX IF NOT EXISTS product_unic ' \
          'ON products (name, brand_id, model_id, device_type_id, group_devices_type_id);'
    db.execute(sql=sql, commit=True)

    # Создаем таблицу мессенджеров
    sql = "CREATE TABLE IF NOT EXISTS messengers" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL UNIQUE, " \
          "main_chanel boolean NOT NULL DEFAULT FALSE" \
          ");"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу разрешений для пользователя.
    sql = "CREATE TABLE IF NOT EXISTS rules_user" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "name text NOT NULL UNIQUE" \
          ");"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу юзеров
    sql = "CREATE TABLE IF NOT EXISTS users" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "user_id_messenger int NOT NULL, " \
          "name text, " \
          "phone text, " \
          "messenger_id int NOT NULL, " \
          "step_screen text [][], " \
          "rules_list_id int [][], " \
          "FOREIGN KEY (messenger_id) REFERENCES messengers (id) ON DELETE CASCADE" \
          ");"
    db.execute(sql=sql, commit=True)
    sql = 'CREATE UNIQUE INDEX IF NOT EXISTS user_unic ON users (user_id_messenger, messenger_id);'
    db.execute(sql=sql, commit=True)

    # Создаем таблицу менеджеров
    sql = "CREATE TABLE IF NOT EXISTS managers" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "user_id int NOT NULL UNIQUE, " \
          "slave_partner_list_id int [][], " \
          "FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE" \
          ");"
    db.execute(sql=sql, commit=True)

    # Создаем таблицу подбора товара
    sql = "CREATE TABLE IF NOT EXISTS carts" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "user_id int NOT NULL, " \
          "product_id int NOT NULL, " \
          "price money DEFAULT 0, " \
          "date timestamp DEFAULT CURRENT_TIMESTAMP," \
          "FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE, " \
          "FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE" \
          ");"
    db.execute(sql=sql, commit=True)
    sql = 'CREATE UNIQUE INDEX IF NOT EXISTS carts_unic ON carts (user_id, product_id);'
    db.execute(sql=sql, commit=True)

    # Создаем таблицу заказов
    sql = "CREATE TABLE IF NOT EXISTS orders" \
          "(" \
          "id bigserial NOT NULL PRIMARY KEY, " \
          "number text NOT NULL, " \
          "year_order text DEFAULT EXTRACT(YEAR FROM CURRENT_DATE), " \
          "user_id int NOT NULL, " \
          "product_id int NOT NULL, " \
          "price money DEFAULT 0, " \
          "timestamp_order timestamp DEFAULT CURRENT_TIMESTAMP, " \
          "manager_id int, " \
          "closing_date timestamp," \
          "FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE, " \
          "FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE, " \
          "FOREIGN KEY (manager_id) REFERENCES managers (id) ON DELETE CASCADE" \
          ");"
    db.execute(sql=sql, commit=True)
    sql = 'CREATE UNIQUE INDEX IF NOT EXISTS orders_number_unic ON orders (number, year_order);'
    db.execute(sql=sql, commit=True)
    sql = 'CREATE UNIQUE INDEX IF NOT EXISTS orders_unic ON orders (number, year_order, user_id, product_id);'
    db.execute(sql=sql, commit=True)


def delete_db(table_list: str):
    """
    Удаление заданных таблиц.
    :param table_list: строка перечисления таблиц для удаления
    """

    sql = f'DROP TABLE IF EXISTS {table_list};'

    db.execute(sql=sql, commit=True)


def load_default_data_table():
    """
    Загрузка данных по умолчанию для таблиц.
    """
    # Список прав пользователей
    rule_list = ('admin', 'partner', 'editor', 'ban')
    for item in rule_list:
        param = (item,)
        sql = 'SELECT id FROM rules_user WHERE name=%s;'
        result = db.execute(sql=sql, parameters=param, fetchone=True)
        if not result:
            sql = 'INSERT INTO rules_user(name) VALUES (%s) ON CONFLICT (name) DO NOTHING;'
            db.execute(sql=sql, parameters=param, commit=True)

    # Список messenger
    rule_list = ('vk', 'viber', 'telegram')
    for item in rule_list:
        param = (item,)
        sql = 'SELECT id FROM messengers WHERE name=%s;'
        result = db.execute(sql=sql, parameters=param, fetchone=True)
        if not result:
            sql = 'INSERT INTO messengers(name) VALUES (%s) ON CONFLICT (name) DO NOTHING;'
            db.execute(sql=sql, parameters=param, commit=True)


if __name__ == '__main__':
    # Для удаления таблицы вышестоящие должны тоже удалятся.
    # delete_db(table_list='repo_file')
    # delete_db(table_list='carts')
    # delete_db(table_list='orders')
    # delete_db(table_list='managers')
    # delete_db(table_list='users')
    # delete_db(table_list='rules_user')
    # delete_db(table_list='messengers')
    # delete_db(table_list='products')
    #
    # delete_db(table_list='groups_devices_type')
    # delete_db(table_list='devices_type')
    #
    # delete_db(table_list='models')
    # delete_db(table_list='brands')
    # print('Выбранные таблицы удалены')
    #
    create_table()
    print('Таблицы созданы')

    load_default_data_table()
    print('Данные загружены')
