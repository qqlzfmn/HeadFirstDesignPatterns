#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author : 防暴队大盾
Blog   ：https://git.lzf.kim/
GitHub : https://github.com/qqlzfmn
Time   : 2018/7/17 8:45
"""


class Pizza(object):
    name = ""
    dough = ""
    sauce = ""
    toppings = []

    def get_name(self):
        return self.name

    def prepare(self):
        print("Preparing " + self.name)

    def bake(self):
        print("Baking " + self.name)

    def cut(self):
        print("Cutting " + self.name)

    def box(self):
        print("Boxing " + self.name)

    def __str__(self):
        display = []
        display.append("---- " + self.name + " ----")
        display.append(self.dough)
        display.append(self.sauce)
        for topping in self.toppings:
            display.append(topping)
        string = "\n".join(display) + "\n"
        return string


class CheesePizza(Pizza):
    def __init__(self):
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")


class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Grated parmesan cheese")


class ClamPizza(Pizza):
    def __init__(self):
        self.name = "Clam Pizza"
        self.dough = "Thin crust"
        self.sauce = "White garlic sauce"
        self.toppings.append("Clams")
        self.toppings.append("Grated parmesan cheese")


class VeggiePizza(Pizza):
    def __init__(self):
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.append("Shredded mozzarella")
        self.toppings.append("Grated parmesan")
        self.toppings.append("Diced onion")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")


class SimplePizzaFactory(object):
    @staticmethod
    def create_pizza(type):
        pizza = None

        if type == "cheese":
            pizza = CheesePizza()
        elif type == "pepperoni":
            pizza = PepperoniPizza()
        elif type == "clam":
            pizza = ClamPizza()
        elif type == "veggie":
            pizza = VeggiePizza()
        return pizza


class PizzaStore(object):
    factory = SimplePizzaFactory()

    def __init__(self, factory):
        self.factory = factory

    def order_pizza(self, type):
        pizza = self.factory.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__ == '__main__':
    factory = SimplePizzaFactory()
    store = PizzaStore(factory)

    pizza = store.order_pizza("cheese")
    print("We ordered a " + pizza.get_name() + "\n")
    print(pizza)

    pizza = store.order_pizza("veggie")
    print("We ordered a " + pizza.get_name() + "\n")
    print(pizza)
