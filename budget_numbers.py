INCOMES = [[1000000 / 12, "Salary 1", (15, 28)], [1000000 / 12, "Salary 2"]]
EXPENSES = [[10000, "Rent"], [2, "Internet"], [2000, "Food"]]

HOUSE_VALUE = 100

DOWN_PAYMENT = 0

INTEREST_RATE = 0.1

ESTIMATED_HOME_APPRECIATION = 0.06

MORTGAGE_LENGTH = .5


principle = HOUSE_VALUE * (1 - DOWN_PAYMENT)
num_payments = 12 * MORTGAGE_LENGTH
monthly_rate = INTEREST_RATE / 12

monthly_payment = principle * (monthly_rate *
                               (1 + monthly_rate)**num_payments) / (
                                   (1 + monthly_rate)**num_payments - 1)

pass
