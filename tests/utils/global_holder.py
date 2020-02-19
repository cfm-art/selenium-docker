from selenium.webdriver.remote.webdriver import WebDriver

class GlobalHolder():
  """ グローバル変数 """

  # WebDriver
  Browser: WebDriver = None
  # @staticmethod
  # @property
  # def Browser() -> WebDriver:
  #   return GlobalHolder._Browser

  # @staticmethod
  # @Browser.setter
  # def Browser(browser: WebDriver):
  #   GlobalHolder._Browser = browser
