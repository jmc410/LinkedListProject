import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def test_append_and_prepend(self):
        linked = SinglyLinkedList()

        linked.append(20)
        linked.prepend(10)
        linked.append(30)

        self.assertEqual(list(linked), [10, 20, 30])
        self.assertEqual(len(linked), 3)
        self.assertEqual(linked._tail.data, 30)
        self.assertIsNone(linked._tail.next)

    def test_append_and_prepend_empty(self):
        linked = SinglyLinkedList()

        linked.append(1)

        self.assertIs(linked._head, linked._tail)

        linked = SinglyLinkedList()
        linked.prepend(1)

        self.assertIs(linked._head, linked._tail)

    def test_build_forward(self):
        values = [10, 20, 30, 40, 50]
        original = values[:]

        linked = SinglyLinkedList()
        linked.build_list_forward(values)

        self.assertEqual(list(linked), original)
        self.assertEqual(values, original)

    def test_build_backward(self):
        values = [10, 20, 30, 40, 50]
        original = values[:]

        linked = SinglyLinkedList()
        linked.build_list_backward(values)

        self.assertEqual(list(linked), [50, 40, 30, 20, 10])
        self.assertEqual(values, original)

    def test_contains_and_is_empty(self):
        linked = SinglyLinkedList()

        self.assertTrue(linked.is_empty())
        self.assertFalse(linked.contains(5))

        linked.append(5)

        self.assertFalse(linked.is_empty())
        self.assertTrue(linked.contains(5))

    def test_iteration_and_length(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([1, 2, 3])

        self.assertEqual(list(linked), [1, 2, 3])
        self.assertEqual(len(linked), 3)

    def test_insert_after(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])

        linked.insert_after(20, 25)
        linked.insert_after(30, 40)

        self.assertEqual(list(linked), [10, 20, 25, 30, 40])
        self.assertEqual(linked._tail.data, 40)
        self.assertIsNone(linked._tail.next)

    def test_insert_after_missing(self):
        linked = SinglyLinkedList()
        linked.append(1)

        with self.assertRaises(ValueError):
            linked.insert_after(99, 100)

    def test_remove(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30, 40])

        linked.remove(10)
        linked.remove(30)
        linked.remove(40)

        self.assertEqual(list(linked), [20])

        linked.remove(20)

        self.assertTrue(linked.is_empty())
        self.assertIsNone(linked._head)
        self.assertIsNone(linked._tail)

    def test_remove_missing(self):
        linked = SinglyLinkedList()
        linked.append(1)

        with self.assertRaises(ValueError):
            linked.remove(2)

    def test_remove_all(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([7, 2, 7, 7, 3, 7])

        removed = linked.remove_all(7)

        self.assertEqual(removed, 4)
        self.assertEqual(list(linked), [2, 3])
        self.assertEqual(len(linked), 2)
        self.assertEqual(linked._tail.data, 3)
        self.assertIsNone(linked._tail.next)

    def test_remove_all_no_matches(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([1, 2, 3])

        self.assertEqual(linked.remove_all(9), 0)
        self.assertEqual(list(linked), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()