import tkinter as tk
import pynput
from pynput.keyboard import Listener

if __name__ == "__main__":
    

    tk.Label(text="test", 
            font=("Arial", 40),
            pady=10).pack()

    root = tk.Tk()
    root.title("input-overlay")
    root.eval("tk::PlaceWindow . center") #centers window

    root.mainloop()