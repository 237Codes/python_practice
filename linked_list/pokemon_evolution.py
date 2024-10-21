class Pokemon():
    def __init__(self, name, types, evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

# Remove 'self' since this is not a method of a class
def get_evolutionary_line(starter_pokemon):
    '''
    Evolution = None || Pokemon
    Evolve means pokemon changes to a different pokemon
    '''
    possible_evolve_list = []
    possible_evolve_list.append(starter_pokemon.name)
    
    # Check for evolution and add evolved Pokemon to the list
    current_pokemon = starter_pokemon
    while current_pokemon.evolution is not None:
        if set(current_pokemon.evolution.types).intersection(current_pokemon.types):
            possible_evolve_list.append(current_pokemon.evolution.name)
        current_pokemon = current_pokemon.evolution

    return possible_evolve_list

# Create the Pokemon objects
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

# Now call the function without 'self'
charmander_list = get_evolutionary_line(charmander)
print("Charmander's Evolutionary Line:", charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print("Charmeleon's Evolutionary Line:", charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print("Charizard's Evolutionary Line:", charizard_list)
