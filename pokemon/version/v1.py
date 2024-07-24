from fastapi import APIRouter
from pokemon.schemas import PokemonFilterByName, PokemonResponseModel
from database.asyncdb import asyncdb_dependency
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from pokemon.models import Pokemon, Type

router = APIRouter(prefix="/api/v1/pokemon", tags=["pokemon_version_1"])


@router.get("/", response_model=PokemonResponseModel)
async def get_pokemon(
    db: asyncdb_dependency,
    name: str | None = None,
    type: str | None = None,
):
    pokemon_query = (
        select(Pokemon)
        .options(joinedload(Pokemon.types))
        .options(joinedload(Pokemon.images))
    )

    if name is not None:
        pokemon_query = pokemon_query.where(Pokemon.name == name)

    if type is not None:
        pokemon_query = pokemon_query.where(Pokemon.types.any(Type.name == type))

    pokemon = (await db.scalars(pokemon_query)).unique().all()

    return {"counts": len(pokemon), "results": pokemon}


@router.post("/", response_model=PokemonResponseModel)
async def filter_pokemon_by_name(
    db: asyncdb_dependency, filtername: PokemonFilterByName
):
    pokemon_query = (
        select(Pokemon)
        .where(Pokemon.name.icontains(filtername.name))
        .options(joinedload(Pokemon.types))
        .options(joinedload(Pokemon.images))
    )

    pokemon = (await db.scalars(pokemon_query)).unique().all()
    return {"counts": len(pokemon), "results": pokemon}
