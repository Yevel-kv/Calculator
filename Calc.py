#!/usr/bin/env python3

import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(master, width=15, font=("Arial", 18), bd=10, insertwidth=1, bg="#6495DE", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        row = 1
        col = 0
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", 
            "=",
        ]

        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        print(f"\n[!] Este metodod aun no esta implementado")

    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=6, command=self.clear_display)
        elif button == "=":
            b = tk.Button(self.master, text=button, width=6, command=self.calculate)
        else:
            b = tk.Button(self.master, text=button, width=6)
        b.grid(row=row, column=col)

root = tk.Tk()
my_gui = Calculadora(root)
root.mainloop()