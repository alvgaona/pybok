import unittest

from pybok import Setter, ArgsConstructor


class TestSetter(unittest.TestCase):

    def test_methods(self):
        @Setter
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person("John", 21)

        person.set_name("Jane")
        person.set_age(19)

        self.assertEqual(person._name, "Jane")
        self.assertEqual(person._age, 19)


if __name__ == '__main__':
    unittest.main()
