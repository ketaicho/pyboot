class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.eggs = 0
        self.species = species
        self.name = name

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs


chick1 = Chicken("Alice", "Partridge Silkie")
chick2 = Chicken("Amelia", "Speckled Sussex")

print(Chicken.total_eggs)
print(chick1.eggs)
print(chick2.eggs)
chick1.lay_egg()
chick2.lay_egg()
chick2.lay_egg()
print(chick1.eggs)
print(chick2.eggs)
print(Chicken.total_eggs)
