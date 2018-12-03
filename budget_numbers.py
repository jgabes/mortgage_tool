INCOMES = [[1000000 / 12, "Salary 1", (15, 28)], [1000000 / 12, "Salary 2"]]
EXPENSES = [[10000, "Rent"], [2, "Internet"], [2000, "Food"]]

HOUSE_VALUE = 500000

DOWN_PAYMENT = .2

INTEREST_RATE = 0.03

MORTGAGE_LENGTH = 30

ESTIMATED_HOME_APPRECIATION = 0.06

principle = HOUSE_VALUE * (1 - DOWN_PAYMENT)
num_payments = 12 * MORTGAGE_LENGTH
monthly_rate = INTEREST_RATE / 12

monthly_payment = principle * (monthly_rate *
                               (1 + monthly_rate)**num_payments) / (
                                   (1 + monthly_rate)**num_payments - 1)
