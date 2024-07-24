from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.asyncdb import sessionmanager
from database.base import Base
import pokemon.version.v1 as pokemonapi_version_1
import pokemon.version.v2 as pokemonapi_version_2
import pokemon.loaddata as data_load_api


@asynccontextmanager
async def lifespan(application: FastAPI):
    # on startup code

    async with sessionmanager.get_engine().begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    # on shutdown code
    if sessionmanager.get_engine() is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(pokemonapi_version_1.router)
app.include_router(pokemonapi_version_2.router)
app.include_router(data_load_api.router)


@app.get("/")
async def root():
    return {"message": "please go to doc for api details"}
