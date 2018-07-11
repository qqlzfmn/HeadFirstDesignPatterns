class FlyBehavior(object):
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior(object):
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<<Silence>>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class Duck(object):
    fly_behavior = FlyBehavior()
    quack_behavior = QuackBehavior()

    def __init__(self):
        pass

    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    @staticmethod
    def swim():
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()
