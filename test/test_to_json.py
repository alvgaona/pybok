import unittest
import json

from pybok import ToJSON, ArgsConstructor


class TestToJSON(unittest.TestCase):

    def test_json(self):
        @ToJSON
        @ArgsConstructor
        class Person:
            name: str
            age: int

        person = Person("John", 21)

        expected = {
            "name": "John",
            "age": 21
        }

        self.assertEqual(person.json(), json.dumps(expected, indent=4))

    def test_nested_json_objects(self):
        @ArgsConstructor
        class Eyes:
            color: str

        @ToJSON
        @ArgsConstructor
        class Person:
            name: str
            age: int
            eyes: Eyes

        person = Person("John", 21, Eyes("blue"))

        expected = {
            "name": "John",
            "age": 21,
            "eyes": {
                "color": "blue"
            }
        }

        self.assertEqual(person.json(), json.dumps(expected, indent=4))

    def test_nested_json_lists(self):
        @ArgsConstructor
        class Shirt:
            color: str

        @ToJSON
        @ArgsConstructor
        class Person:
            name: str
            age: int
            shirts: list[Shirt]

        person = Person("John", 21, [Shirt("blue"), Shirt("black"), Shirt("white")])

        expected = {
            "name": "John",
            "age": 21,
            "shirts": [
                {
                    "color": "blue"
                },
                {
                    "color": "black"
                },
                {
                    "color": "white"
                }
            ]
        }

        self.assertEqual(person.json(), json.dumps(expected, indent=4))


if __name__ == '__main__':
    unittest.main()
