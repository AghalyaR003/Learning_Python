print('enter the elements')
list1=list(map(in,input().split())
for i in range(len(list1)):
    if list1[i]%2==0:
        print('not satisfied')
        break