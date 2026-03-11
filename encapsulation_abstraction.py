"""
Abstraction => show only the essential attributes and hide unnecessary details from the user.
Hide the complexity from the user. Abstraction also allows us to abstract out 
common parts of the code to avoid repetition. 

Interface => the "visible part of the class that the program can interact with."

Implementation => the internal part of the class with the code that performs the functionality.
"""

# Public and non-public attributes
class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        # Age attribute will not be modified or accessed outside of the class
        # use leading underscore => _age
        self._age = age
        self.gpa = gpa

new_student = Student("2A1", "Nora Nav", 15, 3.96)
print(new_student._age)
print("----------------")
print("\n")

class Backpack:

    def __init__(self):
        # items attribute SHOULD NOT BE accessed or modified outside of the class
        self._items = []

my_backpack = Backpack()
print(my_backpack._items)
print("----------------")
print("\n")

#----------------------------------------------------#

class Movie:

    # This is a class attribute
    id_counter = 1

    def __init__(self, title, year, language, rating):
        self._id = Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        # This is a counter and generates the id any time the class Movie is called.
        Movie.id_counter += 1

my_movie = Movie("Avangers", 2022, "English", 4.8)
your_movie = Movie("Price and Prejudice", 2005, "French", 4.5)
another_movie = Movie("Revenent", 2014, "Portuguese", 5.0)

# Access the movie id
print(my_movie._id)
print(your_movie._id)
print(another_movie._id)