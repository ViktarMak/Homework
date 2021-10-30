# Task 4.2
# Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys.

# Example:
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]


class HistoryDict:

    def __init__(self, mydict=None):
        if mydict is None:
            mydict = {}
        self.__mydict = mydict
        self.__history = []

    def set_value(self, key, value):
        if key in self.__history:
            if self.__mydict[key] != value:
                self.__history.remove(key)
                self.__history.append(key)
        else:
            self.__history.append(key)
        if len(self.__history) > 10:
            del self.__history[0]
        self.__mydict[key] = value

    def get_history(self):
        return self.__history
