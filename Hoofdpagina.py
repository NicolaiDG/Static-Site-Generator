import shutil
import os
import json
from jinja2 import Template


def Hoofdpagina_titel():

    titel = input("Geef de naam van je hoofdpagina:    ")
    return titel

def Hoofdpagina_html(titel, css):
    #Haalt de webpagina's uit de json file om ze in een lijst te zetten
    lijst = []
    with open("Pagina.json", "r") as f:
        inhoud = json.load(f)
        for i in inhoud:
            lijst.append(i)
    aantal_keer = len(lijst)

    #Maakt een html sjabloon van de hoofdpagina
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ titel }}</title>
        <link rel="stylesheet" href="{{ css }}" />
    </head>
    <body>
        <header>
            <h1>{{ titel }}</h1>
            <div>
            {% for link in lijst %}
                <a href="{{ link }}">{{ link.replace(".html", "") }}</a>
            {% endfor %}
            </div>
        </header>
        <main>
        <h1>Welkom</h1>
        </main>
        <div class="bg"></div>
        <div class="bg bg2"></div>
        <div class="bg bg3"></div>
    </body>
    </html>
    '''

    #Maakt de hoofdpagina html bestand in de toegewezen pad
    project_folder = 'SSG Project/'
    site_folder = os.path.join(project_folder, '_site')
    pagina_naam = "hoofdpagina.html"
    pagina_parse = os.path.join(site_folder,pagina_naam)

    with open(pagina_parse, "w") as f:
        f.write(html)

    #Gebruikt jinja om de toegewezen jinja kernwoorden in de html om te zetten naar verwachten output
    template = Template(html)
    rendered_template = template.render(
        titel=titel,
        css=css,
        lijst=lijst,
    )

    with open(pagina_parse, "w") as f:
        f.write(rendered_template)

def main():
    titel = "Programeer talen"
    css = "sliding.css"
    Hoofdpagina_html(titel, css)
    

if __name__ == "__main__":
    main()
