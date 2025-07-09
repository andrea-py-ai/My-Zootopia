from storage.storage_json import load_data


def get_animal_name(animals):
    animal_names = []

    for animal in animals:
        if animal:
            animal_names.append(animal["name"])

    return animal_names


def get_animal_diet(animals):
    pass

def get_animal_first_location(animals):
    pass


def get_animal_type(animals):
    pass


def get_animal_info(animals):
    all_animal_info = {"animal_names": get_animal_name,
                       "animal_diet": get_animal_diet,
                       "animal_first_location": get_animal_first_location,
                       "animal_type": get_animal_type}

    return all_animal_info


def print_animal_info(animals):
    pass


def main():
    animals_data = load_data("data/animals_data.json")
    animal_info = get_animal_info(animals_data)
    print_animal_info(animal_info)


if __name__ == "__main__":
    main()
