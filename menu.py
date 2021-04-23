import random
from time import time_ns

from bubble_sort import bubble
from insertion_sort import insertion
from selection_sort import selection_sort
from quick_sort import quick
from merge_sort import merge
from heap_sort import heap


def main():
    menu = {
        "bubble": lambda v: bubble(v),
        "insertion": lambda v: insertion(v),
        "selection": lambda v: selection_sort(v),
        "quick": lambda v: quick(v),
        "merge": lambda v: merge(v),
        "heap": lambda v: heap(v),
    }

    vec = [i for i in range(10000)]
    vec[0], vec[-1] = vec[-1], vec[0]

    for key, function in menu.items():
        print(f"{key}")

        j = 1
        while j <= 10000:

            s = time_ns()
            function(vec[:j])
            e = time_ns()
            diff = e - s
            print(f"{diff / (10 ** 9)}".replace(".", ","))

            j = j * 10


if __name__ == '__main__':
    main()
