list1 = [10,11,12,13,14,15,16]
x = 22
list_size = len(list1)

#tries every pair until a matching one is found

def search(list1,x,list_size):

    for i in range(list_size - 1):
    #all elements in the list, except the last one

        for j in range(i + 1, list_size):
        #starts from i element until the last

            if (list1[i] + list1[j] == x):
                print("paired ", (list1[i], list1[j]))
                return

    print("no pair found")

search(list1,x,list_size)


#with enumerate
def search2(list1,x):
    dict = {}

    for idx,val in enumerate(list1):

        if x - val in dict:
            print("paired ", (list1[dict.get(x-val)], list1[idx]))
            #get() returns val of specified key
            return

        dict[val] = idx

    print("not pair found")

search2(list1,x)


#without sort funcs
list_again = [5,1,2,3,54,6,78,8,9,6]
size = len(list_again)

print("before", list_again)

for i in range(size):
    for j in range(i + 1, size):
        if list_again[i] > list_again[j]:
            list_again[i], list_again[j] = list_again[j], list_again[i]

print("after", list_again)