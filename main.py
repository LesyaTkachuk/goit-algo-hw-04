import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == "__main__":
    data_small = [random.randint(0, 100) for _ in range(100)]
    data_medium = [random.randint(0, 1000) for _ in range(1000)]
    data_large = [random.randint(0, 10000) for _ in range(10000)]

    # time needed for small data amount sorting for 4 algorithm types
    time_insertion_sort_small_data = timeit.timeit(
        lambda: insertion_sort(data_small[:]), number=5
    )
    time_merge_sort_small_data = timeit.timeit(
        lambda: merge_sort(data_small[:]), number=5
    )
    time_timsort_sorted_small_data = timeit.timeit(
        lambda: sorted(data_small[:]), number=5
    )
    time_timsort_sort_small_data = timeit.timeit(lambda: data_small[:].sort(), number=5)

    # time needed for medium data amount sorting for 4 algorithm types
    time_insertion_sort_medium_data = timeit.timeit(
        lambda: insertion_sort(data_medium[:]), number=5
    )
    time_merge_sort_medium_data = timeit.timeit(
        lambda: merge_sort(data_medium[:]), number=5
    )
    time_timsort_sorted_medium_data = timeit.timeit(
        lambda: sorted(data_medium[:]), number=5
    )
    time_timsort_sort_medium_data = timeit.timeit(
        lambda: data_medium[:].sort(), number=5
    )

    # time needed for large data amount sorting for 4 algorithm types
    time_insertion_sort_large_data = timeit.timeit(
        lambda: insertion_sort(data_large[:]), number=5
    )
    time_merge_sort_large_data = timeit.timeit(
        lambda: merge_sort(data_large[:]), number=5
    )
    time_timsort_sorted_large_data = timeit.timeit(
        lambda: sorted(data_large[:]), number=5
    )
    time_timsort_sort_large_data = timeit.timeit(lambda: data_large[:].sort(), number=5)

    # printing of the results
    print(
        f"{'Algorithm':<20} | {'Small data sorting time':<25} | {'Medium data sorting time':<25} | {'Large data sorting time':<25}"
    )
    print(f"{'-'*20} | {'-'*25} | {'-'*25} | {'-'*25}")
    print(
        f"{'Insertion sort':<20} | {time_insertion_sort_small_data:<25} | {time_insertion_sort_medium_data:<25} | {time_insertion_sort_large_data:<25}"
    )
    print(
        f"{'Merge sort':<20} | {time_merge_sort_small_data:<25} | {time_merge_sort_medium_data:<25} | {time_merge_sort_large_data:<25}"
    )
    print(
        f"{'Timsort sorted':<20} | {time_timsort_sorted_small_data:<25} | {time_timsort_sorted_medium_data:<25} | {time_timsort_sorted_large_data:<25}"
    )
    print(
        f"{'Timsort sort':<20} | {time_timsort_sort_small_data:<25} | {time_timsort_sort_medium_data:<25} | {time_timsort_sort_large_data:<25}"
    )
    print(f"{'-'*20} | {'-'*25} | {'-'*25} | {'-'*25}")
