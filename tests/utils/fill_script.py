import re

from utils.browser import Browser
from utils.waiter import Waiter


class ScriptForFiller(object):
    """ filler用 """

    def __init__(self, cell: str):
        self.__cell = cell.strip()

    def is_script(self):
        return (
            self.is_comment() or
            self.__cell.split(':').count() == 2)

    def is_comment(self):
        return (
            self.__cell.startswith('//') or
            self.__cell.startswith('--') or
            self.__cell.lower().startswith('nop'))

    def run(self):
        if not self.is_script():
            return
        if self.is_comment():
            return

        tokens = self.__cell.split(':')
        proc = tokens[0]
        selector = tokens[1]

        if proc == 'click':
            Browser().document().query_selector_all(selector).click()
        elif proc == 'wait':
            w = Waiter()
            if re.match('^[1-9]\\d*s$', selector):
                w.wait_seconds(int(selector[:selector.count() - 1]))
            elif re.match('^[1-9]\\d*m$', selector):
                w.wait_seconds(int(selector[:selector.count() - 1]) * 60)
            else:
                w.wait_element(selector)
        else:
            raise Exception('unkown command')
