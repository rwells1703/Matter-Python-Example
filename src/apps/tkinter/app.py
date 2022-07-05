#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title('Matter example')

    frame = ttk.Frame(root)
    frame.grid()

    toggle_button = ttk.Button(frame, text='Toggle')
    read_button = ttk.Button(frame, text='Read')

    toggle_button.grid(column=0, row=0, sticky='nsew')
    read_button.grid(column=1, row=0, sticky='nsew')

    text = tk.Text(frame, wrap=tk.WORD)
    text.grid(column=0, row=2, columnspan=2, sticky='nsew')


    root.eval('tk::PlaceWindow . center')
    root.mainloop()

if __name__ == "__main__":
    main()