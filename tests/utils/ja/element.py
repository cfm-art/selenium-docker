# coding: utf-8
from typing import Callable
from typing import Iterator
from typing import Union
from utils.element import Element
from selenium.webdriver.remote.webelement import WebElement


class 要素(object):

    __element: Element

    def __init__(self, element: Union[Element, WebElement]):
        if isinstance(element, Element):
            self.__element = element
        elif isinstance(element, 要素):
            self.__element = element.__element
        else:
            self.__element = Element(element)

    @staticmethod
    def document() -> '要素':
        return 要素(Element.document())

    # -- 日本語 --
    def クリック(self):
        self.__element.click()

    # -- value --
    def 値設定(self, 値: str):
        self.__element.set_value(値)

    def ファイル設定(self, ファイルパス: str):
        self.__element.set_file(ファイルパス)

    def 値取得(self) -> str:
        return self.__element.get_value()

    def 値クリア(self):
        self.__element.delete_value()

    # -- inner content --
    def テキスト取得(self) -> str:
        return self.__element.get_text()

    def テキスト一括取得(self) -> str:
        return self.__element.get_texts()

    def テキスト設定(self, 値: str):
        self.__element.set_text(値)

    def html取得(self) -> str:
        return self.__element.get_html()

    def html一括取得(self) -> [str]:
        return self.__element.get_htmls()

    def html設定(self, html: str):
        self.__element.set_html(html)

    def 属性値取得(self, 属性名: str) -> str:
        return self.__element.get_attribute(属性名)

    def 属性値一括取得(self, 属性名: str) -> [str]:
        return self.__element.get_attributes(属性名)

    # -- radio / checkbox --
    def チェックつける(self):
        self.__element.check()

    def チェック外す(self):
        self.__element.uncheck()

    def チェック済みか(self) -> bool:
        return self.__element.is_checked()

    # -- find --
    def idで検索(self, id名: str) -> '要素':
        return 要素(self.__element.find_by_id(id名))

    def タグで検索(self, タグ名: str) -> '要素':
        return 要素(self.__element.find_by_tag(タグ名))

    def クラスで検索(self, クラス名: str) -> '要素':
        return 要素(self.__element.find_by_class(クラス名))

    def nameで検索(self, 名前: str) -> '要素':
        return 要素(self.__element.find_by_name(名前))

    def セレクタで検索(self, セレクタクエリ: str) -> '要素':
        return 要素(self.__element.query_selector_all(セレクタクエリ))

    # -- tag --
    def タグ名取得(self) -> str:
        return self.__element.get_tag()

    def タグ名一括取得(self) -> [str]:
        return self.__element.get_tags()

    def 空か(self) -> bool:
        return self.__element.is_empty()

    def 最初(self) -> '要素':
        return 要素(self.__element.first())

    def 要素取得(self, index: int) -> '要素':
        return 要素(self.__element.at(index))

    def 一括処理(self, func: Callable[['要素'], None]):
        for e in self.__element.list():
            func(要素(e))

    def フィルタリング(self, フィルター: Callable[['要素'], bool]):
        elements = map(lambda x: 要素(x), self.__element.list())
        filtered = filter(フィルター, elements)
        return map(lambda x: x.first(), filtered)

    # -- list --
    def リスト(self) -> [WebElement]:
        """ 内部リストを取得 """
        return self.__element.list()

    def __len__(self) -> int:
        """ 要素数 """
        return len(self.__element.__elements)

    def __length_hint__(self) -> int:
        """ """
        return len(self.__element.__elements)

    def __contains__(self, value: '要素') -> bool:
        """ """
        return value.list()[0] in self.__element.__elements

    def __getitem__(self, index: Union[int, slice]) -> '要素':
        """ インデクサ """
        return 要素(self.__elements[index])

    def __iter__(self) -> Iterator['要素']:
        """ for-in用イテレータ """
        return iter(map(lambda x: 要素(x), self.__element.__elements))

    def __reversed__(self) -> Iterator['要素']:
        """ for-in用逆イテレータ """
        elements = self.__element.__elements
        return iter(map(lambda x: 要素(x), reversed(elements)))
