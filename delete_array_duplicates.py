def delete_array_duplicates(array: list) -> list:
    result = list()
    for num, elem in enumerate(array):
        if num >= 1 and elem != array[num - 1]:
            result.append(elem)
    return result


if __name__ == '__main__':
    my_array = [1, 23, 23, 23, 23, 4, 5, 6]
    print(delete_array_duplicates(my_array))
    assert delete_array_duplicates(my_array) == [23, 4, 5, 6]