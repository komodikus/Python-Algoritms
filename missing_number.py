def get_missing_number(array: list):
    n = len(array)
    total = (n + 1) * (n + 2) / 2
    sum_of_arr = sum(array)
    return int(total - sum_of_arr)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 6, 7, 8, 9]
    assert get_missing_number(array) == 5
