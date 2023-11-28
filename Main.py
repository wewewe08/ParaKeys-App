import time
import tkinter as tk
from queue import Queue

if __name__ == "__main__":
        root = tk.Tk()
        root.title("input-overlay")
        root.eval("tk::PlaceWindow . center") #centers window

        global input_label, input_text

        input_text = ""
        input_label = tk.Label(
                root,
                text="type something!",
                font=("Arial", 40),
                pady=10
        )
        input_label.pack()

        keys_pressed = set()
        displayed_keys = set()

        def on_press(event):
                global input_text
                current_key = event.keysym.upper()

                if len(displayed_keys) > 0 and input_text != "":
                        input_text = ""
                        keys_pressed.clear()
                        displayed_keys.clear()

                if current_key not in keys_pressed:
                        keys_pressed.add(current_key)
                        input_text = current_key if input_text == "" else input_text + " + " + current_key

        def on_release(event):
                global input_label, input_text, displayed_keys
                try:
                        input_label["text"] = input_text
                        displayed_keys.add(input_text)
                except KeyError:
                        pass

        root.bind('<KeyPress>', on_press)
        root.bind('<KeyRelease>', on_release)
        root.mainloop()