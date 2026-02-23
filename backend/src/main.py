from .pokemon.pokemon_repository import PokemonRepository
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"hello": "world again"}


@app.get("/pokemon/all")
def get_all_pokemon():
    repo = PokemonRepository()
    return repo.get_all_pokemon()


@app.get("/pokemon/{pokedex_number}")
def get_pokemon_by_pokedex_number(pokedex_number: int):
    repo = PokemonRepository()
    return repo.get_pokemon_by_pokedex_number(pokedex_number)


@app.get("/pokemon/{pokedex_number}/{name}")
def get_pokemon_by_pokedex_number_and_name(pokedex_number: int, name: str):
    repo = PokemonRepository()
    return repo.get_pokemon_by_pokedex_number_and_name(pokedex_number, name)
