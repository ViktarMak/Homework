# Task 4.7
# Implement a class Money to represent value and currency. You need to implement methods to use all basic arithmetics
# expressions (comparison, division, multiplication, addition and subtraction). Tip: use class attribute exchange rate
# which is dictionary and stores information about exchange rates to your default currency:

# exchange_rate = {
#    "EUR": 0.93,
#    "BYN": 2.1,
#    ...
# }

from functools import total_ordering


@total_ordering
class Money:

    exchange_rate = {"BYN": 1.00, "USD": 2.4226, "EUR": 2.8233, "RUR": 0.034363}

    def __init__(self, sum, currency):
        self.sum = float(sum)
        self.currency = currency
        self.sum_byn = self.sum * self.exchange_rate[self.currency]

    def __eq__(self, other):
        return self.sum_byn == other.sum_byn

    def __lt__(self, other):
        return self.sum_byn < other.sum_byn

    def __str__(self):
        return f"{self.sum} {self.currency}"

    def __add__(self, other):
        sum = round((self.sum_byn + other.sum_byn) / self.exchange_rate[self.currency], 2)
        return Money(sum, self.currency)

    def __radd__(self, other):
        if other == 0:
            return self

    def __mul__(self, other):
        mul = round((self.sum_byn * other) / self.exchange_rate[self.currency], 2)
        return Money(mul, self.currency)
