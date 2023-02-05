import unittest
from pybok import Builder, ArgsConstructor, Getter, Setter


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
        self.assertEqual(person.get_name(), "John")
        self.assertEqual(person.get_age(), 23)

        person.set_name("Jane")
        person.set_age(19)

        self.assertEqual(person.get_name(), "Jane")
        self.assertEqual(person.get_age(), 19)

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
        self.assertEqual(person.get_name(), "John")
        self.assertEqual(person.get_age(), 23)

        person.set_name("Jane")
        person.set_age(19)

        self.assertEqual(person.get_name(), "Jane")
        self.assertEqual(person.get_age(), 19)

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


if __name__ == '__main__':
    unittest.main()
