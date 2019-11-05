import random

my_list_o = [random.randint(1, 100) for i in range(10)]


def insertion_sort(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


if __name__ == "__main__":
    print(my_list_o)
    print(insertion_sort(my_list_o))
