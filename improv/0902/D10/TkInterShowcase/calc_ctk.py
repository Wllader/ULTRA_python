import customtkinter as ctk
from tkinter import Event

class CalculatorWidget(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self._expression = ""
        self._build_ui()
        self.bind("<Key>", self._on_key_shortcut)

    @property
    def expression(self):
        return self._expression
    
    @expression.setter
    def expression(self, value):
        self._expression = value
        self.display.delete(0, ctk.END)
        self.display.insert(ctk.END, value)

    def _build_ui(self):
        #Display
        self.display = ctk.CTkEntry(self, font=("Consolas", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

        buttons = (
            "789/",
            "456*",
            "123-",
            "0.=+"
        )

        for r, row_values in enumerate(buttons, start=1):
            for c, char in enumerate(row_values):
                btn = ctk.CTkButton(
                    self, text=char, font=("Consolas", 18),
                    command=lambda ch=char: self._on_button_click(ch)
                )

                if char == "=":
                    btn.configure(fg_color="#eb4034")
                elif not char.isnumeric():
                    btn.configure(fg_color="#098f28")

                btn.grid(row=r, column=c, padx=2, pady=1, sticky="nswe")


        #Configure weights
        for i in range(5):
            self.rowconfigure(i, weight=3)
        for j in range(4):
            self.columnconfigure(j, weight=3)

        self.columnconfigure(3, weight=12)


    def _on_button_click(self, char:str):
        if char == "=":
            self._eval()
        else:
            self.expression += char

    def _eval(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except:
            self.expression = ""
            self.display.insert(ctk.END, "Error")


    def _on_key_shortcut(self, event:Event):
        if event.keysym == "Return":
            self._on_button_click("=")
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
        elif event.char.isnumeric() or event.char in "./*-+":
            self._on_button_click(event.char)
        elif event.char == ",":
            self._on_button_click(".")


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.geometry("500x300")

    CalculatorWidget(app, height=300).pack()

    app.mainloop()