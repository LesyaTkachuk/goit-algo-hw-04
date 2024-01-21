def merge_sort(list):
    list=list[:]
    n = len(list)
    if n <= 1:
        return list

    middle_element = n // 2
    left_part = list[:middle_element]
    right_part = list[middle_element:]
    return merge(merge_sort(left_part), merge_sort(right_part))

def merge(left,right):
    merged=[]
    left_index=0
    right_index=0
    
    # merge smaller elements
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<=right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1

    # add left elements from both parts
    while left_index<len(left):
        merged.append(left[left_index])
        left_index+=1

    while right_index<len(right):
        merged.append(right[right_index])
        right_index+=1

    return merged

if __name__ == "__main__":
    numbers = [5, 3, 6, 4, 8, 2]
    sorted_list = merge_sort(numbers)
    print(sorted_list)