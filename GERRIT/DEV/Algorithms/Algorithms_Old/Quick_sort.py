
def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)

        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr

def partition(arr,low,high):

    i = low -1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

if __name__ == '__main__':
    arr = [4, 6, 2, 3, 1, 9, 5,]
    print(quick_sort(arr,0,len(arr)-1))