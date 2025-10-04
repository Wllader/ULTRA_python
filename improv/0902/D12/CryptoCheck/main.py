import customtkinter as ctk
from input_frame import InputFrame
from plot_frame import PlotFrame

from typing import Callable

class CryptoCheck(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CryptoCheck")
        self.geometry("800x800")

        self.input_frame = InputFrame(self, fetch=self.add_tab)
        self.input_frame.pack(padx=10, pady=10)

        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(padx=10, pady=10)

        self.call_on_closing:list[Callable] = []
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.bind("<Key>", func=lambda event: self.add_tab() if event.keysym == "Return" else None)

    def add_tab(self):
        name:str = self.input_frame.symbol
        if name == "" or name.isspace(): return

        tab = self.tab_view.add(name)
        pf = PlotFrame(tab, name.lower())
        pf.update_plot(name.lower(), self.input_frame.days)

        pf.pack()
        self.tab_view.set(name)

        self.call_on_closing.append(pf.on_closing)
        self.clear_inputs()


    def clear_inputs(self):
        self.input_frame.symbol_entry.delete(0, ctk.END)
        self.input_frame.days_entry.delete(0, ctk.END)
        self.input_frame.symbol_entry.focus()


    def on_closing(self):
        for f in self.call_on_closing:
            f()

        self.quit()


if __name__ == "__main__":
    app = CryptoCheck()
    app.mainloop()