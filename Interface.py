# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:01:31 2023
Interface webapp
@author: epcmic
"""

import tkinter as tk

def button_click():
    label.config(text="Bonjour, " + entry.get())

app = tk.Tk()
app.title("Ma Application")

label = tk.Label(app, text="Entrez votre nom :")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Cliquez ici", command=button_click)
button.pack()

app.mainloop()

