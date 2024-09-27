# dict1 = {101: [67, 70], 102: [75, 70], 103: [67, 75]}
#
# for i,j in dict1.items():
#     if j==[67,70]:
#         print(i)


# dict1 = {104: 45, 105: 65, 106: 95}
# for i, j in dict1.items():
#     if j == 95:
#         print(i)

# dict1 = {107: [90, 80], 108: [80, 70], 109: [70, 80]}
# for i, j in dict1.items():
#     if j[0] == 90 and j[1] == 80:
#         print(i)

# dict1={111:{'c++':95,'java':80},112:{'c++':70,'java':65}}
# dict2={}
# dict2[113]={'c++':95,'java':85}
# print(dict1,dict2)


# dict1={"rollno":101,"name":"alex","mark":[90,70,60,80]}
# print(dict1.keys())
# dict1["cgpa"]=89
# print(dict1.keys())


# set1={13,17}
# set2={3,7,10,12}
# ans=set2.isdisjoint(set1)
# print("disjoint",ans)


# dict1={111:{'c++':95,'java':80},112:{'c++':70,'java':65},113:{'c++':95,'java':85}}
# for i,j in dict1.items():
#     if j['c++']==95:
#         print(i)

# #
# dict1={101:{"rent":6000,"floor":7000},
#        102:{"rent":8000,"floor":5000},
#        103:{"rent":10000,"floor":6000}}
# for i,j in dict1.items():
#     if j["rent"]>=10000 and j["floor"]<=6000:
#         print(i)
#
# #
# dict1={101:{"rent":8000,"bhk":1,"bedroom":6000},
#        102:{"rent":8000,"bhk":2,"bedroom":6000},
#        103:{"rent":6500,"3bhk":1,"bedroom":7500}}
# for i,j in dict1.items():
#     if j["rent"]>=8000 and j["bhk"]==1 and j["bedroom"]<=6000:
#         print(i)