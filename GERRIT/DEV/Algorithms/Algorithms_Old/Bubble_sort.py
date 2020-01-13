
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            print(arr)
    return arr


if __name__ == '__main__':
    arr = [4,6,2,3,1,9,5,]
    print(bubble_sort(arr))
