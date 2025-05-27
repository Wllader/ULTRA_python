import customtkinter as ctk
import requests
from pandas import to_datetime
from typing import Any, Callable

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigC

class PlotFrame(ctk.CTkFrame):
    def __init__(self, master, symbol:str, days=30, **kwargs):
        super().__init__(master, **kwargs)
        self.symbol = symbol

        self.canvas_frame = ctk.CTkFrame(self)
        self.canvas_frame.pack(fill="both", expand=True)

        self.days_slider = ctk.CTkSlider(self, from_=1, to=365, command=self.update_slider)
        self.days_slider.set(days)
        self.slider_label = ctk.CTkLabel(self, text=f"Adjust Number of days: {days}")

        self.slider_label.pack(padx=10, pady=10)
        self.days_slider.pack(padx=10, pady=10)

        ctk.CTkButton(self, text="Refresh", command=lambda: self.update_plot(self.symbol)).pack()

        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

    @property
    def days(self):
        return int(self.days_slider.get())
    
    def update_slider(self, value):
        self.slider_label.configure(text=f"Adjust Number of Days: {int(value)}")

    def fetch_crypto_data(self, symbol) -> dict[str, Any]: #todo return pd.Dataframe
        url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
        params = {
            "vs_currency" : "usd",
            "days" : self.days
        }

        response = requests.get(url, params=params)
        return response.json()

    def update_plot(self, symbol:str):
        data = self.fetch_crypto_data(symbol)

        for w in self.canvas_frame.winfo_children():
            w.destroy()

        fig, ax = plt.subplots()
        if "status" in data:
            print("Rate exceeded!")
            return
        
        dates = [ to_datetime(item[0], unit="ms") for item in data["prices"] ] #todo get rid of this
        prices = [ item[1] for item in data["prices"] ]

        ax.plot(dates, prices) #todo use df["Date"], df["Price"]
        ax.set_xlabel("Date")
        ax.set_ylabel("USD")
        ax.set_title(f"{symbol.capitalize()} price History of last {self.days} days")
        ax.tick_params("x", rotation=60)
        ax.grid(True)
        
        fig.tight_layout()

        canvas =  FigC(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def on_closing(self):
        if self.canvas_frame:
            for w in self.canvas_frame.winfo_children():
                w.destroy()

        self.quit()
        self.destroy()

if __name__ == "__main__":
    app = ctk.CTk()
    pf = PlotFrame(app)
    pf.pack()

    app.mainloop()