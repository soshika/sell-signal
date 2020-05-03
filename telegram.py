# -*- coding: utf-8 -*-

from telethon import TelegramClient

api_id = ''
api_hash = ''

def send_message(to, message):
    with TelegramClient('signals', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(to, message))
