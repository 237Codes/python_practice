'''
Step 1: Copy the following code into Replit.

Step 2: Add a line of code (outside of the class) to 
instantiate an instance of the class Pokemon and store 
it in a variable named my_pokemon. The Pokemon instance 
created should have name "Pikachu" and its types should 
be ["Electric"].

'''
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

my_pokemon = Pokemon("Pikachu", ["Electric"])
print(my_pokemon.name)
print(my_pokemon.types)