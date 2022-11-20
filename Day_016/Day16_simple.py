from money_machine import MoneyMachine
from coffe_maker import CoffeeMaker
from menu import Menu, MenuItem
from prettytable import PrettyTable
from turtle import Turtle, Screen
import another_module
print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()
# same

timmmy = Turtle()
timmmy.shape("turtle")
timmmy.color("DarkGreen")
timmmy.forward(100)
my_screen = Screen()
my_screen.exitonclick()
# use turtle

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
# how to install package and use
# use pip


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


loop = True

while loop:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        loop = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
