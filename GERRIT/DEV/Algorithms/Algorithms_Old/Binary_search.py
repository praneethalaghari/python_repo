# The max number of searches - or the worst number of searches both same i,e to reduce the number of elements to 1 is
#   max_num_of_changes = log2(n) where n is the number of elements in the array

# The input should be sorted for binary search

import datetime
from timeit import default_timer as timer

def binary_search(arr,elem,num_of_iter):
    num_of_iter +=1
    i = len(arr)
    found = 0
    if arr[int(i/2)] == elem:
        found = 1
    elif len(arr) == 1 and arr[int(i/2)]!= elem:
        found = 0
    elif arr[int(i/2)] < elem:
        found,num_of_iter = binary_search(arr[int(i/2):],elem,num_of_iter)
    else:
        found, num_of_iter = binary_search(arr[:int(i/2)],elem,num_of_iter)

    return found,num_of_iter

if __name__ == '__main__':
    arr = [1,5,6,7,3,4,9,2,8,12,11,13,14,15,16,17]
    arr_sorted = sorted(arr)
    print(arr_sorted)
    elem = 9
    num_of_iter = 0

    p,q = binary_search(arr_sorted,elem,num_of_iter)

    if p:
        print("Element found in {} iterations".format(q))
    else:
        print("Element not found in the array")



