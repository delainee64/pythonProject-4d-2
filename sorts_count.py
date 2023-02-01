# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/01/2023
# Description: Write a bubble sort that counts the number of comparisons and the number of
# exchanges made while sorting a list and returns a tuple of the two values
# (comparisons first, exchanges second). Do the same for insertion sort.

def bubble_count(num_list):
    """Bubble counts and returns the number of comparisons and exchanges."""
    comparisons = 0
    exchanges = 0
    for index in range(len(num_list)):
        for pass_num in range(index + 1, len(num_list)):
            comparisons += 1
            if num_list[index] > num_list[pass_num]:
                temp = num_list[index]
                num_list[index] = num_list[pass_num]
                num_list[pass_num] = temp
                exchanges += 1
    return comparisons, exchanges


def insertion_count(num_list):
    """Counts by insertion and returns the number of comparisons and exchanges."""
    comparisons = 0
    exchanges = 0
    for index in range(1, len(num_list)):
        num = num_list[index]
        pos = index - 1
        while pos >= 0:
            comparisons += 1
            if num < num_list[pos]:
                exchanges += 1
                num_list[pos + 1] = num_list[pos]
                pos -= 1
            else:
                break

    return comparisons, exchanges
