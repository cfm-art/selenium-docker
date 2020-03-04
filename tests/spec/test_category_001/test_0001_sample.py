# coding: utf-8

import unittest

from utils.ja.browser import ブラウザ
from utils.browser import Browser
from utils.ja.waiter import 待機
from utils.waiter import Waiter
from utils.log import Log
from utils.ja.log import ログ


class test_0001_sample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_サンプル(self):
        browser = ブラウザ()
        browser.ページ移動('https://www.google.com/')
        document = browser.document()
        ログ.情報(document.idで検索('gb').テキスト取得())

        待機().指定秒(1).待つ()
        browser.スクリーンショット('sample')

    def test_002_サンプル(self):
        browser = Browser()
        browser.navigate_to('https://www.google.com/')
        document = browser.document()
        Log.info(document.query_selector_all('#gb').get_text())

        Waiter().wait_seconds(1)
        browser.screen_shot('sample')
