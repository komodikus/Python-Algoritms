import random

my_list_o = [random.randint(1, 100) for i in range(10)]


def choise_sort(data):
        for i, e in enumerate(data):
            min_el = min(range(i, len(data)), key=data.__getitem__)
            data[i], data[min_el] = data[min_el], e
        return data


if __name__ == "__main__":
    print(my_list_o)
    print(choise_sort(my_list_o))
