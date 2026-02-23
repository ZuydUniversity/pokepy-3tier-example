import mariadb

from .pokemon import Pokemon
from src.config_reader import read_config


class PokemonRepository(object):
    def __init__(self):
        config_file = read_config()
        self.connection = mariadb.connect(
            port=config_file["db_port"],
            host=config_file["db_host"],
            user=config_file["db_user"],
            password=config_file["db_password"],
            database=config_file["db_name"]
        )

    def get_all_pokemon(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Pokedex_number, Name, Type_1, Type_2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary FROM Pokemon")
        results = cursor.fetchall()

        all_pokemon = []
        for pokemon in results:
            all_pokemon.append(
                Pokemon(int(pokemon[0]), pokemon[1], pokemon[2], pokemon[3], pokemon[4], pokemon[5], pokemon[6], pokemon[7],
                        pokemon[8], pokemon[9], pokemon[10], pokemon[11], pokemon[12]))

        return all_pokemon

    def get_pokemon_by_pokedex_number(self, pokedex_number):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Pokedex_number, Name, Type_1, Type_2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary FROM Pokemon WHERE Pokedex_Number = ?",
            (pokedex_number,))
        results = cursor.fetchall()

        pokemon_with_pokedex_number = []
        for pokemon in results:
            pokemon_with_pokedex_number.append(
                Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[3], pokemon[4], pokemon[5], pokemon[6], pokemon[7],
                        pokemon[8], pokemon[9], pokemon[10], pokemon[11], pokemon[12]))

        return pokemon_with_pokedex_number

    def get_pokemon_by_pokedex_number_and_name(self, pokedex_number, name):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Pokedex_number, Name, Type_1, Type_2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary FROM pokemon WHERE Pokedex_Number = ? AND Name = ?",
            (pokedex_number, name))

        pokemon = cursor.fetchone()
        return Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[3], pokemon[4], pokemon[5], pokemon[6],
                       pokemon[7],
                       pokemon[8], pokemon[9], pokemon[10], pokemon[11], pokemon[12])

    def fill_mariadb_database(self):
        pokemon_list = self.get_all_pokemon()
        cursor = self.connection.cursor()
        try:
            for pokemon in pokemon_list:
                cursor.execute(
                    "INSERT INTO Pokemon (Pokedex_number, Name, Type_1, Type_2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (pokemon.Pokedex_Number, pokemon.Name, pokemon.Type_1, pokemon.Type_2, pokemon.Total_Stats,
                     pokemon.HP, pokemon.Attack, pokemon.Defense, pokemon.Sp_Atk, pokemon.Sp_Def, pokemon.Speed,
                     pokemon.Generation, pokemon.Legendary))
        except mariadb.Error as e:
            print(f"Error: {e}")

        self.connection.commit()
        print(f"Last Inserted ID: {cursor.lastrowid}")
