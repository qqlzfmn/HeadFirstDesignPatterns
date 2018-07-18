class Beverage(object):
    description = "Unknown Beverage"
    TALL = 1
    GRANDE = 2
    VENTI = 3
    size = GRANDE

    def get_description(self):
        return self.description

    def get_size(self):
        return self.size

    def set_size(self, size=GRANDE):
        self.size = size

    def cost(self):
        pass


class CondimentDecorator(Beverage):
    def get_description(self):
        pass


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return .99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"

    def cost(self):
        return 1.05


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99


class Milk(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        if self.beverage.get_size() == self.beverage.TALL:
            return .05 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.GRANDE:
            return .10 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.VENTI:
            return .15 + self.beverage.cost()


class Mocha(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        if self.beverage.get_size() == self.beverage.TALL:
            return .15 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.GRANDE:
            return .20 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.VENTI:
            return .25 + self.beverage.cost()


class Soy(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        if self.beverage.get_size() == self.beverage.TALL:
            return .10 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.GRANDE:
            return .15 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.VENTI:
            return .20 + self.beverage.cost()


class Whip(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        if self.beverage.get_size() == self.beverage.TALL:
            return .05 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.GRANDE:
            return .10 + self.beverage.cost()
        elif self.beverage.get_size() == self.beverage.VENTI:
            return .15 + self.beverage.cost()


if __name__ == '__main__':
    b4 = Decaf()
    b4.set_size(b4.VENTI)
    b4 = Mocha(b4)
    print("Venti %s $%s" % (b4.get_description(), b4.cost()))

    b5 = Decaf()
    b5.set_size(b5.TALL)
    b5 = Mocha(b5)
    print("Tall %s $%s" % (b5.get_description(), b5.cost()))
