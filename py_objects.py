# Objects can be passed by => value 
#                            => reference

# In python, objects are passed by reference.

"""
How the objects are stored in a memory and the role of the id of an object:

In python, everything is an object. When we create an object and assign it to a variable,
the object is stored in a specific memory address and a reference to this memory address is returned.
This is what variables "store", the reference to the object in memory. Each object has its own unique id (integer)
during its lifetime that identifies the memory address where it is located.

Explain the purpose of the is operator. How is it related to the id object:

The "is" operator returns True if the two operands are or reference the object in memory.
If this is the case, the id of the two operands is the same integer. If the ids are not equal, 
the two operands are not the same object in memory and the "is" operator returns False. 
The id is a unique integer that is assigned to an object during its lifetime to reference its memory address.
The if of an objectcan be retrieved using id() function by passing THE OBJECT as argument.
"""

# THIS IS THE OBJECT
my_list = [6, 2, 8, 2]

def print_data(seq):
    print("Inside function: ", id(seq))
    for elem in seq:
        print(elem)

def multiply_by_two(seq):
    print("Inside the function:", id(seq))
    for i in range(len(seq)):
        seq[i] *= 2


class Sale:
    
    def __init__(self, amount):
        self.amount = amount

    @property
    def print_sale(self):
        return print(self.amount)

def find_total(sales_list):
    total = 0

    # sale is the object
    for sale in sales_list:
        print("New sale")
        print(sale.amount)
        # amount WITHOUT following self can be used this way 
        # because it is OUTSIDE THE CLASS. 
        total += sale.amount
    
    return total

sale_one = Sale(1000)
sale_one.print_sale

# These are the objects created using Sale class
jan_sales = [Sale(400), Sale(345), Sale(45)]

print(find_total(jan_sales))