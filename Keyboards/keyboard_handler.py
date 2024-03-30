# -*- coding: utf-8 -*-

from Database.database import DataBase


class KeyboardHeandler:

    def __init__(self, command_btn: str):
        self.db = DataBase()
        self.btn_text = command_btn


if __name__ == '__main__':
    print('test')
