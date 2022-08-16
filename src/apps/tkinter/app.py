import tkinter as tk
from tkinter import ttk

from ...controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Matter example')

        self.frame = ttk.Frame(self)
        self.frame.grid()

        self.toggle_button = ttk.Button(self.frame, text='Toggle')
        self.toggle_button.grid(column=0, row=0, sticky='nsew')

        self.read_button = ttk.Button(self.frame, text='Read')
        self.read_button.grid(column=1, row=0, sticky='nsew')

        self.onoff_val = tk.IntVar()
        self.onoff_label = tk.Label(self.frame, textvariable=self.onoff_val)
        self.onoff_label.grid(column=0, row=1, columnspan=2, sticky='nsew')
        
        self.open_connect_window()

    def open_connect_window(self):
        connect_window = ConnectWindow(self)
        connect_window.grab_set()

    def connect_controller(self, connection_window, device_ip, device_pin_code, device_node_id):
        self.controller = Controller(1, device_ip, device_pin_code, device_node_id)
        self.controller.commission_device()

        self.load_ui()

        connection_window.destroy()

    def load_ui(self):
        self.toggle_button.configure(command=self.toggle_light)
        self.read_button.configure(command=self.read_light)

        self.read_light()

    def toggle_light(self):
        self.controller.toggle_light()
        self.read_light()

    def read_light(self):
        onoff_result = self.controller.read_light()
        self.onoff_val.set("On" if onoff_result.value else "Off")

class ConnectWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Connect Window')
        self.geometry('300x100')
        
        frame = ttk.Frame(self)
        frame.grid()

        device_ip = tk.StringVar()

        ip_label = ttk.Label(frame, text='IP')
        ip_label.grid(column=0, row=0, sticky='nsew')

        ip_entry = ttk.Entry(frame, textvariable=device_ip)
        ip_entry.grid(column=1, row=0, sticky='nsew')
        device_ip.set("2a00:23a8:89b:da01:5bac:df45:7887:b359")

        device_pin_code = tk.IntVar()

        pin_code_label = ttk.Label(frame, text='Pin Code')
        pin_code_label.grid(column=0, row=1, sticky='nsew')

        pin_code_entry = ttk.Entry(frame, textvariable=device_pin_code)
        pin_code_entry.grid(column=1, row=1, sticky='nsew')
        device_pin_code.set(20202021)

        device_node_id = tk.IntVar()

        node_id_label = ttk.Label(frame, text='Node ID')
        node_id_label.grid(column=0, row=2, sticky='nsew')

        node_id_entry = ttk.Entry(frame, textvariable=device_node_id)
        node_id_entry.grid(column=1, row=2, sticky='nsew')
        device_node_id.set(1234)

        connect_button = ttk.Button(frame, text='Connect', command=lambda: parent.connect_controller(self, device_ip.get(), device_pin_code.get(), device_node_id.get()))
        connect_button.grid(column=0, row=3)


if __name__ == "__main__":
    app = App()
    app.eval('tk::PlaceWindow . center')
    app.mainloop()