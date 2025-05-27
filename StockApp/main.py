import customtkinter as ctk
from typing import Callable

from input_frame import InputFrame
from plot_frame import PlotFrame

class CryptoCheck(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CryptoCheck")
        self.geometry("800x800")

        self.main_frame = InputFrame(self, self.add_tab)
        self.main_frame.pack()

        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack()

        self.to_destroy = []

        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def add_tab(self):
        name = self.main_frame.symbol

        tab = self.tab_view.add(name)
        pf = PlotFrame(tab, name)
        if not pf.update_plot(name, self.main_frame.days): #new
            self.tab_view.delete(name)
            return
        
        pf.pack()

        self.to_destroy.append(pf.on_closing)

        self.tab_view.set(name)

    def on_closing(self):
        for c in self.to_destroy:
            c()

        self.quit() #new musí tu být
        self.destroy()
            



if __name__ == "__main__":
    app = CryptoCheck()
    app.mainloop()


        