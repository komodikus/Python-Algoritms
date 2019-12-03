from typing import Iterable


def merge_arrays(array):
    result = list()
    for el in array:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            result.extend(merge_arrays(el))
        else:
            result.append(el)
    return result

if __name__ == '__main__':
    test_arr = [123,1232143,[1,2,[3,4]]]
    print(merge_arrays(test_arr))
