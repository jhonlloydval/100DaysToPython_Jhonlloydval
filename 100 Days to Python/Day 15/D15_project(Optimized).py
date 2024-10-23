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

# Global variable to track money earned
money = 0.00

# Function to check if resources are sufficient for the coffee
def sufficient_resources(coffee):
    """Check if there are enough resources to make the coffee."""
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Function to process coins
def coin_process(coffee):
    """Handle coin insertion and check if the payment is sufficient."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    # Calculate the total value of the coins
    total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    # Check if the total is enough
    if total_coins < MENU[coffee]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += MENU[coffee]["cost"]
        change = round(total_coins - MENU[coffee]["cost"], 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {coffee}. Enjoy!")
        return True

# Function to deduct resources
def make_coffee(coffee):
    """Deduct the resources needed for the coffee."""
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        resources[ingredient] -= amount

# Main function for the coffee machine
def coffee_machine():
    """Main function to run the coffee machine."""
    global operation
    operation = True

    while operation:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            operation = False
            print("Turning off the coffee machine.")
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif choice in MENU:
            if sufficient_resources(choice):
                if coin_process(choice):
                    make_coffee(choice)
        else:
            print("Invalid input. Please choose from espresso, latte, cappuccino, report, or off.")

# Start the coffee machine
coffee_machine()