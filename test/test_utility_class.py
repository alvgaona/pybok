import unittest

import pytest

from pybok import UtilityClass


class TestUtilityClass(unittest.TestCase):

    def test_utility_class(self):
        @UtilityClass
        class MyClass:
            def greet():
                return 'Hi, Stranger!'
            
        
        with pytest.raises(NotImplementedError) as e:
            MyClass()

        self.assertEqual(str(e.value), 'This is a utility class and cannot be instantiated')
        self.assertEqual(MyClass.greet(), 'Hi, Stranger!')


if __name__ == '__main__':
    unittest.main()
