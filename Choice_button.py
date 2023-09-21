from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from bs4 import BeautifulSoup

# choice button blueprint
class Choice_button:
    def __init__(self, display_frame, text, choice, data, callback_random_method):
        # method called on clicking in a meal category
        def callback_method():
            print(self.choice)

            main_category_response = requests.get(f'https://www.marmiton.org/recettes/index/categorie/{choice}/')

            if main_category_response.status_code == 200:
                main_category_soup = BeautifulSoup(main_category_response.text, 'html.parser')
                recipe_results_div = main_category_soup.find('div', class_='recipe-results fix-inline-block')

                if recipe_results_div:
                    subcategory_elements = recipe_results_div.find_all('div', class_='recipe-card')
                    subcategories = []

                    for subcategory_element in subcategory_elements:
                        subcategory_name = subcategory_element.find('h4', class_='recipe-card__title').text.strip()
                        subcategories.append(subcategory_name)

                    data.set_subcategories(subcategories)

                    # random choice method given in argument (dirty)
                    callback_random_method()

                else:
                    print('No recipe results found on the page.')
            else:
                print('Failed to retrieve the main category page. Status code:', main_category_response.status_code)

        # button instanciation
        self.button = ttk.Button(display_frame, text=text, command=callback_method)
        self.choice = choice
