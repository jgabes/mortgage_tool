__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import random
import unittest

import budget
import dates


class TestBudgets(unittest.TestCase):

    def setUp(self):
        random.seed(10)
        self.budget_name = "test_budget"

    def test_budget(self):
        """
        Test:
            -budgets can be created with correct
            -sums can be added and withdrawn from a budget
        """
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount)
        deposit = random.random() * 100
        withdraw = random.random() * 100

        my_budget.deposit(deposit)
        self.assertEqual(my_budget.amount, starting_amount + deposit)

        my_budget.withdraw(withdraw)
        self.assertEqual(my_budget.amount,
                         starting_amount + deposit - withdraw)

    def test_step(self):
        """
        Test:
            -Test that date math works when stepping through budgets
        """
        day = 15
        month = "January"
        year = 2000
        date = dates.Date(day, month, year)
        my_budget = budget.Budget(self.budget_name, date=date)
        my_budget.step(days=1)
        new_date = my_budget.date
        self.assertEqual(new_date.day, day + 1)
        self.assertEqual(new_date.month, month)

        my_budget.step(days=10, months=6)
        new_date = my_budget.date
        self.assertEqual(new_date.day, day + 11)
        self.assertEqual(new_date.month, "July")

        my_budget.step(days=1, months=6, years=1)
        new_date = my_budget.date
        self.assertEqual(new_date.day, day + 12)
        self.assertEqual(new_date.month, "January")
        self.assertEqual(new_date.year, year + 2)


if __name__ == '__main__':
    unittest.main()
