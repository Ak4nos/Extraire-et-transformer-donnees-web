from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
  soup = BeautifulSoup(file, 'html.parser')
print(soup.prettify())
titres = soup.find('title')
print(titres)

texte_h1 = soup.find_all('h1')
print(texte_h1)

nom = "h2"
nom_et_prix_ul = soup.find_all('h2')
nom_et_prix_ul_liste = []
for nom_et_prix in nom_et_prix_ul:
  nom_et_prix_ul_liste.append(nom_et_prix.string)

print(nom_et_prix_ul_liste)

description_ul = soup.find_all('p')
description_ul_liste = []

for description in description_ul:
  description_ul_liste.append(description.string)

print(description_ul_liste)