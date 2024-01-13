# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/m4mallu/inine-tube-mate
# Author   : Renjith Mangal [ https://t.me/space4renjith ]
# Credits  : https://github.com/SpEcHiDe/AnyDLBot


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5088657122:AAGByZ5PLpv205PaXhxDEZ_JixPIn1OaVnk")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "3335796"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "763990585").split())

    # Super users to broadcast messages & fetch subscribers count
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://abirhasan2005:abirhasan@cluster0.i6qzp.mongodb.net/cluster0?retryWrites=true&w=majority")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
