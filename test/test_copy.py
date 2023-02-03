import unittest
import pytest

from pybok import Copy, ArgsConstructor


class TestCopy(unittest.TestCase):
    def test_copy(self):
        @ArgsConstructor
        class Eyes:
            color: str

        @Copy
        @ArgsConstructor
        class Person:
            name: str
            age: int
            eyes: Eyes  

        person = Person("Jane", 19, Eyes("blue"))

        shallow_copy = person.copy()

        self.assertEqual(person._name, shallow_copy._name)
        self.assertEqual(person._age, shallow_copy._age)
        self.assertEqual(person._eyes, shallow_copy._eyes)

    def test_deepcopy(self):
        @ArgsConstructor
        class Eyes:
            color: str

        @Copy
        @ArgsConstructor
        class Person:
            name: str
            age: int
            eyes: Eyes  
            
        person = Person("Jane", 19, Eyes("blue"))

        deep_copy = person.deepcopy()    

        self.assertEqual(person._name, deep_copy._name)
        self.assertEqual(person._age, deep_copy._age)
        self.assertNotEqual(person._eyes, deep_copy._eyes)
        

if __name__ == '__main__':
    unittest.main()
