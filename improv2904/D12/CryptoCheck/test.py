import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigC


import customtkinter as ctk


x = np.linspace(-10, 10, 150)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

fig.tight_layout()

app = ctk.CTk()

canvas_frame = ctk.CTkFrame(app)
canvas_frame.pack()

canvas = FigC(fig, master=canvas_frame)
canvas.draw()
canvas.get_tk_widget().pack()

slider = ctk.CTkSlider(app, from_=1, to=365, command=lambda v: print(int(v)))
slider.pack()


app.mainloop()