
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


turn_off = False

while not turn_off:
    options = menu.get_items()
    drink = input(f"What would you like? ({options})\n").lower()
    if drink == "off":
        turn_off = True
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_item = menu.find_drink(drink)
        if drink_item:
            if coffee_maker.is_resource_sufficient(drink_item):
                if money_machine.make_payment(drink_item.cost):
                    coffee_maker.make_coffee(drink_item)