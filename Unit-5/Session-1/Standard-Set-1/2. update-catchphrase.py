'''

'''

class Villager:
  def __init__(self, name, species, catchphrase):
    self.name = name
    self.species = species
    self.catchphrase = catchphrase
    self.furniture = []

  def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
  
  def set_catchphrase(self, new_catchphrase):
    catch_len = len(new_catchphrase)
    if catch_len >= 20:
      print("Invalid catchphrase")
      return
    
    for char in new_catchphrase:
      if char.isalpha() or char == " ":
        self.catchphrase = new_catchphrase
        print("Catchphrase updated")
        return
      else:
        print("Invalid catchphrase")
        return
    '''
    if new_catchphrase.isalpha():
      self.catchphrase = new_catchphrase
      print("Catchphrase updated")
      return
    '''

bones = Villager("Bones", "Dog", "ruff it up")

#print(bones.name)
#print(bones.species)  
#print(bones.catchphrase) 
#print(bones.furniture)
#print(bones.greet_player("Luisangel"))
#print(bones.greet_player("Samia"))

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
