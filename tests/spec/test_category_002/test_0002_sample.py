# coding: utf-8

import unittest

from assertion.expect import Assert


class test_0002_sample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_003_サンプル(self):
        Assert.expect(' test ').equals_to('test')
        Assert.expect(1).equals_to(1)
        Assert.expect(1).greater_than(0)
        Assert.expect(1).less_than(2)
        Assert.expect(1).greater_than_or_equals(0)
        Assert.expect(1).less_than_or_eauals(2)
        Assert.expect(0.1 + 0.2).float_equals_to(0.3)
        Assert.expect(False).is_false()
        Assert.expect(True).is_true()
        Assert.expect(0).is_falsy()
        Assert.expect(1).is_truthy()
        Assert.expect(None).is_null()
        Assert.expect(1).is_not_null()
