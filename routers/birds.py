import requests
from fastapi import APIRouter, HTTPException
from schemas.bird_schema import Bird, BirdList
from services.map_generator import generate_map

router = APIRouter(prefix="/birds", tags=["birds"])

BASE_URL = "https://xeno-canto.org/api/2/recordings"


@router.get("/", response_model=BirdList)
async def get_birds(country: str = "Colombia"):
    response = requests.get(f"{BASE_URL}?query=cnt:{country}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error al obtener los datos")

    data = response.json()

    print("Ejemplo de record:", data["recordings"][0])

    birds_formatted = []
    for record in data["recordings"]:
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

    return {"birds": birds_formatted}


@router.get("/generate-map/")
async def birds_map(country: str = "Colombia"):
    response = requests.get(f"{BASE_URL}?query=cnt:{country}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error al obtener los datos")

    data = response.json()

    birds_formatted = []
    for record in data["recordings"]:
        birds_formatted.append({
            "gen": record.get("gen"),
            "sp": record.get("sp"),
            "en": record.get("en"),
            "lat": record.get("lat"),
            "lng": record.get("lng")
        })

    map_path = generate_map(birds_formatted)
    return {"message": "Mapa generado", "map_file": map_path}
