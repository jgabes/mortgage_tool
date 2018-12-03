__author__ = "James Gabriel <JamesCGabriel@gmail.com>"


class Budget():
    """Budget object which keeps a running tally of all the money"""

    def __init__(self):
        pass


class CashFlow:
    """CashFlow callback object which can add or remove money to to budget"""

    def __init__(self, budget: Budget, name):
        self._budget = budget
        self._name = name

    @property
    def name(self):
        return self._name

    def on_day_end(self, date):
        return

    def on_month_end(self, date):
        return


class Expense(CashFlow):
    def __init__(self, budget: Budget, name: str):
        super().__init__(budget, name)


class Income(CashFlow):
    def __init__(self, budget: Budget, name: str):
        super().__init__(budget, name)


class Morgage(CashFlow):
    """Morgage is a CashFlow but it keeps its own internal state"""

    def __init__(self):
        pass
