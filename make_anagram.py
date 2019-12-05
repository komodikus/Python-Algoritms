def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia - ib)
    return count


if __name__ == '__main__':
    assert makeAnagram("cde","abc") == 4
    assert makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") == 30
