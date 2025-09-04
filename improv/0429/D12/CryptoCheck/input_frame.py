import customtkinter as ctk
from typing import Callable

class InputFrame(ctk.CTkFrame):
    def __init__(self, master, fetch:Callable, **kwargs):
        super().__init__(master, **kwargs)
        self.fetch = fetch

        ctk.CTkLabel(self, text="Enter Crypto Symbol:").grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Enter Number of Days:").grid(row=1, column=0, padx=10, pady=10)

        self.symbol_entry = ctk.CTkEntry(self)
        self.symbol_entry.grid(row=0, column=1, padx=10, pady=10)

        self.days_entry = ctk.CTkEntry(self)
        self.days_entry.grid(row=1, column=1, padx=10, pady=10)

        self.fetch_button = ctk.CTkButton(self, text="Fetch Data and Plot", command=self.fetch)
        self.fetch_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    @property
    def symbol(self):
        return self.symbol_entry.get()
    
    @property
    def days(self):
        return int(self.days_entry.get())


if __name__ == "__main__":
    app = ctk.CTk()
    InputFrame(app, lambda: print("Fetching...")).pack()

    app.mainloop()