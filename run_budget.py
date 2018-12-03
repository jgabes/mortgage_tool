__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import budget
import budget_numbers

my_budget = budget.Budget(0, "<NAME> budget")
for income in budget_numbers.INCOMES:
    my_budget.register_income(*income)

for expense in budget_numbers.EXPENSES:
    my_budget.register_expenses(*expense)
