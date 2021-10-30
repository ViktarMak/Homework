# Task 4.4
# Create hierarchy out of birds. Implement 4 classes:

# class Bird with an attribute name and methods fly and walk.
# class FlyingBird with attributes name, ration, and with the same methods. ration must have default value.
# Implement the method eat which will describe its typical ration.
# class NonFlyingBird with same characteristics but which obviously without attribute fly. Add same "eat" method but
# with other implementation regarding the swimming bird tastes.
# class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
# Implement str() function call for each class.


class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk "

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.ration = 'grain'

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird:
    def __init__(self, name, ration='fish'):
        self.ration = ration
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk "

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


if __name__ == '__main__':
    s = SuperBird("cormorant")
    print(str(s))
    print(s.eat())
    print(s.swim())
