import tkinter as tk

class CalculatorWidget(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

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
        self.display.insert(0, "Error")
        self._expression = ""

    def _build_ui(self):
        # Display entry
        self.display = tk.Entry(self, font=("Consolas", 20), borderwidth=2,
                                relief="groove", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

        # Buttons
        buttons = (
            "789/",
            "456*",
            "123-",
            "0.=+"
        )

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = tk.Button(self, text=char, font=("Consolas", 18),
                                command=lambda ch=char: self._on_button_click(ch))
                btn.grid(row=r, column=c, sticky="nsew")


        # Configure weights
        for i in range(5):
            self.rowconfigure(i, weight=7)

        for j in range(4):
            self.columnconfigure(j, weight=7)

        self.columnconfigure(3, weight=3)

    def _on_key_shortcut(self, event:tk.Event):
        print(event.keysym)

        if event.keysym == "Return":
            self._on_button_click("=")

        if event.keysym == "BackSpace":
            self.expression = self.expression[:-1]

        if event.char == ",":
            self._on_button_click(".")

        if (ch := event.char).isnumeric() or ch in "./*+-":
            self._on_button_click(ch)
              
    def _on_button_click(self, ch:str):
        if ch == "=":
            self._eval()
        else:
            self.expression += ch

    def _eval(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception as e:
            del(self.expression)


if __name__ == "__main__":
    app = tk.Tk()


    calc = CalculatorWidget(app)
    calc.pack()

    app.mainloop()