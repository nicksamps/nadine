import unittest

from nadine import test_cases


class TestAsserts(test_cases.NadineTestCase):
    def test_equality(self):
        self.assertEqual(1, 1)

    def test_is_none(self):
        self.assertIsNone(None)

    def test_raises(self):
        with self.assertRaises(ValueError):
            raise ValueError('Test')


if __name__ == '__main__':
        unittest.main()
