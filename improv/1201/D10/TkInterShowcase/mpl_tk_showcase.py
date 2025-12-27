import customtkinter as ctk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigC

import numpy as np

plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")


app = ctk.CTk()
canvas_frame = ctk.CTkFrame(app)

x = np.linspace(-5, 3*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Axis x")
ax.set_ylabel("Axis y")
ax.set_title("Test plot")
ax.grid(True)
fig.tight_layout()

canvas = FigC(fig, master=canvas_frame)
canvas.draw()
canvas.get_tk_widget().pack()

canvas_frame.pack()

app.mainloop()