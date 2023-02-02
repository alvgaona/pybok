import unittest

from pybok import Singleton, ArgsConstructor


class TestSingleton(unittest.TestCase):

    def test_singleton(self):
        @Singleton
        @ArgsConstructor
        class Person:
            name: str
            age: int

        john = Person("John", 21)
        jane = Person("Jane", 19)
        empty = Person()

        self.assertEqual(john._name, jane._name)
        self.assertEqual(john._age, jane._age)
        self.assertEqual(john._age, empty._age)


if __name__ == '__main__':
    unittest.main()
