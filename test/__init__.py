import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # Valid email addresses:
        self.valid_addresses = [
            'niceandsimple@example.com',
            'very.common@example.com',
            'a.little.lengthy.but.fine@dept.example.com',
            'disposable.style.email.with+symbol@example.com',
            'other.email-with-dash@example.com',
            '"much.more unusual"@example.com',
            '"very.unusual.@.unusual.com"@example.com',
            ('"very.(),:;<>[]\\".VERY.\\"very@\\\\ \\"very\\".unusual"'
             '@strange.example.com'),
            'postbox@com',
            'admin@mailserver1',
            '!#$%&\'*+-/=?^_`{}|~@example.org',
            '"()<>[]:,;@\\\\\\"!#$%&\'*+-/=?^_`{}| ~.a"@example.org',
            '" "@example.org',
            'abc."defghi".xyz@example.com'
        ]

        # invalid email addresses:
        self.invalid_addresses = [
            'Abc.example.com',
            'A@b@c@example.com',
            'a"b(c)d,e:f;g<h>i[j\\k]l@example.com',
            'just"not"right@example.com',
            'this is"not\\allowed@example.com',
            'this\\ still\\"not\\\\allowed@example.com',
            'abc"defghi"xyz@example.com'
        ]
