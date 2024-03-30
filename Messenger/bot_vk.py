# -*- coding: utf-8 -*-
import time
import logging
import traceback
import vk_api.vk_api
import requests

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType  # VkBotLongPoll работа от имени группы

from Settings.setting_loader import set_token
from Events.event_controller import EventController
from vk_api.utils import get_random_id


class MyLongPoll(VkBotLongPoll):
    """
    Переопределяем метод Listen родителя
    """
    def listen(self):
        """
        Устраняем не отрабатываемое разрывание соединения сервером
        """
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                # print(e)
                # Перехват ошибки сервера, без остановки бота
                continue


class VkBot:
    """
    Класс бота.
    """
    def __init__(self):
        # подключаемся к VK API
        self.vk = vk_api.VkApi(token=set_token['token'])
        # подключение к long_poll
        __group_id = set_token['group_id']
        self.long_poll = MyLongPoll(self.vk, __group_id)
        self.event_type = VkBotEventType

        # для использования методов VK
        self.vk_api = self.vk.get_api()

        self.from_id = 0

    def send_msg(self, parameters={}):
        """
        Отправка сообщения пользователю

        :param parameters: Словарь содержащий коллекцию
                        'message': message,
                        'keyboard': keyboard,
                        'attachment': attachment,
                        'user_id': 11111
        """
        parameters.update({'random_id': get_random_id()})  # Идентификатор отправляемого сообщения. можно=0
        print('parameters= ', parameters)
        self.vk.method('messages.send', parameters)
        logging.info(f'Отправлено сообщение пользователю {self.from_id}')

    def start(self):
        """
        Основной метод бота
        """
        logging.info('Запущен основной цикл бота группы')

        try:
            for event in self.long_poll.listen():
                print('входное сообщение: raw ', event.raw)

                event_control = EventController(event_incoming=event.raw)

                if event_control.valid_msg():
                    msg, keyboard = event_control.handler_msg_vk()
                    param_msg = event_control.param_for_msg(message=msg, keyboard=keyboard)
                    tmp_param_msg = param_msg.copy()
                    # Отправка сообщения списку получателей или одному
                    for user_id in param_msg['users_id']:
                        tmp_param_msg.pop('users_id')
                        tmp_param_msg.update({'user_id': user_id})
                        if tmp_param_msg['message'] != '':
                            self.send_msg(parameters=tmp_param_msg)

        except requests.exceptions.ReadTimeout:
            error_msg = traceback.format_exc()
            logging.error(f'ошибка подключения: {error_msg}')
            time.sleep(10)

        except Exception:
            error_msg = traceback.format_exc()
            # print(f'Произошла ошибка в файле бота:\n    {error_msg}\nПерезапуск...')
            logging.info(f'источник краша...')
            logging.error(f'Произошла ошибка в файле бота:{error_msg}')
            logging.info('Перезапуск...')
            time.sleep(5)


if __name__ == '__main__':
    print('test')
