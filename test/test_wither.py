import unittest

from pybok import ArgsConstructor, With


class TestWith(unittest.TestCase):

    def test_with(self):
        @With
        @ArgsConstructor
        class Person:
            name: str
            age: int
        
        person = Person("Jane", 19)
        same = person.with_name("Jane")
        another = person.with_age(21)
                
        self.assertEqual(person, same)
        self.assertNotEqual(person, another)
        

if __name__ == '__main__':
    unittest.main()
