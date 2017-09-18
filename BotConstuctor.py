#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import telepot, time
from config import *

debug = 'debug console:'
TOKEN = telegram_token
TelegramBot = telepot.Bot(TOKEN)


def handle(obj):

    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    command = msg['text'].strip().lower()
    TelegramBot.sendMessage(chat_id, 'Hello')

    if command == '/help':
        TelegramBot.sendMessage(chat_id, 'msg')


print(debug + 'Listening..')
TelegramBot.message_loop(handle)


while True:
    time.sleep(30)