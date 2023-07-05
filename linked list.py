class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_data, data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError("Target data not found")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError("Data not found")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.prepend(5)
linked_list.insert_after(10, 15)
linked_list.delete(20)

linked_list.print_list()  # Output: 5 10 15 30
print(linked_list.search(15))  # Output: True
print(linked_list.search(20))  # Output: False
print(linked_list.get_size())  # Output: 4
