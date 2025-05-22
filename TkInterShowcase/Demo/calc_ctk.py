import customtkinter as ctk
from tkinter import Event

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Calculator")
        self.geometry("500x300")
        ctk.set_appearance_mode("System")  # Optional: "Light", "Dark", "System"
        ctk.set_default_color_theme("blue")  # Optional: "blue", "green", "dark-blue"
        self.expression = ""
        self._build_ui()
        self.bind("<Key>", self._on_key_shortcut)

    def _build_ui(self):
        # Display Entry
        self.display = ctk.CTkEntry(self, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

        # Buttons layout
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+")
        ]

        for r, row_values in enumerate(buttons, start=1):
            for c, char in enumerate(row_values):
                btn = ctk.CTkButton(
                    self, text=char, font=("Arial", 18),
                    command=lambda ch=char: self._on_button_click(ch)
                )

                if char == "=":
                    btn.configure(fg_color="#eb4034")
                elif not char.isnumeric():
                    btn.configure(fg_color="#098f28")


                btn.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")

        # Configure row/column weights for responsiveness
        for i in range(5):
            self.rowconfigure(i, weight=4)
        for j in range(4):
            self.columnconfigure(j, weight=4)

        self.columnconfigure(3, weight=7)


    def _on_key_shortcut(self, event:Event):
        print(type(event))

        if event.keysym == "Return":
            self._on_button_click("=")
        if event.char.isnumeric() or event.char in [".", "/", "*", "-", "+"]:
            self._on_button_click(event.char)

    def _on_button_click(self, char):
        if char == "=":
            self._eval()
        else:
            self.expression += char
            self.display.delete(0, ctk.END)
            self.display.insert(ctk.END, self.expression)

    def _eval(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, ctk.END)
            self.display.insert(ctk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, ctk.END)
            self.display.insert(ctk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
