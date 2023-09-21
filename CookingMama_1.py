# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:09:05 2023

@author: samue
"""

# Import necessary libraries

import bs4
from bs4 import BeautifulSoup
import requests
import random

# Define the URL of the website you want to scrape
url = 'https://www.marmiton.org/recettes/index/categorie/plat-principal/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element with class "mrtn-tags-list"
    liste_preferences = soup.find(class_='mrtn-tags-list')

    # Check if the element was found
    if liste_preferences:
        # Extract the text from the element and split it into a list
        texte_liste_preferences = [title.text.strip() for title in liste_preferences.find_all('li')]

        # Print the list of preferences
        print(texte_liste_preferences)
    else:
        print('Element with class "mrtn-tags-list" not found on the page.')
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
    

# User Input
# Get the user's preferred main category (e.g., 'viande', 'poisson').

# Define a list of valid main categories
valid_main_categories = ['viande', 'poisson', 'fruits-de-mer', 'plat-unique', 'œufs', 'plat-vegetarien', 'pates-riz-semoule', 'plats-au-fromage']

# Prompt the user for input and ensure it is a valid main category
while True:
    user_input = input("Please enter your preferred main category: ").lower()
    
    if user_input in valid_main_categories:
        # User input is valid, break the loop
        break
    else:
        print("Invalid category. Please choose from the following options:")
        print(valid_main_categories)

# Now, 'user_input' contains the user's preferred main category
print("You selected:", user_input)


# Step 2: Scrape Subcategories
# Based on the user's choice, scrape the list of subcategories within the selected main category.


# Send an HTTP GET request to the main category page
main_category_response = requests.get(f'https://www.marmiton.org/recettes/index/categorie/{user_input}/')

# Check if the request was successful (status code 200)
if main_category_response.status_code == 200:
    # Parse the HTML content of the main category page using BeautifulSoup
    main_category_soup = BeautifulSoup(main_category_response.text, 'html.parser')

    # Find the <div class="recipe-results fix-inline-block"> element
    recipe_results_div = main_category_soup.find('div', class_='recipe-results fix-inline-block')

    if recipe_results_div:
        # Find all <div class="recipe-card"> elements within the recipe_results_div
        subcategory_elements = recipe_results_div.find_all('div', class_='recipe-card')

        # Extract the subcategory names from each subcategory element
        subcategories = []

        for subcategory_element in subcategory_elements:
            # Extract the subcategory name from the <h4> tag
            subcategory_name = subcategory_element.find('h4', class_='recipe-card__title').text.strip()
            subcategories.append(subcategory_name)

        # Now 'subcategories' contains the list of subcategory names within the selected main category
        print("Subcategories within the selected main category:")
        for subcategory in subcategories:
            print(subcategory)
    else:
        print('No recipe results found on the page.')
else:
    print('Failed to retrieve the main category page. Status code:', main_category_response.status_code)


# Step 3: Random Meal Selection
# Randomly select a subcategory (meal) from the list obtained in Step 2.

if subcategories:
    # Use random.choice() to select a random subcategory from the list
    random_subcategory = random.choice(subcategories)

    # Print the randomly selected subcategory
    print("Randomly selected subcategory (meal):", random_subcategory)

    # You can use 'random_subcategory' for further processing, like scraping recipes from this subcategory.
else:
    print("No subcategories found to select from.")


