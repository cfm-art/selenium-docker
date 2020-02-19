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

from utils.global_holder import GlobalHolder

class ElementAccessor(object):
  @staticmethod
  def set_value(element: WebElement, value: str):
    if element is None:
      return
    GlobalHolder.Browser.execute_script(
      'arguments[0].value = arguments[1]',
      element,
      value)

  @staticmethod
  def set(element: WebElement, value: str):
    """ 対象のinputに値を設定 """
    if element is None:
      return
    value = str(value)
    tag_name = element.tag_name
    if tag_name == 'input' or \
        tag_name == 'button' or \
        tag_name == 'option' or \
        tag_name == 'data' or \
        tag_name == 'meter' or \
        tag_name == 'progress':
      # input系はvalueを設定
      element.clear()
      if re.search('[ｱ-ﾝ]', value) is not None:
        # 半角ｶﾅが含まれる
        ElementAccessor.set_value(element, value)
      else:
        element.send_keys(value)
    elif tag_name == 'textarea':
      # textareaは特殊
      element.click()
      element.clear()
      if re.search('[ｱ-ﾝ]', value) is not None:
        # 半角ｶﾅが含まれる
        ElementAccessor.set_value(element, value)
      else:
        element.send_keys(value)
    elif tag_name == 'select':
      element.select_by_value(value)
    else:
      ElementAccessor.set_value(element, value)

  @staticmethod
  def set_file(element: WebElement, file: str):
    if element is None:
      return
    # /を頭につける
    file = str(file)
    if not file.startswith('/'):
        file = '/' + file
    # inputにファイルパスを送る
    element.clear()

    # 絶対パス
    path = os.path.abspath('../input' + file)
    element.send_keys(path)

  @staticmethod
  def get(element: WebElement) -> str:
    if element is None:
      return ''
    """ 対象の要素の値を取得 """
    if element.tag_name == 'input' or \
        element.tag_name == 'select' or \
        element.tag_name == 'button' or \
        element.tag_name == 'option' or \
        element.tag_name == 'data' or \
        element.tag_name == 'meter' or \
        element.tag_name == 'progress':
      # input系はvalueを取得
      return element.get_attribute('value')
    elif element.tag_name == 'textarea':
      # textareaは特殊
      return element.text
    else:
      return element.text

  @staticmethod
  def check(element: WebElement):
    if element is None:
      return
    return GlobalHolder.Browser.execute_script(
      'arguments[0].checked = true',
      element)

  @staticmethod
  def uncheck(element: WebElement):
    if element is None:
      return
    return GlobalHolder.Browser.execute_script(
      'arguments[0].checked = false',
      element)

  @staticmethod
  def is_checked(element: WebElement) -> bool:
    if element is None:
      return False
    return GlobalHolder.Browser.execute_script(
      'return arguments[0].checked',
      element)

  @staticmethod
  def inner_text(element: WebElement) -> str:
    if element is None:
      return ''
    return GlobalHolder.Browser.execute_script(
      'return arguments[0].textContent',
      element)


  @staticmethod
  def inner_html(element: WebElement) -> str:
    if element is None:
      return ''
    return GlobalHolder.Browser.execute_script(
      'return arguments[0].innerHTML',
      element)
