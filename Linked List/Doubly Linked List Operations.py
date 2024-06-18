class Node:
    def __init__(self, data):
        """Initialize a node with data, next, and prev pointers as None."""
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None

    def traverse(self):
        """Access each element of the doubly linked list."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def insert(self, data, position=None):
        """Insert a new node with the given data at the specified position."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        if position is None or position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node.next and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node.prev:
                    current_node.prev.next = current_node.next
                return
            current_node = current_node.next

    def search(self, key):
        """Search for a node with the given key in the list."""
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def sort(self):
        """Sort the nodes of the doubly linked list."""
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            sorted_list = self._sorted_insert(sorted_list, current_node)
            current_node = next_node
        self.head = sorted_list

    def _sorted_insert(self, head, node):
        """Helper function to insert a node into a sorted doubly linked list."""
        if not head or node.data < head.data:
            node.next = head
            if head:
                head.prev = node
            head = node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            if current.next:
                current.next.prev = node
            current.next = node
            node.prev = current
        return head

    def print_list(self):
        """Print the doubly linked list in a readable format."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("null")

# Test cases
if __name__ == "__main__":
    # Create a doubly linked list and add nodes
    doubly_list = DoublyLinkedList()
    doubly_list.insert(3)
    doubly_list.insert(5)
    doubly_list.insert(13)
    doubly_list.insert(2)

    # Print the doubly linked list
    print("Initial list:")
    doubly_list.print_list()

    # Test traverse method
    print("\nTraversed list:", doubly_list.traverse())

    # Test insert method
    doubly_list.insert(1, 0)  # Insert at head
    doubly_list.insert(7, 3)  # Insert at position 3
    print("\nList after insertions:")
    doubly_list.print_list()

    # Test search method
    key_to_search = 13
    if doubly_list.search(key_to_search):
        print(f"\nNode with data {key_to_search} found.")
    else:
        print(f"\nNode with data {key_to_search} not found.")

    # Test delete method
    doubly_list.delete(5)
    print("\nList after deleting 5:")
    doubly_list.print_list()

    # Test sort method
    doubly_list.sort()
    print("\nList after sorting:")
    doubly_list.print_list()
