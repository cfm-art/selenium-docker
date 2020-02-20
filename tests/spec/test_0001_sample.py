# coding: utf-8

import unittest

from utils.ja.browser import BrowserJa
from utils.browser import Browser

class test_0001_sample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_サンプル(self):
        browser = BrowserJa()
        browser.ページ移動('https://www.google.com/')
        document = browser.document()
        print(document.idで検索('gb').テキスト取得())
        browser.スクリーンショット('sample')

    def test_002_サンプル(self):
        browser = Browser()
        browser.navigate_to('https://www.google.com/')
        document = browser.document()
        print(document.find_by_id('gb').get_text())
        browser.screen_shot('sample')
