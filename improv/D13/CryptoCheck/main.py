import customtkinter as ctk
from input_frame import InputFrame
from plot_frame import PlotFrame

class CryptoCheck(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CryptoCheck")
        self.geometry("800x900")

        self.main_frame = InputFrame(self, self.add_tab)
        self.main_frame.pack(padx=10, pady=10)

        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(padx=10, pady=10)

        self.call_on_closing = []
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_tab(self):
        name = self.main_frame.symbol

        tab = self.tab_view.add(name)
        pf = PlotFrame(tab, name, self.main_frame.days)
        # todo Check if ticker exist and do not create tab if it doesn't
        pf.update_plot(name)
        pf.pack()

        self.call_on_closing.append(pf.on_closing)

        self.tab_view.set(name)

    def on_closing(self):
        for f in self.call_on_closing:
            f()

        self.quit()
        self.destroy()


if __name__ == "__main__":
    app = CryptoCheck()
    app.mainloop()