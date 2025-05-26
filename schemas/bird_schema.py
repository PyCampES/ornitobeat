from pydantic import BaseModel
from typing import List, Optional

class Bird(BaseModel):
    id: str
    gen: Optional[str]  # género
    sp: Optional[str]   # especie
    en: Optional[str]   # nombre en inglés
    file: Optional[str] # archivo de sonido
    lat: Optional[str]  # latitud (string)
    lng: Optional[str]  # longitud (string)
    loc: Optional[str]  # localidad

class BirdList(BaseModel):
    birds: List[Bird]