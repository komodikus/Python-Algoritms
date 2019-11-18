import string

alpha = string.ascii_lowercase


def draw_ragnoli(height):
    L = []
    for i in range(height):
        line = "-".join(alpha[i:height])
        L.append((line[::-1] + line[1:]).center(4 * height - 3, "-"))
    print("\n".join(L[::-1] + L))


if __name__ == '__main__':
    b = int(input("Input size ragnoli:"))
    draw_ragnoli(b)
