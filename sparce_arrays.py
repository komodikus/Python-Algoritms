"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
"""


def sparce_arrays(query_array, string_array):
    result = list()
    for string in string_array:
        count = 0
        for query in query_array:
            if string == query:
                count += 1
        result.append(count)
    return result


if __name__ == '__main__':
    assert sparce_arrays(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']) == [2, 1, 0]
