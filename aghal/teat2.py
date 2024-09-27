# dict1={101:{"rent":6000,"floor":4000},
#        102:{"rent":8000,"floor":3000},
#        103:{"rent":9000,"floor":5000},
#        104:{"rent":10000,"floor":6000}}
# for i,j in dict1.items():
#     if j["floor"]<=6000 and j["rent"]>=10000:
#         print(i)



def demo(list1):
    for i in range(len(list1)):
        if list1[i]%2==0:
            print(list1[i])
def fun1():
    print('enter the elements')
    list1=list(map(int,input().split()))
    demo(list1)
fun1()


