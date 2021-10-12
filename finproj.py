from breezypythongui import EasyFrame



class fastfood(EasyFrame):
    def __init__(self):
        """set up the window and widgets"""
        EasyFrame.__init__(self,title = "Fast food ordering system")

        #title
        self.addLabel(text= "Fast food ordering system", row = 0, column = 0, columnspan = 2, sticky = "NSEW")


        #name
        self.addLabel(text= "Name", row = 1, column = 0)
        self.inputField = self.addTextField(text = "",
                                              row = 1,
                                              column = 1,
                                              width = 8)

        #address
        self.addLabel(text = "address", row = 2, column = 0)
        self.inputField = self.addTextField(text = (),
                                            row= 2,
                                            column = 1,
                                            width = 8)
        #selecting intro
        self.addLabel(text= "Menu", row = 3, column = 0, columnspan = 2, sticky = "NSEW")
        self.addLabel(text="Name", row=4, column=0, sticky = "NSEW")
        self.addLabel(text="Quantity", row=4, column=1, sticky="NSEW")


        #foods and the food quality
        self.addLabel(text="food1", row=5, column=0, sticky="NSEW")
        self.inputField = self.addIntegerField(value = 0,
                                               row= 5,
                                               column = 1,
                                               width = 3)

        self.addLabel(text="food2", row=6, column=0, sticky="NSEW")
        self.inputField = self.addIntegerField(value=0,
                                               row=6,
                                               column=1,
                                               width=3)

        self.addLabel(text="food3", row=7, column=0, sticky="NSEW")
        self.inputField = self.addIntegerField(value=0,
                                               row=7,
                                               column=1,
                                               width=3)

def main():
    """Instantiates and pops up the window."""
    fastfood().mainloop()

if __name__ == "__main__":
    main()