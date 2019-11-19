import datetime
import sys

sys.setrecursionlimit(12000)


def rec_print(n):
    if n < 2:
        return [1]
    return [n] + rec_print(n - 1)


def acerman_rec(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return acerman_rec(m - 1, 1)
    if m > 0 and n > 0:
        return acerman_rec(m - 1, acerman_rec(m, n - 1))


def rank_of_two(n):
    if n == 0:
        return 1
    return 2 * rank_of_two(n - 1)


def sum_of_nums(number):
    if number < 10:
        return number
    return sum_of_nums(number // 10) + number % 10


def inverse_number(number):
    if number < 10:
        return number
    return int(str(number % 10) + str(inverse_number(number // 10)))


def print_number(number):
    if number < 10:
        return number
    return int(str(print_number(number // 10)) + str(number % 10))


def is_prime(number):
    return all(number % i for i in range(2, number))


def multiplers_of_nums(number, d=1):
    if d > number // 2:
        return 1
    if number % d == 0:
        if is_prime(d):
            print(d)
    return multiplers_of_nums(number, d + 1)


def is_palindrome(my_str):
    if len(my_str) < 2:
        return True
    else:
        return my_str[0] == my_str[-1] and is_palindrome(my_str[1: -1])


def max_element(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        m = max_element(my_list[1:])
        return m if m > my_list[0] else my_list[0]


if __name__ == '__main__':
    # print(rec_print(10))
    # print(acerman_rec(2, 2))
    # print(rank_of_two(10))
    # print(sum_of_nums(55666))
    # print(inverse_number(123))
    # print(print_number(1245))
    # time_now = datetime.datetime.now()
    # print(multiplers_of_nums(950))
    # print(datetime.datetime.now()- time_now)
    # print(all(5 % i for i in range(2, 5)))
    # print(is_palindrome("helleh"))
    # print(max_element([1,23,4,656,34,656,23,12,321,154,564,123,54,324,65,23,656,]))
