# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:14:59 2023

@author: hobbe
"""

def get_user_preferences():
    print("Welcome to the Food Recommendation System!")
    print("Please enter your food preferences:")
    
    vegetarian = input("Are you a vegetarian? (yes/no): ").strip().lower()
    vegan = input("Are you a vegan? (yes/no): ").strip().lower()
    allergies = input("Do you have any allergies? (comma-separated list, e.g., nuts, dairy): ").strip()
    
    # You can add more preferences/questions here as needed
    
    preferences = {
        "vegetarian": vegetarian == "yes",
        "vegan": vegan == "yes",
        "allergies": [allergy.strip() for allergy in allergies.split(",") if allergy.strip()],
    }
    
    return preferences

# Example usage:
user_preferences = get_user_preferences()
print("User Preferences:")
print(user_preferences)


import requests
from bs4 import BeautifulSoup

def scrape_bbc_good_food_recipes(preferences):
    # Define the URL of the BBC Good Food website
    url = 'https://www.bbcgoodfood.com/recipes'
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all recipe elements on the page
        recipes = soup.find_all(class_='view view-recipes view-id-recipes view-display-id-panel_pane_1 view-dom-id-c6d1984e97bb36b24a2b3ec1dbfdd433')
        
        # Create a list to store the scraped recipes
        scraped_recipes = []
        
        for recipe in recipes:
            # Extract information about each recipe
            recipe_title = recipe.find(class_='teaser-item__title').text.strip()
            recipe_url = 'https://www.bbcgoodfood.com' + recipe.find('a')['href']
            recipe_description = recipe.find(class_='field-name-field-summary').text.strip()
            
            # Check if the recipe is vegetarian based on user preferences
            is_vegetarian = 'vegetarian' in recipe_description.lower()
            
            # If the recipe is vegetarian and matches user preferences, add it to the list
            if preferences['vegetarian'] and is_vegetarian:
                scraped_recipes.append({
                    'title': recipe_title,
                    'url': recipe_url,
                    'description': recipe_description,
                })
        
        return scraped_recipes
    else:
        print("Failed to retrieve data from the website.")
        return []

# Example usage:
user_preferences = {
    'vegetarian': True,  # You can customize the user's preferences
}

vegetarian_recipes = scrape_bbc_good_food_recipes(user_preferences)

# Print the scraped vegetarian recipes
for recipe in vegetarian_recipes:
    print(f"Title: {recipe['title']}")
    print(f"URL: {recipe['url']}")
    print(f"Description: {recipe['description']}")
    print()

