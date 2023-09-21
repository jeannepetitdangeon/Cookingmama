import os
import ttkthemes

exec(open('C:/Users/epcmic/OneDrive/Documents/GitHub/Cookingmama/CookingMama_1.py', encoding='utf-8').read())
exec(open('C:/Users/epcmic/OneDrive/Documents/GitHub/Cookingmama/Choice_button.py', encoding='utf-8').read())


from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
# from CookingMama_1.py import *
#from Choice_button import Choice_button
from bs4 import BeautifulSoup
import requests
import random

class App:
    # initializes the theme and app window 
    def __init__(self):
        self.data = None
        # window instanciation
        self.window = ThemedTk(theme='Adapta')
        self.window.geometry('400x500')

        # frames instanciation
        self.actual_frame = None
        self.start_frame = Frame(self.window)
        self.meal_display_frame = Frame(self.window)
        
        # start frame creation
        category_choice_text = Label(self.start_frame, text="Choisissez une catégorie :", height=500, anchor="n")
        category_choice_text.pack()

    # launches the app
    def launch(self):
        self.show_start_frame()
        # this function runs the app
        self.window.mainloop()

    # first menu display
    def show_start_frame(self):
        self.set_frame(self.start_frame)

        # data storage instaciation
        self.data = Data()

        # btn coordinates
        y=0.2
        # btn index for their placement
        i=0

        def show_random_meal():
            self.actual_frame.pack_forget()
            self.data.set_random_subcategory()
            self.show_meal_display()
        
        for category in self.data.valid_main_categories:
            # formats the category name to delete the "-" and capitalize the first letter
            formatted_name = category.replace('-', ' ')
            formatted_name = formatted_name.capitalize()

            category_button = Choice_button(self.start_frame, formatted_name, category, self.data, show_random_meal)
            category_button.button.place(relx=0.5, rely=y + i, anchor=CENTER)
            i = i + 0.1

    def show_meal_display(self):
        self.set_frame(self.meal_display_frame)
        print(self.data.random_subcategory)

        # meal title and name creation
        meal_display_title = Label(text = "Voici votre plat au hasard :", height=1)
        meal_name = Label(text = self.data.random_subcategory, height=1)
        # pic = PhotoImage()

        meal_display_title.pack()
        meal_name.pack()

    # changes the actual frame with the given one
    def set_frame(self, frame):
        self.actual_frame = frame
        self.actual_frame.pack(expand=False)

class Data:
    def __init__(self):
        self.valid_main_categories = ['viande', 'poisson', 'fruits-de-mer', 'plat-unique', 'œufs', 'plat-vegetarien', 'pates-riz-semoule', 'plats-au-fromage']
        self.subcategories = []

    def set_subcategories(self, new_subcategories):
        self.subcategories = new_subcategories

    def set_random_subcategory(self):
        self.random_subcategory = random.choice(self.subcategories)

app = App()
app.launch()
