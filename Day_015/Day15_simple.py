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

eat_money = 0


def check(select):
    need_res = MENU[select]["ingredients"]
    for i in need_res:
        if resources[i] < need_res[i]:
            return False
    return True


def input_money():
    print("Please insert coins. ")
    quarters = int(input("how many quarters?: "))

    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money


def compare_money(money, select):
    need = MENU[select]["cost"]
    global eat_money
    if money - need >= 0:
        eat_money += need
        change = round(money - need, 2)
        print(f"Here is {change} in change.")
        return True
    else:
        return False


def res_change(select):
    need_res = MENU[select]["ingredients"]
    for i in need_res:
        resources[i] = resources[i] - need_res[i]


def run(select):
    if check(select):
        res_change(select)
        money = input_money()
        change = compare_money(money, select)
        if change:
            print(f"Here is your latte. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry there is not enough {check(select)}.")


loop = True
while loop:
    select = input("​What would you like? (espresso/latte/cappuccino): ")
    if select == "off":
        loop = False
    elif select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${eat_money}")
    else:
        run(select)
