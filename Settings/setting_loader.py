# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # ищем файл настроек окружения .env

# Описание загружаемых ключей
info_key = os.getenv('CONFIG-DESC')
print('Загружен конфигурационный файл: ', info_key)


set_data = {
    'path_log': 'log.log'
}

set_db = {
    'host': os.getenv('DB-HOST'),
    'port': os.getenv('DB-PORT'),
    'name': os.getenv('DB-NAME'),
    'login': os.getenv('DB-LOGIN'),
    'pass': os.getenv('DB-PASS')
}

set_token = {
    'token': os.getenv('TOKEN-VK'),
    'admin_id': os.getenv('ADMIN-VK'),
    'group_id': os.getenv('GROUP-VK')
}

if __name__ == '__main__':
    print('set_db: ', set_db)
