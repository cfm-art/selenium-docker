# coding: utf-8

import re
import unittest


class TestCollector:
    """ テスト対象の取得 """

    def __init__(self):
        self.suite = self.__create_test_suite()

    def __create_test_suite(self):
        """ テストランナーの生成 """
        suite = unittest.TestSuite()
        tests = unittest.defaultTestLoader.discover(
                'spec', pattern='test_*.py')
        self.__sort(suite, tests)
        return suite

    def __sort(self, suite, tests, module=''):
        """ テストを番号順にソートして追加する """
        temporary = {}
        other = []

        # ソート用数値を取り出す正規表現
        exp = re.compile('test_(\\d*)_(.*)')

        # 数値順でソート
        for test in tests:
            for inner_tests in test:
                try:
                    for actual_test in inner_tests:
                        # ファイル名をチェック
                        actual_test_name = actual_test.__class__.__name__
                        if actual_test_name.startswith('test_') and \
                                module in actual_test.__module__:
                            matched = exp.search(actual_test.__module__)
                            if matched is None:
                                # クラス名をチェック
                                matched = exp.search(actual_test_name)

                            # 数値がついていればソート対象
                            if matched is None:
                                other.append(inner_tests)
                            else:
                                key = matched.group(1) + '_' + matched.group(2)
                                temporary[key] = inner_tests
                            break
                except Exception as e:
                    print('記述エラー:' + str(e))
                    print(inner_tests)
                    pass

        # 指定された順番で登録
        for test in sorted(temporary.items()):
            # print(test[1])
            suite.addTest(test[1])

        # 指定なしを登録
        for test in other:
            # print(test)
            suite.addTest(test)
