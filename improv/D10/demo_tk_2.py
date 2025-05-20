import tkinter as tk
from tkinter import messagebox

class ExampleApp(tk.Frame):
    def __init__(self, master = None,):
        super().__init__(master)

        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text="Zadej jméno:").pack(pady=5)
        self.entry = tk.Entry(self, width=25)
        self.entry.pack(pady=5)

        self.pets = tk.StringVar(value="None")
        tk.Label(self, text="Vyber svoje oblíbené zvířátko:").pack(pady=5)
        tk.Radiobutton(self, text="Kočka", variable=self.pets, value="Kočka").pack()
        tk.Radiobutton(self, text="Pes", variable=self.pets, value="Pes").pack()

        self.subscribed = tk.BooleanVar()
        tk.Checkbutton(self, text="Přihlásit se k odběru?", variable=self.subscribed).pack(pady=5)

        self.country = tk.StringVar(value="Vyber")
        tk.Label(self, text="Vyber zemi:").pack(pady=5)
        countries = ["Česká republika", "Slovenská republika", "Německo", "Itálie", "Rakousko"]
        tk.OptionMenu(self, self.country, "Vyber", *countries).pack()

        tk.Button(self, text="Poslat", command=self._on_click).pack(pady=10)

    def _on_click(self):
        name = self.entry.get()
        pet = self.pets.get()
        sub = self.subscribed.get()
        cntry = self.country.get()

        if not name:
            messagebox.showwarning("Chybí povinná informace", "Prosím uveďte svoje jméno!")
            return
        
        if cntry == "Vyber":
            messagebox.showwarning("Chybí povinná informace", "Prosím vyber zemi")
            return

        info = f"Jméno: {name}\nDomácí mazlíček: {pet}\nOdběr: {sub}\nZemě: {cntry}"
        messagebox.showinfo("Informace o dotazníku", info)


if __name__ == "__main__":
    root = tk.Tk()

    ExampleApp(root).grid(row=0, column=0, sticky="we")
    ExampleApp(root).grid(row=1, column=1, sticky="ns")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    root.mainloop()