# coding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from utils.global_holder import GlobalHolder
from utils.url import URL
from utils.reraise import reraise


class Waiter(object):
    """ 一時停止系 """

    def wait_seconds(self, seconds: float):
        """　指定秒停止 """
        GlobalHolder.Browser.implicitly_wait(seconds)

    def wait_page(
            self,
            path: str,
            wait_seconds: float = 1.0,
            throws: bool = True):
        """ ページ遷移待ち """
        wait = WebDriverWait(GlobalHolder.Browser, wait_seconds)
        target = URL().get_absolute_path(path)
        path_lower = target.lower()
        try:
            wait.until(lambda x: self._is_url(path_lower))
        except Exception as e:
            if throws:
                reraise(
                    e,
                    'timeout wait page',
                    'Expect:' + path,
                    'Actual:' + URL().current_url())

    def wait_element(
            self,
            selector: str,
            visible: bool = True,
            wait_seconds: float = 1.0,
            throws: bool = True):
        """ 要素待ち """
        wait = WebDriverWait(GlobalHolder.Browser, wait_seconds)
        try:
            q = By.cssSelector(selector)
            cond = expected_conditions.presence_of_all_elements_located(q)
            if visible:
                wait.until(cond)
            else:
                wait.until_not(cond)
        except Exception as e:
            if throws:
                reraise(
                    e,
                    'time out wait element'
                    'Target:' + selector)

    def wait_element_clickable(
            self,
            selector: str,
            clickable: bool = True,
            wait_seconds: float = 1.0,
            throws: bool = True):
        """ クリック可否状態待ち """
        wait = WebDriverWait(GlobalHolder.Browser, wait_seconds)
        try:
            q = By.cssSelector(selector)
            cond = expected_conditions.element_to_be_clickable(q)
            if clickable:
                wait.until(cond)
            else:
                wait.until_not(cond)
        except Exception as e:
            if throws:
                reraise(
                    e,
                    'time out wait element clickable'
                    'Target:' + selector)

    def wait_title_contains(
            self,
            title: str,
            wait_seconds: float = 1.0,
            throws: bool = True):
        """ タイトル待ち """
        wait = WebDriverWait(GlobalHolder.Browser, wait_seconds)
        try:
            cond = expected_conditions.title_contains(title)
            wait.until(cond)
        except Exception as e:
            if throws:
                reraise(
                    e,
                    'time out wait title'
                    'Except:' + title,
                    'Actual:' + GlobalHolder.Browser.title)

    def wait_loaded(
            self,
            wait_seconds: float = 1.0,
            throws: bool = True):
        wait = WebDriverWait(GlobalHolder.Browser, wait_seconds)
        try:
            wait.until(expected_conditions.presence_of_all_elements_located)
        except Exception as e:
            if throws:
                reraise(
                    e,
                    'time out wait loaded')

    def _is_url(self, path_lower: str) -> bool:
        url = URL().current_url().lower()
        return path_lower in url or \
            url in path_lower
