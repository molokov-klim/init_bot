"""
Базовый модуль бота
"""
import inspect
# pylint: disable=import-error
import logging
import os
import threading
from telebot.types import Message

import telebot


class BotManager:
    """
    Базовый класс бота
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.getenv("BOT_TOKEN"), parse_mode="MARKDOWN")
        self.bot_thread = threading.Thread(target=self.bot.infinity_polling)
        self.setup_handlers()

    def setup_handlers(self):
        """
        Инициализация хэндлеров
        """
        @self.bot.message_handler(commands=['hello'])
        def hello(message: Message):
            """
            Ответ на команду hello
            """
            logging.debug("%s", inspect.currentframe().f_code.co_name)
            self.bot.send_message(chat_id=message.chat.id,
                                  text='Hello',
                                  reply_to_message_id=message.reply_to_message.message_id if
                                  message.reply_to_message else None)

    def start(self):
        """
        Запуск бота
        """
        logging.debug("%s", inspect.currentframe().f_code.co_name)
        if not self.bot_thread.is_alive():
            self.bot_thread = threading.Thread(target=self.bot.infinity_polling)
            self.bot_thread.start()
        else:
            logging.warning("Bot is already running.")

    def stop(self):
        """
        Остановка бота
        """
        logging.debug("%s", inspect.currentframe().f_code.co_name)
        self.bot.stop_polling()
        if self.bot_thread.is_alive():
            self.bot_thread.join()
