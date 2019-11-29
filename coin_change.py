def coins_change(target: int, coins_to_change: tuple) -> int:
    count = 0
    coins_to_change = reversed(sorted(coins_to_change))
    for coin in coins_to_change:
        count += target // coin
        target = target % coin
    return count


if __name__ == '__main__':
    assert coins_change(39, (10, 5, 3, 2)) == 5
