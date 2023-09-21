# Import necessary libraries

from bs4 import BeautifulSoup
import requests
import random
import re


## STEP 1 : Scrap the main food categories from the main url


# Define the URL of the website you want to scrape
url_mainpage = 'https://www.marmiton.org/recettes/index/categorie/plat-principal/'

# Send an HTTP GET request to the URL
response = requests.get(url_mainpage)

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


## STEP 2 : Get user's preferred main category (e.g., 'viande', 'poisson').


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


## STEP 3 : Loop over the recovered recipe urls from selected food preferences
##          and select one at random until the user is satisfied, and then provide 
##          the list of ingredients



while True:
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
        
    # Define a regular expression pattern to match the desired text
    pattern = r"/recette_(.*?)_"

    # Use re.search to find the pattern in the URL
    match = re.search(pattern, selected_url)

    if match:
        result_recipe = match.group(1)  # Extract the captured text within the parentheses
        print(result_recipe)
    else:
        print("Pattern not found in the URL.")
    answer = input(f"Are you satisfied by this recipe? {result_recipe} (yes/no): ").lower()  # Convert the input to lowercase for case-insensitivity
    
    if answer == "yes":
        print("Great! Glad to hear that.")
        response_ingredients = requests.get(selected_url)

        soup_ingredients = BeautifulSoup(response_ingredients.text, 'html.parser')
        span_element_1 = soup_ingredients.find_all('span', class_='RCP__sc-8cqrvd-3')


        span_element_1_as_string = str(span_element_1)


        # Parse the HTML code
        soup = BeautifulSoup(span_element_1_as_string, 'html.parser')

        # Find all <span> elements with the specified classes and extract their text
        text_parts = [span.text for span in soup.find_all('span', class_=["RCP__sc-8cqrvd-3 itCXhd", "RCP__sc-8cqrvd-3 cDbUWZ"])]

        # Print the list of extracted text parts
        print(f"Here is the list of ingredients to buy:{text_parts}")
        print("Good luck and Bon appétit")
        break  # Exit the loop if the user answers "yes"
    elif answer == "no":
        print("I'm sorry to hear that. Let me ask again.")
    else:
        print("Invalid response. Please answer with 'yes' or 'no'.")

     
    
