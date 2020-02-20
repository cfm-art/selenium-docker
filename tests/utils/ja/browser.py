# coding :utf-8

from utils.browser import Browser
from utils.ja.element import ElementJa


class BrowserJa(object):
    __browser: Browser

    def __init__(self):
        self.__browser = Browser()

    def document(self) -> ElementJa:
        return ElementJa.document()

    def スクリーンショット(self, filename: str):
        self.__browser.screen_shot(filename)

    def 一時停止(self, seconds: float):
        self.__browser.wait(seconds)

    def ページ移動(self, path: str):
        self.__browser.navigate_to(path)

    def url取得(self) -> str:
        return self.__browser.url()
