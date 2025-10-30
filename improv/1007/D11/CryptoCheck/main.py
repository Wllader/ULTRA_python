import customtkinter as ctk

from typing import Callable

class CryptoCheck(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CryptoCheck")
        self.geometry("800x800")
        