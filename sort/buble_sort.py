import random

my_list = [random.randint(1, 100) for i in range(10)]


def buble_sort(my_list):
    for i in range(len(my_list)):
        for in_element in range(1, len(my_list)):
            if my_list[in_element] < my_list[in_element - 1]:
                my_list[in_element], my_list[in_element - 1] = my_list[in_element - 1], my_list[in_element]
    return my_list


if __name__ == "__main__":
    print(my_list)
    print(buble_sort(my_list))
