from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True
while is_on:
    item = (input(f"What would you like to have? {menu.get_items()}")).lower()
    if item == "report":
        coffee_maker.report()
        money_machine.report()
    elif item == "off":
        is_on = False
    else:
        drink = menu.find_drink(item)
        cost = drink.cost
        print(f"{item} costs {cost}")
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost):
            coffee_maker.make_coffee(drink)


