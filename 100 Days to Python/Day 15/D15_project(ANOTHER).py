# # COFFE MACHINE

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resources_sufficient(machine_resources, coffee_resources):
#     for item in resources:
#         if resources[item] > MENU[coffee]["ingredients"][item]:
#             return True
#     else:
#         print(f"There is not enough {resources[item]}")
#         return False

# def process_coins():
#     print("Please insert coins.")
#     quarters = int(input("how many quarters?: ")) * 0.25
#     dimes = int(input("how many dimes?: ")) * 0.10
#     nickles = int(input("how many nickles?: ")) * 0.05
#     pennies = int(input("how many pennies?: ")) * 0.01

#     total_coins = quarters + dimes + nickles + pennies
#     if total_coins >= payment:
#         global money
#         money += payment
#         change = total_coins - payment
#         print(f"Here is ${change} in change.")
#         return True
#     else:
#         print("Sorry, that's not enough money. Money refunded.")
#         return False

# def transaction(coffee):
#     for item in resources:
#         resources[item] -= MENU[coffee]["ingredients"][item]
#         print("Here is your coffee!")
#         return


# is_on = True
# money = 0

# while is_on:
#     coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

#     if coffee == "off":
#         is_on = False

#     if coffee == "report":
#         print(f"Water : {resources["water"]}ml")
#         print(f"Milk : {resources["milk"]}ml")
#         print(f"Coffee : {resources["coffee"]}g")
#         print(f"Money : ${money}")

#     else:
#         if is_resources_sufficient(resources, coffee):
#             payment = MENU[coffee]["cost"]
#             if process_coins():
#                 transaction(coffee)




            
