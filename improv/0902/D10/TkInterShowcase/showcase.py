import tkinter as tk

root = tk.Tk()
root.title("My app")
root.geometry("300x600")


label = tk.Label(root, text="Hello, TkInter!")
styled_label = tk.Label(root, text="Styled text", fg="blue", bg="yellow", font=("Arial", 14))

label.pack()
styled_label.pack()

entry = tk.Entry(root)
entry.pack()

# value = entry.get()
entry.insert(0, "Default text")


button = tk.Button(root, text="Click Me", command=lambda: print(entry.get()))
button.pack()

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()



text = tk.Text(root, height=2, width=30)
text.pack()


varA = tk.BooleanVar()
check = tk.Checkbutton(root, text="Check me", variable=varA)
check.pack()

tk.Button(root, text="Click me", command=lambda: print(varA.get())).pack()


varB = tk.StringVar(value="0")
varC = tk.StringVar(value="?")
rb1 = tk.Radiobutton(root, text="Option 1", variable=varB, value="1")
rb2 = tk.Radiobutton(root, text="Option 2", variable=varB, value="2")
rb3 = tk.Radiobutton(root, text="Option 3", variable=varC, value="3")
rb1.pack()
rb2.pack()
rb3.pack()
tk.Button(root, text="Click me", command=lambda: print(varB.get())).pack()


listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()


frame = tk.Frame(root, bg="yellow")
tk.Button(frame, text="Quit", command=root.destroy).grid(row=0, column=0)
tk.Button(frame, text="Ahoj", command=lambda: print("Ahoj")).grid(row=5, column=5)
frame.pack()
tk.Button(root, text="Ahoj", command=lambda: print("Ahoj")).pack()

from tkinter import messagebox

tk.Button(root, text="Messagebox", command=lambda: messagebox.showwarning("Title", "Text")).place(x=50, y=60)

def on_key(event:tk.Event):
    print("You pressed", event.keysym)

root.bind("<Key>", on_key)

root.mainloop()