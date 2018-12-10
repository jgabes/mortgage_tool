import collections
import budget


class History:
    def __init__(self, start_date, reference_budget: budget.Budget):
        self._budget = reference_budget
        self._history = collections.OrderedDict()
        self._history[start_date] = self._budget.amount

    def update(self):
        if self._budget.date in self._history:
            raise ValueError("This day is already recorded")
        else:
            self._history[self._budget.date] = self._budget.amount
