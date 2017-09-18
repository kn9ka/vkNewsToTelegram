#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk
import telepot
import time
from config import *


VK_TOKEN = vk_token
BOT_TOKEN = telegram_token
CHANNEL_NAME = '@Email_channel'
ID_LIST = []

session = vk.Session(access_token=VK_TOKEN)
api = vk.API(session)
tkBot = telepot.Bot(BOT_TOKEN)
response = api.wall.get(domain='borodachi.moscow')

while True:

    response = api.wall.get(domain='borodachi.moscow')
    response_text = response[1]['text'].replace('<br>', '\n')
    response_image = response[1]['attachment']['photo']['src_big']
    response_id = response[1]['id']

    if response_id not in ID_LIST:
        ID_LIST.append(response_id)
        print('Add new ID: %s' % response_id)
        tkBot.sendMessage(CHANNEL_NAME, response_text)
        tkBot.sendPhoto(CHANNEL_NAME, response_image)
    else:
        pass
    time.sleep(10)