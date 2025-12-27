import tkinter as tk

root = tk.Tk()
root.title("My app")
# root.geometry("300x600")

label = tk.Label(root, text="Hello, TkInter!")
styled_label = tk.Label(root, text="Styled text", fg="blue", bg="yellow", font=("Arial", 14))

label.pack()
styled_label.pack()


entry = tk.Entry(root)
entry.pack()


entry.insert(0, "Default text")

button = tk.Button(root, text="Click me!", command=lambda: print(entry.get()))
button.pack()

tk.Button(root, text="Quit", command=root.destroy).pack()


text = tk.Text(root, height=3, width=30)
text.pack()

varA = tk.BooleanVar()
check = tk.Checkbutton(root, text="Check me", variable=varA)
check.pack()
tk.Button(root, text="Click me!", command=lambda: print(varA.get())).pack()

varB = tk.StringVar(value="0")
varC = tk.StringVar(value="2")
tk.Radiobutton(root, text="Option 1", variable=varB, value="1").pack()
tk.Radiobutton(root, text="Option 2", variable=varB, value="2").pack()
tk.Radiobutton(root, text="Option 3", variable=varC, value="3").pack()
tk.Button(root, text="Click me!", command=lambda: print(varB.get())).pack()
tk.Button(root, text="Click me!", command=lambda: print(varC.get())).pack()


listbox = tk.Listbox(root)
listbox.insert(0, "Item 1", "Item 2")
listbox.insert(1, "Item A")
listbox.pack()

frame = tk.Frame(root, bg="yellow")
tk.Button(frame, text="Ahoj", command=lambda: print("Ahoj!")).grid(row=0, column=0)
tk.Button(frame, text="Ahoj?", command=lambda: print("Ahoj??")).grid(row=1, column=1)
tk.Button(frame, text="Čau", command=lambda: print("Čau!")).grid(row=2, column=2)
frame.pack()

from tkinter import messagebox
tk.Button(root, text="Error", command=lambda:messagebox.showerror("Title", "Text")).pack()
tk.Button(root, text="Warning", command=lambda:messagebox.showwarning("Title", "Text")).pack()
tk.Button(root, text="Info", command=lambda:messagebox.showinfo("Title", "Text")).pack()


def on_key(event:tk.Event):
    print("You pressed:", event.keysym)

root.bind("<Key>", on_key)

root.mainloop()