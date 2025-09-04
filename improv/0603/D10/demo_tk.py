import tkinter as tk
from tkinter import messagebox

class ExampleApp(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title("TkInter Example App")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        #Label
        tk.Label(self, text="Enter your name:").pack(pady=5)

        #Entry
        self.entry = tk.Entry(self, width=25)
        self.entry.pack()

        #RadioButtons
        self.pets_var = tk.StringVar(value="None")
        tk.Label(self, text="Selcet your favorite pet:").pack(pady=5)
        tk.Radiobutton(self, text="Cats", variable=self.pets_var, value="Cats").pack()
        tk.Radiobutton(self, text="Dogs", variable=self.pets_var, value="Dogs").pack()

        #CheckBox
        self.subscribe_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self, text="Subscribe to newsletter", variable=self.subscribe_var).pack(pady=5)

        #Dropdown Menu
        self.country_var = tk.StringVar(value="Select")
        tk.Label(self, text="Select Country:").pack(pady=5)
        countries = ["USA", "Canada", "Mexico", "UK", "India"]
        tk.OptionMenu(self, self.country_var, *countries).pack()

        #Button
        tk.Button(self, text="Submit", command=self.on_click).pack(pady=10)

    def on_click(self):
        name = self.entry.get()
        pets = self.pets_var.get()
        subscribed = self.subscribe_var.get()
        country = self.country_var.get()

        if not name:
            messagebox.showwarning("Input needed!", "Please enter your name.")
            return

        if country == "Select":
            messagebox.showerror("Country not found", "Please select valid country")
            return
        
        info = f"Name: {name}\nPets: {pets}\nSubscribed: {subscribed}\nCountry: {country}"
        messagebox.showinfo("Submission Info", info)


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
        
