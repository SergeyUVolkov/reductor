# -*- coding: utf-8 -*-
import unittest
from Messenger.bot_vk import VkBot
from Keyboards.keyboard import KeyboardTemplates


class TestEventBotVk(unittest.TestCase):

    def setUp(self) -> None:
        self.user_id = 1640521
        self.msg = 'Вы добавили в корзину\n' \
                   'Сплит-система Newtek NT-65M07 Black Glass\n' \
                   '___2 шт__\n' \
                   'Сплит-система Newtek NT-65M09 Black Glass\n' \
                   '___2 шт__'
        self.kb = KeyboardTemplates()

    def test_bot(self):
        vk_bot = VkBot()
        param = {
            'message': self.msg,
            'keyboard': self.kb.generator(command_btn='screen5'),
            'attachment': [],
            'user_id': self.user_id
        }
        result = vk_bot.send_msg(parameters=param)
        print('result= ', result)


if __name__ == '__main__':
    unittest.main()
