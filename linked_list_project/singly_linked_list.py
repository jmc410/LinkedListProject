from node import Node


class SinglyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def append(self, value):
        new_node = Node(value)

        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def prepend(self, value):
        new_node = Node(value)

        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._count += 1

    def insert_after(self, existing_value, new_value):
        current = self._head

        while current is not None:
            if current.data == existing_value:
                new_node = Node(new_value)

                new_node.next = current.next
                current.next = new_node

                if current == self._tail:
                    self._tail = new_node

                self._count += 1
                return

            current = current.next

        raise ValueError(f"{existing_value} was not found in the list.")

    def remove(self, value):
        current = self._head
        previous = None

        while current is not None:
            if current.data == value:

                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next

                if current == self._tail:
                    self._tail = previous

                self._count -= 1

                if self._count == 0:
                    self._head = None
                    self._tail = None

                current.next = None
                return

            previous = current
            current = current.next

        raise ValueError(f"{value} was not found in the list.")

    def contains(self, value):
        current = self._head

        while current is not None:
            if current.data == value:
                return True

            current = current.next

        return False

    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.data
            current = current.next

    def build_list_forward(self, values):
        for value in values:
            self.append(value)

    def build_list_backward(self, values):
        for value in values:
            self.prepend(value)

    def remove_all(self, value):
        current = self._head
        previous = None
        removed_count = 0

        while current is not None:

            if current.data == value:

                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next

                if current == self._tail:
                    self._tail = previous

                removed_count += 1
                self._count -= 1

                current.next = None

                if previous is None:
                    current = self._head
                else:
                    current = previous.next

            else:
                previous = current
                current = current.next

        if self._count == 0:
            self._head = None
            self._tail = None

        return removed_count

    def __str__(self):
        values = " -> ".join(str(value) for value in self)

        if values:
            return f"Head -> {values} -> None"

        return "Head -> None"