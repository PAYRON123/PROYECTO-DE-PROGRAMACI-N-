import random
import time

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
    rd = random.Random()

    for k in range(len(n)):
        array = [0] * n[k]
        array[0] = rd.randint(1, n[k])
        for i in range(1, n[k]):
            array[i] = rd.randint(1, n[k])
            for j in range(i - 1):
                if array[i] == array[j]:
                    i -= 1

        inicio = time.time_ns()
        quick_sort(array, 0, len(array) - 1)
        fin = time.time_ns()
        result_quick = fin - inicio

        inicio = time.time_ns()
        array = mergesort(array)
        fin = time.time_ns()
        result_merge = fin - inicio

        print(f"Tiempo QuickSort ({n[k]} elementos): {result_quick} nanosegundos")
        print(f"Tiempo MergeSort ({n[k]} elementos): {result_merge} nanosegundos")

if __name__ == "__main__":
    main()
