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
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount)
        deposit = random.random() * 100
        withdraw = random.random() * 100

        my_budget.deposit(deposit)
        self.assertEqual(my_budget.amount, starting_amount + deposit)

        my_budget.withdraw(withdraw)
        self.assertEqual(my_budget.amount,
                         starting_amount + deposit - withdraw)

    def test_eom_expense(self):
        date = dates.Date(5, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount)

        expense_amount = random.random() * 100
        expense = budget.Expense(my_budget, "EOM expense", expense_amount)
        expense.on_day_end(date)
        self.assertEqual(my_budget.amount, starting_amount)

        expense.on_month_end()
        self.assertEqual(my_budget.amount, starting_amount - expense_amount)

    def test_eod_expense(self):
        date = dates.Date(4, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount)

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
        my_budget = budget.Budget(self.budget_name, starting_amount)

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

    def test_loan(self):
        principal = 100
        interest = .10
        length = 6
        name = "test_loan"
        monthly_payment = 17.156139418559246

        loan = budget.Loan(name, principal, interest, length)
        self.assertAlmostEqual(loan._monthly_payment, monthly_payment)
        for n in range(length):
            self.assertAlmostEqual(loan.on_month_end(), monthly_payment)
        self.assertAlmostEqual(loan.on_month_end(), 0)

    def test_cash_property(self):
        my_budget = budget.Budget(self.budget_name, 100)
        initial_value = 100
        appreciation = 0.5
        property = budget.Property("cash house", my_budget, initial_value, appreciation)
        self.assertEqual(my_budget.amount, 100 + initial_value)

        my_budget.on_month_end()
        delta = appreciation / 12 * initial_value
        self.assertEqual(property.value, initial_value + delta)
        self.assertEqual(my_budget.amount, 100 + initial_value + delta)

    def test_financed_property(self):
        my_budget = budget.Budget(self.budget_name, 100)

        principal = 100
        interest = .10
        length = 6
        name = "test_loan"
        loan = budget.Loan(name, principal, interest, length)

        initial_value = 100
        appreciation = 0.5
        property = budget.Property("cash house", my_budget, initial_value, appreciation, loan)
        self.assertEqual(my_budget.amount, 100 + initial_value)

        my_budget.on_month_end()
        delta = appreciation / 12 * initial_value
        self.assertEqual(property.value, initial_value + delta)
        self.assertEqual(my_budget.amount, 100 + initial_value + delta - loan.monthly_payment)


if __name__ == '__main__':
    unittest.main()
