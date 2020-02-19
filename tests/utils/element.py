# coding: utf-8

from collections import Counter
import datetime
from itertools import chain
import os
import re
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Any
from typing import Callable
from typing import Iterator
from typing import List
from typing import Union

from utils.element_accessor import ElementAccessor
from utils.global_holder import GlobalHolder

class Element(object):
  """ SeleniumのElementをラップ """

  @staticmethod
  def document() -> 'Element':
    documents: WebElement = GlobalHolder.Browser.find_elements_by_tag_name('html')
    return Element(documents)

  def __first(self) -> WebElement:
    """ リストの先頭要素 """
    element = self.__elements
    if isinstance(element, list):
      return element[0] if len(element) > 0 else None
    return element

  def __init__(self, element: Union[WebElement, List[WebElement]]):
    """ 要素を指定して初期化 """
    self.__elements = element if isinstance(element, list) else [element]

  def is_empty(self):
    """ 要素があるかどうか """
    return len(self.__elements) == 0

  def first(self):
      """ 1番目の要素 """
      return Element(self.__first())

  def at(self, index: int):
    """ 指定番目の要素を取得 """
    return Element(self.__elements[index])

  def click(self):
    """ クリック """
    self.foreach(lambda x: x.click())

  def set(self, value: str):
    """ 値を設定 """
    self.foreach(lambda x: ElementAccessor.set(x, value))

  def set_file(self, path: str):
    """ ファイルを設定 """
    self.foreach(lambda x: ElementAccessor.set_file(x, path))

  def get(self) -> str:
    """ 値を取得 """
    return ElementAccessor.get(self.__first())

  @property
  def text(self) -> str:
    """ 値を取得(Selenium互換) """
    return self.get()

  @text.setter
  def set_text(self, value: str):
    """ 値を設定(Selenium互換) """
    self.set(value)

  @text.deleter
  def delete_text(self):
    """ 値を削除 """
    self.set('')

  def get_text(self) -> str:
    return ElementAccessor.inner_text(self.__first())

  def get_html(self) -> str:
    return ElementAccessor.inner_html(self.__first())

  def get_attribute(self, name: str):
    """ タグの属性を取得 """
    return self.__first().get_attribute(name)

  def check(self):
    """ チェックボックスやラジオのチェックを外す """
    self.foreach(lambda x: ElementAccessor.check(x))

  def uncheck(self):
    """ チェックボックスやラジオのチェックを外す """
    self.foreach(lambda x: ElementAccessor.uncheck(x))

  def is_checked(self) -> bool:
    """ チェックボックスやラジオがチェック中か判定 """
    return ElementAccessor.is_checked(self.__first())

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

  @property
  def tag(self) -> str:
    """　タグ名 """
    return self.__first().tag_name

  def list(self) -> List[WebElement]:
    """ 内部リストを取得 """
    return self.__elements

  def foreach(self, func: Callable[['Element'], None]):
    """ 一括処理 """
    for e in self.__elements:
        func(Element(e))

  def filter(self, func: Callable[['Element'], bool]):
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