import unittest
from abc import ABC, abstractmethod
from inspect import signature

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

    def test_super(self):
        @ArgsConstructor
        class Vehicle:
            wheels: int
            doors: bool

        @ArgsConstructor
        class Car(Vehicle):
            model: str

        car = Car('Mercedes-AMG GT Black Series', 4, True)

        self.assertEqual(
            str(signature(car.__init__)),
            '(model, wheels, doors) -> None'
        )

        self.assertEqual(car._model, 'Mercedes-AMG GT Black Series')
        self.assertEqual(car._wheels, 4)
        self.assertTrue(car._doors)

    def test_super_default_parent_args(self):
        @ArgsConstructor
        class Vehicle:
            wheels: int = 4
            doors: bool

        @ArgsConstructor
        class Car(Vehicle):
            model: str

        car = Car('Mercedes-AMG GT Black Series', True)

        self.assertEqual(
            str(signature(car.__init__)),
            '(model, doors, *, wheels=4) -> None'
        )

        self.assertEqual(car._model, 'Mercedes-AMG GT Black Series')
        self.assertEqual(car._wheels, 4)
        self.assertTrue(car._doors)

    def test_super_super_args(self):
        @ArgsConstructor
        class Vehicle:
            wheels: int
            doors: bool

        @ArgsConstructor
        class Car(Vehicle):
            model: str

        @ArgsConstructor
        class F1(Car):
            halo: bool

        f1 = F1(True, 'W15', 4, True)

        self.assertEqual(
            str(signature(f1.__init__)),
            '(halo, model, wheels, doors) -> None'
        )

        self.assertTrue(f1._halo)
        self.assertEqual(f1._model, 'W15')
        self.assertEqual(f1._wheels, 4)
        self.assertTrue(f1._doors)

    def test_super_super_default_args(self):
        @ArgsConstructor
        class Vehicle:
            wheels: int
            doors: bool

        @ArgsConstructor
        class Car(Vehicle):
            model: str
            max_speed: int = 200

        @ArgsConstructor
        class F1(Car):
            halo: bool

        f1 = F1(True, 'W15', 4, True)

        self.assertEqual(
            str(signature(f1.__init__)),
            '(halo, model, wheels, doors, *, max_speed=200) -> None'
        )

        self.assertTrue(f1._halo)
        self.assertEqual(f1._model, 'W15')
        self.assertEqual(f1._wheels, 4)
        self.assertTrue(f1._doors)

    def test_super_no_constructor(self):
        class Vehicle:
            wheels: int
            doors: bool = True

        @ArgsConstructor
        class Car(Vehicle):
            model: str
            max_speed: int

        car = Car('Mercedes-AMG GT Black Series', 200, 4)

        self.assertEqual(
            str(signature(car.__init__)),
            '(model, max_speed, wheels, *, doors=True) -> None'
        )

        self.assertEqual(car._model, 'Mercedes-AMG GT Black Series')
        self.assertEqual(car._wheels, 4)
        self.assertEqual(car._max_speed, 200)
        self.assertTrue(car._doors)

    def test_super_abstract(self):
        class Vehicle(ABC):
            wheels: int
            doors: bool = True

            @abstractmethod
            def func(self):
                pass

        @ArgsConstructor
        class Car(Vehicle):
            model: str
            max_speed: int

            def func(self):
                pass

        car = Car('Mercedes-AMG GT Black Series', 200, 4)

        self.assertEqual(
            str(signature(car.__init__)),
            '(model, max_speed, wheels, *, doors=True) -> None'
        )

        self.assertEqual(car._model, 'Mercedes-AMG GT Black Series')
        self.assertEqual(car._wheels, 4)
        self.assertEqual(car._max_speed, 200)
        self.assertTrue(car._doors)


if __name__ == '__main__':
    unittest.main()
