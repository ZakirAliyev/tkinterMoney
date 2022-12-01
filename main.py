from tkinter import *

win = Tk()
win.geometry("500x500")
win['background'] = '#2596be'

variable = StringVar(win)
variable.set("From currency")

variable1 = StringVar(win)
variable1.set("To currency")

labelStart = Label(win, text="Currency Converter")
labelStart.place(x=63, y=25)
labelStart.config(bg="#2596be", font=('Cascadia Code', 27), fg='#873e23')

optionMenu1 = OptionMenu(win, variable, "USD", "EUR", "GBP", "TRY", "AZN")
optionMenu1.place(x=70, y=120, height=40, width=150)

optionMenu2 = OptionMenu(win, variable1, "USD", "EUR", "GBP", "TRY", "AZN")
optionMenu2.place(x=285, y=120, height=40, width=150)

entryFrom = Label(win, font=('Cascadia Code', 10),text="Please enter value",bg='#2596be')
entryFrom.place(x=60, y=275, height=20, width=170)

textBoxFrom = Entry(win, font=('Arial', 22))
textBoxFrom.place(x=70, y=300, height=40, width=150)

entryTo = Label(win, font=('Cascadia Code', 10),text="Result of conversion",bg='#2596be')
entryTo.place(x=275, y=275, height=20, width=170)

result = Label(win, text="")
result.grid(row=3, column=1, sticky=W)
result.place(x=285, y=300, height=40, width=150)

labelConvert = Button(win, text="Convert",font=('Arial',18))
labelConvert.place(x=203, y=380)

mainloop()
