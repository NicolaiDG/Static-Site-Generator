import os
from datetime import datetime
import shutil
import yaml
import markdown
from jinja2 import Environment, FileSystemLoader
from mixen import Mixen_van_Md_en_html

project_naam = "SSG Project"

def Mappen_maker():
    
    # Maak een nieuwe map voor het project
    try: 
        os.mkdir(project_naam)

        # Maak submappen voor "pages", "posts" en "templates"
        os.mkdir(os.path.join(project_naam, "pages"))
        os.mkdir(os.path.join(project_naam, "posts"))
        os.mkdir(os.path.join(project_naam, "templates"))

    except FileExistsError:
        print("Deze mappen bestaan al!")

def Sjabloon_veplaatsen():

    sjabloon = input("Geef de sjablonen die wilt gebruiken (dit zijn je html files):    ")
    # Zoek de volledige padnaam naar de "pages" map van het SSG-project
    pages_dir = os.path.join(os.getcwd(), project_naam, "templates")
    # Verplaats het Markdown-bestand naar de "pages" map
    shutil.move(sjabloon, pages_dir)

    return sjabloon

def Sjabloon_keuze():

    sjabloon_html = input("Geef de sjabloon html die wilt gebruiken voor dit project:    ")
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

def Markdown_verplaatsen():


    markdown_file = input("Geef de markdown bestanden die wilt gebruiken voor dit project:    ")
    # Zoek de volledige padnaam naar de "pages" map van het SSG-project
    pages_dir = os.path.join(os.getcwd(), project_naam, "pages")
    # Verplaats het Markdown-bestand naar de "pages" map
    shutil.move(markdown_file, pages_dir)

    return markdown_file

def CSS_verplaatsen(sjabloon):

    correct = True
    while correct:
        try:
            CSS = input(f"Geef de CSS bestand die bij de sjabloon '{sjabloon}' hoort:   ")
            pages_dir = os.path.join(os.getcwd(), project_naam, "_site")
            shutil.move(CSS, pages_dir)
            correct= False
        except FileNotFoundError:
            print("Deze bestand is niet gevonden!")

def main():

    Mappen_maker()
    Markdown_file =  Markdown_verplaatsen()
    Sjabloon = Sjabloon_veplaatsen()
    keuze_sjabloon = Sjabloon_keuze()
    Yaml(keuze_sjabloon)
    Mixen_van_Md_en_html( Markdown_file ,keuze_sjabloon)
    CSS_verplaatsen(Sjabloon)

if __name__ == "__main__":
    main()