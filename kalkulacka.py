def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def odmocnina(a):
    if a < 0:
        raise ValueError("Druha odmocnina zaporneho cisla neni realne cislo")
    return a ** 0.5


if __name__ == "__main__":
    print("2 + 3 =", secti(2, 3))
    print("5 - 1 =", odecti(5, 1))
    print("Odmocnina z 9 =", odmocnina(9))
