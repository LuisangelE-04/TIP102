class Villager:
  def __init__(self, name, species, catchphrase):
    self.name = name
    self.species = species
    self.catchphrase = catchphrase
    self.friends = []

  def get_mutuals(self, new_contact):
    mutual_friends = []

    for friend in new_contact.friends:
      if friend in self.friends:
        mutual_friends.append(friend.name)

    return mutual_friends

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))
