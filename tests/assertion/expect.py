# coding: utf-8

__unittest = True


def assert_fail(error: str, message: str):
    """ 失敗 """
    if message is None or message == '':
        raise AssertionError(error + '?\n')
    else:
        raise AssertionError(error + '?\n' + message + '\n')


class Expect(object):
    def __msg(self) -> str:
        return 'actual is [' + str(self.__actual) + ']\n'

    def __init__(self, actual):
        self.__actual = actual

    def is_true(self, message: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and \
                isinstance(actual, bool) and actual:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = True', message)

    def is_false(self, message: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and \
                isinstance(actual, bool) and not actual:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = False', message)

    def is_truthy(self, message: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and bool(actual):
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≈ True', message)

    def is_falsy(self, message: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None and not bool(actual):
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≈ False', message)

    def is_null(self, message: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is None:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] is null', message)

    def is_not_null(self, message: str = ''):
        """" actual = true """
        actual = self.__actual
        if actual is not None:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] isnot null', message)

    def equals_to(self, expect, message: str = ""):
        """ expect = actual """
        actual = self.__actual
        if expect is None and actual is None:
            return
        if expect is not None and actual is not None:
            if expect == actual:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = ' + str(expect), message)

    def not_equals_to(self, expect, message: str = ""):
        """ expect ≠ actual """
        actual = self.__actual
        if actual is None and expect is not None:
            return
        if actual is not None and expect is None:
            return
        if actual != expect:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] ≠ ' + str(expect), message)

    def approximately_equals_to(self, expect: float, message: str = ""):
        """ expect = actual """
        actual = self.__actual
        if expect is None and actual is None:
            return
        if expect is not None and actual is not None:
            diff = abs(expect - actual)
            if diff < 1.19209e-07:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = ' + str(expect), message)

    def greater_than(self, value, message: str = ""):
        """ actual > value """
        actual = self.__actual
        if value is not None and actual is not None:
            if actual > value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] > ' + str(value), message)

    def less_than(self, value, message: str = ""):
        """ actual < value """
        actual = self.__actual
        if value is not None and actual is not None:
            if actual < value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] < ' + str(value), message)

    def greater_than_or_equals(self, value, message: str = ""):
        """ actual >= value """
        actual = self.__actual
        if value is not None and actual is not None:
            if actual > value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] >= ' + str(value), message)

    def less_than_or_eauals(self, value, message: str = ""):
        """ actual <= value """
        actual = self.__actual
        if value is not None and actual is not None:
            if actual <= value:
                return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] <= ' + str(value), message)

    def reference_equals_to(self, expect, message: str = ""):
        """ expect = actual """
        actual = self.__actual
        if expect is actual:
            return
        assert_fail(
            self.__msg() +
            '[' + str(actual) + '] = ' + str(expect), message)

    def is_incetance_of(self, t: type, message: str = ''):
        """ type(actual) = type """
        actual = self.__actual
        if isinstance(actual, t):
            return
        assert_fail(
            self.__msg() +
            '[' + str(type(actual)) + '] = ' + str(t), message)


class Assert(object):
    """ アサーション """

    @staticmethod
    def fail(message: str = ''):
        """ 失敗 """
        assert_fail(message)

    @staticmethod
    def expect(o) -> Expect:
        return Expect(o)
