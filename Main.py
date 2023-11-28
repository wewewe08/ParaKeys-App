import tkinter as tk
import pynput
from pynput.keyboard import Listener

if __name__ == "__main__":
        root = tk.Tk()
        root.title("input-overlay")
        root.eval("tk::PlaceWindow . center") #centers window

        global input_label
        input_label = tk.Label(
                root,
                text="test",
                font=("Arial", 40),
                pady=10
        )
        input_label.pack()

        def on_release(event):
                global input_label
                input_text = event.keysym
                input_label["text"] = input_text.upper()

        root.bind('<KeyRelease>', on_release)
        root.mainloop()