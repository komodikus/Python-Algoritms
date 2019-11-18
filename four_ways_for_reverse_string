def f1(s):
    return s[::-1]


def f2(s):
    return "".join(reversed(s))


def f3(s):
    result = ""
    for i in s:
        result = i + result
    return result

def f4(s):
    if len(s)==0:
        return s
    return f4(s[1:]) + s[0]

if __name__ == '__main__':
    test_string = "GlobalKot"
    print(f1(test_string), f2(test_string), f3(test_string), f4(test_string), sep="\n")
