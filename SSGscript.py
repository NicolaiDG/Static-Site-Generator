import os
from datetime import datetime
import shutil
import yaml
import markdown
import json

from jinja2 import Environment, FileSystemLoader

from mixen import Mixen_van_Md_en_html
from Hoofdpagina import Hoofdpagina_titel
from Hoofdpagina import Hoofdpagina_html

project_naam = "SSG Project"

def Mappen_maker():
    
    # Maak een nieuwe map voor het project
    try: 
        os.mkdir(project_naam)

        # Maak submappen voor "pages", "posts" en "templates"
        os.mkdir(os.path.join(project_naam, "pages"))
        os.mkdir(os.path.join(project_naam, "posts"))
        os.mkdir(os.path.join(project_naam, "templates"))
        os.mkdir(os.path.join(project_naam, "_site"))
        return True
    
    except FileExistsError:
        print("Deze mappen bestaan al!")
        return False
        

def Sjabloon_veplaatsen():

    
    Nog_doorgaan = True

    while Nog_doorgaan: 
        doorgaan = True
        while doorgaan:
            try: 
                sjabloon = input("Geef de sjablonen die wilt gebruiken (dit zijn html bestanden):  ")
                # Zoek de volledige padnaam naar de "pages" map van het SSG-project
                pages_dir = os.path.join(os.getcwd(), project_naam, "templates")
                # Verplaats het Markdown-bestand naar de "pages" map
                shutil.move(sjabloon, pages_dir)
                doorgaan = False
            except FileNotFoundError:
                print("Deze html bestaat niet! Probeer het opnieuw!")
                doorgaan = True
        
        doorgaan = True
        while doorgaan:
            try:
                CSS = input(f"Geef de CSS bestand die bij de sjabloon '{sjabloon}' hoort:   ")
                pages_dir = os.path.join(os.getcwd(), project_naam, "_site")
                shutil.move(CSS, pages_dir)
                doorgaan = False
            except FileNotFoundError:
                print("Deze bestand is niet gevonden!")
                doorgaan = True

        opnieuw_foutief = True
        while opnieuw_foutief:
            Nog_een_sjabloon = input("Wil je nog een sjabloon toevoegen ? (0 = Nee) (1 = Ja):    ")
            if Nog_een_sjabloon == "0":
                Nog_doorgaan = False
                opnieuw_foutief = False
            elif Nog_een_sjabloon == "1":
                Nog_doorgaan = True
                opnieuw_foutief = False
            else:
                print("Onbekende keuze! Probeer het opniew!")
                opnieuw_foutief = True
    
    return CSS


def Sjabloon_keuze():

    directory = "SSG project/templates"
    html_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            html_files.append(filename) 

    print("Je hebt momenteel deze html bestanden in je project om te gebruiken:    ")
    for items in html_files:
        print(items)

    print("")

    sjabloon_html = input("Geef de sjabloon html die je wilt gebruiken voor dit project:    ")
    return sjabloon_html

def Yaml(sjabloon):

    # Schrijf de front matter in YAML-bovenkant van elke pagina of post in de "pages" map
    for filename in os.listdir(os.path.join(project_naam, "pages")):
        if filename.endswith(".md"):
            filepath = os.path.join(project_naam, "pages", filename)
            with open(filepath, "r") as f:
                content = f.readlines()
            with open(filepath, "w") as f:
                f.write("---\n")
                f.write("title: {}\n".format(filename[:-3]))
                f.write("date: {}\n".format(datetime.now().strftime("%Y-%m-%d")))
                f.write(f"template: {sjabloon}\n")
                f.write("---\n")
                f.write("\n")
                f.write("".join(content))

    # Schrijf de front matter in YAML-bovenkant van elke pagina of post in de "posts" map
    for filename in os.listdir(os.path.join(project_naam, "posts")):
        if filename.endswith(".md"):
            filepath = os.path.join(project_naam, "posts", filename)
            with open(filepath, "r") as f:
                content = f.readlines()
            with open(filepath, "w") as f:
                f.write("---\n")
                f.write("title: {}\n".format(filename[:-3]))
                f.write("date: {}\n".format(datetime.now().strftime("%Y-%m-%d")))
                f.write(f"template: {sjabloon}\n")
                f.write("---\n")
                f.write("\n")
                f.write("".join(content))


def Markdowns_toevoegen():

    meer_bestanden = True
    
    while meer_bestanden:
        correct = True

        markdown_file = input("Geef de markdown bestanden die je wilt gebruiken voor dit project:    ")
        # Zoek de volledige padnaam naar de "pages" map van het SSG-project
        pages_dir = os.path.join(os.getcwd(), project_naam, "pages")
        # Verplaats het Markdown-bestand naar de "pages" map
        shutil.move(markdown_file, pages_dir)

        while correct:
            Verdergaan = input("Wil je nog een markdown bestand toevoegen? (0= Nee) (1= ja)   ")
            if Verdergaan == "0":
                correct = False
                meer_bestanden = False
            elif Verdergaan == "1":
                correct = False
            else:
                print("Onbekende keuze, probeer het opnieuw!")
                correct = True


def Markdown_lijst():

    directory = "SSG project/pages"
    MD_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            MD_files.append(filename) 

    print("Je hebt momenteel deze markdown bestanden in je project om te gebruiken:    ")

    for items in MD_files:
        print(items)
    
    print("\n")

def Pagina_omzetter(sjabloon,titel):

    lijst = []
    root = project_naam
    md_folder = "pages"

    pages_path = os.path.join(root, "pages")
    posts_path = os.path.join(root, "posts")
    templates_path = os.path.join(root, "templates")

    for item in os.listdir(pages_path):
        keuze = item
        pagina = Mixen_van_Md_en_html(keuze,sjabloon,titel)
        lijst.append(pagina)
    
    with open("Pagina.json", "w") as f:
            json.dump(lijst, f)

def Uitvoeren():

    Programma_verder_runnen = Mappen_maker()

    if Programma_verder_runnen == True:

        titel = Hoofdpagina_titel()
        print(titel)
        Markdowns_toevoegen()
        Markdown_lijst()
        CSS = Sjabloon_veplaatsen()
        keuze_sjabloon = Sjabloon_keuze()
        Yaml(keuze_sjabloon)
        Pagina_omzetter(keuze_sjabloon,titel)
        Hoofdpagina_html(titel, CSS)
        
    else:
        print("Probeer het opnieuw!")

def main():
    Uitvoeren()

if __name__ == "__main__":
    main()

# YAML headers moeten in lossen bestanden wat je posts zijn in je folder. Je geeft dat ook een eigen tab in je home page.
# YAML naar een JSON zetten of een list
# Aparte custom file maken waar je zegt welke sjablonen te gebruiken en welke indelingen
