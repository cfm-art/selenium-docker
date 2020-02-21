# coding: utf-8

import os
import platform
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait

from utils.element import Element
from utils.global_holder import GlobalHolder


class Browser(object):
    """ ブラウザ制御系 """

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

        now = GlobalHolder.LunchTime
        if 'windows' in platform.system():
            image_path = '.\\output\\captures\\{2}\\{0}\\{1}.png' \
                .format(
                    now.strftime('%Y%m%d_%H%M_%S'),
                    output.replace('/', '\\'),
                    now.strftime('%Y%m%d'))
        else:
            image_path = './output/captures/{2}/{0}/{1}.png' \
                .format(
                    now.strftime('%Y%m%d_%H%M_%S'),
                    output.replace('/', '\\'),
                    now.strftime('%Y%m%d'))

        path = Path(image_path)
        os.makedirs(path.parent, exist_ok=True)
        GlobalHolder.Browser.save_screenshot(image_path)

    def wait(self, seconds: float):
        """　指定秒停止 """
        GlobalHolder.Browser.implicitly_wait(seconds)

    def navigate_to(self, path: str):
        """ 指定URLへ移動 """
        wait = WebDriverWait(GlobalHolder.Browser, 1.0)
        path_lower = path.lower()
        GlobalHolder.Browser.get(path)
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
