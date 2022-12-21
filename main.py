"""
University : Baku State University
Faculty : Applied Mathematics and Cybernetics
Speciality : Computer Sciences
Group : KE022S2
Name : Zakir
Surname : Aliyev
E-Mail : aliyevzakir814@gmail.com

Project : Coding Currency Converter with PYTHON Language

Date : '21/12/2022'
Time : '05:43'
"""

import tkinter.constants
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.messagebox

color = '#47b5d6'


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

    elif from_currency == "From" or to_currency == "To":
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


# Create an instance of tkinter frame
root = Tk()

# Set the geometry of tkinter frame
root.geometry("700x700")

# List
CurrenyCode_list = ["TRY", "USD", "CAD", "EUR", "JPY", "BGN", "CZK", "GBP", "IDR"]

# Variables
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("From")
variable2.set("To")

# Create a canvas
canvas = Canvas(root, width=700, height=150, bg=color, highlightthickness=0)
canvas.grid(row=0, column=0)

canvas1 = Canvas(root, width=700, height=550, bg='#2d9dc3', highlightthickness=0)
canvas1.grid(row=1, column=0)

# Load an image in the script
img = (Image.open("logo.png"))

# Resize the Image using resize method
resized_image = img.resize((420, 120), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas Items
canvas.create_image(350, 73, anchor=CENTER, image=new_image)

# Add all label to Tkinter project
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg=color, fg="black")
label1.place(x=10, y=270)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg=color, fg="black")
label1.place(x=10, y=340)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg=color, fg="black")
label1.place(x=10, y=410)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg=color, fg="black")
label1.place(x=10, y=480)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.place(x=500, y=340, height=35, width=127)
ToCurrency_option.place(x=500, y=410, height=35, width=127)

Amount1_field = tk.Entry(root, font=24)
Amount1_field.place(x=500, y=270, height=25, width=127)

Amount2_field = tk.Entry(root, font=24)
Amount2_field.place(x=500, y=480, height=25, width=127)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.place(x=110, y=580, width=200)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.place(x=420, y=580, width=200)

root.mainloop()
