import unittest

class TestKernel(unittest.TestCase):

    def test_safe_float(self):
        import math

        self.assertEqual(ck.safe_float(1, 0), 1.0)
        self.assertEqual(ck.safe_float('a', 0), 0)
        self.assertEqual(ck.safe_float('-5.35', 0), -5.35)
        self.assertEqual(ck.safe_float('Infinity', 0), float('inf'))
        self.assertTrue(math.isnan(ck.safe_float('nan', 0)))
