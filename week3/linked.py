class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append item
    def append(self, data):
        new_node = Node(data)
        if self.head is None:       # first item
            self.head = new_node
        else:                       # n:th item
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    # Insert item
    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for _ in range(index - 1):
                if node is None:
                    raise IndexError("Index out of range")
                node = node.next
            if node is None:
                raise IndexError("Index out of range")
            new_node.next = node.next
            node.next = new_node

    # Delete item
    def delete(self, index):
        if self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data
        else:
            node = self.head
            for _ in range(index - 1):
                if node.next is None:
                    raise IndexError("Index out of range")
                node = node.next
            if node.next is None:
                raise IndexError("Index out of range")
            deleted_data = node.next.data
            node.next = node.next.next
            return deleted_data
        
    # Find index of item
    def index(self, data):
        node = self.head
        index = 0
        while node:
            if node.data == data:
                return index
            node = node.next
            index += 1
        return -1
    
    # Swap items
    def swap(self, i, j):
        if i == j:
            return

        previous_i = None
        current_i = self.head
        for _ in range(i):
            if current_i is None:
                return
            previous_i = current_i
            current_i = current_i.next

        previous_j = None
        current_j = self.head
        for _ in range(j):
            if current_j is None:
                return
            previous_j = current_j
            current_j = current_j.next

        if previous_i:
            previous_i.next = current_j
        else:
            self.head = current_j

        if previous_j:
            previous_j.next = current_i
        else:
            self.head = current_i

        current_i.next, current_j.next = current_j.next, current_i.next

    # Insertion sort
    def isort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while (sorted_current.next is not None and sorted_current.next.data < current.data):
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node

        self.head = sorted_list

        
    # print list
    def print(self):
        node = self.head
        elements = []
        while node:
            elements.append(str(node.data))
            node = node.next
        for element in elements:
            if element != elements[-1]:
                print(element, end=" -> ")
            else:
                print(element)

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()
    L.delete(0)
    L.print()



if __name__ == "__main__":
    print("\nFind index and swapping")
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()
    print(L.index(7))   
    print(L.index(9))   
    L.swap(1, 4)
    L.print()
    L.swap(2, 0)
    L.print()

if __name__ == "__main__":
    print("\nInsertion sort")
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()
    L.isort()
    L.print()
