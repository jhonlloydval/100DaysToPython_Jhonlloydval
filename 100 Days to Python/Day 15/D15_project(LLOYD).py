# Day 15
# Coffee Machine Program Requirements

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Turn off the Coffee Machine by entering "off" to the prompt.
# Print report

def coin_process(coffee):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    total_coins = quarters + dimes + nickles + pennies
    
    if total_coins < MENU[coffee]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        coffee_machine()
    else:
        global money
        money += MENU[coffee]["cost"]
        return_coins = total_coins - MENU[coffee]["cost"]
        if return_coins != 0:
            print(f"Here is ${return_coins:.2f} in change.")
        print(f"Here is your {coffee}. Enjoy!")
        
        coffee_machine()
        
def sufficient_resources(coffee):
    is_sufficient = True
    for item in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            is_sufficient = False
    if is_sufficient:
        for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]
        coin_process(coffee)
    else:
        coffee_machine()

operation = True
money = 0.00

def coffee_machine():
    global operation
    while operation:
        coffee = input("What would you like (espresso/latte/cappuccino): ").lower()
        
        if coffee == "off":
            operation = False
        
        if coffee == "report":
            print(f"Water : {resources["water"]}ml")
            print(f"Milk : {resources["milk"]}ml")
            print(f"Coffee : {resources["coffee"]}g")
            print(f"Money : ${money:.2f}")
        
        if coffee in ["espresso", "latte", "cappuccino"]:
            sufficient_resources(coffee)

coffee_machine()