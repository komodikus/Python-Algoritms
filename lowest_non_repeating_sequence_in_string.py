def lowest_non_repeating_sequence_in_string(my_str: str) -> str:
    for i in my_str:
        if my_str.count(i) == 1:
            return i
    return "There aren't this char"


if __name__ == '__main__':
    assert 'b' == lowest_non_repeating_sequence_in_string("abcdefghija")
    assert 'h' == lowest_non_repeating_sequence_in_string("hello")
    assert 'J' == lowest_non_repeating_sequence_in_string("Java")
    assert 'i' == lowest_non_repeating_sequence_in_string("simplest")
