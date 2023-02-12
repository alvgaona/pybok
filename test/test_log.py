import unittest

from pybok import ArgsConstructor, Log


class TestLog(unittest.TestCase):
    def test_log(self):
        @Log
        @ArgsConstructor
        class Person:
            name: str
            age: int

        @Log
        @ArgsConstructor
        class Cat:
            name: str
            age: int

        person = Person("Jane", 19)
        cat = Cat("Tom", 8)
        
        self.assertEqual(person.logger, cat.logger)        
        

if __name__ == '__main__':
    unittest.main()
