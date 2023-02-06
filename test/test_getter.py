import unittest

from pybok import Getter, ArgsConstructor


class TestGetter(unittest.TestCase):

    def test_methods(self):
        @Getter
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person("John", 21)

        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 21)


if __name__ == '__main__':
    unittest.main()
