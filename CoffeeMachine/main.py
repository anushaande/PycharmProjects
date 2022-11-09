# TODO create a menu of coffee as a list of dictionaries
# TODO create a list of coins and the coin value in dollars
# TODO For each menu item mention the requirements and the price of that item.
# TODO take user input for item.
# TODO Write a function to check if there are enough resources for the item requested.
# TODO If there are enough resources, ask user to insert coins. else give the resources report and exit.
# TODO write a function to take the user coins, calculate total amount, compare it with the original price of coffee.
# TODO if the original price matches with the user total, give the coffee and update the resources.
# TODO else, if it is less, alert to give enough money and don't give the coffee.
# TODO else, ask user to insert exact change.
#
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_amount = 0.0
machine_on = True


def resources_available(choice):
    for ingredient in MENU[choice]["ingredients"]:
        if resources[ingredient] < MENU[choice]["ingredients"][ingredient]:
            return False
        else:
            resources[ingredient] = resources[ingredient] - MENU[choice]["ingredients"][ingredient]
            return True


def calc_pay():
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return float(total)


while machine_on:
    user_choice = (input("what would you like?(espresso/latte/cappuccino): ")).lower()
    if user_choice == "report":
        print(
            f'water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\ncoffee: {resources["coffee"]}ml\nmoney: ${total_amount}')
    elif user_choice == "off":
        machine_on = False
    else:
        if resources_available(user_choice):
            item_cost = MENU[user_choice]["cost"]
            print(f"{user_choice} costs: ${item_cost} \nPlease insert coins.")
            user_pay = calc_pay()
            if user_pay < item_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif user_pay > item_cost:
                print(f"Here is your change ${round(user_pay - item_cost,2)}")
                print(f"Here is your {user_choice} ☕. Enjoy!")
            else:
                print(f"Here is your {user_choice} ☕. Enjoy!")
                total_amount += float(MENU[user_choice]["cost"])
                machine_on = True
        else:
            print("Not enough resources. Please refill and use the machine!")

