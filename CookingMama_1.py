from bs4 import BeautifulSoup
import requests
import random

## STEP 1 : Get User's Input

# Define a list of valid main categories
valid_main_categories = ['viande', 'poisson', 'fruits-de-mer', 'plat-vegetarien']

# Prompt the user to choose a preferred main category
print("Available main categories:")
for category in valid_main_categories:
    print("- " + category)

while True:
    user_input = input("Please enter your preferred main category: ").lower()
    
    if user_input in valid_main_categories:
        # User input is valid, break the loop
        break
    else:
        print("Invalid category. Please choose from the available options.")

# Now, 'user_input' contains the user's preferred main category
print("You selected:", user_input)

## STEP 2 : Recover recipe data from selected food preferences

# Define a function to scrape a random recipe from the chosen category
def scrape_random_recipe(category):
    url = f"https://www.marmiton.org/recettes/index/categorie/{category}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        recipe_links = soup.find_all("a", class_="recipe-card-link")
        if not recipe_links:
            print("No recipes found for this category.")
            return None
        selected_url = random.choice([link["href"] for link in recipe_links])
        return selected_url
    else:
        print("Failed to retrieve the web page.")
        return None

# Initialize a flag to control the loop
recipe_found = False

# Continue the loop until a suitable recipe is found
while not recipe_found:
    # Scrape and display a random recipe URL
    initial_recipe_url = scrape_random_recipe(user_input)
    if initial_recipe_url:
        print("Randomly Selected Recipe URL:", initial_recipe_url)
        
        # Ask if the recipe is suitable
        suitability = input("Is this recipe suitable for you? (yes/no): ").strip().lower()
        
        if suitability == "yes":
            # Set the flag to end the loop
            recipe_found = True
        else:
            # Continue the loop to find a new random recipe
            print("Fetching a new random recipe URL...")

## STEP 3 : Fetch and display the list of ingredients for the selected recipe if the user is satisfied

if recipe_found:
    # Fetch and display the list of ingredients for the selected recipe
    print("Fetching ingredients...")
    response_ingredients = requests.get(initial_recipe_url)
    soup_ingredients = BeautifulSoup(response_ingredients.text, 'html.parser')
    span_element_1 = soup_ingredients.find_all('span', class_='RCP__sc-8cqrvd-3')
    span_element_1_as_string = str(span_element_1)
    soup = BeautifulSoup(span_element_1_as_string, 'html.parser')
    text_parts = [span.text for span in soup.find_all('span', class_=["RCP__sc-8cqrvd-3 itCXhd", "RCP__sc-8cqrvd-3 cDbUWZ"])]

    # Print the list of extracted text parts (ingredients)
    print("Ingredients:")
    for ingredient in text_parts:
        print("- " + ingredient)
