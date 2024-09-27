# list=[5,3,4,8,9,12]
# for i in range(len(list)):
#     if i%2!=0:
#           list[i]=list[i]+100
#
#     print(list[i],end=" ")
#

list1=[6,7,3,4,12,23,41,6,7,4,7]
for i in range(len(list1)):
    if list1[i]%2==0:
        print("index of",list1[i],"is",end=" ")
        for j in range(len(list1)):
            if list1[j]==list1[i]:
                print(j,end=" ")
        print()





