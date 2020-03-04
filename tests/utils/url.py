import os
import re

from utils.global_holder import GlobalHolder


class URL(object):
    BASE_URL = ''

    def get_absolute_path(self, path: str):
        """ フルパスへ """
        if re.match('^\\w+://', path) or path.startswith('//:'):
            # full path
            target = path
        else:
            # related path
            target = os.path.join(URL.BASE_URL, path)
        return target

    def current_url(self) -> str:
        """ 現在のURL """
        return GlobalHolder.Browser.current_url

    def set_baseurl(self, url: str):
        """ navigate_toの基本URL """
        URL.BASE_URL = url
