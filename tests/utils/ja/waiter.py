# coding: utf-8

from typing import Callable
from utils.waiter import Waiter


class 待機処理(object):

    def __init__(self, exec: Callable):
        self.__exec = exec

    def 待つ(self):
        self.__exec()


class 待機(object):
    """ 一時停止系 """

    _waiter = Waiter()

    def 指定秒(self, seconds: float):
        """　指定秒停止 """
        def proc():
            self._waiter.wait_seconds(seconds)
        return 待機処理(proc)

    def ページ遷移(
            self,
            パス: str,
            待機秒: float = 1.0,
            例外有無: bool = True):
        """ ページ遷移待ち """
        def proc():
            self._waiter.wait_page(
                パス,
                待機秒,
                例外有無)
        return 待機処理(proc)

    def 要素表示状態(
            self,
            CSSセレクタ: str,
            表示有無: bool = True,
            待機秒: float = 1.0,
            例外有無: bool = True):
        """ 要素待ち """
        def proc():
            self._waiter.wait_element(
                CSSセレクタ,
                表示有無,
                待機秒,
                例外有無)
        return 待機処理(proc)

    def 要素クリック可否(
            self,
            CSSセレクタ: str,
            クリック可否: bool = True,
            待機秒: float = 1.0,
            例外有無: bool = True):
        """ クリック可否状態待ち """
        def proc():
            self._waiter.wait_element_clickable(
                CSSセレクタ,
                クリック可否,
                待機秒,
                例外有無)
        return 待機処理(proc)

    def タイトル含む(
            self,
            タイトル: str,
            待機秒: float = 1.0,
            例外有無: bool = True):
        """ タイトル待ち """
        def proc():
            self._waiter.wait_title_contains(
                タイトル,
                待機秒,
                例外有無)
        return 待機処理(proc)

    def 読み込み(
            self,
            待機秒: float = 1.0,
            例外有無: bool = True):
        def proc():
            self._waiter.wait_loaded(
                待機秒,
                例外有無)
        return 待機処理(proc)
