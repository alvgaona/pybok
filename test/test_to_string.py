import unittest

from pybok import ToString, ArgsConstructor


class TestToString(unittest.TestCase):

    def test_methods(self):
        @ToString
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person("John", 21)

        self.assertEqual(str(person), 'Person(name=John,age=21)')


if __name__ == '__main__':
    unittest.main()
