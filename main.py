from art import cup
import time
import random

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

PROFIT = 0

def checked_resource(coffee):
    need = MENU[coffee]["ingredients"]
    for res in need:
        if need[res] > resources[res]:
            print(f"We cannot make coffee for you. Not enough {res} :(")
            return False
    return True


def give_me_youre_money(coffee):
    print("Please put coins in the machine.")
    while True:
        quarters = input("Quarters: ")
        try:
            quarters = int(quarters)*0.25
            if quarters < 0:
                print("Value cannot be negative")
            else:
                break
        except:
            print("Need count.")
    while True:
        dimes = input("Dimes: ")
        try:
            dimes = int(dimes)*0.10
            if dimes < 0:
                print("Value cannot be negative")
            else:
                break
            break
        except:
            print("Need count.")
    while True:
        nickles = input("Nickles: ")
        try:
            nickles = int(nickles)*0.05
            if nickles < 0:
                print("Value cannot be negative")
            else:
                break
            break
        except:
            print("Need count.")
    while True:
        pennies = input("Pennies: ")
        try:
            pennies = int(pennies)*0.01
            if pennies < 0:
                print("Value cannot be negative")
            else:
                break
            break
        except:
            print("Need count.")

    result = quarters + dimes + nickles + pennies
    need_money = MENU[coffee]['cost']
    if result < need_money:
        print("Insufficient funds.")
        return False
    else:
        if type(result) == float:
            result = round(result, 2)
        print(f"You have deposited coins for a total of ${result}. Funds accepted. The order is being processed.")
        if result > need_money:
            change = result - need_money
            if type(change) == float:
                change = round(change, 2)
            print(f"Your change is ${change}.")
            print(f"Collect your change, which consists of:")
            change_quaters = 0
            change_dimes = 0
            change_nickles = 0
            change_pennies = 0

            change = round(change, 2)
            while change >= 0.25:
                change-=0.25
                change = round(change, 2)
                change_quaters +=1
            if change_quaters > 0:
                print(f"Quaters - {change_quaters}")

            change = round(change, 2)
            while change >= 0.1:
                change-=0.1
                change = round(change, 2)
                change_dimes +=1
            if change_dimes > 0:
                print(f"Dimes - {change_dimes}")

            change = round(change, 2)
            while change >= 0.05:
                change-=0.05
                change = round(change, 2)
                change_nickles +=1
            if change_nickles > 0:
                print(f"Nickles - {change_nickles}")

            change = round(change, 2)
            while change >= 0.01:
                change-=0.01
                change = round(change, 2)
                change_pennies +=1
            if change_pennies > 0:
                print(f"Pennies - {change_pennies}")

        return True




COFFEMACHINE = True
while COFFEMACHINE:
    while True:
        choose = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choose == 'espresso':
            if checked_resource("espresso") and give_me_youre_money("espresso"):
                for ing in MENU['espresso']['ingredients']:
                    resources[ing] -= MENU['espresso']['ingredients'][ing]
                PROFIT += MENU['espresso']['cost']
                print("We prepare coffee. :)")
                time.sleep(random.randint(1, 3))
                print("We pour water.")
                time.sleep(random.randint(1, 3))
                print(cup)
                print("Your espresso is ready. Thank you for your purchase :)")
        elif choose == 'latte':
            if checked_resource("latte") and give_me_youre_money("latte"):
                for ing in MENU['latte']['ingredients']:
                    resources[ing] -= MENU['latte']['ingredients'][ing]
                PROFIT += MENU['latte']['cost']
                print("Preparing and pouring espresso :)")
                time.sleep(random.randint(3, 5))
                print("Pouring hot milk.")
                time.sleep(random.randint(1, 3))
                print("We make foam for you.")
                time.sleep(random.randint(1, 3))
                print(cup)
                print("Your latte is ready. Thank you for your purchase :)")
        elif choose == 'cappuccino':
            if checked_resource("cappuccino") and give_me_youre_money("cappuccino"):
                for ing in MENU['cappuccino']['ingredients']:
                    resources[ing] -= MENU['cappuccino']['ingredients'][ing]
                PROFIT += MENU['cappuccino']['cost']
                print("Preparing and pouring espresso :)")
                time.sleep(random.randint(3, 5))
                print("Pouring hot milk.")
                time.sleep(random.randint(1, 3))
                print("We make foam for you.")
                time.sleep(random.randint(1, 3))
                print(cup)
                print("Your cappuccino is ready. Thank you for your purchase :)")
        elif choose == 'exit':
            COFFEMACHINE = False
            break
        elif choose == 'profit':
            print(f"Profit: ${PROFIT}")
        elif choose == 'report':
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
        else:
            print("Unknown command.")