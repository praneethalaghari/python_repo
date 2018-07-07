def linear_search(arr,elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return 1,i
    else:
        return -1,i

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    elem = 6

    p,q = linear_search(arr, elem)


    if p == 1:
        print("Element found in the array hurray in place : {}!!!".format(q+1))
    else:
        print("Element not found after iterating all the : {} elements".format(q+1))
        #print("Element not found after iterating all the : %d elements" %(q+1))
        # Adding a new feature - adding an element in the array(list) if that element is not there
        arr.insert(0,elem)
