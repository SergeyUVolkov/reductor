# -*- coding: utf-8 -*-
from Database.database import DataBase


class Rule:
    """
    Класс обработки правил пользователей
    """
    def __init__(self, user_id_vk):
        self.db = DataBase()
        self.user_id_vk = user_id_vk

    def read_rules_name(self):
        """
        Составление списка имен правил.
        :return:
        """
        sql = 'SELECT rules_list_id FROM users WHERE user_id_messenger=%s;'
        param = (self.user_id_vk,)
        result = self.db.execute(sql=sql, parameters=param, fetchone=True)
        rule_name_list = []
        if result:
            if result[0] is not None:
                for item in result[0]:
                    sql = 'SELECT name FROM rules_user WHERE id=%s;'
                    param = (item,)
                    result_name = self.db.execute(sql=sql, parameters=param, fetchone=True)
                    print('name', result_name)
                    if result_name is not None:
                        rule_name_list.append(result_name[0])
        return rule_name_list


if __name__ == '__main__':
    rule = Rule(user_id_vk=12563)
    print(rule.read_rules_name())
