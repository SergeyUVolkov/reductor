# -*- coding: utf-8 -*-
from Group.group import Group
from Messages.msg_handler import MessageHandler
from Rules.rules import Rule
from Settings.default_setting import COMMAND_LIST, command_list
from Users.user import User

# виды callback-кнопок
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')



class EventController:
    """
    Распределитель входных сообщений
    """

    def __init__(self, event_incoming: {}):
        self.__event_inc = event_incoming
        self.__event_type = event_incoming['type']
        self.__event_body = event_incoming['object']
        self.user_id = 0
        # кто отправил сообщение
        if 'user_id' in self.__event_body:
            self.user_id = int(self.__event_body['user_id'])
        elif 'from_id' in self.__event_body:
            self.user_id = self.__event_body['from_id']
        self.user = User(user_id_vk=self.user_id)
        self.group = Group(user_id_vk=self.user_id)
        self.rule = Rule(user_id_vk=self.user_id)

    @staticmethod
    def valid_msg():
        """
        Проверка допустимости обработки события.
        :return: bool
        """
        return True

    def handler_msg_vk(self):
        """
        Получить ответ для отправки сообщения пользователю вк.
        :return: list('msg:', 'keyboard:')
        """
        answer = ''
        key_board = None

        # Прервать если сообщение пришло от группы
        if int(self.user_id) < 0:
            return answer, key_board

        # Прервать если у пользователя запрет на получение сообщений.
        if not self.group.msg_allow():
            return answer, key_board

        # Проверка прав на доступ к контенту
        rules_list = self.user.checking_access_rules()

        if 'message' in self.__event_type:
            # Обрабатываем сообщения от партнера
            if 'message_new' in self.__event_type:
                cleared_msg = self.correct_msg(msg_dirty=self.__event_body['text'])

                # Прерываем если сообщение не команда из списка
                if not (cleared_msg in command_list()):
                    answer = ''
                    return answer, key_board

                if not rules_list[0]:
                    msg_handler = MessageHandler()
                    answer, key_board = msg_handler.hello()
                    answer = 'Ваш запрос на предоставление доступа обрабатывается.\n\n' \
                             'После предоставления доступа вам поступит сообщение с приглашение ' \
                             'к посещению нашего виртуального магазина.\nСпасибо за ожидание.'
                    return answer, key_board

                else:  # Проверяем на БАН
                    if 'ban' in self.rule.read_rules_name():
                        msg_handler = MessageHandler()
                        answer, key_board = msg_handler.goodbye()
                        answer = 'Для получения доступа, пожалуйста, позвоните в офис компании\n' \
                                 'по т.+7(3412)56-66-29'
                        return answer, key_board

                if self.group.member_group():
                    msg_handler = MessageHandler(msg_text=cleared_msg)
                    answer, key_board = msg_handler.handler()

                else:
                    # Необходимо вступить в группу
                    msg_handler = MessageHandler()
                    answer, key_board = msg_handler.no_membership()

            elif 'message_read' in self.__event_type:
                # answer = 'Сообщение прочтено'
                pass

            elif 'message_reply' in self.__event_type:
                # answer = 'Пришел ответ на сообщение группы'
                pass

            elif 'message_event' in self.__event_type:
                if self.__event_body['payload']['type'] in CALLBACK_TYPES:
                    # answer = 'Обработка CallBack кнопок'
                    pass

        elif 'group' in self.__event_type:
            # Обрабатываем события группы.
            if 'group_leave' in self.__event_type:
                msg_handler = MessageHandler()
                answer, key_board = msg_handler.goodbye()

            elif 'group_join' in self.__event_type:
                msg_handler = MessageHandler()
                answer, key_board = msg_handler.hello()

        print('handler_msg_vk answer= ', answer)

        return answer, key_board

    def param_for_msg(self, message, keyboard=[], attachment=[]):
        """
        Создаем словарь для отправки сообщения.
        :return: dict
        Словарь содержащий коллекцию
            'message': message,
            'keyboard': keyboard,
            'attachment': attachment,
            'users_id': ()
        """
        param_msg = {
            'message': message,
            'keyboard': keyboard,
            'attachment': attachment,
            'users_id': (self.user_id,)
        }

        return param_msg

    @staticmethod
    def correct_msg(msg_dirty: str):
        """
        Переводим сообщение в нижний регистр и удаляем пробелы в начале и в конце строки

        :param msg_dirty: Обрабатываемая строка
        :return: str
        """
        tmp_str = msg_dirty.lower().strip()
        while "  " in tmp_str:
            tmp_str = tmp_str.replace("  ", " ")
        return tmp_str


if __name__ == '__main__':
    ek = EventController({'group_id': 219183463, 'type': 'message_new',
                          'event_id': '46ab38fe4f4c648de53d6c7f69e5e7689e722eb5', 'v': '5.92',
                          'object': {'date': 1710555671, 'from_id': 1640521, 'id': 1529, 'out': 0,
                                     'version': 10005051, 'attachments': [], 'conversation_message_id': 1238,
                                     'fwd_messages': [], 'important': False, 'is_hidden': False,
                                     'peer_id': 1640521, 'random_id': 0, 'text': '/Партнеру'}})

    print(ek.handler_msg_vk())
