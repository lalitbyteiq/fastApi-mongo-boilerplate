# import os
#
#
# class Config:
#     MONGO_URI = "mongodb://mongo:27017/"
#     OPENAI_API_KEY = "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"
#


import os
from dotenv import load_dotenv
import logging

from errors import InternalError

load_dotenv()


class Config:
    version = "0.1.0"
    title = "releads"

    app_settings = {
        'db_name': os.getenv('MONGO_DB'),
        'mongodb_url': os.getenv('MONGO_URL'),
        'db_username': os.getenv('MONGO_USER'),
        'db_password': os.getenv('MONGO_PASSWORD'),
        'max_db_conn_count': os.getenv('MAX_CONNECTIONS_COUNT'),
        'min_db_conn_count': os.getenv('MIN_CONNECTIONS_COUNT'),
    }

    @classmethod
    def app_settings_validate(cls):
        for k, v in cls.app_settings.items():
            if None is v:
                logging.error(f'Config variable error. {k} cannot be None')
                raise InternalError([{"message": "Server configure error"}])
            else:
                logging.info(f'Config variable {k} is {v}')


