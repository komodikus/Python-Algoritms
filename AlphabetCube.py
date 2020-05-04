import string

alpha = string.ascii_lowercase


def draw_ragnoli(height):
    result = []
    for i in range(height):
        line = "-".join(alpha[i:height])
        result.append((line[::-1] + line[1:]).center(4 * height - 3, "-"))
    print("\n".join(result[::-1] + result))


if __name__ == '__main__':
    b = int(input("Input size ragnoli:"))
    draw_ragnoli(b)
