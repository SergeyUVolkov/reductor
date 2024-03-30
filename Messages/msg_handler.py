# -*- coding: utf-8 -*-


from Settings.default_setting import COMMAND_LIST, ANSWER_LIST
from Keyboards.keyboard import KeyboardTemplates
from Group.group import Group


class MessageHandler:

    def __init__(self, msg_text: str = ''):
        self.__msg_text = msg_text
        self.kb = KeyboardTemplates()

    def handler(self):
        """
        Обработчик текстовой команды.
        :return: string
        """
        print('str_command= ', self.__msg_text)
        if self.__msg_text == '/магазин':
            answer_msg = 'Выберите интересующий вас тип оборудования.'
            key_board_list = self.kb.generator(command_btn='/Партнеру')
            return answer_msg, key_board_list

        elif self.__msg_text == '/партнеру':
            answer_msg = 'Ваша заявка на открытие доступа отправлена.'
            key_board_list = self.kb.generator(command_btn='/Партнеру')
            return answer_msg, key_board_list

        elif self.__msg_text == '/прайс':
            answer_msg = 'Высылаем прайс.'
            key_board_list = self.kb.generator(command_btn='/Партнеру')
            return answer_msg, key_board_list
        else:
            answer_msg = 'Неизвестная команда'
            key_board_list = self.kb.generator(command_btn='/Начало')
            return answer_msg, key_board_list


    def goodbye(self):
        """
        Обработка выхода из группы.
        :return:
        """
        answer_msg = 'До свидания. Надеемся на ваше скорейшее возвращение.'
        key_board_list = self.kb.goodbye()
        return answer_msg, key_board_list

    def no_membership(self):
        """
        Сообщение не член группы.
        :return:
        """
        answer_msg = 'Пожалуйста вступите в нашу группу. \n' \
                     'Подписчики первыми получают информацию об акциях и новинках.'
        key_board_list = self.kb.goodbye()
        return answer_msg, key_board_list

    def hello(self):
        """
        Обработка присоединения к группе.
        :return:
        """
        answer_msg = 'Добро пожаловать в нашу группу.'
        key_board_list = self.kb.hello()
        return answer_msg, key_board_list


if __name__ == '__main__':
    msg_handler = MessageHandler(msg_text='/сплит')

    print(msg_handler.hello())
    print(msg_handler.goodbye())
