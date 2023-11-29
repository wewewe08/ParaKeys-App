import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        global input_label, input_text, displayed_keys

        input_text = ""
        displayed_keys = set()
        input_label = tk.Label(
                self.parent,
                text="type something!",
                font=("Arial", 30),
                wraplength=300,
                pady=10
        )
        input_label.pack()

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