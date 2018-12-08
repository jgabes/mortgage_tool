__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import unittest
import dates
import random


class TestDates(unittest.TestCase):
    def setUp(self):
        random.seed(10)

    def test_normal_day_next(self):
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
            self.assertEqual(my_date.month, months[i + 1])
            self.assertEqual(my_date.year, year)

    def test_year_roll(self):
        month = "December"
        day = 31
        year = random.randint(1980, 2018)
        my_date = dates.Date(day, month, year)
        my_date.next()
        self.assertEqual(my_date.day, 1)
        self.assertEqual(my_date.month, "January")
        self.assertEqual(my_date.year, year + 1)

    def test_eom(self):
        for month, length in dates.MONTHS.items():
            for day in range(1, length + 1):
                date = dates.Date(day, month, 1990)
                if date.day == length:
                    self.assertTrue(date.eom)
                else:
                    self.assertFalse(date.eom)

    def test_eoy(self):
        for month, length in dates.MONTHS.items():
            for day in range(1, length + 1):
                date = dates.Date(day, month, 1990)
                if date.day == dates.MONTHS["December"] and date.month == "December":
                    self.assertTrue(date.eoy)
                else:
                    self.assertFalse(date.eoy)


if __name__ == '__main__':
    unittest.main()
