import datetime
from selenium.webdriver.remote.webdriver import WebDriver


class GlobalHolder():
    """ グローバル変数 """

    # WebDriver
    Browser: WebDriver = None

    # 起動日時
    LunchTime: datetime.datetime = None

    # 連番
    ScreenShotNo: int = 1
