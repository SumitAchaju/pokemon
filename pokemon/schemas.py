from pydantic import BaseModel


class TypeSchema(BaseModel):
    id: int
    name: str


class ImageSchema(BaseModel):
    id: int
    back_default: str | None = None
    back_female: str | None = None
    pokemon_id: int


class PokemonSchema(BaseModel):
    id: int
    name: str
    types: list[TypeSchema]
    images: ImageSchema | None = None


class PokemonResponseModel(BaseModel):
    counts: int
    results: list[PokemonSchema]


class PokemonFilterByName(BaseModel):
    name: str
