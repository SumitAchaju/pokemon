# Pokemon Api

Rest api for serving the list of pokemons with their name, types and images in docker container

## Setup

To Setup this project clone this project

```bash
  git clone https://github.com/SumitAchaju/pokemon.git
```

Run

```bash
  docker compose up --build
```

> **Note:**
> Make sure docker is installed and initilized in your computer and you are in root directory of this project.

## API Reference

#### Load 100 pokemons data from https://pokeapi.co/

```http
GET /api/pokemon/loaddata
```

> **Note:**
> Pokemon table must be empty in database to load this data

#### Get all pokemons

```http
GET /api/v1/pokemon
```

#### Get filtered pokemons

```http
GET /api/v1/pokemon
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `name`    | `string` | **Optional**. name of pokemon      |
| `type`    | `string` | **Optional**. type name of pokemon |

#### Get filtered pokemon by name

```http
POST /api/v1/pokemon
```

| Body   | Type     | Description                                     |
| :----- | :------- | :---------------------------------------------- |
| `name` | `string` | **Required**. keyword to filter pokemon by name |
