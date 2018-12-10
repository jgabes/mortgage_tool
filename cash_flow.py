__author__ = "James Gabriel <JamesCGabriel@gmail.com>"


import budget


class CashFlow:
    """CashFlow callback object which can add or remove money to to budget"""

    def __init__(self, member_budget: budget.Budget, name, amount):
        self._budget = member_budget
        self._name = name
        self._amount = amount
        if amount < 0:
            raise ValueError("Amounts should always be positive. You entered {}".format(amount))

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    def on_day_end(self):
        return

    def on_month_end(self):
        return


class Expense(CashFlow):

    def __init__(self, member_budget, name: str, amount, execution_days=None):
        super().__init__(member_budget, name, amount)
        self._execution_days = execution_days
        self._budget.register_expenses(self)

    def on_day_end(self):
        if self._execution_days is not None:
            if isinstance(self._execution_days, int):
                if self._budget.date.day == self._execution_days:
                    self._budget.withdraw(self._amount)
            if isinstance(self._execution_days, list):
                if self._budget.date.day in self._execution_days:
                    self._budget.withdraw(
                        self._amount / len(self._execution_days))

    def on_month_end(self):
        if self._execution_days is None:
            self._budget.withdraw(self._amount)


class Income(CashFlow):

    def __init__(self, member_budget, name: str, amount, execution_days):
        super().__init__(member_budget, name, amount)
        self._execution_days = execution_days
        self._budget.register_income(self)

    def on_day_end(self):
        if self._execution_days is not None:
            if isinstance(self._execution_days, int):
                if self._budget.date.day == self._execution_days:
                    self._budget.deposit(self._amount)
            if isinstance(self._execution_days, list):
                if self._budget.date.day in self._execution_days:
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
