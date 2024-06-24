import timeit


def isEven_1(value):
    return value % 2 == 0


def isEven_2(value):
    return not value & 1


if __name__ == "__main__":
    num = 123894534252523452324234434534
    iterations = 10_000_000
    time_1 = timeit.timeit("isEven_1(num)", globals=globals(), number=iterations)
    time_2 = timeit.timeit("isEven_2(num)", globals=globals(), number=iterations)
    print('Время выполнения "isEven_1": ', time_1)
    print('Время выполнения "isEven_2": ', time_2)
