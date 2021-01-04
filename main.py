MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 100,
    "milk": 200,
    "coffee": 100,
}

def checkingredients(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received == drink_cost:
        return True
    elif money_received > drink_cost:
        change_amount = money_received - drink_cost
        print(f"Your change is: {change_amount}")
    return False

#Code starts here

user_selection = input('What would you like? (espresso/latte/cappuccino):')

if user_selection == "report":
    print ("Coffee Machine Report")
    print("----------------------")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
else:
    drink = MENU[user_selection]
    print ("You selected " + user_selection)
    print(checkingredients(drink["ingredients"]))
    payment = process_coins()
    if is_transaction_successful(payment, drink["cost"]):
        print("Making drink!")
    else:
        print("Something went wrong")
