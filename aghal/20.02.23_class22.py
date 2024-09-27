# dict1={101:"alex",102:"ibrahim",103:"jacob",102:"sarah"}
# print(dict1)


# dict1={101:'aa',109:'ll',112:'lp',145:'yy'}
# ans=dict1[109]
# print(ans)
#
# dict1={'aghal':[90,85,'a'],'achu':[85,80,'b']}
# ans=dict1['achu'][2]
# print('achu grade is',ans)


# dict1={103:{'c++':80,'java':90},
#        116:{'c++':95,'java':100}}
# ans=dict1[116]['java']
# print(ans)
#
# dict1={101:90,116:80,152:60}
# mark=int(input('enter'))
# for i,j in dict1.items():
#     if j==mark:
#         print(i)

# dict1={103:85,116:95,152:80}
# # for i in dict1.values():
# #     print(i)
# for i,j in dict1.items():
#     print(i,j)

dict1={"class":{"student":{"name":"mike","marks":{"physics":70,"history":80}}}}
ans=dict1['class']['student']['marks']['history']
print(ans)