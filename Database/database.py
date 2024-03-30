# -*- coding: utf-8 -*-

import psycopg2
from Settings.setting_loader import set_db


class DataBase:
    def __init__(self, profile_db: str = 'postgres'):
        """
        Инициализация подключения к БД
        :param profile_db: Строка 'school'  или 'donut'
        """
        if 'postgres' == profile_db:
            self.parm_db = set_db

    @staticmethod
    def equality_variables_values(sql, param):
        """
        Проверка равенства запрашиваемых переменных и переданных параметров в запрос.
        :param sql- строка запроса
        :param param- кортеж параметров.
        :return: bool
        """
        count = sql.count('%s')
        if param:
            count_param = len(param)
            if count == count_param:
                return True
            return False
        return True

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        """
        Метод выполнения запроса к БД
        :param sql: Строка запроса
        :param parameters: Параметр запроса кортеж
        :param fetchone: Получение одной строки в ответе
        :param fetchall: Получение много строк в ответе
        :param commit: Выполнение commit БД
        :return: Ответ от выполнения выбранного запроса
        """

        connect = psycopg2.connect(
            database=self.parm_db['name'],
            user=self.parm_db['login'],
            password=self.parm_db['pass'],
            host=self.parm_db['host'],
            port=self.parm_db['port']
        )

        data = None
        # проверяем кол-во переданных параметров и переменных
        if not self.equality_variables_values(sql=sql, param=parameters):
            return data
        cursor = connect.cursor()
        cursor.execute(sql, parameters)
        if fetchone and commit:  # Когда необходимо от результата commit получить ответ. Например: ID при Insert.
            data = cursor.fetchone()
            connect.commit()
        else:
            if commit:
                connect.commit()
                data = cursor.rowcount
            if fetchone:
                data = cursor.fetchone()
            elif fetchall:
                data = cursor.fetchall()
        cursor.close()

        connect.close()

        return data


if __name__ == '__main__':
    print('test')
