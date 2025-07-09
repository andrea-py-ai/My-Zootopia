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
            if value:
                print(f'{category}: {value[i]}')
            else:
                continue
            print()


def main():
    animals_data = load_data("data/animals_data.json")
    animal_info = get_animal_info(animals_data)
    print_animal_info(animal_info)


if __name__ == "__main__":
    main()
