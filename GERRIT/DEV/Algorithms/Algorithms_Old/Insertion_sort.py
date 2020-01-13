
def insertion_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,i+1):
            if arr[i-j] > arr[i+1-j]:
                arr[i-j],arr[i+1-j] = arr[i+1-j],arr[i-j]
    return arr

if __name__ == '__main__':
    arr = [4,6,2,3,1,9,5,]
    print(insertion_sort(arr))