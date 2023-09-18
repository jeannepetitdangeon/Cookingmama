# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:16:47 2023

@author: hobbe
"""

from bs4 import BeautifulSoup
import requests


url = 'https://www.marmiton.org/recettes/index/categorie/plat-principal/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

soup.find(class_ ="mrtn-tags-list")

liste_préférences = soup.find(class_ ="mrtn-tags-list")

print(liste_préférences)

texte_liste_préférences = [title.text.strip() for title in liste_préférences]

print(texte_liste_préférences)

