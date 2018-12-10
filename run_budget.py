__author__ = "James Gabriel <JamesCGabriel@gmail.com>"

import budget
import start_numbers
import dates
import plotter
import cash_flow


present_day = dates.Date(1, "January", 2019)

my_budget = budget.Budget(0, "<NAME> budget", present_day)
for income in start_numbers.INCOMES:
    my_budget.register_income(cash_flow.Income(*income))

for expense in start_numbers.EXPENSES:
    my_budget.register_expenses(expense)

my_budget.step(years=1)
plotter.plot_budget(my_budget)
