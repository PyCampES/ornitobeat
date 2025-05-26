import json
import requests

BASE_URL = "https://xeno-canto.org/api/2/recordings"


def guardar_bird_data(country="Colombia", limite=100, filename="aves_colombia.json"):
    response = requests.get(f"{BASE_URL}?query=cnt:{country}")
    if response.status_code != 200:
        raise Exception("Error al obtener los datos de Xeno-Canto")

    data = response.json()
    recordings = data.get("recordings", [])[:limite]

    birds_formatted = []
    for record in recordings:
        birds_formatted.append({
            "id": record.get("id"),
            "gen": record.get("gen"),
            "sp": record.get("sp"),
            "en": record.get("en"),
            "file": record.get("file"),
            "lat": record.get("lat"),
            "lng": record.get("lng"),
            "loc": record.get("loc")
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(birds_formatted, f, ensure_ascii=False, indent=2)

    print(f"Archivo guardado como {filename}")

guardar_bird_data()