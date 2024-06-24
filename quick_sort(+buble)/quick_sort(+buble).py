import timeit
from random import randint


def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    middle = randint(0, len(array) - 1)
    pivot = array[middle]
    array.remove(pivot)
    left = [i for i in array if i <= pivot]
    right = [i for i in array if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def bubble_sort(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    array = [randint(0, 100) for _ in range(1000)]
    iterations = 100
    array_copy = array.copy()
    time_1 = timeit.timeit("quick_sort(array_copy)", globals=globals(), number=iterations)
    array_copy = array.copy()
    time_2 = timeit.timeit("bubble_sort(array_copy)", globals=globals(), number=iterations)
    print(f'quick_sort time: {time_1}')
    print(f'bubble_sort time: {time_2}')
