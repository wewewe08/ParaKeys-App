import tkinter as tk
from PIL import ImageTk, Image

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Title Label
        img = ImageTk.PhotoImage(Image.open("title_label.png"))
        image_label = tk.Label(
            self.parent,
            image=img,
            bg="#26242f",
            pady=5)
        image_label.pack(side="top", anchor="center")
        image_label.image = img

        # Display Label
        global input_label, input_text, displayed_keys
        input_text = ""
        displayed_keys = set()
        input_label = tk.Label(
                self.parent,
                text="{}",
                font=("Arial", 20),
                bg="#26242f",
                fg="white",
                wraplength=180,
                pady=10)
        input_label.pack(side="top")

    def on_press(self, event):
        global input_text, displayed_keys
        keys_pressed = set()
        current_key = event.keysym.upper()

        if len(displayed_keys) > 0 and input_text != "":
                input_text = ""
                keys_pressed.clear()
                displayed_keys.clear()

        if current_key not in keys_pressed:
                keys_pressed.add(current_key)
                input_text = current_key if input_text == "" else input_text + " + " + current_key

    def on_release(self, event):
        global input_label, input_text, displayed_keys
        try:
                input_label["text"] = input_text
                displayed_keys.add(input_text)
        except KeyError:
                pass