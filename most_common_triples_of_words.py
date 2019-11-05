from collections import Counter

words = "abba com mother bill mother com abba dog abba mother com".split()


def get_triples(arr):
    for i in range(1, len(arr) - 2):
        yield tuple(sorted(arr[i:i + 3]))


if __name__ == '__main__':
    all_triples = Counter(list(get_triples(words)))
    print(all_triples.most_common(1))
