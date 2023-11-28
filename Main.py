import tkinter as tk

from InputWindow import InputWindow

class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.input_window = InputWindow(self.parent)

        self.input_window.pack(side="top", fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("input-overlay")
    root.eval("tk::PlaceWindow . center") #centers window

    app = Main(root)
    root.mainloop()