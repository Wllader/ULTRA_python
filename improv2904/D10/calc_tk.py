import tkinter as tk

class CalculatorWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._expression = ""
        self._build_ui()

    @property
    def expression(self):
        return self._expression
    
    @expression.setter
    def expression(self, value):
        self._expression = value
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, value)


    def _build_ui(self):
        # Display entry
        self.display = tk.Entry(self, font=("Consolas", 20), borderwidth=2,
                                relief="groove", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

        # Buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            list("123-"),
            list("0.=+")
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                tk.Button(self, text=char, font=("Consolas", 18),
                          command=lambda ch=char: self._on_button_click(ch)).grid(row=r, column=c, sticky="nsew")
                
        for i in range(len(buttons)):
            self.rowconfigure(i, weight=7)
        for i in range(len(buttons[1])):
            self.columnconfigure(i, weight=7)

        self.columnconfigure(3, weight=3)

    def _on_button_click(self, char):
        if char == "=":
            self._eval()
        else:
            self.expression += char

    def _eval(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception as e:
            self.expression = "Error"
            self._expression = ""

    def _on_key_shortcut(self, event:tk.Event):
        if event.keysym == "Return":
            self._on_button_click("=")
        elif event.char.isnumeric() or event.char in list("./*-+"):
            self._on_button_click(event.char)

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorWidget(root).grid(row=0, column=0, sticky="news", padx=15)
    CalculatorWidget(root).grid(row=0, column=1, sticky="news", padx=15)

    root.mainloop()
            
        