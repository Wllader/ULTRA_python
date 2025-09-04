import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TkInter example app")
root.geometry("400x400")

tk.Label(root, text="Zadej jméno:").pack(pady=5)
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

pets = tk.StringVar(value="None")
tk.Label(root, text="Vyber svoje oblíbené zvířátko:").pack(pady=5)
tk.Radiobutton(root, text="Kočka", variable=pets, value="Kočka").pack()
tk.Radiobutton(root, text="Pes", variable=pets, value="Pes").pack()

subscribed = tk.BooleanVar()
tk.Checkbutton(root, text="Přihlásit se k odběru?", variable=subscribed).pack(pady=5)

country = tk.StringVar(value="Vyber")
tk.Label(root, text="Vyber zemi:").pack(pady=5)
countries = ["Česká republika", "Slovenská republika", "Německo", "Itálie", "Rakousko"]
tk.OptionMenu(root, country, "Vyber", *countries).pack()

def on_click():
    name = entry.get()
    pet = pets.get()
    sub = subscribed.get()
    cntry = country.get()

    if not name:
        messagebox.showwarning("Chybí povinná informace", "Prosím uveďte svoje jméno!")
        return
    
    if cntry == "Vyber":
        messagebox.showwarning("Chybí povinná informace", "Prosím vyber zemi")
        return

    info = f"Jméno: {name}\nDomácí mazlíček: {pet}\nOdběr: {sub}\nZemě: {cntry}"
    messagebox.showinfo("Informace o dotazníku", info)

tk.Button(root, text="Poslat", command=on_click).pack(pady=10)


root.mainloop()
