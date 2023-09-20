# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:01:31 2023
Interface webapp
@author: Jeanne
"""
import requests 
from bs4 import BeautifulSoup
import re 
import tqdm 

starting_url = "https://www.marmiton.org/recettes/selections.aspx"

# Get html content
response = requests.get(starting_url)
result = response.content

# Parse html with BS
soup = BeautifulSoup(result, 'html.parser')

# In the body content find all href that matches the regex query (start with wiki and ignore !: to avoid artifacts like jpeg )
for link in soup.find("div",attrs={'id':'bodyContent'}).find_all("a",href = re.compile("^(/wiki/)((?!:).)*$")):
    print(link.get("href"))