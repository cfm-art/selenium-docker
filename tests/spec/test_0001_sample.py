# coding: utf-8

import unittest

from utils.ja.browser import BrowserJa
from utils.browser import Browser
from utils.log import Log
from utils.ja.log import ログ

from assertion.expect import Assert


class test_0001_sample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_サンプル(self):
        browser = BrowserJa()
        browser.ページ移動('https://www.google.com/')
        document = browser.document()
        Log.info(document.idで検索('gb').テキスト取得())
        browser.スクリーンショット('sample')

    def test_002_サンプル(self):
        browser = Browser()
        browser.navigate_to('https://www.google.com/')
        document = browser.document()
        ログ.情報(document.find_by_id('gb').get_text())
        browser.screen_shot('sample')

    def test_003_サンプル(self):
        Assert.expect(1).equals_to(1)
        Assert.expect(1).greater_than(0)
        Assert.expect(1).less_than(2)
        Assert.expect(1).greater_than_or_equals(0)
        Assert.expect(1).less_than_or_eauals(2)
        Assert.expect(0.1 + 0.2).float_equals_to(0.3)
        Assert.expect(False).is_false()
        Assert.expect(True).is_true()
        Assert.expect(0).is_falsy()
        Assert.expect(1).is_truthy()
        Assert.expect(None).is_null()
        Assert.expect(1).is_not_null()
