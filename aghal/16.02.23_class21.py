# tup1=(57,15,23,12)
# num1,num2,num3,num4=tup1
# print(num1,num2)

# tup1=("python","hi","programming","hi")
# print(tup1.index("hi"))

#
# set1={5,3,7,8}
# for i in set1:
#     print(i)
# for i in range(len(set)):
#     print(set1[i])

# set1={5,3,7,8}
# set1.add(7)
# print(set1)

# set1={5,3,7,8}
# set1.remove(5)
# print(set1)

# set1={6,7,4,3}
# set2=set1.copy()
# print(set2)

# set1={5,3,7,8}
# set2={100,50,200}
# set1.update(set2)
# print(set1)


# set1={8,7,4,8}
# set2={8,2,5,9}
# ans=set1.union(set2)
# print(ans)

#
# set1={7,3,5}
# set2={10,3,8}
# ans=set1.intersection(set2)
# print(ans)


# set1={6,7,4,3,80,56}
# set2={"hi","python",6}
# set1.intersection_update(set2)
# print(set1)

set1={6,7,4,3}
set2={9,2,5,6}
ans=set2.symmetric_difference(set1)
print(ans)