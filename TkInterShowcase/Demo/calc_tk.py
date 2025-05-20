import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x400")
        self._build_ui()
        self.expression = ""
        self.bind("<Key>", self._on_key_shortcut)

    def _build_ui(self):
        # Display Entry
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2,
                                relief="groove", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

        # Buttons
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+")
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = tk.Button(self, text=char, font=("Arial", 18),
                                command=lambda ch=char: self._on_button_click(ch))
                btn.grid(row=r, column=c, sticky="nsew")

        # Configure row/column weights for responsiveness
        for i in range(5):
            self.rowconfigure(i, weight=7)
        for j in range(4):
            self.columnconfigure(j, weight=7)

        self.columnconfigure(3, weight=3)

    def _on_key_shortcut(self, event:tk.Event):
        if event.keysym == "Return":
            self._on_button_click("=")
        if event.char.isnumeric() or event.char in [".", "/", "*", "-", "+"]:
            self._on_button_click(event.char)

    def _on_button_click(self, char):
        if char == "=":
            self._eval()
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def _eval(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
