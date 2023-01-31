import unittest
import pytest

from pybok import Builder, ArgsConstructor


class TestBuilder(unittest.TestCase):

    def test_all_required_args(self):
        @Builder
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person.name("John").age(23).build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person._name, "John")
        self.assertEqual(person._age, 23)

    def test_default_args(self):
        @Builder
        @ArgsConstructor
        class Person:
            name: str
            age: int = 23

        person = Person.name("John").build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person._name, "John")
        self.assertEqual(person._age, 23)

    def test_required_arg(self):
        @Builder
        @ArgsConstructor
        class Person:
            name: str
            age: int

        with pytest.raises(TypeError) as e:
            Person.age(23).build()

        self.assertEqual(str(e.value), "__init__() missing 1 required positional argument: 'name'")


if __name__ == '__main__':
    unittest.main()
