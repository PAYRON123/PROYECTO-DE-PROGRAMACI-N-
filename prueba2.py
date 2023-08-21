import random
import time


def generate_random_code():
    return ''.join(random.choice('0123456789') for _ in range(8))


def quick_sort(a, first, last):
    i, j = first, last
    pivote = a[(first + last) // 2]
    while i <= j:
        while a[i] < pivote:
            i += 1
        while a[j] > pivote:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if first < j:
        quick_sort(a, first, j)
    if i < last:
        quick_sort(a, i, last)


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def mergesort(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = mergesort(left)
        right = mergesort(right)

        return merge(left, right)


def merge(a, b):
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


def main():
    n = [10, 100, 1000, 10000]

    for k in range(len(n)):
        array_quick = [generate_random_code() for _ in range(n[k])]
        array_merge = array_quick.copy()
        array_bubble = array_quick.copy()

        inicio = time.time_ns()
        quick_sort(array_quick, 0, len(array_quick) - 1)
        fin = time.time_ns()
        result_quick = fin - inicio

        inicio = time.time_ns()
        array_merge = mergesort(array_merge)
        fin = time.time_ns()
        result_merge = fin - inicio

        inicio = time.time_ns()
        bubble_sort(array_bubble)
        fin = time.time_ns()
        result_bubble = fin - inicio

        print(f"Tiempo QuickSort ({n[k]} elementos): {result_quick} nanosegundos")
        print(f"Tiempo MergeSort ({n[k]} elementos): {result_merge} nanosegundos")
        print(f"Tiempo BubbleSort ({n[k]} elementos): {result_bubble} nanosegundos")


if __name__ == "__main__":
    main()
