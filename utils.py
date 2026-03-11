class Node:
    """"A class that represent a node.
    
    This class will be used as a module and imported to "data_struct_nodes_linked_list.py",
    which is the main source code.

    Attributes:
        value (int): the value of the node, the value that will be stored in the data structure.
        next: reference to another node, it is a POINTER. Used to create the connection between e.g node1 -> node2 
        the next node. It is optional and by default starts as None
    """
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node
    
    # This is a property to get the value
    @property
    def value(self):
        return self._value
    
    # This is a property to set a new value
    @value.setter
    def value(self, new_value):
        self._value = new_value

    # This is a property to POINT to the next node (node2)
    @property
    def next(self):
        return self._next
    
    # This is a property to set a next value to the node
    @next.setter
    def next(self, new_next):
        self._next = new_next

from utils import Node   # importing Node class from node module. 

class Linked_List:

    def __init__(self):
        # This is a instance attribute that represents the first node of a linked list
        self.head = None

    def insert_node(self, value):
        # Create a node and assign it to the new_node var
        new_node = Node(value)

        if self.head is None:  ### that is, if the linked list is EMPTY.
            self.head = new_node
        # Condition to the new_node becomes the first node (head)
        # when the value is >= the other nodes. 
        elif self.head.value >= value:
            # the first node (head) points to the first node in the list.
            new_node.next = self.head
            # The new_node becomes the first node (head)
            self.head = new_node
        else:
            # previous refers to the head node 
            previous = self.head
            # runner refers to the second node in the liked list
            runner = self.head.next

            # Until this condition is False, it continues to move to the right 
            # until the end of the linked list.
            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
            # The new_node POINTS to the runner.
            new_node.next = runner
            # The previous node POINTS to the new_node
            previous.next = new_node

    # This METHOD traverse the elements of the linked list.
    # MEANING, prints all elements/data of EACH node.
    def print_list_items(self):
        if self.head is None:
            print("Empty")
        else:
            # This is the node will be updated as moving 
            # through the list to access each one of the nodes.
            runner = self.head
            while runner is not None:
                # Print the value of the nodes on the same line,
                # end= parameter separate the values with a space end= " "
                # and print them all on the same line.
                print(runner.value, end=" ")
                # Move through the list towards the right going node by node
                # and check its value.
                runner = runner.next
            # Get the output separated with one line for method call.
            print()

    # This METHOD counts the nodes INTERACTIVELY
    def count_nodes_interact(self):
        count = 0
        # This is a reference to the first node visited
        runner = self.head

        # Use the while nodes because it is unknown how many items 
        # will be in the linked list. Also, while the runner IS NOT None,
        # this indicates the node IS NOT None.
        while runner is not None:
            count += 1
            # Get the next node and assign to the new runner
            runner = runner.next
        
        return count
    
    def count_nodes(self):
        return self.count_nodes_recurse(self.head)
    
    # This METHOD counts the nodes RECURSIVELY
    def count_nodes_recurse(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recurse(node.next)
        
    def find_node(self, target_value):
        # This variable is used to move through the linked list.
        runner = self.head
        while runner is not None:
            # Condition to check if the value of the current node
            # is the target
            if runner.value == target_value:
                return True
            else:
                runner = runner.next

        return False
    
    def delete_node(self, target_value):
        if self.head is None:
            return False
        elif self.head.value == target_value:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next
            # The end of the list is not reached and 
            # the target_value > current value of the runner. 
            while (runner is not None) and (target_value > runner.value):
                previous = runner
                runner = runner.next

            if (runner is not None) and (runner.value == target_value):
                # This POINTS to the node before runner.
                # Previous will now point to the node 
                # that comes after the runner node.
                previous.next = runner.next
                return True
            else:
                return False

