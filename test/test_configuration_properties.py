import os
import unittest

import pytest

from pybok import ConfigurationProperties, Singleton


class TestConfigurationProperties(unittest.TestCase):
    DAY = 'DAY'
    MONTH = 'MONTH'
    YEAR = 'YEAR'

    def tearDown(self) -> None:
        if self.DAY in os.environ:
            del os.environ[self.DAY]

        if self.MONTH in os.environ:
            del os.environ[self.MONTH]

        if self.YEAR in os.environ:
            del os.environ['YEAR']

    def test_default(self):
        os.environ[self.DAY] = "1"
        os.environ[self.MONTH] = "10"
        os.environ[self.YEAR] = "1991"

        @ConfigurationProperties
        class MyProps:
            day: int
            month: int
            year: int

        myprops = MyProps()

        self.assertEqual(myprops._day, "1")
        self.assertEqual(myprops._month, "10")
        self.assertEqual(myprops._year, "1991")

    def test_optional_values(self):
        os.environ[self.DAY] = "1"
        os.environ[self.MONTH] = "10"

        @ConfigurationProperties
        class MyProps:
            day: str
            month: str
            year: str = '1991'

        myprops = MyProps()

        self.assertEqual(myprops._day, "1")
        self.assertEqual(myprops._month, "10")
        self.assertEqual(myprops._year, "1991")

    def test_missing_required_arg(self):
        os.environ['MONTH'] = "10"
        os.environ[self.YEAR] = "1991"

        with pytest.raises(ValueError) as e:
            @ConfigurationProperties
            class MyProps:
                day: int
                month: int
                year: int

        self.assertEqual(str(e.value), "DAY is required.")
    
    def test_singleton(self):
        os.environ[self.DAY] = "1"
        os.environ[self.MONTH] = "10"
        os.environ[self.YEAR] = "1991"

        @Singleton
        @ConfigurationProperties
        class MyProps:
            day: int
            month: int
            year: int

        myprops = MyProps()

        self.assertEqual(myprops._day, "1")
        self.assertEqual(myprops._month, "10")
        self.assertEqual(myprops._year, "1991")

        my_other_props = MyProps()

        self.assertEqual(myprops, my_other_props)


if __name__ == '__main__':
    unittest.main()
