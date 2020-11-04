
# Doubly Linked List (Singly Linked List would not have prev)
class LinkedListNode:
    def _init_(self, value):
        self.value = value
        self.next = None
        self.prev = None

x = LinkedListNode("X")
y = LinkedListNode("Y")
z = LinkedListNode("Z")

x.next = y
y.next = z

y.prev = z
z.prev = y

# traverse a linked list
# print out its contents
def print_ll(node):
    # we'll traverse the ll along the next reference
    # some way to keep track of where we are as we're iterating
    # use a variable/reference
    # set your "current" variable to the starting node
    current = node
    
    # keep moving current in a loop
    # while current is not None:
    while current:
        #how do we move "current"?
        # the variable itself
        # and wha the variable is referring
        # and what the variable is referring
        print(current.value)
        current = current.next 
        
print(print_ll(x))