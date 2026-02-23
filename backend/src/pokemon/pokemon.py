class Pokemon:
    def __init__(self, pokedex_number, name, type1, type2, total_stats, hp, attack, defense, sp_atk, sp_def, speed,
                 generation, legendary):
        self.Pokedex_Number = pokedex_number
        self.Name = name
        self.Type_1 = type1
        self.Type_2 = type2
        self.Total_Stats = total_stats
        self.HP = hp
        self.Attack = attack
        self.Defense = defense
        self.Sp_Atk = sp_atk
        self.Sp_Def = sp_def
        self.Speed = speed
        self.Generation = generation
        self.Legendary = legendary

    def __repr__(self):
        return f'Pokemon({self.Pokedex_Number}, {self.Name})\n'
