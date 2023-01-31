import unittest
import pytest

from pybok.argsconstructor import ArgsConstructor


class TestArgsConstructor(unittest.TestCase):

    def test_init_required_args(self):
        @ArgsConstructor
        class Student:
            name: str
            age: int

        student = Student("John", 21)

        self.assertEqual(student._name, "John")
        self.assertEqual(student._age, 21)

    def test_init_required_and_default_args(self):
        @ArgsConstructor
        class Student:
            name: str
            age: int = 25

        student = Student("John")

        self.assertEqual(student._name, "John")
        self.assertEqual(student._age, 25)

    def test_init_error_required_arg(self):
        @ArgsConstructor
        class Student:
            name: str
            age: int

        with pytest.raises(TypeError) as e:
            Student("John")

        self.assertEqual(str(e.value), "__init__() missing 1 required positional argument: 'age'")


if __name__ == '__main__':
    unittest.main()
