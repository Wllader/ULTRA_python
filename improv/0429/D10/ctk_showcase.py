import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CutomTkinter App")
app.geometry("400x400")

label = ctk.CTkLabel(app, text="Tohle je hezčí aplikace!", font=("Consolas", 20))
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Enter text", border_color="lightblue")
entry.pack(pady=10)

ctk.CTkButton(app, text="Click me!").pack(pady=10)
ctk.CTkTextbox(app, text_color="#ab1269").pack(pady=10)
ctk.CTkCheckBox(app, width=200, height=100).pack(pady=10)

ctk.CTkSegmentedButton(app, values=["Option1", "Option2", "Albert"]).pack(pady=10)
ctk.CTkSlider(app, from_=0, to=100, number_of_steps=12).pack(pady=10)
pg = ctk.CTkProgressBar(app, mode="determinate")
pg.set(0.73)
pg.pack(pady=10)


om = ctk.CTkOptionMenu(app, values=["Option1", "Option2", "Albert"]).pack(pady=10)


frame = ctk.CTkFrame(app, fg_color="#696969")
ctk.CTkButton(frame, text="Btn1").grid(row=0, column=0, sticky="nesw")
ctk.CTkButton(frame, text="Btn2").grid(row=1, column=1, sticky="nesw")

frame.pack(pady=10)



app.mainloop()