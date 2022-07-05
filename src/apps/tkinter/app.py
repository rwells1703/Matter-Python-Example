#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title('Matter example')

    frame = ttk.Frame(root)
    frame.grid()


    commission_button = ttk.Button(frame, text='Commission')
    toggle_button = ttk.Button(frame, text='Toggle')
    read_button = ttk.Button(frame, text='Read')

    commission_button.grid(column=0, row=0, sticky='nsew')
    toggle_button.grid(column=1, row=0, sticky='nsew')
    read_button.grid(column=2, row=0, sticky='nsew')

    text = tk.Text(frame, wrap=tk.WORD)
    text.grid(column=0, row=2, columnspan=3, sticky='nsew')


    root.eval('tk::PlaceWindow . center')
    root.mainloop()

if __name__ == "__main__":
    main()