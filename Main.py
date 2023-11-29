import tkinter as tk
import os, sys
from MainWindow import MainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        if getattr(sys, 'frozen', False):
            path = os.path.dirname(sys.executable)
        elif __file__:
            path = os.path.dirname(__file__)
    except Exception:
        path = os.path.abspath(".")

    return os.path.join(path, relative_path)

Logo = resource_path("../parakeet.ico")

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.main_window = MainWindow(self.parent)
        self.main_window.pack(side="top", fill="both")

if __name__ == "__main__":
        root = tk.Tk()
        root.title("ParaKeys")
        root.iconbitmap(bitmap=Logo)
        root.config(bg="#26242f")
        root.geometry("270x180")
        root.resizable(width=False, height=False)

        app = MainApp(root)
        root.bind('<KeyPress>', app.main_window.on_press)
        root.bind('<KeyRelease>', app.main_window.on_release)
        root.mainloop()