#remove method
# list_integer=[3,4,5,9,3,8,3]
# list_integer.remove(3)
# print(list_integer)

#pop method

# list1=[16,18,14,13,90,75,13]
# list1.pop(5)
# print(list1)

#del method

# list1=[16,18,14,13,90,75,13]
# del list1[2]
# print(list1)


# list1=[16,18,14,13,90,75,13]
# list2=[]
# for i in range(len(list1)):
#
#     if list1[i]!=13:
#
#         list2.append(list1[i])
# print(list2)

#assginment


list1=[13,18,14,13,90,78,13]

list2=[]
for i in range(len(list1)):
    if list1[i]==13:
        list2.append(list1[i])
        print(i,end=" ")




