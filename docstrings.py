# Documenting a function in python
def make_frequency_dict(sequence):
    """Return a dictionary that maps each element in sequence to its frequency.

    Create a dictionary that maps each element in the list sequence
    to the number of times the element occurs in the list. The element
    will be the key of the key-value pair in the dictionary and its frequency
    will be the value of the key-value pair.

    Argument:
        sequence: A list of values. These values have to be of an 
            immutable data type because they will be assigned as keys
            of the dictionary. For example, they can be integers, booleans,
            tuples, or strings.

    Return:
        A dictionary that maps each element in the list to its frequency.
        From example, this function call:

        make_frequency_dict([1, 6, 2, 6, 2])

        returns this dictionary:

        {1: 1, 6: 2, 2: 2}

    Raise:
        VaueError: if the list if empty.
    
    """

    if not sequence:
        raise ValueError("The list cannot be empty")
    
    freq = {}

    for elem in sequence:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1

    return freq

"""
Classes
 - What the class represents,
 - Public methods,
 - Class and instance variables,
 - Effects of inheritance

"""

# Multi-line docstrings
class Backpack:
    """A class that represents a Backpack.

    Attribute:
        items (list): represent the list of items in the backpack (initially empty).

    Methods:
        add_items(self, item):
            Add the item to the backpack.
        remove_item(self, item):
            Remove the item from the backpack.
        has_item(self, item):
            Return True if the item is in the backpak. Else, return False.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not in the list")

    def has_item(self, item):
        return item in self.items
    
import math

class Circle:
    """A class that represents a circle.

    Attributes:
        radious (float): the distance from the center of the circle
            to its circumference.
        color (string): the color of the circle.
        diameter (float): the distance through the center of the circle
            from one side to the other.

    Methods:
        find_area(self):
            Return the area of the circle.
        find_perimeter(self):
            Return the perimeter of the circle.
    
    """

    def __init__(self, radious, color):
        """Initialize an instance of Circle.

        Arguments:
            radious (float): the distance from the center 
            of the circle to its circumference.
            color (string): the color of the circle.
        """
        self._radious = radious
        self._color = color

    @property
    def radious(self):
        """Return the radious of the circle.

        This is a float that represents the distance from
        the center of the circle to its circumference."""
        return self._radious
    
    @property
    def color(self):
        """Return the color of the circle represented as a string.
        
        The color is described by a string that must be capitalized.
        For example: "Red", "Blue", "Green", "Yellow".
        """
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def diameter(self):
        """Return the diameter of the circle.
        
        This is a float that represens the distance through 
        the center of the circle from one side to the other.        
        """
        return 2 * self._radious
    
    def find_area(self):
        """Find and return the area of a circle.

        The area is calculated with the circle radious
        using the formula Pi * (radious ** 2)
        """
        return math.pi * (self._radious ** 2)
    
    def find_perimeter(self):
        """FInd and return the perimeter of a circle.

        The perimeter is calculater with the circle radious
        using the formula (2 * Pi * radious).        
        """
        return 2 * math.pi * self._radious
    
help(Circle)
print(Circle.__doc__)
print(len.__doc__)
print(sorted)
help(list.sort)
help(tuple.count)
help(str.capitalize)
print(list.sort.__doc__)
print("\n")

#--------------------------------------------------------------#
class Flight:
    """Class that represents an international flight.

    Attributes:
        number (str): the flight number represented as a string.
        origin (str): a three-letter abbreviation of the country of origin. e.g. "USA".
        destination (str): a three-letter abbrevitation of the destination. e.g. "USA".
        num_passengers (int): an integer that represents the number of passengers that are
        currently registered from the flight.

    Methods:
        display_flight_data(): displays the data of the flight in a user-friendly format.
    """

    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """Initializes the values of the instance attributes of Flight.

        Args:
            number (str): the flight number represented as a string.
            origin (str): a three-letter abbreviation of the country of origin. e.g. "USA".
            destination (str): a three-letter abbreviation of the destination. e.g. "USA".
            num_passengers (int): an integer that represents the number of passengers that are
            currently registered for the flight.
            total_weight (float): the approximate weight of the flight including baggage, passengers,
            fuel, crew, and other elements.
            pilot (Pilot): the pilot assigned to the flight.
            crew (list of Crew): the crew assigned to the flight.
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew

    @property
    def total_weight(self):
        """Total weight of the flight, including luggage, crew, and fuel."""
        return self._total_weight
    
    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight
    
    @property
    def pilot(self):
        """Pilot assigned to the flight."""
        return self._pilot
    
    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot

    @property
    def crew(self):
        """Crew assigned to the flight."""
        return self._crew
    
    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew
    
    def display_flight_data(self):
        """Print flight data in a user-friendly format."""
        print("== Flight ==")
        print("Number: ", self.number)
        print("Print the number of passengers: ", self.num_passengers)
        print("Weight: ", self._total_weight)
        print("Pilot: ", self._pilot)
        print("Crew: ", self._crew)