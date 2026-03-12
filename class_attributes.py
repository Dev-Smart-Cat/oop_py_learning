class Dog:

    # This is a class attribute
    # All dog instance will be created from this class
    # will have this class attribute
    species = "Canis Lupus"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

my_dog = Dog("dog", 12, "one")

print(my_dog.species)
print("----------------")
print("\n")

class Backpack:

    # This is a class attribute
    max_num_items = 10

    def __init__(self):
        self.items = []

my_backpack = Backpack()
you_backpack = Backpack()

# Access the class attribute through the class directly
print(Backpack.max_num_items)

# Access the class attribute through the instance
print(my_backpack.max_num_items)
print(you_backpack.max_num_items)
print("----------------")
print("\n")

class Backpack:

    # This is a class attribute
    max_num_items = 10

    def __init__(self):
        self.items = []

# Access the class attribute directly through the class
print(Backpack.max_num_items)

# Access the class attribute through a instance
print("original backpack max_num_items")
one_backpack = Backpack()
print(one_backpack.max_num_items)

# Updating the class attribute max_num_items
Backpack.max_num_items = 15

print("after updating the max_num_items")
print(Backpack.max_num_items)
print(one_backpack.max_num_items)