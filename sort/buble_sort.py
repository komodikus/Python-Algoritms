import random

my_list = [random.randint(1, 100) for i in range(10)]


def bubble_sort(array: list) -> list:
    len_array_minus_one = len(array) - 1
    for i in range(len_array_minus_one):
        for j in range(len_array_minus_one - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array



if __name__ == "__main__":
    print(my_list)
    print(bubble_sort(my_list))
