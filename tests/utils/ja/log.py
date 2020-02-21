# coding: utf-8

from utils.log import Log

__unittest = True


class ログ(object):
    """ ログ出力 """

    LEVEL_トレース: int = 1
    LEVEL_情報: int = 2
    LEVEL_デバッグ: int = 3
    LEVEL_警告: int = 4
    LEVEL_エラー: int = 5
    LEVEL_致命的: int = 6

    @staticmethod
    def レベル設定(level: int):
        """ ログを残すレベル """
        Log.set_level(level)

    @staticmethod
    def 保存(レベル: int, タグ: str, 文言: str):
        Log.print(レベル, タグ, 文言)

    @staticmethod
    def トレース(文言: str):
        Log.trace(文言)

    @staticmethod
    def 情報(文言: str):
        Log.info(文言)

    @staticmethod
    def デバッグ(文言: str):
        Log.debug(文言)

    @staticmethod
    def 警告(文言: str):
        Log.warnng(文言)

    @staticmethod
    def エラー(文言: str):
        Log.error(文言)

    @staticmethod
    def 致命的(文言: str):
        Log.fatal(文言)
