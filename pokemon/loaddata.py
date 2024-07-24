from fastapi import APIRouter
from database.asyncdb import asyncdb_dependency
from sqlalchemy import select
from .models import Pokemon, Type, Images
import requests

router = APIRouter(prefix="/api/pokemon", tags=["load data"])


@router.get("/loaddata")
async def load_data(db: asyncdb_dependency):

    pokemon_data = (await db.scalars(select(Pokemon))).unique().all()

    if pokemon_data:
        return {"detail": "please empty the database to load data into it"}

    pokemontypes = requests.get("https://pokeapi.co/api/v2/type/")
    type_list = {}

    for ptype in pokemontypes.json()["results"]:
        newType = Type(name=ptype["name"])
        type_list[newType.name] = newType
        db.add(newType)

    pokemons = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=100")

    for pokemon in pokemons.json()["results"]:
        response = requests.get(pokemon["url"]).json()
        pokemonModel = Pokemon(name=response["name"])

        for ptype in response["types"]:
            pokemonModel.types.append(type_list[ptype["type"]["name"]])

        db.add(pokemonModel)
        await db.flush()
        await db.refresh(pokemonModel)

        pokemonImage = Images(
            pokemon_id=pokemonModel.id,
            back_default=response["sprites"]["back_default"],
            back_female=response["sprites"]["back_female"],
        )

        db.add(pokemonImage)

    await db.commit()

    return {"detail": "all data is sucessfully loaded"}
