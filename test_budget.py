__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import random
import unittest

import budget
import dates


class TestBudgets(unittest.TestCase):

    def setUp(self):
        random.seed(10)

    def test_budget(self):
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(starting_amount)
        deposit = random.random() * 100
        withdrawl = random.random() * 100

        my_budget.deposit(deposit)
        self.assertEqual(my_budget.amount, starting_amount + deposit)

        my_budget.withdraw(withdrawl)
        self.assertEqual(my_budget.amount,
                         starting_amount + deposit - withdrawl)

    def test_eom_expense(self):
        date = dates.Date(5, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(starting_amount)

        expense_amount = random.random() * 100
        expense = budget.Expense(my_budget, "EOM expense", expense_amount)
        expense.on_day_end(date)
        self.assertEqual(my_budget.amount, starting_amount)

        expense.on_month_end()
        self.assertEqual(my_budget.amount, starting_amount - expense_amount)

    def test_on_day_expense(self):
        date = dates.Date(4, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(starting_amount)

        expense_amount = random.random() * 100
        expense = budget.Expense(my_budget, "EOM expense", expense_amount, 5)
        expense.on_day_end(date)
        self.assertEqual(my_budget.amount, starting_amount)

        date.next()
        expense.on_day_end(date)
        self.assertEqual(my_budget.amount, starting_amount - expense_amount)

    def test_split_day_expense(self):
        date = dates.Date(4, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(starting_amount)

        expense_amount = random.random() * 100
        expense = budget.Expense(my_budget, "EOM expense", expense_amount, [5, 6])
        expense.on_day_end(date)
        self.assertEqual(my_budget.amount, starting_amount)

        date.next()
        expense.on_day_end(date)
        self.assertAlmostEqual(my_budget.amount, starting_amount - expense_amount / 2)

        date.next()
        expense.on_day_end(date)
        self.assertAlmostEqual(my_budget.amount, starting_amount - expense_amount)


if __name__ == '__main__':
    unittest.main()
