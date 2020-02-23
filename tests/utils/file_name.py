# coding: utf-8

import os
import platform
from utils.global_holder import GlobalHolder


class FileName(object):
    """ ファイルパスの解決 """

    @staticmethod
    def input(path: str) -> str:
        """ 入力フォルダのパスを取得 """
        if 'windows' in platform.system():
            return os.path.join('.\\input', path.replace('/', '\\'))
        else:
            return os.path.join('./input', path.replace('\\', '/'))

    @staticmethod
    def output(path: str) -> str:
        """ 出力フォルダのパスを取得 """
        now = GlobalHolder.LunchTime
        if 'windows' in platform.system():
            return os.path.join(
                '.\\output\\captures\\{0}\\{1}'.format(
                    now.strftime('%Y%m%d'),
                    now.strftime('%Y%m%d_%H%M_%S')),
                path.replace('/', '\\'))
        else:
            return os.path.join(
                './output/captures/{0}/{1}'.format(
                    now.strftime('%Y%m%d'),
                    now.strftime('%Y%m%d_%H%M_%S')),
                path.replace('\\', '/'))
