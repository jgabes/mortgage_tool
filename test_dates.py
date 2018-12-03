__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import unittest
import dates
import random


class TestDates(unittest.TestCase):
    def setUp(self):
        random.seed(10)

    def test_normal_day_next(self):
        pas
        day = random.randint(5, 20)
        month = random.choice(list(dates.MONTHS.keys()))
        year = random.randint(1980, 2018)
        my_date = dates.Date(day, month, year)
        my_date.next()
        self.assertEqual(my_date.day, day + 1)
        self.assertEqual(my_date.month, month)
        self.assertEqual(my_date.year, year)

    def test_month_roll(self):
        months = list(dates.MONTHS.keys())
        for i, month in enumerate(months[:-1]):
            day = dates.MONTHS[month]
            year = random.randint(1980, 2018)
            my_date = dates.Date(day, month, year)
            my_date.next()
            self.assertEqual(my_date.day, 1)
            self.assertEqual(my_date.month, months[i+1])
            self.assertEqual(my_date.year, year)


if __name__ == '__main__':
    unittest.main()
