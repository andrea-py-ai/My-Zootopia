# 🐾 Animal Data HTML Generator

This Python module processes structured animal data from JSON and generates an HTML file displaying formatted animal information for a website.

---

## 📄 Overview

The script reads animal data, extracts key attributes (such as name, diet, location, and type), and converts them into an HTML list format for use in a web page template.  

It integrates with helper modules for data and HTML template loading, and produces a complete `animals.html` page ready for display.

---

## ⚙️ Features

- Loads animal data from a JSON file  
- Extracts and structures key animal details  
- Generates HTML snippets dynamically  
- Replaces placeholders in a template HTML file  
- Writes the final formatted HTML output  

---

## 🧩 Functions

| Function | Description |
|-----------|-------------|
| `get_animal_name(animals)` | Returns a list of animal names. |
| `get_animal_diet(animals)` | Returns a list of animal diets, or `None` if missing. |
| `get_animal_first_location(animals)` | Returns the first listed location for each animal. |
| `get_animal_type(animals)` | Returns a list of animal types, or `None` if missing. |
| `get_animal_info(animals)` | Builds a dictionary with all animal attributes. |
| `serialize_animal(animals, i)` | Serializes one animal’s data into an HTML string. |
| `convert_animal_data_into_html_string(animals)` | Converts all animal data into a combined HTML string. |
| `replace_data_in_html(animals_html)` | Inserts the animal HTML into a template. |
| `create_animals_html(html_data)` | Writes the final HTML string to a file. |
| `main()` | Orchestrates the full process: load → convert → generate HTML. |

---

## 🗂️ Project Structure

```
├── data/
│   └── animals_data.json
├── storage/
│   ├── storage_json.py
│   └── storage_html.py
├── static/
│   └── animals.html   # Generated output file
└── main.py            # (or your script name)
```

---

## ▶️ Usage

Run the script directly:

```bash
python main.py
```

Output will be written to:
```
static/animals.html
```

---

## 🧠 Example Workflow

1. `load_data()` loads animal information from `animals_data.json`.  
2. `get_animal_info()` organizes attributes into a dictionary.  
3. `convert_animal_data_into_html_string()` creates formatted HTML for each animal.  
4. `replace_data_in_html()` merges that HTML into a base template.  
5. `create_animals_html()` saves the final file to `static/animals.html`.

---

## 🪶 Notes

- Requires valid input JSON and HTML template files.  
- Designed for modular integration with `storage_json` and `storage_html` helpers.  
- Outputs clean, semantic HTML for easy styling and web embedding.

---

## 📜 License

This project is shared under a custom open-use license.
You may view, study, and modify the code for personal or educational purposes.
Redistribution or commercial use requires written permission from the author.
All software is provided “as is,” without warranty of any kind.
