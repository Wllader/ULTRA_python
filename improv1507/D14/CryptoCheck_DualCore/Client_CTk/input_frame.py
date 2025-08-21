import customtkinter as ctk
from typing import Callable
from enum import StrEnum, auto

class TickerType(StrEnum):
    COIN = auto()
    SHARE = auto()

class InputFrame(ctk.CTkFrame):
    def __init__(self, master, fetch:Callable = None, **kwargs):
        super().__init__(master, **kwargs)
        self.fetch = fetch if fetch is not None else lambda: print(f"TestFetch {self.symbol=}, {self.days=}")

        ctk.CTkLabel(self, text="Enter Crypto Symbol:").grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Enter number of Days:").grid(row=1, column=0, padx=10, pady=10)

        self.symbol_entry = ctk.CTkEntry(self, placeholder_text="tick goes here")
        self.symbol_entry.grid(row=0, column=1, padx=10, pady=10)

        self.days_entry = ctk.CTkEntry(self, placeholder_text="#days")
        self.days_entry.grid(row=1, column=1, padx=10, pady=10)

        self.fetch_button = ctk.CTkButton(self, text="Fetch Data and Plot", command=self.fetch)
        self.fetch_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.type_var = ctk.StringVar(value=TickerType.COIN)
        ctk.CTkRadioButton(self, text="Coin", variable=self.type_var, value=TickerType.COIN).grid(row=2, column=0)
        ctk.CTkRadioButton(self, text="Share", variable=self.type_var, value=TickerType.SHARE).grid(row=2, column=1)

    @property
    def symbol(self):
        return self.symbol_entry.get()
    
    @property
    def days(self):
        d = self.days_entry.get()
        return int(d) if d.isnumeric() else 0
    
    @property
    def type(self):
        return self.type_var.get()



if __name__ == "__main__":
    app = ctk.CTk()
    InputFrame(app).pack()

    app.mainloop()