__author__ = "James Gabriel <JamesCGabriel@gmail.com>"


import budget

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
