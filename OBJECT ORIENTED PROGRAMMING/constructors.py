# Magic or Dunder methods
class Fruit():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    
a = Fruit("Apple", 100)
a.color = "Red"





class Guitar:
    def __init__(self):
        print(f"A new guitar is being created. This object is {self}")


acoustic = Guitar


# Adding Attributes to Objects
# Attribute is a piece of data stored on an object; a variable belonging to an object
class Guitar:
    def __init__(self):
        print(f"A new guitar is being created. This object is {self}")


acoustic = Guitar
electric = Guitar

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990
print(acoustic.wood)
  
electric.nickname = "Sound Viking 3000"
print(electric.nickname)
