__author__ = "James Gabriel <JamesCGabriel@gmail.com>"
import collections

MONTHS = collections.OrderedDict([
    ("January", 31),
    ("February", 28),
    ("March", 31),
    ("April", 30),
    ("June", 30),
    ("May", 31),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)]
)


class Date:
    """Wrapper for the date"""

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def next(self):
        self._day += 1
        if self._day > MONTHS[self._month]:
            self._day = 1
            if self._month == "December":
                self._month = "January"
                self._year += 1
            else:
                months = list(MONTHS.keys())
                for i, v in enumerate(months):
                    if v == self._month:
                        self._month = months[i + 1]
                        break

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year
