import tkinter as tk
from tkinter import ttk

from ...controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        controller = Controller(1, "2a00:23a8:89b:da01:5bac:df45:7887:b359", 20202021, 1234)

        self.title('Matter example')

        frame = ttk.Frame(self)
        frame.grid()

        toggle_button = ttk.Button(frame, text='Toggle', command=controller.toggle_light)
        read_button = ttk.Button(frame, text='Read', command=controller.read_light)

        toggle_button.grid(column=0, row=0, sticky='nsew')
        read_button.grid(column=1, row=0, sticky='nsew')

        text = tk.Text(frame, wrap=tk.WORD)
        text.grid(column=0, row=2, columnspan=2, sticky='nsew')

        self.open_connect_window()

    def open_connect_window(self):
        connect_window = ConnectWindow(self)
        connect_window.grab_set()

class ConnectWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Connect Window')

        ttk.Button(self,
                text='Connect',
                command=self.destroy).pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.eval('tk::PlaceWindow . center')
    app.mainloop()