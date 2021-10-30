# Task 6.1
# Implement a Counter class which optionally accepts the start value and the counter stop value. If the start value is
# not specified the counter should begin with 0. If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."

# Implement to methods: "increment" and "get"
# If you are familiar with Exception rising use it to display the "Maximal value is reached." message.


class Counter:

    def __init__(self, start: int = 0, stop: int = None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start >= self.stop and self.stop is not None:
            raise Exception("Maximal value is reached.")
        else:
            self.start += 1

    def get(self):
        print(self.start)
