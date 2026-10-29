class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
      def __init__(self):
          self._head = None
          self._tail = None
          self._count = 0

      def append(self, data):
           new_node = Node(data)
           if not self._head:
               self._head = new_node
               self._tail = new_node

           else:
               self._tail.next = new_node
               self._tail = new_node

           self._count += 1

      def prepend(self, data):

