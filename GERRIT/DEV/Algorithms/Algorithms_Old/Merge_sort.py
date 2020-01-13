def merge_sort(arr,low,high):
    if low < high:
        pivot = high/2
        merge_sort(arr, low, pivot-1)
        merge_sort(arr,pivot+1,high)
    print(arr)

if __name__ == '__main__':
    arr =  [4, 6, 2, 3, 1, 9, 5,]
    print(merge_sort(arr,0,len(arr)-1))