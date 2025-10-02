import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("CustomTkInter App")
app.geometry("400x400")

label = ctk.CTkLabel(app, text="Hello, CustomTkInter!")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Enter text")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Click me", command=lambda: print("Clicked!"), hover_color="#DABE25")
button.pack(pady=10)

textbox = ctk.CTkTextbox(app, width=200, height=100)
textbox.pack(pady=10)

var = ctk.BooleanVar()
checkbox = ctk.CTkCheckBox(app, text="Accept Terms", variable=var)
checkbox.pack(pady=10)

ctk.CTkButton(app, text="Check checkbox", command=lambda: print(checkbox.get(), var.get())).pack(pady=10)


seg_button = ctk.CTkSegmentedButton(app, values=["Option 1", "Option 2"])
seg_button.pack(pady=10)



progress = ctk.CTkProgressBar(app, mode='determinate')
progress.set(0.5)
progress.pack(pady=10)


slider = ctk.CTkSlider(app, from_=0, to=100, number_of_steps=5, command=lambda e: progress.set(slider.get() / slider._to))
slider.pack(pady=10)



option_menu = ctk.CTkOptionMenu(app, values=["Option A", "Option B"])
option_menu.pack(pady=10)

selected = option_menu.get()




app.mainloop()