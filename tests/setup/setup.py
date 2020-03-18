# coding: utf-8
import datetime
import locale
import os
import platform
import sys
import traceback
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from setup.log_stream import LogStream
from setup.test_collector import TestCollector
from spec.config import Config
from utils.global_holder import GlobalHolder


def run(selenium_host: str):
    sys.path.insert(0, os.getcwd())
    locale.setlocale(locale.LC_ALL, '')

    # ログファイル生成
    logfile_name = '.\\output\\results\\{1}\\result_{0}.txt' \
        if 'windows' in platform.system() \
        else './output/results/{1}/result_{0}.txt'
    now = datetime.datetime.now()
    GlobalHolder.LunchTime = now
    logfile = LogStream(logfile_name.format(
        now.strftime('%Y%m%d_%H%M_%S'),
        now.strftime('%Y%m%d')))

    config = Config()

    browser = None
    try:
        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://' + selenium_host + '/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        GlobalHolder.Browser = browser

        # 最大化
        browser.maximize_window()

        # テスト対象取得
        collector = TestCollector()
        Verbosity = 2

        config.initialize()

        unittest.TextTestRunner(verbosity=Verbosity).run(collector.suite)
    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        # 終了
        if browser is not None:
            browser.close()
            browser.quit()

        try:
            config.exit()
        except Exception as e:
            print(e)
            traceback.print_exc()

        # ログ終了
        logfile.close()
