from tkinter import *
expression = ""


class App(Tk):
    
    def __init__(self):
        super(Tk, self).__init__()
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("575x700+300+300")
        self.root.iconbitmap("C:/Users/U-PC/Pictures/calculator.ico")
        self.root.resizable(0, 0)
        self.root.config(bg="#363636")  

        self.equation = StringVar()
        self.expression_field = Label(self.root, textvariable=self.equation, 
                                      bg="#363636", fg="#FFFFFF",
                                      font=("Helvetica", 20), anchor=SE)
        self.expression_field.grid(columnspan=50, ipadx=168, ipady=110)

        self.button1 = Button(self.root, text="1", width=15, height=7, 
                              command=lambda: self.press_num(1), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self.root, text="2", width=15, height=7, 
                              command=lambda: self.press_num(2), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button2.grid(row=2, column=1)

        self.button3 = Button(self.root, text="3", width=15, height=7, 
                              command=lambda: self.press_num(3), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button3.grid(row=2, column=2)

        self.button4 = Button(self.root, text="4", width=15, height=7, 
                              command=lambda: self.press_num(4),
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button4.grid(row=3, column=0)

        self.button5 = Button(self.root, text="5", width=15, height=7, 
                              command=lambda: self.press_num(5), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button5.grid(row=3, column=1)

        self.button6 = Button(self.root, text="6", width=15, height=7, 
                              command=lambda: self.press_num(6), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button6.grid(row=3, column=2)

        self.button7 = Button(self.root, text="7", width=15, height=7, 
                              command=lambda: self.press_num(7), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button7.grid(row=4, column=0)

        self.button8 = Button(self.root, text="8", width=15, height=7, 
                              command=lambda: self.press_num(8), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button8.grid(row=4, column=1)

        self.button9 = Button(self.root, text="9", width=15, height=7, 
                              command=lambda: self.press_num(9),
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button9.grid(row=4, column=2)

        self.button0 = Button(self.root, text="0", width=15, height=7, 
                              command=lambda: self.press_num(0), 
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.button0.grid(row=5, column=0)

        self.plus = Button(self.root, text="+", width=15, height=7,  
                           command=lambda: self.press_num("+"),
                           bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.plus.grid(row=2, column=3)

        self.minus = Button(self.root, text="-", width=15, height=7, 
                            command=lambda: self.press_num("-"), 
                            bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.minus.grid(row=3, column=3)

        self.multiplication = Button(self.root, text="x", width=15, height=7, 
                                     command=lambda: self.press_num("*"),
                                     bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.multiplication.grid(row=4, column=3)

        self.division = Button(self.root, text="/", width=15, height=7, 
                               command=lambda: self.press_num("/"),
                               bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.division.grid(row=5, column=3)

        self.equal = Button(self.root, text="=", width=15, height=7, 
                            command=lambda: self.equal_press(),
                            bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.equal.grid(row=5, column=2)

        self.clear = Button(self.root, text="C", width=15, height=7, 
                            command=lambda: self.button_clear(),
                            bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.clear.grid(row=5, column=1)

        self.decimal = Button(self.root, text=".", width=15, height=7, 
                              command=lambda: self.press_num("."),
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.decimal.grid(row=2, column=4)

        self.modulus = Button(self.root, text="%", width=15, height=7, 
                              command=lambda: self.press_num("%"),
                              bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.modulus.grid(row=3, column=4)

        self.square = Button(self.root, text="^", width=15, height=7, 
                             command=lambda: self.press_num("**"),
                             bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.square.grid(row=4, column=4)

        self.backspace = Button(self.root, text="CE", width=15, height=7, 
                                command=lambda: self.back_space(),
                                bg="#363636", fg="#FFFFFF", font=("Helvetica", 9))
        self.backspace.grid(row=5, column=4)

        self.root.mainloop()


    def press_num(self, num):
        global expression
        expression = expression + str(num)
        self.equation.set(expression)


    def equal_press(self):
        try:

            global expression
            total = str(eval(expression))
            self.equation.set(total)
            expression = ""

        except Exception as e:
            self.equation.set(e)
            expression = ""


    def button_clear(self):
        global expression
        expression = ""
        self.equation.set("")


    def back_space(self):
        global expression
        last_index = len(expression) - 1
        expression = expression[:last_index]
        self.equation.set(expression)


app = App()
