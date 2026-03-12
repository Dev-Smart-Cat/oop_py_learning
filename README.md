# OOP Python Learning Repo

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![OOP](https://img.shields.io/badge/OOP-Practice-orange)
![Status](https://img.shields.io/badge/status-learning-blueviolet)
This repository is dedicated to documenting and storing my learning journey in Object-Oriented Programming (OOP). It contains a collection of scripts developed to practice and reinforce OOP concepts in Python. Below, there are detailed descriptions of the main principles and fundamentals of OOP, along with practical examples. This repository serves as a valuable resource for future review and as a hands-on reference to revisit and strengthen understanding of OOP through real-world scripts.

## Repo Summary

This repository is organized into the following main sections:

### OOP Fundamentals in Python
Detailed explanations here below of key Object-Oriented Programming concepts and fundamentals:
- Aliasing, Mutation, and Cloning
- Class Attributes
- Instance Attributes
- Methods
- Data Structures (Nodes, Linked Lists)
- Docstrings and Documentation
- Encapsulation and Abstraction
- Getters and Setters
- Import Statements
- Special Methods
- Inheritance
- Object Identity and Operations

### Practical scripts
Hands-on scripts designed to reinforce OOP concepts through real-world applications. You can find these scripts both as standalone .py files in the root directory and within the 'mini_projects/' folder.

## Project Structure

```
oop_py_learning                         
├── __pycache__                       
│  ├── die.cpython-312.pyc            
│  ├── linked_list.cpython-312.pyc    
│  ├── node.cpython-312.pyc           
│  ├── player.cpython-312.pyc         
│  └── utils.cpython-312.pyc          
├── mini_projects                          
│  ├── bakery_system.py               
│  ├── cash_register_system.py        
│  ├── dice_game.py                   
│  ├── music_school.py                
│  ├── payrol_project.py              
│  └── tic_tac_toe_game.py            
├── LICENSE                           
├── README.md                         
├── alias_mut_imut_clon.py            
├── class_attributes.py               
├── data_struct_nodes_linked_list.py  
├── docstrings.py                     
├── encapsulation_abstraction.py      
├── getters_setters.py                
├── import_statement.md               
├── inheritance_attributes.py         
├── inheritance_methods.py            
├── instance_attributes_self.py       
├── methods_arguments.py              
├── objects_is_oper.py                
├── py_objects.py                     
├── requirements.txt                  
├── special_methods.py                
└── utils.py                          

```

# OOP Fundamentals in Python

## Aliasing, Mutation, and Cloning

### Alias:

Alias => used to indicate an additional name that a person sometimes uses.
Alias in programming => tow or more references to the same memory address in the program.
Accessing a memory address with 2 references.
DIFFERENT NAME ASSIGNED TO THE SAME OBJECT.

### Mutation:

Object -> mutable = can be modified such as:
                    - lists, 
                    - sets, 
                    - dictionaries.
       
       -> imutable = cannot be modified such as:
                    - booleans, 
                    - integers, 
                    - floats, 
                    - string, 
                    - tuples

#### Advantages and Disadvantages of Mutable and Immutable Data Types:

**Memory efficiency** => reuse existing objects instead of making new copies for each change.
Represent real-world objects that are mutable by nature 
Bugs: using mutable objects in a program might introduce bugs. You might unintentionally mutate an object in the program.

Potential risks of Aliasing: mutating objects => we might mutate an object unintentionally through an alias.
Safer from bugs => since they cannot be modified, they are less likely to introduce bugs.
Easier to understand => know their exact value, without any "hidden" or unexpected changes.

Disadvantages of immutable objects
Less efficient => it is needed to create a new copy of the object to make any changes,
which can be costly.

### CLoning:
Create an exact copy of the object that is completely independent from the original object.


## Class Attributes

A class attribute is an attribute of the class.
All instances of the class have access to this attribute.
They share the same value, so any changes made to this value affects all instances.

## Instance Attributes

Classes define the state and the behavior of the objects in a GENERIC way.
It is not specific. The code in the class has to work for any instance of the class

__init__() => special method used to define the initial state of an object.
Called automatically when an instance is created.

self => is a generic way of referring to the current instance of the class.
self is a generic way of referring to the current instance of the class. 
When using self, this referes to any concrete objects or instance of the class.

Instance attributes:
- They belong to the instances.
- Every instance has its own, independent, copy of the attribute
- Changing their value only affects a particular instance. Other instances are not modified

## Methods

Method => A function associated to an object of the class or to the class itself.
The methods defined in a class determine the behavior of the objects created from the class
and how they can interact with their state. 

#### Type Methods:
    - Instance Methods => methods that belong to a specific object. 
    - They have access to the state of the object that calls them.

Calling a method IS THE SAME AS calling a function.
Methods are define below the __init__ method.
Method names usually include verbs sice they represent actions.

#### Default Arguments:
def method_name(self, parameter=value)
The default value HAS TO BE at the end of the list of arguments.

## Data Structures (Nodes, Linked Lists, Pointer)

Data Structure => any of various methods or formats (such as an array, file, or record)
for ORGANIZING DATA in a computer.
Goal of using data structure => organize the data efficiently and optimize common operations
(read, add, remove, and update). 

#### OOP is important in data structure:
- Create instances
- Define elements of the instances
- Store data
- The connections between the data
- Implemente operations

#### Examples of linear data structures:
- arrays
- lists
- Graphs => data structures used to represent connections between elements.
- Linked list => a LINEAR (node1 -> node2 -> node3) collection of data elements where each element (node)
points to the next one. In the linked lists, each node stores a data and points to the next data. 
Linked lists can store each node in non-contious locations and the defined pointers are used to get to the next
node in the sequence, even if they are not physically next to each other in memory.

**HEAD** => is the FIRST node of a linked list.
**TAIL** => is the LAST node of a linked list.

**Singly Linked List** => allowed ONLY to go to a node to the next node (node1 -> node2 -> node3).
It is not allowed to go back to the previous node because there are no connections or pointers to go back. 

**Doubly Linked List** => it has 2 references nodes point to each other, IT IS ALLOWED to go from one node to the next node
and go back to the previous node.

**Traversing in Computer Science** => used to visit every element in the data structure and doing something with the data.

#### Nodes in Data Structure
- Node => basic unit of a data structure.
- Node can store 2 main elements:
    * Data (value stored)
    * Connections to make connections with other nodes.
- Capsules can make connections to other capsules to form a data structure.

**Pointer** => a reference to another node in the data structure OR a connection between one node to another node.
The node stores references to the nodes that it is connected to.

## Docstrings and Documentation

#### Key Guidelines:
- Use Trople double quotes.
- Closing quotes on same lines as opening quotes.
- End the line with a period.
- Write the aefect as a command.
- No blank line before or after.
- Mention return value.

We can read the docstrings that are "linked" to an element with a help()
function by passing the name of the class, function, method, or property name.
This is possible because docstrings are "linked" to the elements that they are
through the __doc__ attribute, a special attribute that we can use to access the docstring.

- **Docsstrings and Documentation**
See the script [docstrings.py](docstrings.py) for practical examples and explanations on how to use docstrings to document your Python classes, methods, and functions.

## Abstraction

**Abstraction** => show only the essential attributes and hide unnecessary details from the user.
Hide the complexity from the user. Abstraction also allows us to abstract out 
common parts of the code to avoid repetition. 

Interface => the "visible part of the class that the program can interact with."

Implementation => the internal part of the class with the code that performs the functionality.

## Getters and Setters

Getters and setters are members of a class, that is, they are methods.
Methods are like functions associated to a specific object or class.
Getters and setters let us get and set the valur of an instance attribute.

**Getters** => Get a value of an attribute. E.g. get_name, get_address, get_color, get_age, get_id 

**Setters** => Set the value of an attribute. To define a setter. Methods that we can call to set the value an instance attribute = self.instance_attribute = instance_attribute.
With setters we can validate the new value before assigning it to the attribute.
set_ + <attribute> e.g: set_name, set_address, set_color, set_age, set_id

We can make the attributes non-public and still provide a way to work with them indirectly.

## Import Statements

    * import <module>
        - This import statement import all the elements of the module.
        - The elements (functions, classes and variables) can be accessed with this
          syntax: <module>.<element>

    * from <module> import <elem>
        - This import statement only imports the specified element from the module.
        - We can use this element directly, without specifying the name of the module.

    * from <module> import *
        - This is a wildcard import statement. It imports all the elements from the module.
        - We do not need to specify the name of the module to use or call the elements.

    * import <module> as <name>
        - This import statement is used to import a module with a different name, 
          so we can use this new name in our code.
        - The elements can be accessed with <name>.<element>.

## Special Methods

**Special methos** => their names start and end with double underscores.

OPERATOR OVERLOADING => occurs when an operator has different implementations
depending on the data type of the operands.
This means that the same operator can have different functionality based on the data
tupe of the operands.

RICH COMPARISON => are special methods that allow us to customize the "behavior" 
of the comparison operators (< <= > >= == !=) when there operators act on instances of the class.

This customization of the behavior is a form of operator overloading because we are providing
a different functionality for the same operator depending on the data type of the operands.

**Rich Comparison methods** => compare objects based on specific criteria.
__lt__ < less than
__le__ <= less than or equal to
__eq__ == equal to
__ne__ != not equal to
__gt__ > greater than
__ge__ >= greater than or equal to

## Inheritance

Define common functionality in the superclass and subclasses will have access to these methods.

### Method Overriding

Method Overriding is used to customize or extend the functionality of a method that is already defined in the superclass.

Overriding involves modifying the behavior of a method within a hierarchy. When a method is overridden, its new implementation takes precedence over previous implementations located higher in the hierarchy.

### Inheritance Concepts

Inheritance: Defining classes that inherit attributes and methods from another class.

Classes usually inherit from more general classes that represent more abstract concepts.

Add new functionality or customize the existing one in the child class.
Eg: truck is a vehicle, meaning truck can be a child class of vehicle.

A class can inherit from multiple classes and multiple classes can inherit from the same class.
vehicle -> landvehicle -> car and truck

**Parent Class (SUPERCLASS):**
The class from which other classes inherit attributes and methods. 
E.g. Dog

**Child Class (SUBCLASS):**
The class that inherits attributes and methods from another class.
E.g: Poodle and Pintcher

## Object Identity and Operations

### Everything is an Object in Python

In Python, everything is an object:
    - int
    - float
    - bool
    - function
    - list
    - tuple
    - dict
    - string
    - exception

Programs keep track of how many references to the object exist.

**Reference:** A name that refers to the location in memory of an object. References keep objects alive and accessible in the program (e.g., variables, attributes, items).

Variables in Python store references to objects in memory. The object is stored somewhere in memory and the variable knows where to get that object from memory because it has a reference to that object.

When there are no references to the object in the program, the object is deleted from memory.

### The id() Function

The id() function returns the address of the object in memory. This is the address of the object in memory.

### The is Operator and ==

The operators is and is not test for an object's identity: x is y is true if and only if x and y are the same object.

If two variables do not reference the same object, they will have different ids.
If two variables reference the same object, they will have the same id.

The is operator returns True if both operands reference the same object. Else, it returns False.

**Differences between is vs ==:**
    - is checks the objects (if different references point to the same object)
    - == checks the values

Two objects may have the same value and still be different objects in memory.

### Optimizing Memory Usage (Integer Caching)

When accessing one of the integers from -5 to 256, the existing object will be reused. The integers with the same value will be the same object in memory. Python uses an object that already exists in memory for these values.

Unexpected results: the current implementation keeps an array of integer objects for all integers between -5 and 256. When you create an int in that range, you actually just get back a reference to the existing object.

### String Interning

String interning is the process of keeping only one distinct copy of the string in memory.

Since strings are immutable, Python can use the same object in memory for identical string values.

True because all of these variables reference the same object in memory.

### Passing Objects by Reference

Objects can be passed by value or reference. In Python, objects are passed by reference. We pass a reference to the object, not a new copy, so the original object can be modified.

Objects can be passed by:
    - value
    - reference

In Python, objects are passed by reference.

### How objects are stored in memory and the role of the id of an object:

In Python, everything is an object. When we create an object and assign it to a variable, the object is stored in a specific memory address and a reference to this memory address is returned. This is what variables "store": the reference to the object in memory. Each object has its own unique id (integer) during its lifetime that identifies the memory address where it is located.

### The is operator and object identity:

The "is" operator returns True if the two operands are or reference the same object in memory. If this is the case, the id of the two operands is the same integer. If the ids are not equal, the two operands are not the same object in memory and the "is" operator returns False. The id is a unique integer that is assigned to an object during its lifetime to reference its memory address. The id of an object can be retrieved using the id() function by passing the object as argument.

## License
MIT


