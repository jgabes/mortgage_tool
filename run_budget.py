__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import budget
import budget_numbers
import dates

present_day = dates.Date(1, "January", 2019)


my_budget = budget.Budget(0, "<NAME> budget", present_day)
for income in budget_numbers.INCOMES:
    my_budget.register_income(*income)

for expense in budget_numbers.EXPENSES:
    my_budget.register_expenses(*expense)


