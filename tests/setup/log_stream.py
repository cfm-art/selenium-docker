# coding: utf-8

""" 結果用 """

from io import IOBase
import os
from pathlib import Path
import sys


class LogStream(IOBase):
    """ テスト結果をファイルとコンソールの両方に出す """

    @staticmethod
    def open(name: str) -> 'LogStream':
        return LogStream(name)

    def __init__(self, name: str):
        try:
            path = Path(name)
            os.makedirs(path.parent, exist_ok=True)
            self.file_ = open(name, "w+", encoding='utf-8')
        except Exception as e:
            message = (
                'ログファイルが生成できません：' + str(e))
            print(message)
            raise Exception(message)
        # ファイル生成成功したら
        self.default_ = sys.stdout
        self.default_err_ = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def close(self):
        sys.stdout = self.default_
        sys.stderr = self.default_err_
        self.file_.close()

    @property
    def closed(self):
        return self.file_.closed

    @closed.getter
    def get_closed(self):
        return self.file_.closed

    def fileno(self):
        return self.file_.fileno()

    def flush(self):
        self.file_.flush()

    def isatty(self):
        return False

    def readable(self):
        return False

    def seekable(self):
        return False

    def tell(self):
        return self.file_.tell()

    def writable(self):
        return True

    def writelines(self, lines):
        self.file_.writelines(lines)
        self.default_.writelines(lines)

    def write(self, b):
        self.file_.write(b)
        self.default_.write(b)
