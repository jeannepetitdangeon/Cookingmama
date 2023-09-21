# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:00:38 2023

@author: epcmic
"""
exec(open('C:/Users/epcmic/OneDrive/Documents/GitHub/Cookingmama/CookingMama_1.py', encoding='utf-8').read())
exec(open('C:/Users/epcmic/OneDrive/Documents/GitHub/Cookingmama/Choice_button.py', encoding='utf-8').read())

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

class App:
    def __init__(self):
        self.root = ThemedTk(theme='Adapta')
        self.root.geometry('400x500')
        self.frame = None
        self.recipe_name_label = None
        self.recipe_image_label = None
        self.data = Data()

    def launch(self):
        self.show_start()
        self.root.mainloop()

    def show_start(self):
        self.frame = Frame(self.root)
        self.frame.pack(expand=False)

        category_choice_text = Text(self.frame, fg="black", padx=70, pady=30)
        category_choice_text.insert(1.0, "Choisissez une catégorie :")
        category_choice_text.config(font=("arial", 16), state=DISABLED)
        category_choice_text.pack()

        y = 0.2
        i = 0

        def show_random_meal():
            selected_recipe = self.data.get_random_subcategory()
            self.update_recipe_display(selected_recipe)

        for category in self.data.valid_main_categories:
            formatted_name = category.replace('-', ' ')
            formatted_name = formatted_name.capitalize()

            category_button = Choice_button(formatted_name, category, self.data, show_random_meal)
            category_button.button.place(relx=0.5, rely=y + i, anchor=CENTER)
            i = i + 0.1

        # Create labels for recipe name and image
        self.recipe_name_label = Label(self.frame, text="", font=("arial", 14))
        self.recipe_name_label.pack()
        self.recipe_image_label = Label(self.frame)
        self.recipe_image_label.pack()

    def update_recipe_display(self, recipe_data):
        # Update the recipe name label
        recipe_name = recipe_data.get("name", "Nom de la recette inconnu")
        self.recipe_name_label.config(text=recipe_name)

        # Update the recipe image (assuming recipe_data contains an image URL)
        recipe_image_url = recipe_data.get("image_url", "")
        if recipe_image_url:
            # Load and display the image (you may need to fetch the image)
            # For example, using Pillow library to load images
            from PIL import Image, ImageTk
            import requests
            response = requests.get(recipe_image_url)
            img = Image.open(BytesIO(response.content))
            img = ImageTk.PhotoImage(img)
            self.recipe_image_label.config(image=img)
            self.recipe_image_label.image = img  # Keep a reference to avoid garbage collection

class Data:
    def __init__(self):
        self.valid_main_categories = ['viande', 'poisson', 'fruits-de-mer', 'plat-unique', 'œufs', 'plat-vegetarien', 'pates-riz-semoule', 'plats-au-fromage']
        self.recipes = [
            {"name": "Recette 1", "image_url": "URL_de_l_image_1.jpg"},
            {"name": "Recette 2", "image_url": "URL_de_l_image_2.jpg"},
            # Add more recipe data here
        ]

    def get_random_subcategory(self):
        return random.choice(self.recipes)

app = App()
app.launch()
