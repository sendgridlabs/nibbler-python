import unittest
from nibbler.parser import parse_email
from test import BaseTestCase
from nose.tools import (assert_true, assert_false)


class TestCase(BaseTestCase):
    def test_valid_email(self):
        for e in self.valid_addresses:
            valid, email_parsed = parse_email(e)
            assert_true(valid, 'Error: email %s should be valid' % e)

    def test_invalid_email(self):
        for e in self.invalid_addresses:
            valid, email_parsed = parse_email(e)
            assert_false(valid, 'Error: email %s should be invalid' % e)

if __name__ == '__main__':
    unittest.main()
