__author__ = "James Gabriel <JamesCGabriel@gmail.com>"


import cash_flow
import budget
import random
import dates
import unittest


class TestCashFlow(unittest.TestCase):
    def setUp(self):
        random.seed(10)
        self.budget_name = "test_budget"

    def test_eom_expense(self):
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount)

        expense_amount = random.random() * 100
        expense = cash_flow.Expense(my_budget, "EOM expense", expense_amount)
        expense.on_day_end()
        self.assertEqual(my_budget.amount, starting_amount)

        expense.on_month_end()
        self.assertEqual(my_budget.amount, starting_amount - expense_amount)
        self.assertTrue(False)

    def test_eod_expense(self):
        date = dates.Date(4, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount, date)

        expense_amount = random.random() * 100
        expense = cash_flow.Expense(my_budget, "EOM expense", expense_amount, 5)
        expense.on_day_end()
        self.assertEqual(my_budget.amount, starting_amount)

        date.next()
        expense.on_day_end()
        self.assertEqual(my_budget.amount, starting_amount - expense_amount)

    def test_split_day_expense(self):
        date = dates.Date(4, "January", 2017)
        starting_amount = random.random() * 1000
        my_budget = budget.Budget(self.budget_name, starting_amount, date)

        expense_amount = random.random() * 100
        expense = cash_flow.Expense(my_budget, "EOM expense", expense_amount, [5, 6])
        expense.on_day_end()
        self.assertEqual(my_budget.amount, starting_amount)

        date.next()
        expense.on_day_end()
        self.assertAlmostEqual(my_budget.amount, starting_amount - expense_amount / 2)

        date.next()
        expense.on_day_end()
        self.assertAlmostEqual(my_budget.amount, starting_amount - expense_amount)

    def test_loan(self):
        principal = 100
        interest = .10
        length = 6
        name = "test_loan"
        monthly_payment = 17.156139418559246

        loan = cash_flow.Loan(name, principal, interest, length)
        self.assertAlmostEqual(loan._monthly_payment, monthly_payment)
        for n in range(length):
            self.assertAlmostEqual(loan.on_month_end(), monthly_payment)
        self.assertAlmostEqual(loan.on_month_end(), 0)


if __name__ == '__main__':
    unittest.main()
