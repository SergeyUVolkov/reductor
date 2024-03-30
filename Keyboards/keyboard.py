# -*- coding: utf-8 -*-

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from Settings.default_setting import COMMAND_LIST
from Database.database import DataBase


class KeyboardTemplates:

    def __init__(self):
        self.keyboard = VkKeyboard()  # inline=True
        self.color = VkKeyboardColor
        self.db = DataBase()

    def cart_key_board(self):
        """
        Клавиатура для работы в корзине.
        :return: VkKeyboard
        """
        self.keyboard.add_button('/редактировать')
        self.keyboard.add_button('/продолжить выбор')
        self.keyboard.add_line()
        self.keyboard.add_button('/Отправить заказ', color=self.color.POSITIVE)
        self.keyboard.add_line()
        self.keyboard.add_button('/очистить&#8505;&#65039;', color=self.color.NEGATIVE)
        self.keyboard.add_button('/сохранить', color=self.color.PRIMARY)
        result = self.keyboard.get_keyboard()
        return result

    def goodbye(self):
        """
        Скрываем клавиатуру у покидающего группу.
        """
        result = self.keyboard.get_empty_keyboard()
        return result

    def hello(self):
        """
        Начальная клавиатура.
        """
        self.keyboard.add_button('/Прайс', color=self.color.POSITIVE)
        self.keyboard.add_button('/Партнеру', color=self.color.PRIMARY)
        result = self.keyboard.get_keyboard()
        return result

    def generator(self, command_btn: str):
        """
        Формирует клавиатуру по номеру screen
        :return: Keyboard json
        """
        if command_btn == '/Начало':
            self.keyboard.add_button('/Прайс', color=self.color.POSITIVE)
            self.keyboard.add_button('/Партнеру', color=self.color.PRIMARY)
            return self.keyboard.get_keyboard()

        # self.keyboard.add_button('Корзина', color=self.color.POSITIVE)
        # self.keyboard.add_button('/Zanussi', color=self.color.PRIMARY)
        # self.keyboard.add_button('/AC Electric', color=self.color.PRIMARY)
        # self.keyboard.add_button('/Newtek', color=self.color.PRIMARY)
        # self.keyboard.add_line()
        # self.keyboard.add_button('/Кабинет')
        self.keyboard.add_button('/Сплит', color=self.color.PRIMARY)
        self.keyboard.add_button('/Мульти', color=self.color.PRIMARY)
        self.keyboard.add_button('/Пром', color=self.color.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('/Водогрей', color=self.color.POSITIVE)
        self.keyboard.add_button('/Конвекторы', color=self.color.POSITIVE)
        self.keyboard.add_button('/Завесы', color=self.color.POSITIVE)
        self.keyboard.add_line()
        self.keyboard.add_button('/Вентиляция')
        self.keyboard.add_button('/Увлажнители')
        self.keyboard.add_button('/Камины')
        # self.keyboard.add_button('/Магазин', color=self.color.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('/Назад', color=self.color.NEGATIVE)
        # self.keyboard.add_button('/Магазин', color=self.color.PRIMARY)

        result = self.keyboard.get_keyboard()


        #
        # if screen_name in COMMAND_LIST.keys():
        #     count_key = 0
        #     for caption_button in COMMAND_LIST[screen_name]:
        #         short_name_button = caption_button[1:]
        #
        #         if short_name_button == 'назад':
        #             color_button = self.color.NEGATIVE
        #             count_key += 4
        #
        #         elif short_name_button == 'прайс':
        #             color_button = self.color.POSITIVE
        #             count_key += 1
        #
        #         elif short_name_button == 'магазин':
        #             color_button = self.color.PRIMARY
        #             count_key += 1
        #
        #         elif short_name_button == 'inf':
        #             color_button = self.color.SECONDARY
        #             count_key += 1
        #
        #         else:
        #             color_button = self.color.PRIMARY
        #             count_key += 1
        #
        #         if count_key > 3:
        #             self.keyboard.add_line()
        #             count_key = 1
        #
        #         print('short_name_button= ', caption_button, ' счет кнопок', count_key)
        #
        #         self.keyboard.add_button(caption_button, color=color_button)
        #
        #
        #     if len(COMMAND_LIST[screen_name]) == 0:   # Если нет клавиш в запрошенном экране
        #         collection_of_button = self.keyboard.get_empty_keyboard()
        #     else:
        #         collection_of_button = self.keyboard.get_keyboard()
        # else:
        #     collection_of_button = self.keyboard.get_keyboard()

        return result



    def welcome_key_board(self):
        """
        Начальная клавиатура
        :return: VkKeyboard
        """
        self.keyboard.add_button('/Прайс', color=self.color.POSITIVE)
        # self.keyboard.add_button('/Партнеру', color=self.color.PRIMARY)
        self.keyboard.add_button('/Магазин', color=self.color.PRIMARY)
        result = self.keyboard.get_keyboard()
        return result

    def product_key_board(self):
        """
        Клавиатура для работы с товаром.
        :return: VkKeyboard
        """
        self.keyboard.add_button('/Сплит', color=self.color.PRIMARY)
        self.keyboard.add_button('/Мульти', color=self.color.PRIMARY)
        self.keyboard.add_button('/Пром', color=self.color.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('/Водогрей', color=self.color.POSITIVE)
        self.keyboard.add_button('/Конвекторы', color=self.color.POSITIVE)
        self.keyboard.add_button('/Завесы', color=self.color.POSITIVE)
        self.keyboard.add_line()
        self.keyboard.add_button('/Вентиляция')
        self.keyboard.add_button('/Увлажнители')
        self.keyboard.add_button('/Камины')
        self.keyboard.add_line()
        self.keyboard.add_button('/Назад', color=self.color.NEGATIVE)
        result = self.keyboard.get_keyboard()
        return result

    def product_split(self):
        """
        Клавиатура для сплит систем.
        :return: VkKeyboard
        """
        self.keyboard.add_button('/Модели on`off', color=self.color.PRIMARY)
        self.keyboard.add_button('/Инвертор', color=self.color.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('/Назад', color=self.color.NEGATIVE)
        result = self.keyboard.get_keyboard()
        return result

    def product_split_brand(self):
        """
        Клавиатура для сплит систем.
        :return: VkKeyboard
        """
        self.keyboard.add_button('/Newtek', color=self.color.PRIMARY)
        self.keyboard.add_button('/AC Electric', color=self.color.PRIMARY)
        self.keyboard.add_button('/Ballu', color=self.color.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('/Royal Clima', color=self.color.PRIMARY)
        self.keyboard.add_button('/Zanussi', color=self.color.PRIMARY)
        self.keyboard.add_button('/Electrolux', color=self.color.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('/Назад', color=self.color.NEGATIVE)
        self.keyboard.add_button('&#128722; (25)')
        result = self.keyboard.get_keyboard()
        return result


    def kb_test_inline(self):
        # Настройки для обоих клавиатур
        settings = dict(one_time=False, inline=True)
        APP_ID = 100
        OWNER_ID = 1457823

        # №1. Клавиатура с 3 кнопками: "показать всплывающее сообщение", "открыть URL" и изменить меню (свой собственный тип)
        keyboard_1 = VkKeyboard(**settings)
        # pop-up кнопка
        keyboard_1.add_callback_button(label='Покажи pop-up сообщение', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "show_snackbar", "text": "Это исчезающее сообщение"})
        keyboard_1.add_line()
        # кнопка с URL
        url_site = 'https://www.klimat18.ru/'
        keyboard_1.add_callback_button(label='конди Ballu BSUI-FM/in-07HN8/EU', color=VkKeyboardColor.POSITIVE,
                                       payload={"type": "open_link", "link": url_site})
        keyboard_1.add_line()
        keyboard_1.add_callback_button(label='+', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "open_link", "link": url_site})

        keyboard_1.add_callback_button(label='-', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "open_link", "link": url_site})

        keyboard_1.add_callback_button(label='&#128722; (25)', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "open_link", "link": url_site})
        keyboard_1.add_line()
        keyboard_1.add_callback_button(label='BA2OI-FM/out-18HN8/EU', color=VkKeyboardColor.POSITIVE,
                                       payload={"type": "open_link", "link": url_site})
        keyboard_1.add_line()
        keyboard_1.add_callback_button(label='+', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "open_link", "link": url_site})

        keyboard_1.add_callback_button(label='-', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "open_link", "link": url_site})

        keyboard_1.add_callback_button(label='&#128722; (5)', color=VkKeyboardColor.SECONDARY,
                                       payload={"type": "open_link", "link": url_site})
        # keyboard_1.add_line()
        # # кнопка по открытию ВК-приложения
        # keyboard_1.add_callback_button(label='Открыть приложение', color=VkKeyboardColor.NEGATIVE,
        #                                payload={"type": "open_app", "app_id": APP_ID, "owner_id": OWNER_ID,
        #                                         "hash": "anything_data_100500"})
        # keyboard_1.add_line()
        # # кнопка переключения на 2ое меню
        # keyboard_1.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY,
        #                                payload={"type": "my_own_100500_type_edit"})
        result = keyboard_1.get_keyboard()
        return result

    def kb2_test(self):
        # Настройки для обоих клавиатур
        settings = dict(one_time=False, inline=True)

        # №2. Клавиатура с одной красной callback-кнопкой. Нажатие изменяет меню на предыдущее.
        keyboard_2 = VkKeyboard(**settings)
        # кнопка переключения назад, на 1ое меню.
        keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE,
                                       payload={"type": "my_own_100500_type_edit"})
        result = self.keyboard.get_keyboard()
        return result


if __name__ == '__main__':
    kb = KeyboardTemplates()
    print(kb.goodbye())
