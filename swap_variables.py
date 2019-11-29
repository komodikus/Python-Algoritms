def swap_variables_one(x=10, y=20):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y


def swap_variables_two(x=10, y=20):
    x = x + y
    y = x - y
    x = x - y
    return x, y


def swap_variables_three(x=10, y=20):
    x, y = y, x
    return x, y


if __name__ == '__main__':
    assert swap_variables_one(40, 30) == (30, 40)
    assert swap_variables_two(40, 30) == (30, 40)
    assert swap_variables_three(40, 30) == (30, 40)
