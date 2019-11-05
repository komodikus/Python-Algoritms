import random
from typing import List

my_list_o = [random.randint(1, 100) for i in range(10)]


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


def merge_sort(data: List[int]):
    if len(data) == 1:
        return data
    mid = len(data) // 2
    right_list = merge_sort(data[mid:])
    left_list = merge_sort(data[:mid])
    return merge(left_list, right_list)


if __name__ == "__main__":
    print(my_list_o)
    print(merge_sort(my_list_o))
