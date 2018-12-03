__author__ = "James Gabriel <JamesCGabriel@gmail.com>"


class Budget:
    """Budget object which keeps a running tally of all the money"""

    def __init__(self, starting_amount):
        self._cash = starting_amount

    @property
    def amount(self):
        return self._cash

    def deposit(self, other):
        self._cash += other

    def withdraw(self, other):
        self._cash -= other


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

    def on_day_end(self, date):
        if self._execution_days is not None:
            if isinstance(self._execution_days, int):
                if date.day == self._execution_days:
                    self._budget.withdraw(self._amount)
            if isinstance(self._execution_days, list):
                if date.day in self._execution_days:
                    self._budget.withdraw(self._amount / len(self._execution_days))

    def on_month_end(self):
        if self._execution_days is None:
            self._budget.withdraw(self._amount)


class Income(CashFlow):
    def __init__(self, budget: Budget, name: str, amount, execution_days):
        super().__init__(budget, name, amount)
        self._execution_days = execution_days

    def on_day_end(self, date):
        if self._execution_days is not None:
            if isinstance(self._execution_days, int):
                if date.day == self._execution_days:
                    self._budget.deposit(self._amount)
            if isinstance(self._execution_days, list):
                if date.day in self._execution_days:
                    self._budget.deposit(self._amount / len(self._execution_days))

    def on_month_end(self):
        if self._execution_days is None:
            self._budget.deposit(self._amount)


class Morgage(CashFlow):
    """Morgage is a CashFlow but it keeps its own internal state"""

    def __init__(self):
        pass
