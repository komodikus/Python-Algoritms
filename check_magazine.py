from collections import defaultdict


def check_magazine(magazine, note):
    my_dcit = defaultdict(int)
    for word in magazine:
        my_dcit[word] += 1
    for word in note:
        my_dcit[word] -= 1
    if all([a > 0 for a in my_dcit.values()]):
        return True
    else:
        return False


if __name__ == '__main__':
    magazine = 'ive got a lovely bunch of coconuts'.split()
    note = 'ive got some coconuts'.split()
    assert check_magazine(magazine, note) == False
