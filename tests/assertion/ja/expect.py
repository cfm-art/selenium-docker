# coding: utf-8

from utils.ja.log import ログ


__unittest = True


def assert_fail(error: str, message: str):
    """ 失敗 """
    if message is None or message == '':
        raise AssertionError(error + '?\n')
    else:
        raise AssertionError(error + '?\n' + message + '\n')


class 判定(object):
    def __msg(self) -> str:
        return '指定値 = [' + str(self.__actual) + ']\n'

    def __init__(self, 値):
        self.__actual = 値

    def 真値か(self, エラーメッセージ: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and \
                isinstance(actual, bool) and actual:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = 真値', エラーメッセージ)

    def 偽値か(self, エラーメッセージ: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and \
                isinstance(actual, bool) and not actual:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = 偽値', エラーメッセージ)

    def 実質真か(self, エラーメッセージ: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and bool(actual):
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≒ 真値', エラーメッセージ)

    def 実質偽か(self, エラーメッセージ: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and not bool(actual):
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≒ 偽値', エラーメッセージ)

    def nullか(self, エラーメッセージ: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is None:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ＝ null', エラーメッセージ)

    def nullではないか(self, エラーメッセージ: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≠ null', エラーメッセージ)

    def 等しいか(self, 期待値, エラーメッセージ: str = ""):
        """ expect = actual """
        actual = self.__actual
        expect = 期待値
        if expect is None and actual is None:
            return
        if isinstance(expect, float):
            ログ.警告('小数が等しい?')
        if expect is not None and actual is not None:
            if expect == actual:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = ' + str(expect), エラーメッセージ)

    def 等しくないか(self, 期待値, エラーメッセージ: str = ""):
        """ expect ≠ actual """
        expect = 期待値
        actual = self.__actual
        if actual is None and expect is not None:
            return
        if actual is not None and expect is None:
            return
        if isinstance(expect, float):
            ログ.警告('小数が等しくない?')
        if actual != expect:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≠ ' + str(expect), エラーメッセージ)

    def 小数が等しい(self, 期待値: float, エラーメッセージ: str = ""):
        """ expect = actual """
        expect = 期待値
        actual = self.__actual
        if expect is None and actual is None:
            return
        if expect is not None and actual is not None:
            diff = abs(expect - actual)
            if diff <= 1.19209e-07:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = ' + str(expect), エラーメッセージ)

    def 小数が等しくない(self, 期待値: float, エラーメッセージ: str = ""):
        """ expect = actual """
        expect = 期待値
        actual = self.__actual
        if expect is None and actual is None:
            return
        if expect is not None and actual is not None:
            diff = abs(expect - actual)
            if diff > 1.19209e-07:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≒ ' + str(expect), エラーメッセージ)
            
    def 大きいか(self, 値, エラーメッセージ: str = ""):
        """ actual > value """
        value = 値
        actual = self.__actual
        if value is not None and actual is not None:
            if actual > value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] > ' + str(value), エラーメッセージ)

    def 小さいか(self, 値, エラーメッセージ: str = ""):
        """ actual < value """
        value = 値
        actual = self.__actual
        if value is not None and actual is not None:
            if actual < value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] < ' + str(value), エラーメッセージ)

    def 以上か(self, 値, エラーメッセージ: str = ""):
        """ actual >= value """
        value = 値
        actual = self.__actual
        if value is not None and actual is not None:
            if actual > value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] >= ' + str(value), エラーメッセージ)

    def 以下か(self, 値, エラーメッセージ: str = ""):
        """ actual <= value """
        value = 値
        actual = self.__actual
        if value is not None and actual is not None:
            if actual <= value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] <= ' + str(value), エラーメッセージ)

    def 参照が等しいか(self, 期待値, エラーメッセージ: str = ""):
        """ expect = actual """
        actual = self.__actual
        expect = 期待値
        if expect is actual:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = ' + str(expect), エラーメッセージ)

    def 型が一致するか(self, 型: type, エラーメッセージ: str = ''):
        """ type(actual) = type """
        t = 型
        actual = self.__actual
        if isinstance(actual, t):
            return
        assert_fail(
            self.__msg() +
            '[' + str(type(actual)) + '] = ' + str(t), エラーメッセージ)


class 結果(object):
    """ アサーション """

    @staticmethod
    def テスト失敗(エラーメッセージ: str = ''):
        """ 失敗 """
        assert_fail(エラーメッセージ)

    @staticmethod
    def 判定(o) -> 判定:
        return 判定(o)
