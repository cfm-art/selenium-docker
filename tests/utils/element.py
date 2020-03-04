# coding: utf-8

from itertools import chain
from selenium.webdriver.remote.webelement import WebElement
from typing import Callable
from typing import Iterator
from typing import List
from typing import Union

from utils.element_accessor import ElementAccessor
from utils.global_holder import GlobalHolder


class Element(object):
    """ SeleniumのElementをラップ """

    __elements: List[WebElement]

    @staticmethod
    def document() -> 'Element':
        documents = GlobalHolder.Browser.find_elements_by_tag_name('html')
        return Element(documents)

    def __first(self) -> WebElement:
        """ リストの先頭要素 """
        element = self.__elements
        return element[0] if len(element) > 0 else None

    def __e(self, element: object) -> List[WebElement]:
        return element

    def __init__(self, element: Union[WebElement, List[WebElement]]):
        """ 要素を指定して初期化 """
        if isinstance(element, list):
            self.__elements = self.__e(element)
        elif isinstance(element, Element):
            self.__elements = self.__e(element.__elements)
        elif isinstance(element, WebElement):
            self.__elements = self.__e([element])
        else:
            self.__elements = self.__e(element.__element)

    def click(self):
        """ クリック """
        self.foreach(lambda x: x.__first().click())

    # -- value --
    def set_value(self, value: str):
        """ 値を設定 """
        self.foreach(lambda x: ElementAccessor.set(x.__first(), value))

    def set_file(self, path: str):
        """ ファイルを設定 """
        self.foreach(lambda x: ElementAccessor.set_file(x.__first(), path))

    def get_value(self) -> str:
        """ 値を取得 """
        return ElementAccessor.get(self.__first())

    def delete_value(self):
        self.set_value('')

    # -- inner content --
    def get_text(self) -> str:
        return ElementAccessor.inner_text(self.__first())

    def get_texts(self) -> str:
        return map(lambda x: ElementAccessor.inner_text(x), self.__elements)

    def set_text(self, text: str):
        setter = ElementAccessor.set_inner_text
        self.foreach(lambda x: setter(x.__first(), text))

    def get_html(self) -> str:
        return ElementAccessor.inner_html(self.__first())

    def get_htmls(self) -> [str]:
        return map(lambda x: ElementAccessor.inner_html(x), self.__elements)

    def set_html(self, html: str):
        setter = ElementAccessor.set_inner_html
        self.foreach(lambda x: setter(x.__first(), html))

    def get_attribute(self, name: str) -> str:
        """ タグの属性を取得 """
        return self.__first().get_attribute(name)

    def get_attributes(self, name: str) -> [str]:
        """ タグの属性を取得 """
        return map(lambda x: x.get_attribute(name), self.__element)

    # -- radio / checkbox --
    def check(self):
        """ チェックボックスやラジオのチェックをつける """
        self.foreach(lambda x: ElementAccessor.check(x.__first()))

    def uncheck(self):
        """ チェックボックスやラジオのチェックを外す """
        self.foreach(lambda x: ElementAccessor.uncheck(x.__first()))

    def is_checked(self) -> bool:
        """ チェックボックスやラジオがチェック中か判定 """
        return ElementAccessor.is_checked(self.__first())

    # -- find --
    def find_by_id(self, key: str) -> 'Element':
        """ idで検索 """
        return Element(list(chain.from_iterable(
            map(lambda x: x.find_elements_by_id(key), self.__elements))))

    def find_by_tag(self, key: str) -> 'Element':
        """ タグを指定して検索 """
        return Element(list(chain.from_iterable(
            map(lambda x: x.find_elements_by_tag(key), self.__elements))))

    def find_by_class(self, key: str) -> 'Element':
        """ classを指定して検索 """
        return Element(list(chain.from_iterable(
            map(lambda x: x.find_elements_by_class(key), self.__elements))))

    def find_by_name(self, key: str) -> 'Element':
        """ nameを指定して検索 """
        return Element(list(chain.from_iterable(
            map(lambda x: x.find_elements_by_name(key), self.__elements))))

    def query_selector_all(self, query: str) -> 'Element':
        """ querySelectorAll """
        e = self.__elements
        return Element(list(chain.from_iterable(
            map(lambda x: x.find_elements_by_css_selector(query), e))))
        # browser = GlobalHolder.Browser
        # js = 'return arguments[0].querySelectorAll(arguments[1])'

        # def exec(x):
        #     return browser.execute_script(js, x, query)
        # return Element(list(chain.from_iterable(
        #     map(exec, self.__elements))))

    # -- tag --
    def get_tag(self) -> str:
        """　タグ名 """
        return self.__first().tag_name

    def get_tags(self) -> [str]:
        return map(lambda x: x.tag_name, self.__elements)

    # -- list --
    def list(self) -> List[WebElement]:
        """ 内部リストを取得 """
        return self.__elements

    def is_empty(self) -> bool:
        """ 要素があるかどうか """
        return len(self.__elements) == 0

    def first(self) -> 'Element':
        """ 1番目の要素 """
        return Element(self.__first())

    def at(self, index: int) -> 'Element':
        """ 指定番目の要素を取得 """
        if len(self.__elements) <= index:
            return Element([])
        return Element(self.__elements[index])

    def foreach(self, func: Callable[['Element'], None]):
        """ 一括処理 """
        for e in self.__elements:
            func(Element(e))

    def filter(self, func: Callable[['Element'], bool]) -> [WebElement]:
        """ フィルター """
        filtered = filter(func, map(lambda x: Element(x), self.__elements))
        return map(lambda x: x.__first(), filtered)

    def __len__(self) -> int:
        """ 要素数 """
        return len(self.__elements)

    def __length_hint__(self) -> int:
        """ """
        return len(self.__elements)

    def __contains__(self, value: 'Element') -> bool:
        """ """
        return value.list()[0] in self.__elements

    def __getitem__(self, index: Union[int, slice]) -> 'Element':
        """ インデクサ """
        return Element(self.__elements[index])

    def __iter__(self) -> Iterator['Element']:
        """ for-in用イテレータ """
        return iter(map(lambda x: Element(x), self.__elements))

    def __reversed__(self) -> Iterator['Element']:
        """ for-in用逆イテレータ """
        return iter(map(lambda x: Element(x), reversed(self.__elements)))


class ElementIterator(object):
    """ Element用のイテレータ """

    def __init__(self, element: Element):
        """ """
        self.__element = element
        self.__count = len(element.list())
        self.__index = 0

    def __iter__(self) -> 'ElementIterator':
        """ """
        return self

    def __next__(self) -> Element:
        """ """
        if self.__index >= self.__count:
            raise StopIteration()
        e = self.__element[self.__index]
        self.__index += 1
        return Element(e)
