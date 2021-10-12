# importing the packages
import tkinter as tk

from tkinter import *

from tkinter import messagebox

# creating windows
homepage = tk.Tk()
custinfo = tk.Tk()


homepage.minsize(300, 500)

homepage.title("Fast food ordering system")

#title
l1 = Label(homepage, text="Welcome to Fast food ordering system")
l1.grid(row=0, column=0, columnspan=5)

#name
l2 = Label(homepage, text="Name")
l2.grid(row=1, column=0)

#address
l3 = Label(homepage, text="Address")
l3.grid(row=2, column=0)

#card
l4 = Label(homepage, text="Credit/Debit Card")
l4.grid(row=3, column=0)

#selecting intro
l5 = Label(homepage, text="Menu")
l5.grid(row=4, column=0)

l6 = Label(homepage, text="Name")
l6.grid(row=5, column=0)

l7 = Label(homepage, text="Quantity")
l7.grid(row=5, column=1)


#Button

b1 = Button(homepage, text="button1")
b1.grid(row=6, column=2)

def main():
    homepage.mainloop()


if __name__ == "__main__":
    main()