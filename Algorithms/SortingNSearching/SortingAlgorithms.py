def merge_sort(integers: list, left_index: int, right_index: int):
    """ merge sort that is done in place for a list of integers """
    # base case, essentially we've reached one number which by definition is already sorted, do nothing.
    if left_index == right_index:
        return

    # when it is not one number, we need to find the middle to split
    middle_index = (left_index + right_index) // 2

    # Recursive call to keep halving and making our views smaller
    merge_sort(integers, left_index, middle_index)
    merge_sort(integers, middle_index + 1, right_index)

    # Helper function to merge it with two pointers continually grabbing the smallest
    pointer_merge(integers, left_index, right_index, middle_index)


def pointer_merge(integers: list, left_index: int, right_index: int, middle_index: int):
    """ helper function that essentially merges two sections of a list """
    left_half = integers[left_index: middle_index + 1]
    right_half = integers[middle_index + 1:right_index + 1]
    left_half_index = 0
    right_half_index = 0
    current_index = left_index

    # here we will iterate through the two halves until one half is exhausted
    while left_half_index < len(left_half) and right_half_index < len(right_half):

        # If the current number in the left half is smaller than the current number in the right half.
        # The left half gets selected to be entered in as the next smallest. Pointer is moved on the left half.
        if left_half[left_half_index] <= right_half[right_half_index]:
            integers[current_index] = left_half[left_half_index]
            left_half_index += 1

        # If the current number in the right half is smaller than the current number in the left half.
        # The right half number gets selected to be entered in as the next smallest. Pointer is moved on the right half.
        else:
            integers[current_index] = right_half[right_half_index]
            right_half_index += 1

        # We've determined the number to be in current_index in the integers list, we can move to the next index
        current_index += 1

    # This is our final clean up since we've only exhausted one of the halves.
    # We check if we have number remaining in the left half, if so add them to integers
    if left_half_index < len(left_half):
        for index in range(left_half_index, len(left_half)):
            integers[current_index] = left_half[index]
            current_index += 1

    # if it wasn't the left half that had integers remaining, then it's the right half, add those in order
    else:
        for index in range(right_half_index, len(right_half)):
            integers[current_index] = right_half[index]
            current_index += 1


def insertion_sort(integers: list):
    """ insertion sort that is done in place for a list of integers """
    # we start at range 1 because our first ones to check are at 0th and 1 index
    for integer_index in range(1, len(integers)):
        right_index = integer_index
        left_index = right_index - 1

        # iterate until we reach the beginning of the list
        while left_index >= 0:
            # whenever the right integer is greater than the left integer, swap, keep moveing left
            # and repeating this comparison until no longer the case
            if integers[right_index] < integers[left_index]:
                temp_left_integer = integers[right_index]
                temp_right_integer = integers[left_index]
                integers[left_index] = temp_left_integer
                integers[right_index] = temp_right_integer
                right_index -= 1
                left_index -= 1
            # break out since the integers are in the correct position, no need to keep comparing and move left.
            else:
                break


def run_a_sort(file_location: str, output_file_name: str, sorting_type: str):
    assert sorting_type in ["insertion", "merge"], "sorting type must be one of insertion or merge"
    with open(file_location, 'r') as data:
        all_insertion_sort_solutions = []
        for line in data:
            line = line.rstrip()
            integers = line.split(" ")
            integers = [int(x) for x in integers]
            integers = integers[1:]
            if sorting_type == "insertion":
                insertion_sort(integers)
            else:
                merge_sort(integers, 0, len(integers) - 1)
            all_insertion_sort_solutions.append(integers)

    with open(output_file_name, 'w') as output_file:
        for result in all_insertion_sort_solutions:
            for number in result:
                output_file.write(str(number) + " ")
            output_file.write("\n")


if __name__ == "__main__":

    file_location = "data.txt"
    insertion_sort_file_location = "insert.out"
    merge_sort_file_location = "merge.out"

    print("RUNNING INSERTION SORT FOR THE DATA IN data.txt")
    run_a_sort(file_location, insertion_sort_file_location, "insertion")
    print("INSERTION SORT COMPLETED, PLEASE THE RESULTS IN insert.out\n")
    print("RUNNING MERGE SORT FOR THE DATA IN data.txt")
    run_a_sort(file_location, merge_sort_file_location, "merge")
    print("MERGE SORT COMPLETED, PLEASE THE RESULTS IN merge.out\n")
