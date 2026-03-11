"""
Data Structure => any of various methods or formats (such as an array, file, or record)
for ORGANIZING DATA in a computer.

Goal of using data structure => organize the data efficiently and optimize common operations
(read, add, remove, and update). 

OOP is important in data structure:
- Create instances
- Define elements of the instances
- Store data
- The connections between the data
- Implemente operations

Examples of linear data structures:
- arrays
- lists
- Graphs => data structures used to represent connections between elements.


#---------------------------------------------------------------------------------------------------------#

- Linked list => a LINEAR (node1 -> node2 -> node3) collection of data elements where each element (node)
points to the next one. In the linked lists, each node stores a data and points to the next data. 
Linked lists can store each node in non-contious locations and the defined pointers are used to get to the next
node in the sequence, even if they are not physically next to each other in memory.

HEAD => is the FIRST node of a linked list.
TAIL => is the LAST node of a linked list.

Singly Linked List => allowed ONLY to go to a node to the next node (node1 -> node2 -> node3).
It is not allowed to go back to the previous node because there are no connections or pointers to go back. 

Doubly Linked List => it has 2 references nodes point to each other, IT IS ALLOWED to go from one node to the next node
and go back to the previous node.

#---------------------------------------------------------------------------------------------------------#

Traversing in Computer Science => used to visit every element in the data structure and doing something with the data.

#---------------------------------------------------------------------------------------------------------#

Nodes in Data Structure
- Node => basic unit of a data structure.

- Node can store 2 main elements:
    * Data (value stored)
    * Connections to make connections with other nodes.

- Capsules can make connections to other capsules to form a data structure.

Pointer => a reference to another node in the data structure OR a connection between one node to another node.
The node stores references to the nodes that it is connected to.

"""

from utils import Node

# Create an instance and pass the value 1.
node2 = Node(3)
# Node 1 is pointing to node 2
# node1 (point) -> node2 
node1 = Node(5, node2)


print(node1.value)
print(node2.value)
# node1 (is pointing to) -> node2
print("node1 (is pointing to) -> node2")
print(node1.next)
# Confirm if next pointer of the Node one is node two.
print("Confirm if next pointer of Node one is node two")
print(node1.next is node2)
print(node2.next)
print("\n")

print("---------------------------------")
print("Practice: Create a Sequence of Nodes")

node_d = Node("d", None)
node_c = Node("c", node_d)
node_b = Node("b", node_c)
node_a = Node("a", node_b)

print("Print the attributes value and next.")
print("\n")
print("Graphical representation of the result:")
print("node_a -> node_b -> node_c -> node_d")
print("\n")
print("node_a: ")
print(node_a.value)
print(node_a.next)
print(node_a.next is node_b)
print("\n")

print("node_b: ")
print(node_b.value)
print(node_b.next)
print(node_b.next is node_c)
print("\n")


print("node_c: ")
print(node_c.value)
print(node_c.next)
print(node_c.next is node_d)
print("\n")

print("node_d: ")
print(node_d.value)
print(node_d.next)
print("\n")

#----------------------------------------------------------------------------------#
print("Creating a linked list:")
from utils import Linked_List

my_linked_list = Linked_List()
print(my_linked_list.head)
my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(15)
# This is the how the linked list looks like
print("1st: 9")
print("2nd: 3 -> 9")
print("3rd: 3 -> 6 -> 9")
print("4th: 3 -> 6 -> 9 -> 15")
# Print the HEAD value
print(my_linked_list.head.value)
# Print the value 6 = middle node
print(my_linked_list.head.next.value)
# Print the TAIL, EACH .next POINTS to the previous node (value 3, 6, 9)
print(my_linked_list.head.next.next.value)
# Print the TAIL, EACH .next POINTS to the previous node (value 3, 6, 9, 15)
print(my_linked_list.head.next.next.next.value)
# Print each node of the linked list
print(my_linked_list.print_list_items())
# Count the notes
print(my_linked_list.count_nodes_interact())
my_linked_list.insert_node(0)
# Count the nodes after adding the node 0
print(my_linked_list.count_nodes_interact())
# Count the nodes
print(my_linked_list.count_nodes())
# Find a value in the linked list
print(my_linked_list.find_node(11))


# Print the nodes BEFORE delete node 0
my_linked_list.print_list_items()
# Delete a node in the linked list
print(my_linked_list.delete_node(0))
# Print the list of nodes AFTER printing the nodes 
my_linked_list.print_list_items()

# Print the nodes BEFORE delete the MIDDLE node
my_linked_list.print_list_items()
# Delete value 9, which in the middle of the linkec list
print(my_linked_list.delete_node(9))
# Print the list of nodes AFTER printing the MIDDLE node
my_linked_list.print_list_items()


