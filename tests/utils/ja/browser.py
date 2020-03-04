# coding :utf-8

from utils.browser import Browser
from utils.ja.element import 要素


class ブラウザ(object):
    __browser: Browser

    def __init__(self):
        self.__browser = Browser()

    def document(self) -> 要素:
        return 要素.document()

    def スクリーンショット(self, filename: str):
        self.__browser.screen_shot(filename)

    def ページ移動(self, path: str):
        self.__browser.navigate_to(path)

    def url取得(self) -> str:
        return self.__browser.url()

    def ベースURL設定(self, url: str):
        self.__browser.set_baseurl(url)
