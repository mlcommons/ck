import unittest
import sys

ck=None # Will be updated by CK (initialized CK kernel)

def dummy_exit(code):
    print('Exit code: ' + str(code))

def get_io():
    if sys.version_info[0]>2:
        import io
        return io.StringIO()
    else:
        from StringIO import StringIO
        return StringIO()

class TestKernel(unittest.TestCase):

    def test_out(self):
        saved_stdout = sys.stdout
        try:
            out = get_io()
            sys.stdout = out
            ck.out('test')
            self.assertEqual('test', out.getvalue().strip())
        finally:
            sys.stdout = saved_stdout


    def test_err(self):
        saved_stdout = sys.stdout
        saved_exit = sys.exit
        try:
            out = get_io()
            sys.stdout = out
            sys.exit = dummy_exit
            ck.err({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.\nExit code: 2', out.getvalue().strip())
        finally:
            sys.stdout = saved_stdout
            sys.exit = saved_exit

    def test_jerr(self):
        saved_stdout = sys.stdout
        try:
            out = get_io()
            sys.stdout = out
            with self.assertRaises(KeyboardInterrupt):
                ck.jerr({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.', out.getvalue().strip())
        finally:
            sys.stdout = saved_stdout

    def test_safe_float(self):
        import math

        self.assertEqual(ck.safe_float(1, 0), 1.0)
        self.assertEqual(ck.safe_float('a', 0), 0)
        self.assertEqual(ck.safe_float('-5.35', 0), -5.35)
        self.assertEqual(ck.safe_float('Infinity', 0), float('inf'))
        self.assertTrue(math.isnan(ck.safe_float('nan', 0)))

    def test_safe_int(self):
        import math

        self.assertEqual(ck.safe_int(1, 0), 1)
        self.assertEqual(ck.safe_int('a', 0), 0)
        self.assertEqual(ck.safe_int('-5', 0), -5)

    def test_safe_get_val_from_list(self):
        self.assertEqual(ck.safe_get_val_from_list([1, 2], 0, 0), 1)
        self.assertEqual(ck.safe_get_val_from_list([1, 2], 1, 0), 2)
        self.assertEqual(ck.safe_get_val_from_list([], 1, 0), 0)
