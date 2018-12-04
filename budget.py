__author__ = "James Gabriel <JamesCGabriel@gmail.com>"


class Budget:
    """Budget object which keeps a running tally of all the money"""

    def __init__(self, name, starting_amount):
        self._name = name
        self._cash = starting_amount
        self._incomes = []
        self._expenses = []
        self._properties = []
        self._taxes = 0

    @property
    def amount(self):
        return self._cash

    @property
    def name(self):
        return self._name

    def deposit(self, other):
        self._cash += other

    def withdraw(self, other):
        self._cash -= other

    def register_expenses(self, expense):
        self._expenses.append(expense)

    def register_income(self, income):
        self._incomes.append(income)

    def register_property(self, property):
        self._properties.append(property)
        self.deposit(property.value)

    def on_month_end(self):
        for income in self._incomes:
            income.on_month_end()
        for expense in self._expenses:
            expense.on_month_end()
        for property in self._properties:
            property.on_month_end()


class CashFlow:
    """CashFlow callback object which can add or remove money to to budget"""

    def __init__(self, budget: Budget, name, amount):
        self._budget = budget
        self._name = name
        self._amount = amount

    @property
    def name(self):
        return self._name

    def on_day_end(self, date):
        return

    def on_month_end(self):
        return


class Expense(CashFlow):

    def __init__(self, budget: Budget, name: str, amount, execution_days=None):
        super().__init__(budget, name, amount)
        self._execution_days = execution_days
        self._budget.register_expenses(self)

    def on_day_end(self, date):
        if self._execution_days is not None:
            if isinstance(self._execution_days, int):
                if date.day == self._execution_days:
                    self._budget.withdraw(self._amount)
            if isinstance(self._execution_days, list):
                if date.day in self._execution_days:
                    self._budget.withdraw(
                        self._amount / len(self._execution_days))

    def on_month_end(self):
        if self._execution_days is None:
            self._budget.withdraw(self._amount)


class Income(CashFlow):

    def __init__(self, budget: Budget, name: str, amount, execution_days):
        super().__init__(budget, name, amount)
        self._execution_days = execution_days
        self._budget.register_income(self)

    def on_day_end(self, date):
        if self._execution_days is not None:
            if isinstance(self._execution_days, int):
                if date.day == self._execution_days:
                    self._budget.deposit(self._amount)
            if isinstance(self._execution_days, list):
                if date.day in self._execution_days:
                    self._budget.deposit(
                        self._amount / len(self._execution_days))

    def on_month_end(self):
        if self._execution_days is None:
            self._budget.deposit(self._amount)


class Loan(CashFlow):
    """Morgage is a CashFlow but it keeps its own internal state"""

    def __init__(self, name, principal, interest, length):
        """
        Args:
            name: name of the loan
            principal: amount of loan in dollars
            interest: yearly interest rate (APR) 10% = 0.10
            length: length of loan in months
        """
        self._name = name
        num_payments = length
        monthly_rate = interest / 12

        self._monthly_payment = principal * (monthly_rate *
                                             (1 + monthly_rate) ** num_payments) / (
                                        (1 + monthly_rate) ** num_payments - 1)
        self._months_remaining = num_payments

    @property
    def name(self):
        return self._name

    @property
    def monthly_payment(self):
        return self._monthly_payment

    @property
    def amount_remaining(self):
        return self._monthly_payment * self._months_remaining

    def on_month_end(self):
        if self._months_remaining > 0:
            self._months_remaining -= 1
            return self._monthly_payment
        else:
            return 0


class Property:

    def __init__(self, name, budget: Budget, initial_value, appreciation=None,
                 financing: Loan = None):
        """
        Args:
            budget: budget object this property will be attached to
            name: name of the property
            initial_value: starting value of the property
            appreciation: (can be negative) expected price change over a year (10%=0.10)
            financing: if there is a loan attached to the purchase
        """
        self._name = name
        self._budget = budget
        self._value = initial_value
        self._appreciation = appreciation
        self._financing = financing

        self._budget.register_property(self)

    def on_month_end(self):
        value_diff = self._value * self._appreciation / 12
        self._value += value_diff
        self._budget.deposit(value_diff)
        if self._financing is not None:
            self._budget.withdraw(self._financing.on_month_end())

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value
