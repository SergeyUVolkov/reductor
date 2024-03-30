# -*- coding: utf-8 -*-
# _*_ coding: utf-8 _*_

import time
import schedule
import logging
import traceback
import threading  # библиотека управления потоками

# подключаем конфигурацию
from datetime import datetime
from Settings.setting_loader import set_data
from Messenger.bot_vk import VkBot


# настройка логирования
path_log = set_data['path_log']
logging.basicConfig(handlers=[logging.FileHandler(filename=path_log, encoding='utf-8', mode='a+')],
                    format="%(asctime)s - %(threadName)s - %(levelname)s - %(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)
logging.info('Запуск бота....')

# блокировщик потоков
locker = threading.Lock()


def msg_new_timetable():
    """
    Проверка и рассылка уведомлений об изменениях в расписании.
    """
    print('Запуск schedule для отправка новостей')
    logging.info('Запуск проверки изменений в расписании.')
    pass


def control_schedule_new_timetable():
    """
    Шедулер для проверки изменений в расписании.
    """
    # schedule.every(5).seconds.do(job)
    # schedule.every(3).minutes.do(job)
    # schedule.every().day.at("03:00").do(msg_new_timetable)  # Проверка изменений в расписании в заданное время.
    schedule.every(2).hours.at(":15").do(msg_new_timetable)  # Проверка изменений в расписании каждые 2 часа 15 минут после запуска.
    # schedule.every().day.at("00:30").do(update_chat_data)  # Обновление данных по чатам.
    # schedule.every(2).hours.do(update_chat_data)  # Обновление данных по чатам ч/з каждые 2 часа после запуска.
    # schedule.every(3).days.do(job)
    # schedule.every(3).weeks.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


# thr1 = threading.Thread(target=update_chat_data, name='thr-chatBot', daemon=True)  # формируем поток
# thr1.start()   # запускаем поток чат-бота

# thr2 = threading.Thread(target=control_schedule_new_timetable, name='thr-Schedule', daemon=True)  # формируем поток
# thr2.start()   # запускаем поток scheduler для проверки изменений в расписании


while True:
    try:
        locker.acquire()  # блокировка потока

        print('Запуск бота группы ' + str(datetime.now()))
        logging.info('Запуск бота группы.')
        # создаем экземпляр класса бота группы
        bot = VkBot()

        locker.release()  # снятие блокировки потока
        # запуск бота группы
        bot.start()

    except Exception:
        error_msg = traceback.format_exc()
        # print(f'Произошла ошибка в главном файле:\n    {error_msg}\nПерезапуск...')
        logging.error(f'Произошла ошибка в боте группы:{error_msg}')
        logging.info('Перезапуск бота группы...')
        time.sleep(10)

