from jinja2 import Environment, FileSystemLoader
import os
import markdown
import shutil


def Mixen_van_Md_en_html(Markdown_bestand, HTML_bestand, titel):

    root = "SSG Project"
    md_folder = "pages"
    md_filename = Markdown_bestand

    pages_path = os.path.join(root, "pages")
    posts_path = os.path.join(root, "posts")
    templates_path = os.path.join(root, "templates")

    with open(os.path.join(pages_path, md_filename), 'r') as file:
        markdown_text = file.read()

    # Converteer de Markdown naar HTML
    html = markdown.markdown(markdown_text)

    # Schrijf de HTML naar een nieuw bestand
    tekst = html

    #output_file = os.path.splitext(Markdown_bestand)[0] + ".html"
    #link_inhoud = f'<a href="{output_file}">link text</a>'
    

    environment = Environment(
        loader=FileSystemLoader("SSG Project/templates/"))
    template = environment.get_template(HTML_bestand)
    content = template.render(
        tekst=tekst
    )

    results_filename = HTML_bestand
    results_template = environment.get_template(HTML_bestand)
    context = {
        "tekst": tekst,
        "Titel": titel,
        "content": content  # voeg de gerenderde markdown content toe aan de context
    }

    output_path = os.path.join(root, "_site")


        # Get file paths
    page_path = os.path.join(md_folder, Markdown_bestand)
    output_file = os.path.splitext(Markdown_bestand)[0] + ".html"
    output_path_full = os.path.join(output_path, output_file)

    with open(output_path_full, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))

    return output_file