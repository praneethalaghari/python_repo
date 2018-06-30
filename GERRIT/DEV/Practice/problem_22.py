
with open("names.txt", "r") as f:

    print(f.tell())
    cool = f.read(50)
    print(cool)
    print(f.tell())


    f.seek(0)
    print(f.tell())

    lines_in_file = f.readlines()
    lines_in_file_without_n = [x.strip('\n') for x in lines_in_file]
    print(lines_in_file_without_n.count('Lea'))
    print(lines_in_file_without_n.count('Darth'))
    print(lines_in_file_without_n.count('Luke'))

    print(f.tell())


with open("work_less.txt","r") as g:
    line = g.readline()
    arr = []
    while line:
        arr.append(line.split('/')[2])
        line = g.readline()

    unique_categ = set(arr)
    print(unique_categ.__len__())

    for itr in unique_categ:
        print("Nuber of images corresponding to " + itr + ' is ' + str(arr.count(itr)))

