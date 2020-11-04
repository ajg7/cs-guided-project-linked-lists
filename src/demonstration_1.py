"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(head, index):
    # start traversing our linked list from the head
    # until we get to the node right before the one
    # we're going to delete
    current = head
    # keep a counter to know how many linked list nodes we've traversed
    counter = 1
    
    # iterate until counter == index -1
    while counter != index - 1:
        current = current.next
        counter += 1

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
a = LinkedListNode("A")

x.next = y
y.next = z
z.next = a


delete_node(y)
