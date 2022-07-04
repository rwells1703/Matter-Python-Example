#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title('Demo')

    frame = ttk.Frame(root)
    frame.grid()

    options = {}

    name = tk.StringVar()
    name_entry = ttk.Entry(frame, textvariable=name)
    name_entry.grid(column=0, row=0, sticky='W', **options)

    button1 = ttk.Button(frame, text='Hello')
    button2 = ttk.Button(frame, text='World')

    button1.grid(column=1, row=0, sticky='W', **options)
    button2.grid(column=2, row=0, sticky='W', **options)

    text = tk.Text(frame, wrap=tk.WORD)
    text.grid(column=0, row=1, columnspan=3, **options)

    root.eval('tk::PlaceWindow . center')
    root.mainloop()

if __name__ == "__main__":
    main()