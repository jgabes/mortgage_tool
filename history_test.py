import unittest
import budget
import random


class TestDates(unittest.TestCase):

    def setUp(self):
        random.seed(10)
        self.budget = budget.Budget("test_budget", 100)
