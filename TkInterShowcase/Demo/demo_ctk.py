import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (default), "green", "dark-blue"

class ExampleApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Example App")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        # Label
        label = ctk.CTkLabel(self, text="Enter your name:")
        label.pack(pady=10)

        # Entry
        self.entry = ctk.CTkEntry(self, width=200)
        self.entry.pack()

        # RadioButtons
        self.pets = ctk.StringVar(value="None")
        ctk.CTkLabel(self, text="Select Pet:").pack(pady=10)
        ctk.CTkRadioButton(self, text="Cats", variable=self.pets, value="Cats").pack()
        ctk.CTkRadioButton(self, text="Dogs", variable=self.pets, value="Dogs").pack()

        # CheckBox
        self.subscribe_var = ctk.BooleanVar()
        ctk.CTkCheckBox(self, text="Subscribe to newsletter", variable=self.subscribe_var).pack(pady=10)

        # Dropdown Menu
        ctk.CTkLabel(self, text="Select Country:").pack(pady=10)
        self.country_var = ctk.StringVar(value="Select")
        countries = ["USA", "Canada", "Mexico", "UK", "India"]
        self.country_menu = ctk.CTkOptionMenu(self, variable=self.country_var, values=countries)
        self.country_menu.pack()

        # Button
        button = ctk.CTkButton(self, text="Submit", command=self.on_click)
        button.pack(pady=20)

    def on_click(self):
        name = self.entry.get()
        gender = self.pets.get()
        subscribed = self.subscribe_var.get()
        country = self.country_var.get()

        if not name:
            messagebox.showwarning("Input needed", "Please enter your name.")
            return

        info = f"Name: {name}\nGender: {gender}\nSubscribed: {subscribed}\nCountry: {country}"
        messagebox.showinfo("Submission Info", info)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()