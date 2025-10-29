# menu and resources dictionaries supplied as starting code
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_available(user_input): 
    '''Checks if there are sufficient resources in the machine'''
    ingredients = MENU[user_input]["ingredients"]
    for key in ingredients:
        resources[key] = resources[key] - ingredients[key]
        if resources[key]  <= 0:
            print(f"Not enout {key}")
            return False
        else:
            return True

def money_sufficient(user_input):
    '''Asks for money and returns True of False if you add enough money.
    Also returns change'''
    price = MENU[user_input]["cost"]
    user_money = float(input(f"Pay price of {price}"))
    if user_money == price:
        return True
    elif user_money < price:
        return "Not enough funds"
    else: 
        print(f"Here is your change of {user_money-price}")
        return True


machine_working = True
while machine_working:
    #invoke the user input
    user_input = str(input("What would you like? (espresso/latte/cappuccino):"))
    if user_input == "resources":
        print(resources)
    elif user_input in MENU.keys():
        if resources_available(user_input):
            if money_sufficient(user_input):
                print(f"Making {user_input}")
                print("Enjoy")
                print(resources)
    elif user_input == "off":
        machine_working = False

