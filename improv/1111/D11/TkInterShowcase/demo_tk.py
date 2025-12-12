import tkinter as tk
from tkinter import messagebox

class ExampleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TkInter example App")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter your name:").pack(pady=5)

        self.entry = tk.Entry(self, width=25)
        self.entry.pack()

        self.pets_var = tk.StringVar(value="None")
        tk.Label(self, text="Select your favorite pets:").pack(pady=5)
        tk.Radiobutton(self, text="Cats", variable=self.pets_var, value="Cats").pack()
        tk.Radiobutton(self, text="Dogs", variable=self.pets_var, value="Dogs").pack()

        self.subscribe_var = tk.BooleanVar()
        tk.Checkbutton(self, text="Subscribe to our Newsletter!", variable=self.subscribe_var).pack()

        self.country_var = tk.StringVar(value="SELECT")
        tk.Label(self, text="Select country:").pack(pady=5)
        countries = ["USA", "Canada", "Mexico", "UK", "India"]
        tk.OptionMenu(self, self.country_var, *countries).pack()

        tk.Button(self, text="Submit", command=self.on_click).pack(pady=10)

    def on_click(self):
        name = self.entry.get().capitalize()
        pets = self.pets_var.get()
        subscribed = self.subscribe_var.get()
        country = self.country_var.get()

        if not name:
            messagebox.showwarning("Input needed", "Please enter your name")
            return
        
        if country.lower() == "select":
            messagebox.showwarning("Input needed", "Pick one of the countries!")
            return
        
        info = f"Name: {name}\nPets: {pets}\nSubscribed: {subscribed}\nCountry: {country}"
        messagebox.showinfo("Submission info", info)


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
        