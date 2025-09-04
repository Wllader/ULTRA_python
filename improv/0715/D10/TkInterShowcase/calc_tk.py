import tkinter as tk

class CalculatorWidget(tk.Frame):
    # def __init__(self):
    #     super().__init__()
    #     self.title("Calculator")
    #     self.geometry("400x400")
    #     self._expression = ""
    #     self._build_ui()
    #     self.bind("<Key>", self._on_key_shortcut)

    def __init__(self, master = None):
        super().__init__(master)
        self._expression = ""
        self._build_ui()
        self.bind("<Key>", self._on_key_shortcut)

    @property
    def expression(self):
        return self._expression
    
    @expression.setter
    def expression(self, value):
        self._expression = value
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self._expression)

    @expression.deleter
    def expression(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, "Error")
        self._expression = ""


    def _build_ui(self):
        # Display entry
        self.display = tk.Entry(self, font=("Consolas", 20), borderwidth=2,
                                relief="groove", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

        #Buttons
        buttons = [
            tuple("789/"),
            tuple("456*"),
            tuple("123-"),
            tuple("0.=+")
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = tk.Button(self, text=char, font=("Consolas", 18),
                                command=lambda ch=char: self._on_button_click(ch))
                btn.grid(row=r, column=c, sticky="nsew")
                
        # Button row/col weights
        for i in range(5):
            self.rowconfigure(i, weight=7)
        for j in range(4):
            self.columnconfigure(j, weight=7)

        self.columnconfigure(3, weight=3)
        
    def _on_button_click(self, char):
        if char == "=":
            self._eval()
        else:
            self.expression += char

    def _eval(self):
        try:
            result = str(eval(self._expression))
            self.expression = result
        except Exception as e:
            del(self.expression)

    def _on_key_shortcut(self, event:tk.Event):
        if event.keysym == "Return":
            self._on_button_click("=")

        if event.keysym == "BackSpace":
            self.expression = self.expression[:-1]

        if event.char == ",":
            self._on_button_click(".")

        if (ch := event.char).isnumeric() or ch in tuple("/*-+"):
            self._on_button_click(ch)


if __name__ == "__main__":
    app = tk.Tk()

    counter = 0
    def add_calc():
        global counter
        CalculatorWidget(app).grid(row=1, column=counter, padx=10)
        counter += 1

    tk.Button(app, text="Add calc", command=add_calc).grid(row=0, column=0)
    app.mainloop()