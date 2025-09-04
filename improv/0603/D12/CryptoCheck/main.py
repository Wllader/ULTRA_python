import customtkinter as ctk
from input_frame import InputFrame
from plot_frame import PlotFrame

class CryptoCheck(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CryptoCheck")
        self.geometry("800x800")

        self.main_frame = InputFrame(self, self.add_tab)
        self.main_frame.pack(padx=10, pady=10)

        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(padx=10, pady=10)

        self.call_on_closing = []
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.bind("<Key>", func=lambda event: self.add_tab() if event.keysym == "Return" else None)

    def add_tab(self):
        name = self.main_frame.symbol
        if name == "": return

        tab = self.tab_view.add(name)
        pf = PlotFrame(tab, name.lower())
        pf.update_plot(name, self.main_frame.days)

        pf.pack()
        self.tab_view.set(name)

        self.call_on_closing.append(pf.on_closing)
        self.clear_inputs()
        self.main_frame.symbol_entry.focus()

    def clear_inputs(self):
        self.main_frame.symbol_entry.delete(0, ctk.END)
        self.main_frame.days_entry.delete(0, ctk.END)

    def on_closing(self):
        for f in self.call_on_closing:
            f()


if __name__ == "__main__":
    app = CryptoCheck()
    app.mainloop()