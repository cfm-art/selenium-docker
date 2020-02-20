# coding: utf-8
from typing import Callable
from typing import Iterator
from typing import Union
from utils.element import Element
from selenium.webdriver.remote.webelement import WebElement


class ElementJa(Element):

    __element: Element

    def __init__(self, element: Union[Element, WebElement]):
        if isinstance(element, Element):
            self.__element = element
        elif isinstance(element, ElementJa):
            self.__element = element.__element
        else:
            self.__element = Element(element)

    @staticmethod
    def document() -> 'ElementJa':
        return ElementJa(Element.document())

    # -- 日本語 --
    def クリック(self):
        self.__element.click()

    # -- value --
    def 値設定(self, value: str):
        self.__element.set_value(value)

    def ファイル設定(self, path: str):
        self.__element.set_file(path)

    def 値取得(self) -> str:
        return self.__element.get_value()

    def 値クリア(self):
        self.__element.delete_value()

    # -- inner content --
    def テキスト取得(self) -> str:
        return self.__element.get_text()

    def テキスト一括取得(self) -> str:
        return self.__element.get_texts()

    def テキスト設定(self, text: str):
        self.__element.set_text(text)

    def html取得(self) -> str:
        return self.__element.get_html()

    def html一括取得(self) -> [str]:
        return self.__element.get_htmls()

    def html設定(self, html: str):
        self.__element.set_html(html)

    def 属性値取得(self, name: str) -> str:
        return self.__element.get_attribute(name)

    def 属性値一括取得(self, name: str) -> [str]:
        return self.__element.get_attributes(name)

    # -- radio / checkbox --
    def チェックつける(self):
        self.__element.check()

    def チェック外す(self):
        self.__element.uncheck()

    def チェック済みか(self) -> bool:
        return self.__element.is_checked()

    # -- find --
    def idで検索(self, key: str) -> 'ElementJa':
        return ElementJa(self.__element.find_by_id(key))

    def タグで検索(self, key: str) -> 'ElementJa':
        return ElementJa(self.__element.find_by_tag(key))

    def クラスで検索(self, key: str) -> 'ElementJa':
        return ElementJa(self.__element.find_by_class(key))

    def nameで検索(self, key: str) -> 'ElementJa':
        return ElementJa(self.__element.find_by_name(key))

    # -- tag --
    def タグ名取得(self) -> str:
        return self.__element.get_tag()

    def タグ名一括取得(self) -> [str]:
        return self.__element.get_tags()

    def 空(self) -> bool:
        return self.__element.is_empty()

    def 最初(self) -> 'ElementJa':
        return ElementJa(self.__element.first())

    def 要素取得(self, index: int) -> 'ElementJa':
        return ElementJa(self.__element.at(index))

    def 一括処理(self, func: Callable[['ElementJa'], None]):
        for e in self.__element.list():
            func(ElementJa(e))

    def フィルタリング(self, func: Callable[['ElementJa'], bool]):
        elements = map(lambda x: ElementJa(x), self.__element.list())
        filtered = filter(func, elements)
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

    def __contains__(self, value: 'ElementJa') -> bool:
        """ """
        return value.list()[0] in self.__element.__elements

    def __getitem__(self, index: Union[int, slice]) -> 'ElementJa':
        """ インデクサ """
        return ElementJa(self.__elements[index])

    def __iter__(self) -> Iterator['ElementJa']:
        """ for-in用イテレータ """
        return iter(map(lambda x: ElementJa(x), self.__element.__elements))

    def __reversed__(self) -> Iterator['ElementJa']:
        """ for-in用逆イテレータ """
        elements = self.__element.__elements
        return iter(map(lambda x: ElementJa(x), reversed(elements)))
