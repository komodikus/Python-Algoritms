def binary_search(sorted_list, element):
    if len(sorted_list) == 0:
        return False
    else:
        center_index = len(sorted_list) // 2
        if element == sorted_list[center_index]:
            return True
        if element > sorted_list[center_index]:
            return binary_search(sorted_list[center_index + 1:], element)
        if element < sorted_list[center_index]:
            return binary_search(sorted_list[:center_index], element)


if __name__ == '__main__':
    my_list = [i for i in range(1, 10)]
    print(my_list)
    print(binary_search(my_list, 6))
