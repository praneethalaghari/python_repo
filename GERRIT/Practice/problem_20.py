import random


def generate_random_list():
    list_A = random.sample(range(0, 9), 5)
    return list_A


def search_for_the_number(list_A):
    num = int(input('Enter a num'))
    print(list_A)
    if num in list_A:
        print('number is there in list position : ' + str(list_A.index(num)))

def binary_search(list_B,num_bin):
    sort_list_B = sorted(list_B)
    if len(sort_list_B) == 0:
        print("Element not found!!!")
    elif len(sort_list_B) == 1:
        if num_bin == sort_list_B[0]:
            print('Number found in list!!!')
    else:
        index = int(len(sort_list_B)/2)
        if num_bin == sort_list_B[index]:
            print('Match Found!!! ' + str(sort_list_B.index(num_bin)))
        elif num_bin < sort_list_B[index]:
            sort_list_C = sort_list_B[:index]
            binary_search(sort_list_C,num_bin)
        elif num_bin > sort_list_B[index]:
            sort_list_D = sort_list_B[index:]
            binary_search(sort_list_D,num_bin)


if __name__ == '__main__':
    list_A = generate_random_list()
    print(list_A)
    search_for_the_number(list_A)


    list_B = random.sample(range(0, 9), 6)
    num_bin = int(input('Enter number to search'))
    binary_search(list_B,num_bin)
    print(list_B)
