def insertion_sort(list):
    list = list[:]
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j ]
            j -= 1
        list[j+1] = key

    return list


if __name__ == "__main__":
    numbers = [5, 3, 6, 4, 8, 2]
    sorted_list = insertion_sort(numbers)
    print(sorted_list)
