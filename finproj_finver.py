from tkinter import *

from tkinter import messagebox

from PIL import ImageTk, Image


# creating windows
root = Tk()

# homepage
class Homepage:

    def __init__(self, master):
        self.master = master
        self.master.title("Fast Food Ordering System")

        # Images
        # title img
        img1 = Image.open("D:/finalproj/title.png")
        self.pic1 = ImageTk.PhotoImage(img1)
        self.p1 = Label(image=self.pic1)
        self.p1.grid(row=0, column=0, columnspan=9, sticky="NSEW")

        # food img
        img2 = Image.open("D:/finalproj/hamburger.png")
        self.pic2 = ImageTk.PhotoImage(img2)
        self.p2 = Label(image=self.pic2)
        self.p2.grid(row=4, column=0)

        img3 = Image.open("D:/finalproj/friedchicken.png")
        self.pic3 = ImageTk.PhotoImage(img3)
        self.p3 = Label(image=self.pic3)
        self.p3.grid(row=5, column=0)

        img4 = Image.open("D:/finalproj/nugget.png")
        self.pic4 = ImageTk.PhotoImage(img4)
        self.p4 = Label(image=self.pic4)
        self.p4.grid(row=6, column=0)



        # welcome message
        self.l1 = Label(master, text="Welcome to Fast food ordering system")
        self.l1.grid(row=1, column=0, columnspan=9, sticky="NSEW")

        # selecting intro
        self.l2 = Label(master, text="Menu")
        self.l2.grid(row=2, column=0, columnspan=9, pady=30)

        self.l3 = Label(master, text="Preview")
        self.l3.grid(row=3, column=0, sticky="NSEW")

        self.l4 = Label(master, text="Name")
        self.l4.grid(row=3, column=1, sticky="NSEW")

        self.l5 = Label(master, text="Quantity")
        self.l5.grid(row=3, column=6, sticky="NSEW")

        self.l9 = Label(master, text="Price")
        self.l9.grid(row=3, column=4, sticky="NSEW")

        # food names
        self.l6 = Label(master, text="Hamburger")
        self.l6.grid(row=4, column=1, sticky="NSEW")

        self.l7 = Label(master, text="Fried Chicken(1pc)")
        self.l7.grid(row=5, column=1, sticky="NSEW")

        self.l8 = Label(master, text="Nugget(10pc)")
        self.l8.grid(row=6, column=1, sticky="NSEW")

        #food price
        self.l10 = Label(master, text="$3.99")
        self.l10.grid(row=4, column=4, sticky="NSEW")

        self.l11 = Label(master, text="$4.99")
        self.l11.grid(row=5, column=4, sticky="NSEW")

        self.l12 = Label(master, text="$4.49")
        self.l12.grid(row=6, column=4, sticky="NSEW")


        #selection_input
        # let customer adjust the amount they want to order
        # selection 1
        self.select_decrease1 = Button(master, text="-", command=self.decrease1)
        self.select_decrease1.grid(row=4, column=5)

        self.select_increase1 = Button(master, text="+", command=self.increase1)
        self.select_increase1.grid(row=4, column=7)

        self.quantity1 = Label(master, text="0")
        self.quantity1.grid(row=4, column=6)

        #selection 2
        self.select_decrease2 = Button(master, text="-", command=self.decrease2)
        self.select_decrease2.grid(row=5, column=5)

        self.select_increase2 = Button(master, text="+", command=self.increase2)
        self.select_increase2.grid(row=5, column=7)

        self.quantity2 = Label(master, text="0")
        self.quantity2.grid(row=5, column=6)

        #selection 3
        self.select_decrease3 = Button(master, text="-", command=self.decrease3)
        self.select_decrease3.grid(row=6, column=5)

        self.select_increase3 = Button(master, text="+", command=self.increase3)
        self.select_increase3.grid(row=6, column=7)

        self.quantity3 = Label(master, text="0")
        self.quantity3.grid(row=6, column=6)



        #sauce chosing title
        self.sauce_choice = Label(master, text="Sauces Option")
        self.sauce_choice.grid(row=7, column=0, columnspan=9, sticky="NSEW")

        # a list for sause
        self.flavor =[
            ("Ketchup","Ketchup",1),
            ("Ranch","Ranch",2),
            ("Buffalo sauce","Buffalo sauce",3),
            ("No sauce","No sauce",4)
        ]
        self.sauce = StringVar()
        self.sauce.set("No sauce")

        # a for loop for showing the buttons
        for text, mode, column in self.flavor:
            Radiobutton(master, text=text, variable=self.sauce, value=mode).grid(row=8, column=column, sticky="NSEW")

        #exit button
        self.button_quit = Button(self.master, text="Exit Program", command=self.master.quit)
        self.button_quit.grid(row=10, column=0, pady=20)


        # go to order and fill the customer information
        self.cust = Button(self.master, text="Go To Order", command=self.orderdetail)
        self.cust.grid(row=10, column=7, pady=20)


    # function for adjust the order quantity for all three choice
    def increase1(self):
        value = int(self.quantity1["text"])
        self.quantity1["text"]= f"{value + 1}"
        self.select_decrease1 = Button(self.master, text="-", command=self.decrease1)
        self.select_decrease1.grid(row=4, column=5)


    def decrease1(self):

        value = int(self.quantity1["text"])
        if value == 0:
            self.select_decrease1 = Button(self.master, text="-", state=DISABLED)
            self.select_decrease1.grid(row=4, column=5)
        else:
            self.quantity1["text"] = f"{value - 1}"


    def increase2(self):
        value = int(self.quantity2["text"])
        self.quantity2["text"]= f"{value + 1}"
        self.select_decrease2 = Button(self.master, text="-", command=self.decrease2)
        self.select_decrease2.grid(row=5, column=5)

    def decrease2(self):

        value = int(self.quantity2["text"])
        if value == 0:
            self.select_decrease2 = Button(self.master, text="-", state=DISABLED)
            self.select_decrease2.grid(row=5, column=5)
        else:
            self.quantity2["text"] = f"{value - 1}"


    def increase3(self):
        value = int(self.quantity3["text"])
        self.quantity3["text"]= f"{value + 1}"
        self.select_decrease3 = Button(self.master, text="-", command=self.decrease3)
        self.select_decrease3.grid(row=6, column=5)

    def decrease3(self):
        value = int(self.quantity3["text"])
        if value == 0:
            self.select_decrease3 = Button(self.master, text="-", state=DISABLED)
            self.select_decrease3.grid(row=6, column=5)
        else:
            self.quantity3["text"] = f"{value - 1}"

    # the new window to fill in the customer information
    def orderdetail(self):
        global window
        window = Toplevel()
        l1 = Label(window, text="Customer Information")
        l1.grid(row=0, column=0, columnspan=5)

        # name
        l2 = Label(window, text="Name")
        l2.grid(row=1, column=0)
        global e1
        e1 = Entry(window, width=20)
        e1.grid(row=1, column=1)

        # address
        l3 = Label(window, text="Address")
        l3.grid(row=2, column=0)
        global e2
        e2 = Entry(window, width=20)
        e2.grid(row=2, column=1)

        # phone
        l4 = Label(window, text="Contact number")
        l4.grid(row=3, column=0)
        global e3
        e3 = Entry(window, width=20)
        e3.grid(row=3, column=1)

        # card
        l5 = Label(window, text="Credit/Debit Card")
        l5.grid(row=4, column=0)
        global e4
        e4 = Entry(window, width=30)
        e4.grid(row=4, column=1)

        # show the total price for order
        l6 = Label(window, text="Total")
        l6.grid(row=5, column=1,sticky="E")

        #calculation for the foods
        value1 = float(self.quantity1["text"])
        value2 = float(self.quantity2["text"])
        value3 = float(self.quantity3["text"])
        global result
        caluculate = value1 * 3.99 + value2 * 4.99 + value3 * 4.49
        result = str(round(caluculate,2))
        l6 = Label(window, text=result)
        l6.grid(row=6, column=1, sticky="E")

        # the confirmation button lead to the final result page
        confirm = Button(window, text="Confirm", command=self.finorder)
        confirm.grid(row=8, column=1, sticky="E")

        # a button for quit the customer info window
        button_quit = Button(window, text="Cancel", command=window.destroy)
        button_quit.grid(row=8, column=2)

    # Final ordering confirmation page
    def finorder(self):
        #after the customer input, here is the if-else to check validation
        if len(e1.get()) == 0 or len(e2.get()) == 0 or len(e3.get()) == 0 or len(e4.get()) == 0:
            messagebox.showwarning("Invalid Input", "Please enter the information.")

        else:
            try:
                int(e3.get())

                window2 = Toplevel()

                l1 = Label(window2, text="Ordering Detail")
                l1.grid(row=0, column=0, columnspan=5)

                # name
                l2 = Label(window2, text="Name")
                l2.grid(row=1, column=0)

                l2_output = Label(window2, text=e1.get())
                l2_output.grid(row=1, column=1)

                # Address
                l3 = Label(window2, text="Address")
                l3.grid(row=2, column=0)

                l3_output = Label(window2, text=e2.get())
                l3_output.grid(row=2, column=1)

                # phone
                l4 = Label(window2, text="Contact number")
                l4.grid(row=3, column=0)

                l4_output = Label(window2, text=e3.get())
                l4_output.grid(row=3, column=1)

                # card
                l5 = Label(window2, text="Credit/Debit Card")
                l5.grid(row=4, column=0)

                l5_output = Label(window2, text=e4.get())
                l5_output.grid(row=4, column=1)

                # food order result
                l6 = Label(window2, text="Hamburger")
                l6.grid(row=5, column=0)

                l6_output = Label(window2, text=self.quantity1["text"])
                l6_output.grid(row=5, column=1)

                l7 = Label(window2, text="Fried Chicken")
                l7.grid(row=6, column=0)

                l7_output = Label(window2, text=self.quantity2["text"])
                l7_output.grid(row=6, column=1)

                l8 = Label(window2, text="Hamburger")
                l8.grid(row=7, column=0)

                l8_output = Label(window2, text=self.quantity3["text"])
                l8_output.grid(row=7, column=1)

                # total amount
                l9 = Label(window2, text="Total")
                l9.grid(row=9, column=0)

                l9_result = Label(window2, text=result)
                l9_result.grid(row=9, column=1)

                # the sauce choice
                l10 = Label(window2, text="Sauce")
                l10.grid(row=8, column=0)

                l10_output = Label(window2, text=self.sauce.get())
                l10_output.grid(row=8, column=1)

                # button to confirm the final page
                b1 = Button(window2, text="Ok", command=window2.destroy)
                b1.grid(row=10, column=1)


            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter the number.")








e = Homepage(root)
def main():
    root.mainloop()


if __name__ == "__main__":
    main()