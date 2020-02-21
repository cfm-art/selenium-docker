# coding: utf-8

import datetime

__unittest = True


class Log(object):
    """ ログ出力 """

    INFO: int = 1
    TRACE: int = 2
    DEBUG: int = 3
    WARNING: int = 4
    ERROR: int = 5
    FATAL: int = 6

    __LEVEL: int = 1

    @staticmethod
    def set_level(level: int):
        """ ログを残すレベル """
        Log.__LEVEL = level

    @staticmethod
    def __log(level: int, category: str, text: str):
        if level < Log.__LEVEL:
            return
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        import traceback
        file = ''
        for tb in traceback.extract_stack(None, None):
            if tb[2].startswith('test'):
                file = tb[2]

        if file == '':
            print('[{0}]({1}): {2}\n'.format(category, now, text))
        else:
            print('[{0}]({1}) - {3}: {2}\n'.format(category, now, text, file))

    @staticmethod
    def print(level: int, tag: str, text: str):
        Log.__log(level, tag, text)

    @staticmethod
    def trace(text: str):
        Log.__log(Log.TRACE, 'trace', text)

    @staticmethod
    def info(text: str):
        Log.__log(Log.INFO, 'info', text)

    @staticmethod
    def debug(text: str):
        Log.__log(Log.DEBUG, 'debug', text)

    @staticmethod
    def warning(text: str):
        Log.__log(Log.WARNING, 'warning', text)

    @staticmethod
    def error(text: str):
        Log.__log(Log.ERROR, 'error', text)

    @staticmethod
    def fatal(text: str):
        Log.__log(Log.FATAL, 'fatal', text)
