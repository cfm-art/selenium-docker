# coding: utf-8

import os
from pathlib import Path

from utils.element import Element
from utils.file_name import FileName
from utils.global_holder import GlobalHolder
from utils.url import URL
from utils.waiter import Waiter


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

        image_path = FileName.output(output + '.png')

        path = Path(image_path)
        os.makedirs(path.parent, exist_ok=True)
        GlobalHolder.Browser.save_screenshot(image_path)

    def navigate_to(self, path: str, wait_seconds: float = 1.0):
        """ 指定URLへ移動 """
        target = URL().get_absolute_path(path)
        GlobalHolder.Browser.get(target)
        if wait_seconds > 0:
            Waiter().wait_page(path, wait_seconds, True)

    def url(self) -> str:
        """ 現在のURL """
        return URL().current_url()

    def set_baseurl(self, url: str):
        """ navigate_toの基本URL """
        URL().set_baseurl(url)
