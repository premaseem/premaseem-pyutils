# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from calculator.square import find_square


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(find_square(5), 6)


if __name__ == '__main__':
    unittest.main()
