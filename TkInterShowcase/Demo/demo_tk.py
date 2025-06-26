import tkinter as tk
from tkinter import messagebox

class ExampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Example App")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        # Label
        label = tk.Label(self, text="Enter your name:")
        label.pack(pady=5)

        # Entry
        self.entry = tk.Entry(self, width=25)
        self.entry.pack()

        # RadioButtons
        self.pets = tk.StringVar(value="None")
        tk.Label(self, text="Select Your favorite pet:").pack(pady=5)
        tk.Radiobutton(self, text="Cats", variable=self.pets, value="Cats").pack()
        tk.Radiobutton(self, text="Dogs", variable=self.pets, value="Dogs").pack()

        # CheckBox
        self.subscribe_var = tk.BooleanVar()
        tk.Checkbutton(self, text="Subscribe to newsletter", variable=self.subscribe_var).pack(pady=5)

        # Dropdown Menu
        tk.Label(self, text="Select Country:").pack(pady=5)
        self.country_var = tk.StringVar(value="Select")
        countries = ["USA", "Canada", "Mexico", "UK", "India"]
        tk.OptionMenu(self, self.country_var, *countries).pack()

        # Button
        button = tk.Button(self, text="Submit", command=self.on_click)
        button.pack(pady=10)

    def on_click(self):
        name = self.entry.get()
        pets = self.pets.get()
        subscribed = self.subscribe_var.get()
        country = self.country_var.get()

        if not name:
            messagebox.showwarning("Input needed", "Please enter your name.")
            return

        info = f"Name: {name}\nPets: {pets}\nSubscribed: {subscribed}\nCountry: {country}"
        messagebox.showinfo("Submission Info", info)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()