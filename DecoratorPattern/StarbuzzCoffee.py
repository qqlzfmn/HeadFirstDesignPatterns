class Beverage(object):
    description = "Unknown Beverage"

    def get_description(self):
        return self.description

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

    def cost(self):
        return .10 + self.beverage.cost()


class Mocha(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return .20 + self.beverage.cost()


class Soy(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return .15 + self.beverage.cost()


class Whip(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return .10 + self.beverage.cost()


if __name__ == '__main__':
    beverage = Espresso()
    print("%s $%s" % (beverage.get_description(), beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print("%s $%s" % (beverage2.get_description(), beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print("%s $%s" % (beverage3.get_description(), beverage3.cost()))
