from storage.storage_json import load_data
from storage.storage_html import load_html


def get_animal_name(animals):
    animal_names = []

    for animal in animals:
        animal_names.append(animal["name"])

    return animal_names


def get_animal_diet(animals):
    animal_diets = []

    for animal in animals:
        if "diet" in animal["characteristics"]:
            animal_diets.append(animal["characteristics"]["diet"])
        else:
            animal_diets.append(None)

    return animal_diets


def get_animal_first_location(animals):
    animal_first_locations = []

    for animal in animals:
        animal_first_locations.append(animal["locations"][0])

    return animal_first_locations


def get_animal_type(animals):
    animal_types = []

    for animal in animals:
        if "type" in animal["characteristics"]:
            animal_types.append(animal["characteristics"]["type"])
        else:
            animal_types.append(None)

    return animal_types


def get_animal_info(animals):
    all_animal_info = {
        "Name": get_animal_name(animals),
        "Diet": get_animal_diet(animals),
        "Location": get_animal_first_location(animals),
        "Type": get_animal_type(animals)
    }
    return all_animal_info


def order_animal_info_into_str(animals):
    num_animals = len(animals["Name"])
    animal_info_as_str = ""

    for i in range(num_animals):
        animal_info_as_str += '<li class="cards__item">\n'
        for category, value in animals.items():
            if value is None or value[i] is None:
                continue
            if category == "Name":
                animal_info_as_str += (f'<div class="card__title">{value[i]}'
                                       f'</div>\n<p class="card__text">\n')
            else:
                animal_info_as_str += f'<strong>{category}:</strong> {value[i]}<br/>\n'
        animal_info_as_str += "</p>\n</li>\n"

    return animal_info_as_str


def replace_data_in_html(animals_data):
    html = load_html("storage/storage_html.py")
    modified_html = html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_data.strip('\n')
    )
    return modified_html


def create_animals_html(html_data):
    with open("static/animals.html", "w", encoding="utf-8") as handle:
        handle.write(html_data)


def main():
    animals_data = load_data("data/animals_data.json")
    animal_info = get_animal_info(animals_data)
    animals_data_str = order_animal_info_into_str(animal_info)
    modified_html_str = replace_data_in_html(animals_data_str)
    create_animals_html(modified_html_str)


if __name__ == "__main__":
    main()
