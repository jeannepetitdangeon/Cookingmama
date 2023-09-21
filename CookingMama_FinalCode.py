# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:43:30 2023

@author: samuel
"""

from bs4 import BeautifulSoup
import requests
import random


## STEP 1 : Get User's Input


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



## STEP 2 : Recover recipe urls from selected food preferences


# Define the URL to scrape
url = f"https://www.marmiton.org/recettes/index/categorie/{user_input}/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all the recipe card links
    recipe_links = soup.find_all("a", class_="recipe-card-link")
    
    # Extract the URLs from the links
    recipe_urls = [link["href"] for link in recipe_links]
    
    # Randomly select a URL
    selected_url = random.choice(recipe_urls)
    
    # Print the randomly selected URL
    print("Randomly Selected URL:", selected_url)
else:
    print("Failed to retrieve the web page.")
     
    
## STEP 3 : Recover the list of ingredients for the selected recipe


response_ingredients = requests.get(selected_url)

soup_ingredients = BeautifulSoup(response_ingredients.text, 'html.parser')
span_element_1 = soup_ingredients.find_all('span', class_='RCP__sc-8cqrvd-3')


span_element_1_as_string = str(span_element_1)


# Parse the HTML code
soup = BeautifulSoup(span_element_1_as_string, 'html.parser')

# Find all <span> elements with the specified classes and extract their text
text_parts = [span.text for span in soup.find_all('span', class_=["RCP__sc-8cqrvd-3 itCXhd", "RCP__sc-8cqrvd-3 cDbUWZ"])]

# Print the list of extracted text parts
print(text_parts)