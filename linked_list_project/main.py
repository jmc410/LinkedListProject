from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def main():

    print("=== Forward Construction ===")

    values = [10, 20, 30, 40, 50]

    forward = SinglyLinkedList()
    forward.build_list_forward(values)

    print(forward)

    print("\n=== Backward Construction ===")

    backward = SinglyLinkedList()
    backward.build_list_backward(values)

    print(backward)

    print("\n=== Insert, Remove, and Remove All ===")

    demo = SinglyLinkedList()
    demo.build_list_forward([10, 20, 30, 20, 40, 20])

    demo.insert_after(30, 35)
    print("After insertion:", demo)

    demo.remove(10)
    print("After removal:", demo)

    removed = demo.remove_all(20)

    print(f"Removed {removed} occurrences of 20:")
    print(demo)

    print("\n=== Split Evens and Odds ===")

    source = SplitEvensOdds()
    source.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])

    print("Original list:", source)

    even_list, odd_list = source.split_even_odd()

    print("Even list:", even_list)
    print("Odd list:", odd_list)
    print("Original after split:", source)

    print("\n=== Error Handling ===")

    try:
        demo.remove(999)

    except ValueError as error:
        print("Handled error:", error)


if __name__ == "__main__":
    main()