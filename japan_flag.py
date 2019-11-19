def generate_japan_flag(n):
    canvas = list()
    canvas.append("#" * (n * 3 + 2))
    for i in range(n // 2):
        canvas.append("#" + ''.rjust(3 * n, "-") + "#")
    for i in range(n // 2):
        canvas.append("#" + f'*{"o" * i*2}*'.center(3 * n, "-") + "#")
    return "\n".join(canvas + canvas[::-1])


if __name__ == '__main__':
    print(generate_japan_flag(12))
