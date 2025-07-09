def load_html(file_path):
    """ Loads HTML file """
    with open("./templates/animals_template.html", "r", encoding="utf-8") as html_file:
        html = html_file.read()

    return html
