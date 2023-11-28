import tkinter as tk
import pynput
from pynput.keyboard import Listener

class InputWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self.parent, 
                 text=key_pressed, 
                 font=("Arial", 40),
                 pady=10).pack()