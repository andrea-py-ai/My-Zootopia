from storage.storage_json import load_data


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


def print_animal_info(animals):
    num_animals = len(animals["Name"])

    for i in range(num_animals):
        for category, value in animals.items():
            if value is None or value[i] is None:
                continue
            print(f'{category}: {value[i]}')
        print()


def main():
    animals_data = load_data("data/animals_data.json")
    animal_info = get_animal_info(animals_data)
    print_animal_info(animal_info)


if __name__ == "__main__":
    main()
