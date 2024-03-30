# -*- coding: utf-8 -*-

import vk_api
from Settings.setting_loader import set_token


class Group:
    """
    Для работы с группой ВК
    """
    def __init__(self, user_id_vk=0):
        self.__token = set_token['token']
        self.vk = vk_api.VkApi(token=self.__token)
        self.vk_api = self.vk.get_api()
        self.user_id_vk = user_id_vk

    def member_group(self):
        """
        Проверка на участие в нашей группе
        :return: True / False
        """
        if set_token['group_id'] != self.user_id_vk and set_token['group_id'] != (-1 * self.user_id_vk):
            result = self.vk.method('groups.isMember', {'group_id': set_token['group_id'],
                                                        'user_id': self.user_id_vk})
        else:
            result = 1

        if result == 1:
            return True
        return False

    def msg_allow(self):
        """
        Проверка разрешения получения сообщения от группы.
        :return: bool
        """
        result = self.vk.method('messages.isMessagesFromGroupAllowed', {'group_id': set_token['group_id'],
                                                                        'user_id': self.user_id_vk})
        if result['is_allowed'] == 1:
            return True  # Получение сообщений разрешено пользователем.
        return False  # Получение сообщений Запрещено пользователем.

    def admins_group(self):
        """
        Достает список администраторов группы

        :return: list
        """
        result = self.vk.method("groups.getMembers", {'group_id': set_token['group_id'],
                                                      'filter': 'managers'})
        # достаем список администраторов группы
        return result['items']


if __name__ == '__main__':
    gr = Group(user_id_vk=676516212)

    print('Участник группы: ', gr.member_group())
    print('Разрешено получать сообщения: ', gr.msg_allow())
