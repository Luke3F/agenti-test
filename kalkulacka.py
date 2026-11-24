def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def nasob(a, b):
    return a * b


def vydel(a, b):
    if b == 0:
        raise ValueError("Deleni nulou neni povoleno.")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", secti(2, 3))
    print("5 - 1 =", odecti(5, 1))
    print("4 * 3 =", nasob(4, 3))
    print("10 / 4 =", vydel(10, 4))
    try:
        vydel(1, 0)
    except ValueError as e:
        print("1 / 0 ->", e)
