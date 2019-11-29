"""
You are given two lines a and b. Determine if there is a non-empty string that occurs as a substring in both a and b.
"""


def two_strings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    assert two_strings('world', 'hi') == "NO"
