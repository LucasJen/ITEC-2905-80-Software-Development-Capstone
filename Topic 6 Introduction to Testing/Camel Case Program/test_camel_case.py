import camel_case
import unittest
from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camel_case_sentence(self):
        self.assertEqual('helloWorld', camel_case.camel_case('Hello World'))
        self.assertEqual('helloHowAreYou', camel_case.camel_case('HELLO HOW ARE YOU'))

if __name__ == "__main__":
    unittest.main()