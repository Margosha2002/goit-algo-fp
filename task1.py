class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        current_node = self

        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def insertion_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next
        sorted_head = insert_into_sorted(sorted_head, current)
        current = next_node

    return sorted_head


def insert_into_sorted(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return sorted_head


def merge_sorted_linked_lists(list1, list2):
    dummy_head = Node(0)
    current = dummy_head

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy_head.next


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

print("Head: ", end="")
head.print()

reversed_head = reverse_linked_list(head)

print("Reversed Head: ", end="")
reversed_head.print()

sorted_head = insertion_sort_linked_list(reversed_head)

print("Sorted Head: ", end="")
sorted_head.print()

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

print("List 1: ", end="")
list1.print()

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

print("List 2: ", end="")
list2.print()

merged_head = merge_sorted_linked_lists(list1, list2)

print("Merged and sorted List 1 and List 2: ", end="")
merged_head.print()
