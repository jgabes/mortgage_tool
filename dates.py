__author__ = "James Gabriel <JamesCGabriel@gmail.com>"
import collections
import datetime

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

    @classmethod
    def today(cls):
        d = datetime.date.today()
        return cls(d.day,
                   list(MONTHS.keys())[d.month - 1],
                   d.year)

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def next(self):

        if self.eom:
            if self.eoy:
                self._month = "January"
                self._year += 1
                self._day = 1
            else:
                months = list(MONTHS.keys())
                for i, v in enumerate(months):
                    if v == self._month:
                        self._month = months[i + 1]
                        self._day = 1
                        break
        else:
            self._day += 1

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @property
    def eom(self):
        if self._day == MONTHS[self.month]:
            return True
        else:
            return False

    @property
    def eoy(self):
        if self.eom and self._month == "December":
            return True
        else:
            return False
