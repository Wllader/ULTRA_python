import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Moje aplikace")
root.geometry("300x200")

label = tk.Label(root, text="Já jsem Label!", fg="blue", font=("Consolas", 15), pady=15)
label.pack()

entry = tk.Entry(root)
entry.pack()

entry.insert(0, "Test")


btn = tk.Button(root, text="Klikni na mě!", command=lambda: print(entry.get()))
btn_quit = tk.Button(root, text="Ukončit", command=root.destroy)
btn.pack()
btn_quit.pack()

textb = tk.Text(root, height=3, width=30)
textb.pack()

textb.insert(1.0, "Tohle je textbox!")


check_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Zaškrtni mě!", variable=check_var)
check.pack()

btn = tk.Button(root, text="Zjisti stav checkboxu", command=lambda: print(check_var.get()))
btn.pack()


rb_var = tk.StringVar()
rb1 = tk.Radiobutton(root, text="Možnost 1", variable=rb_var, value="O1")
rb2 = tk.Radiobutton(root, text="Možnost 2", variable=rb_var, value="O2")
rb1.pack()
rb2.pack()

btn = tk.Button(root, text="Zjisti stav checkboxu", command=lambda: print(rb_var.get()))
btn.pack()


listbox = tk.Listbox(root)
listbox.insert(0, "Položka 1")
listbox.insert(1, "Položka 2")
listbox.pack()


frame = tk.Frame(root)
btnA = tk.Button(frame, text="Tl. A")
btnB = tk.Button(frame, text="Tl. B")

btnA.grid(row=0, column=0)
btnB.grid(row=1, column=1)

frame.pack()

btn = tk.Button(root, text="Random tlačítko")
btn.place(x=50, y=150)


def on_key(event:tk.Event):
    print("Zmáčkl jsi: ", event.char)


textb.bind("<Key>", on_key)

btn = tk.Button(root, text="Ukaž messagebox!", command=lambda: messagebox.showerror("MsgBx", "Tady máš messagebox!")).pack()


om_var = tk.StringVar(value="Vyber")
om = tk.OptionMenu(root, om_var, *["Zmrzlina", "Steak", "Koleno"])
om.pack()
 

root.mainloop()