from tkinter import *

window =Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

Miles_entry = Entry(width=10)
Miles_entry.grid(column=1,row=0)
Miles_label = Label(text="Miles")
Miles_label.grid(column=2,row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)
Km_num_label = Label(text="0")
Km_num_label.grid(column=1,row=1)
Km_label = Label(text="Km")
Km_label.grid(column=2,row=1)

def btn_click_listener():
    calcu = float(Miles_entry.get()) * 1.60934
    calcu = round(calcu)
    Km_num_label.config(text=f"{calcu}")
calculate_btn = Button(text= "Calculate",command=btn_click_listener)
calculate_btn.grid(column=1,row=2)

window.mainloop()
