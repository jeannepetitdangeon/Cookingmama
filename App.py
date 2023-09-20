from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from CookingMama_1 import Data
from Choice_button import Choice_button
from bs4 import BeautifulSoup
import requests
import random

# pip install ttkthemes

class App:
    # initializes the theme and app window 
    def __init__(self):
        self.root = ThemedTk(theme='Adapta')
        self.root.geometry('400x500')
        self.frame = None

    def clear_frame(self):
        # print('init')
        for widgets in self.frame.winfo_children():
            print('for')
            widgets.destroy()

    # launches the app
    def launch(self):
        self.show_start()
        # this function runs the app
        self.root.mainloop()

    # first menu display
    def show_start(self):
        self.frame = Frame(self.root)
        self.frame.pack(expand=False)

        category_choice_text = Text(self.frame, fg="black", padx=70, pady=30)
        category_choice_text.insert(1.0, "Choisissez une catégorie :")
        category_choice_text.config(font=("arial", 16), state=DISABLED)
        category_choice_text.pack()

        data = Data()

        y=0.2
        i=0

        def show_random_meal():
            self.clear_frame()
            data.get_random_subcategory()
        
        for category in data.valid_main_categories:
            formatted_name = category.replace('-', ' ')
            formatted_name = formatted_name.capitalize()

            category_button = Choice_button(formatted_name, category, data, show_random_meal)
            category_button.button.place(relx=0.5, rely=y + i, anchor=CENTER)
            i = i + 0.1

class Data:
    def __init__(self):
        self.valid_main_categories = ['viande', 'poisson', 'fruits-de-mer', 'plat-unique', 'œufs', 'plat-vegetarien', 'pates-riz-semoule', 'plats-au-fromage']
        self.subcategories = []

    def set_subcategories(self, new_subcategories):
        self.subcategories = new_subcategories

    def get_random_subcategory(self):
        random_subcategory = random.choice(self.subcategories)
        print("choice: " + random_subcategory)

app = App()
app.launch()