from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):

    def split_even_odd(self):

        if self.is_empty():
            raise ValueError("Cannot split an empty linked list.")

        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        current = self._head

        while current is not None:

            next_node = current.next

            current.next = None

            if current.data % 2 == 0:
                target = even_list
            else:
                target = odd_list

            if target._head is None:
                target._head = current
                target._tail = current
            else:
                target._tail.next = current
                target._tail = current

            target._count += 1

            current = next_node

        self._head = None
        self._tail = None
        self._count = 0

        return even_list, odd_list