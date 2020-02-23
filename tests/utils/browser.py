# coding: utf-8

import os
from pathlib import Path
import re
from selenium.webdriver.support.ui import WebDriverWait

from utils.element import Element
from utils.file_name import FileName
from utils.global_holder import GlobalHolder


class Browser(object):
    """ ブラウザ制御系 """

    BASE_URL = ''

    def document(self) -> Element:
        """ ドキュメントルートの取得 """
        return Element.document()

    def screen_shot(self, filename: str):
        """ スクリーンショット保存 """
        import traceback
        output = 'スクリーンショット'
        for tb in traceback.extract_stack(None, None):
            if tb[2].startswith('test'):
                output = tb[2]

        no = '{0:04d}'.format(GlobalHolder.ScreenShotNo)
        GlobalHolder.ScreenShotNo += 1
        if filename is None or filename == '':
            output = output + '_' + no
        else:
            output = output + '_' + filename + '_' + no

        image_path = FileName.output(output + '.png')

        path = Path(image_path)
        os.makedirs(path.parent, exist_ok=True)
        GlobalHolder.Browser.save_screenshot(image_path)

    def wait(self, seconds: float):
        """　指定秒停止 """
        GlobalHolder.Browser.implicitly_wait(seconds)

    def navigate_to(self, path: str):
        """ 指定URLへ移動 """
        wait = WebDriverWait(GlobalHolder.Browser, 1.0)
        if re.match('^\\w+://', path):
            target = path
        else:
            target = os.path.join(Browser.BASE_URL, path)
        path_lower = target.lower()
        GlobalHolder.Browser.get(target)
        try:
            wait.until(lambda x: self._is_url(path_lower))
        except Exception as e:
            print(str(e))
            print('current url:' + self.url())
            raise

    def _is_url(self, path_lower: str) -> bool:
        return path_lower in self.url().lower() or \
            self.url().lower() in path_lower

    def url(self) -> str:
        """ 現在のURL """
        return GlobalHolder.Browser.current_url

    def set_baseurl(self, url: str):
        """ navigate_toの基本URL """
        Browser.BASE_URL = url
