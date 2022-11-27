from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200) #padding

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=0,y=0) 

#grid , pack cant use together
#just define one
my_label.grid(column=0,row=0)

# my_label["text"] = "New Text"
my_label.config(text= "New Text")
my_label.config(padx=50,pady=50)

def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())

button = Button(text= "Click Me",command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

input = Entry(width=10)
# input.pack()
input.grid(column=3,row=3)
print(input.get())

new_button = Button()
new_button.grid(column= 2,row=0)

window.mainloop()

# def add(*args): #tuple
#     # arg[] use 
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum

# print(add(3,5,7,5))

# def calculate(n, **kwargs): #dictionary
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)

#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2, add=3, multiply=5)

# class Car:

#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#         # self.make = kw.get("make") equal
#         # self.model = kw.get("model")

# my_car = Car(make="Nissan" , model="GT-R")
# print(my_car.make)
# print(my_car.model)