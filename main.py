from storage.storage_json import load_data


def main():
    animals_data = load_data("data/animals_data.json")
    print(animals_data)


if __name__ == "__main__":
    main()