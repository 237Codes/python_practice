class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    def catch_pokemon(self):
        self.is_caught = True
    def choose(self):
        if self.is_caught:
            print(f'{self.name} I choose you!')
        else:
            print(f'{self.name} is wild! Catch me if you can!')
    def add_type(self, new_type):
        self.types.append(new_type)

def get_by_type(lst, search_string):
    
    list_with_types = []
    for pokemon in lst:
        if search_string in pokemon.types:
            list_with_types.append(pokemon.name)
    return list_with_types



# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)