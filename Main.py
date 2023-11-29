import tkinter as tk

from MainWindow import MainWindow

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.main_window = MainWindow(self.parent)
        self.main_window.pack(side="top", fill="both")

if __name__ == "__main__":
        root = tk.Tk()
        root.title("ParaKeys")
        root.iconbitmap("parakeet.ico")
        root.config(bg="#26242f")
        root.geometry("270x180")
        root.resizable(width=False, height=False)

        app = MainApp(root)
        root.bind('<KeyPress>', app.main_window.on_press)
        root.bind('<KeyRelease>', app.main_window.on_release)
        root.mainloop()