import unittest

from MutableString import MutableString


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_mutable_string(self):
        string = "a b c\nd e f"
        muString = MutableString(string)
        muString[0, 7] = 'H'
        print(muString)

        # self.assertEqual(str(mutString), reString)


if __name__ == '__main__':
    unittest.main()
