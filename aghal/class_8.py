# print('enter your salary')
# salary=int(input())
# if salary>=10000 and salary<=19000:
#     bonus=salary*0.04
#     new_salary=salary+bonus
# elif salary>=20000 and salary<=29000:
#     bonus=salary*0.06
#     new_salary=salary+bonus
# elif salary>=30000:
#     bonus=salary*0,1
#     new_salary=salary+bonus
# else:
#     new_salary=salary
#     print('no bonus')
# print(new_salary)

print('enter your per')
class_held=int(input())
class_attend=int(input())
per=class_attend/class_held*100
if per>=75 and per<=84:
    print('allow to exam')
elif per>=85 and per<=100:
    print('allow to sit in exam')
else:
    print('not allow to exam')