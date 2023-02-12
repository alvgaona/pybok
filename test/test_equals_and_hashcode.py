import unittest

from pybok import ArgsConstructor, EqualsAndHashCode


class TestEqualsAndHashCode(unittest.TestCase):

    def test_methods(self):
        @EqualsAndHashCode
        @ArgsConstructor
        class Person:
            name: str
            age: int

        p1 = Person("John", 21)

        self.assertEqual(hash(p1), hash((p1._name, p1._age)))

        p2 = Person("Jane", 19)

        self.assertNotEqual(p1, p2)
        self.assertEqual(p1, p1)


if __name__ == '__main__':
    unittest.main()
