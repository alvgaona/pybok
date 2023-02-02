import unittest

from pybok import Data


class TestData(unittest.TestCase):

    def test_default(self):
        @Data
        class Person:
            name: str
            age: int

        p1 = Person("John", 21)

        self.assertEqual(str(p1), 'Person(name=John,age=21)')

        self.assertEqual(p1.get_name(), "John")
        self.assertEqual(p1.get_age(), 21)

        self.assertEqual(hash(p1), hash((p1._name, p1._age)))

        p2 = Person("Jane", 19)

        self.assertNotEqual(p1, p2)
        self.assertEqual(p1, p1)

        p1.set_name("Mike")
        p1.set_age(28)

        self.assertEqual(p1._name, "Mike")
        self.assertEqual(p1._age, 28)


if __name__ == '__main__':
    unittest.main()
