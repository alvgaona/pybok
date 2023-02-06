import unittest
import pytest
from pybok import Builder, ArgsConstructor, Getter, Setter, Data, Singleton, With, ToJSON, ToString, Copy


class TestOrder(unittest.TestCase):

    def test_order_1(self):
        @Setter
        @Getter
        @Builder
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person.builder().name("John").age(23).build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 23)

        person.name = "Jane"
        person.age = 19

        self.assertEqual(person.name, "Jane")
        self.assertEqual(person.age, 19)

    def test_order_2(self):
        @Builder
        @ArgsConstructor
        @Getter
        @Setter
        class Person:
            name: str
            age: int

        person = Person.builder().name("John").age(23).build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 23)

        person.name = "Jane"
        person.age = 19

        self.assertEqual(person.name, "Jane")
        self.assertEqual(person.age, 19)

    def test_order_3(self):
        @ArgsConstructor
        @Builder
        class Person:
            name: str
            age: int

        person = Person.builder().name("John").age(23).build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person._name, "John")
        self.assertEqual(person._age, 23)

    @pytest.mark.xfail(reason="Singleton failing")
    def test_order_4(self):
        @Singleton
        @Data
        @Builder
        class Person:
            name: str
            age: int

        person = Person.builder().name("John").age(23).build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person._name, "John")
        self.assertEqual(person._age, 23)

    @pytest.mark.xfail(reason="Builder does not support inheritance")
    def test_order_5(self):
        @ToString
        @ArgsConstructor
        class Human:
            height: str

        @ToString
        @Data
        @Builder
        @ToJSON
        @Copy
        @With
        class Person(Human):
            name: str
            age: int

        person = Person.builder().name("John").age(23).height("1.81m").build()

        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person._name, "John")
        self.assertEqual(person._age, 23)


if __name__ == '__main__':
    unittest.main()
