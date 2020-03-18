# coding: utf-8

import os
import re
from selenium.webdriver.remote.webelement import WebElement

from utils.global_holder import GlobalHolder


class ElementAccessor(object):
    @staticmethod
    def __set_value(element: WebElement, value: str):
        if element is None:
            return
        GlobalHolder.Browser.execute_script(
            'arguments[0].value = arguments[1]',
            element,
            value)

    @staticmethod
    def __set_input_value(element: WebElement, value: str):
        # input系はvalueを設定
        element.clear()
        if re.search('[ｱ-ﾝ]', value) is not None:
            # 半角ｶﾅが含まれる
            ElementAccessor.__set_value(element, value)
        else:
            element.send_keys(value)

    @staticmethod
    def set(element: WebElement, value: str):
        """ 対象のinputに値を設定 """
        if element is None:
            return
        value = str(value)
        tag_name = element.tag_name
        if tag_name == 'input':
            input_type = element.get_attribute('type')
            if input_type == 'radio' or input_type == 'checkbox':
                low = value.lower()
                # false/0/no/null/undefined
                is_false = low == 'false' or low == '0' or low == 'no' \
                    or low == 'null' or low == 'undefined'
                if is_false:
                    element.clear()
                else:
                    element.click()
            else:
                ElementAccessor.__set_input_value(element, value)
        if tag_name == 'button' or \
                tag_name == 'option' or \
                tag_name == 'data' or \
                tag_name == 'meter' or \
                tag_name == 'progress':
            ElementAccessor.__set_input_value(element, value)
        elif tag_name == 'textarea':
            # textareaは特殊
            element.click()
            ElementAccessor.__set_input_value(element, value)
        elif tag_name == 'select':
            ElementAccessor.__set_value(element, value)
        else:
            ElementAccessor.__set_value(element, value)

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

    @staticmethod
    def set_inner_text(element: WebElement, text: str) -> str:
        if element is None:
            return ''
        return GlobalHolder.Browser.execute_script(
            'return arguments[0].textContent = arguments[1]',
            element,
            text)

    @staticmethod
    def set_inner_html(element: WebElement, html: str) -> str:
        if element is None:
            return ''
        return GlobalHolder.Browser.execute_script(
            'return arguments[0].innerHTML = arguments[1]',
            element,
            html)
