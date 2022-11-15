import art
import os


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("KIM", "HEEJIN"))
# use return


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Error"
    if is_leap(year) == True:
        month_days[1] = 29
    else:
        month_days[1] = 28
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# leap year use return

""" it 
is
doc
string"""


def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


oper = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def cal():
    os.system('clear')
    print(art.logo)

    num1 = float(input("What's the first number?: "))
    loop = True
    while loop:
        sel_symbol = input("select symbol: ")
        num2 = float(input("What's the second number?: "))
        for symbol in oper:
            print(symbol)
        calcu = oper[sel_symbol]
        answer = calcu(num1, num2)
        print(f"{num1} {sel_symbol} {num2} = {answer}")
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n': ") == "y":
            loop = True
            num1 = answer
        else:
            loop = False
            cal()


cal()
