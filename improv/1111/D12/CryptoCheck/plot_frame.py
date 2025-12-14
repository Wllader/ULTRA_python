import customtkinter as ctk
from typing import Any
import requests

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigC


class PlotFrame(ctk.CTkFrame):
    def __init__(self, master, symbol:str, **kwargs):
        super().__init__(master, **kwargs)
        self.symbol = symbol

        self.canvas_frame = ctk.CTkFrame(self)
        self.canvas_frame.pack(fill="both", expand=True)

        self.days_slider = ctk.CTkSlider(self, from_=1, to=365, command=self.update_slider)
        self.days_slider.set(30)
        self.slider_label = ctk.CTkLabel(self, text="Adjust Number of days: 30")

        self.slider_label.pack(padx=10, pady=10)
        self.days_slider.pack(padx=10, pady=10)

        ctk.CTkButton(self, text="Refresh", command=lambda: self.update_plot(self.symbol, self.days)).pack()

        plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")

    @property
    def days(self):
        return int(self.days_slider.get())
    
    @days.setter
    def days(self, value):
        self.update_slider(value)

    def update_slider(self, value):
        self.days_slider.set(value)
        self.slider_label.configure(text=f"Adjust Number of days: {int(value)}")

    
    def fetch_crypto_data(self, symbol, days) -> dict[str, Any]:
        url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
        params = {
            "vs_currency" : "usd",
            "days" : days
        }

        response = requests.get(url, params)
        return response.json()
    
    def update_plot(self, symbol:str, days:int):
        data = self.fetch_crypto_data(symbol, days)

        if "status" in data:
            print(data["status"])
            return
        
        if "error" in data:
            print(data["error"])
            return
        
        for w in self.canvas_frame.winfo_children():
            w.destroy()

        timestamps, prices = zip(*data["prices"])

        fig, ax = plt.subplots()
        ax.plot(timestamps, prices)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.set_title(f"{symbol.capitalize()} price History over last {days} days")
        ax.grid(True)

        fig.tight_layout()

        canvas = FigC(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.days = days

    def on_closing(self):
        if self.canvas_frame:
            for w in self.canvas_frame.winfo_children():
                w.destroy()

            self.quit()
            self.destroy()


if __name__ == "__main__":
    app = ctk.CTk()
    PlotFrame(app, "bitcoin").pack()

    app.mainloop()