import customtkinter as ctk
from data_fetcher import Fetcher, CryptoFetcher

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigC
import pandas as pd

from input_frame import TickerType

class PlotFrame(ctk.CTkFrame):
    def __init__(self, master, symbol:str, type_:TickerType = TickerType.COIN, **kwargs):
        super().__init__(master, **kwargs)
        self.symbol = symbol
        self.type = type_

        self.canvas_frame = ctk.CTkFrame(self)
        self.canvas_frame.pack(fill="both", expand=True)

        self.days_slider = ctk.CTkSlider(self, from_=1, to=365, command=self.update_slider)
        self.days_slider.set(30)
        self.slider_label = ctk.CTkLabel(self, text=f"Adjust Number of days: {30}")

        self.slider_label.pack(padx=10, pady=10)
        self.days_slider.pack(padx=10, pady=10)

        ctk.CTkButton(self, text="Refresh", command=lambda: self.update_plot(self.symbol, self.days)).pack()

        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

    @property
    def days(self):
        return int(self.days_slider.get())
    
    @days.setter
    def days(self, value):
        self.update_slider(value)
        self.days_slider.set(value)

    def update_slider(self, value):
        self.slider_label.configure(text=f"Adjust Number of days: {int(value)}")

    def fetch_data(self, symbol) -> pd.DataFrame | None:
        f: Fetcher

        match self.type:
            case TickerType.COIN:
                url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
                params = {
                    "vs_currency" : "usd",
                    "days" : self.days
                }

                f = CryptoFetcher(url, "cache.db")

            case TickerType.SHARE:
                print("Not implemented")
                return None
                f = ShareFetcher("", "")


        return f.get(symbol, params)


    def update_plot(self, symbol:str, days:int):
        df = self.fetch_data(symbol)
        if df is None: return
        
        for w in self.canvas_frame.winfo_children():
            w.destroy()
        
        fig, ax = plt.subplots()
        ax.plot(df["Timestamp"], df["Price"])
        ax.set_xlabel("Date")
        ax.set_ylabel("USD")
        ax.set_title(f"{symbol.capitalize()} price History of last {days} days")
        ax.tick_params("x", rotation=60)
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
    PlotFrame(app, "ethereum").pack()

    app.mainloop()