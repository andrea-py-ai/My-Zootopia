from storage.storage_json import load_data
from storage.storage_html import load_html


def get_animal_name(animals):
    """
    Return a list of animal names.
    """
    return [animal["name"] for animal in animals]


def get_animal_diet(animals):
    """
    Return a list of animal diets (or None if missing).
    """
    return [
        animal["characteristics"].get("diet")
        for animal in animals
    ]


def get_animal_first_location(animals):
    """
    Return the first listed location for each animal.
    """
    return [animal["locations"][0] for animal in animals]


def get_animal_type(animals):
    """
    Return a list of animal types (or None if missing).
    """
    return [
        animal["characteristics"].get("type")
        for animal in animals
    ]


def get_animal_info(animals):
    """
    Build a dictionary of animal attributes (each value is a list).
    """
    all_animal_info = {
        "Name": get_animal_name(animals),
        "Diet": get_animal_diet(animals),
        "Location": get_animal_first_location(animals),
        "Type": get_animal_type(animals)
    }
    return all_animal_info


def serialize_animal(animals, i):
    """
    Serialize the i-th animal's data from the
    full animal info dictionary into an HTML string.
    """
    lines = [
        '<li class="cards__item">',
        f'<div class="card__title">{animals["Name"][i]}</div>',
        '<div class="card__text">', '<ul>'
    ]

    for category in ["Diet", "Location", "Type"]:
        value = animals[category][i]
        if value is not None:
            lines.append(f'<li><strong>{category}:</strong> {value}</li>')

    lines.append('</ul>\n</div>\n</li>')

    return "\n".join(lines)


def convert_animal_data_into_html_string(animals):
    """
    Convert full animal info dictionary into an HTML string
    using serialize_animal().
    """
    num_animals = len(animals["Name"])
    lines = [serialize_animal(animals, i) for i in range(num_animals)]

    return "\n".join(lines)


def replace_data_in_html(animals_html):
    """
    Replace placeholder in template HTML with animal info HTML.
    """
    html = load_html("storage/storage_html.py")
    modified_html = html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )
    return modified_html


def create_animals_html(html_data):
    """
    Write the final HTML string to the output file.
    """
    with open("static/animals.html", "w", encoding="utf-8") as f:
        f.write(html_data)


def main():
    animals_data = load_data("data/animals_data.json")
    animal_info = get_animal_info(animals_data)
    animals_html = convert_animal_data_into_html_string(animal_info)
    final_html = replace_data_in_html(animals_html)
    create_animals_html(final_html)


if __name__ == "__main__":
    main()
