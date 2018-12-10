__author__ = "James Gabriel <JamesCGabriel@gmail.com>"
import dates
import history


class Budget:
    """Budget object which keeps a running tally of all the money"""

    def __init__(self, name, starting_amount=0, date=dates.Date.today()):
        self._name = name
        self._cash = starting_amount
        self._incomes = []
        self._expenses = []
        self._properties = []
        self._taxes = 0
        self._date = date
        self._pre_tax_income = 0
        self._pre_tax_expenses = 0
        self._history = history.History(self._date, self)

    def step(self, days=0, months=0, years=0):
        for y in range(years):
            self._step_year()

        for m in range(months):
            self._step_month()

        for d in range(days):
            self._step_day()

    def _step_year(self):
        day = self._date.day
        month = self._date.month
        self._step_day()
        while day != self._date.day or month != self._date.month:
            self._step_day()

    def _step_month(self):
        day = self._date.day
        self._step_day()
        while day != self._date.day:
            self._step_day()

    def _step_day(self):
        self._history.update()
        eom = self._date.eom
        self.on_day_end()
        if eom:
            self.on_month_end()
        self._date.next()

    @property
    def amount(self):
        return self._cash

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def history(self):
        return self._history

    def deposit(self, other):
        self._cash += other

    def withdraw(self, other):
        self._cash -= other

    def register_expenses(self, expense):
        self._expenses.append(expense)
        self._pre_tax_expenses += expense.amount

    def register_income(self, income):
        self._incomes.append(income)
        self._pre_tax_income += income.amount

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

    def on_day_end(self):
        for income in self._incomes:
            income.on_day_end()
        for expense in self._expenses:
            expense.on_day_end()
