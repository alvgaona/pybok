import unittest

from pybok import Getter, Setter, ArgsConstructor


class TestSetter(unittest.TestCase):

    def test_methods(self):
        @Getter
        @Setter
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person("John", 21)

        person.name = "Jane"
        person.age = 19

        self.assertEqual(person._name, "Jane")
        self.assertEqual(person._age, 19)


if __name__ == '__main__':
    unittest.main()
