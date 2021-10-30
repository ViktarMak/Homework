# Task 4.6
# A singleton is a class that allows only a single instance of itself to be created and gives access to that created
# instance. Implement singleton logic inside your custom class using a method to initialize class instance.

# Example:
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True


class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance:
            print("The instance is already exists:", self)

    @classmethod
    def inst(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


p = Singleton.inst()
f = Singleton.inst()
print(p is f)
