# coding: utf-8
import datetime
import locale
import os
import platform
import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from setup.log_stream import LogStream
from setup.test_collector import TestCollector

from utils.global_holder import GlobalHolder

def run():
  sys.path.insert(0, os.getcwd())
  locale.setlocale(locale.LC_ALL, '')

  # ログファイル生成
  logfile_name = '.\\output\\results\\result_{0}.txt' if 'windows' in platform.system() else './output/results/result_{0}.txt'
  logfile = LogStream(
    logfile_name.format(datetime.datetime.now().strftime('%Y%m%d_%H%M_%S')))

  browser = None
  try:
    # HEADLESSブラウザに接続
    browser = webdriver.Remote(
      command_executor='http://selenium-hub:4444/wd/hub',
      desired_capabilities=DesiredCapabilities.CHROME)

    GlobalHolder.Browser = browser

    # 最大化
    browser.maximize_window()

    # テスト対象取得
    collector = TestCollector()
    Verbosity = 2

    unittest.TextTestRunner(verbosity=Verbosity).run(collector.suite)
  except Exception as e:
    print(e)
  finally:
    # 終了
    if browser is not None:
      browser.close()
      browser.quit()

    # ログ終了
    logfile.close()