import cash_flow


class Property:

    def __init__(self, name, budget, initial_value, appreciation=None,
                 financing: cash_flow.Loan = None):
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
