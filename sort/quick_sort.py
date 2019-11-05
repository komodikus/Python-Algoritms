import random
from typing import List

my_list_o = [random.randint(1, 100) for i in range(10)]


def quick_sort(data: List[int]):
    if len(data) <= 1:
        return data
    q = random.choice(data)
    l_data = [n for n in data if n < q]
    e_data = [q] * data.count(q)
    r_data = [n for n in data if n > q]
    return quick_sort(l_data) + e_data + quick_sort(r_data)




if __name__ == "__main__":
    print(my_list_o)
    print(quick_sort(my_list_o))