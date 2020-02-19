# coding: utf-8

import datetime
import os
import platform
from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from utils.element import Element
from utils.global_holder import GlobalHolder

class Browser(object):
  def document(self) -> Element:
    return Element.document()

  def screen_shot(self, filename: str):
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M_%S')
    if 'windows' in platform.system():
      image_path = '.\\output\\captures\\{0}\\{1}'.format(now, filename.replace('/', '\\'))
    else:
      image_path = './output/captures/{0}/{1}'.format(now, filename)

    path = Path(image_path)
    os.makedirs(path.parent, exist_ok=True)
    GlobalHolder.Browser.save_screenshot(image_path)

  def wait(self, seconds: float):
    GlobalHolder.Browser.implicitly_wait(seconds)

  def navigate_to(self, path: str):
    wait = WebDriverWait(GlobalHolder.Browser, 1.0)
    path_lower = path.lower()
    GlobalHolder.Browser.get(path)
    try:
      wait.until(lambda x: path_lower in self.url().lower() or self.url().lower() in path_lower)
    except Exception as e:
      print('current url:' + self.url())
      raise
  
  def url(self) -> str:
    return GlobalHolder.Browser.current_url
