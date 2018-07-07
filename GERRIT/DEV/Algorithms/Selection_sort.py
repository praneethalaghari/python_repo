def selection_sort(arr):

    for i in range(0, len(arr)-1):
        min_value_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        if min_value_index != i:          # It will work even without this line but this can reduce few unnecessary swapping sometimes
            arr[i],arr[min_value_index] = arr[min_value_index],arr[i]
    return arr


if __name__ == '__main__':
    arr = [4, 6, 2, 3, 1, 9, 5, ]
    print(selection_sort(arr))