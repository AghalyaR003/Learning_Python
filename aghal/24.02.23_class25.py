# dict1={}
# for i in range(2):
#     rollno, mark = map(int,input().split())
#     dict1[rollno] = mark
#
# print(dict1)

# dict1={}
# print('enter the no of keys values pairs')
# times=int(input())
# for i in range(times):
#        rollno,mark,cgpa=map(int,input().split())
#        dict1[rollno]=[mark,cgpa]
# print(dict1)


# dict1={}
# print("enter the no of keys values pairs")
# times=int(input())
# for i in range(times):
#     print("enter rollno mark1 mark2")
#     rollno, mark1,mark2= map(int,input().split())
#     dict1[rollno] = {'eng': mark1,'maths':mark2}
#
# print(dict1)

# dict1={101:90,102:65,103:85}
# dict2={}
# for i,j in dict1.items():
#     if j>=50:
#         dict2[i]="pass"
#     else:
#         dict2[i]="fail"
# print(dict2)

# dict1={101:90,102:65,103:85}
# dict2={i:'pass' if j>=50 else 'fail' for i,j in dict1.items()}
# print(dict2)

# dict1={101:[90,85],102:[65,70]}
# dict2={i:'pass' if j[0]>=50 and j[1]>50 else 'fail' for i,j in dict1.items()}
# print(dict2)

# dict1={101:{'eng':50,'maths':75},102:{'eng':60,'maths':80},103:{'eng':75,'maths':95}}
# dict2={}
# for i,j in dict1.items():
#     if j['eng']>=50 and j['maths']>=50:
#         dict2[i]='pass'
#     else:
#         dict2[i]='fail'
# print(dict2)



# dict1={101:{'eng':45,'maths':75},102:{'eng':60,'maths':80},103:{'eng':75,'maths':95}}
# dict2={i:'pass' if j['eng']>=50 and j['maths']>=50 else 'fail' for i,j in dict1.items()}
# print(dict2)

dict1={"name":"kelly",
       "age": 25,
       "salary": 8000,
       "city": "new york"}

#
# dict2={i:'name','salary'  if j[0]='kelly' and j[2]=8000 else 'not found' for i,j in dict1.items()}
# print(dict2)
# list1=[]
# for i in dict1.keys():
#        list1.append('name','salary')
#        print(i)