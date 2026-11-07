import unittest

from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


class TestSplitEvensOdds(unittest.TestCase):

    def make_source(self, values):
        source = SplitEvensOdds()
        source.build_list_forward(values)
        return source

    def test_mixed_values(self):
        source = self.make_source([1, 2, 3, 4, 5, 6, 7, 8])

        original_nodes = []
        current = source._head

        while current is not None:
            original_nodes.append(current)
            current = current.next

        even_list, odd_list = source.split_even_odd()

        self.assertEqual(list(even_list), [2, 4, 6, 8])
        self.assertEqual(list(odd_list), [1, 3, 5, 7])

        result_nodes = []

        for linked in [even_list, odd_list]:
            current = linked._head

            while current is not None:
                result_nodes.append(current)
                current = current.next

        self.assertEqual(
            {id(node) for node in original_nodes},
            {id(node) for node in result_nodes}
        )

        self.assertEqual(len(even_list), 4)
        self.assertEqual(len(odd_list), 4)

        self.assertEqual(even_list._tail.data, 8)
        self.assertEqual(odd_list._tail.data, 7)

        self.assertIsNone(even_list._tail.next)
        self.assertIsNone(odd_list._tail.next)

        self.assertTrue(source.is_empty())
        self.assertIsNone(source._head)
        self.assertIsNone(source._tail)
        self.assertEqual(len(source), 0)

    def test_all_even(self):
        source = self.make_source([2, 4, 6])

        even_list, odd_list = source.split_even_odd()

        self.assertEqual(list(even_list), [2, 4, 6])
        self.assertEqual(list(odd_list), [])

    def test_all_odd(self):
        source = self.make_source([1, 3, 5])

        even_list, odd_list = source.split_even_odd()

        self.assertEqual(list(even_list), [])
        self.assertEqual(list(odd_list), [1, 3, 5])

    def test_single_even(self):
        source = self.make_source([8])

        even_list, odd_list = source.split_even_odd()

        self.assertEqual(list(even_list), [8])
        self.assertEqual(list(odd_list), [])

    def test_single_odd(self):
        source = self.make_source([9])

        even_list, odd_list = source.split_even_odd()

        self.assertEqual(list(even_list), [])
        self.assertEqual(list(odd_list), [9])

    def test_empty_source(self):
        source = SplitEvensOdds()

        with self.assertRaises(ValueError):
            source.split_even_odd()


if __name__ == "__main__":
    unittest.main()



    # self reminder -> console -> py -m unittest -v