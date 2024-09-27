#import re
#str1="ms maaas"
#ans1=re.findall("ma*s",str1)
#ans2=re.findall("ma+s",str1)
#ns3=re.findall("ma?s",str1)
#print(ans1,ans2,ans3)


#import re
#str1="mas maaaaas"
#ans=re.findall("ma{1,3}s",str1)
#print(ans)


#import re
#str1="2134  123"
#ans=re.findall('[0-9]{1,4}',str1)
#print(ans)

#import re
#str1="674 302"
#ans=re.findall('^[0-9]{1}[1-9]{2}\s[0-9]{3}$',str1)
#print(ans)

#import re
#str1="A05 282"
#ans=re.findall('^[a-z A-Z]{1}[0-9]{2}\s[0-9]{3}$',str1)
#print(ans)

#import re
#str1="28/02/2003"
#ans=re.findall('^[0-9]{2}/[0-9]{2}/[0-9]{4}$',str1)
#print(ans)


#import re
#str1="6374053080"
#ans=re.findall('^[6-9]{1}[0-9]{9}$',str1)
#print(ans)


#class A:
#    def __init__(self,m1,m2,m3):
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#    def __add__(self):
#        ans=self.m1+self.m2+self.m3
#        print(ans/3)
#obj1=A(29,80,50)
#obj1.__add__()


#class A:
#    def __init__(self,m1,m2,m3):
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#    def __add__(self, other1,other2):
#        ans1=self.m1+other1.m1+other2.m1
#        ans2=self.m2+other1.m2+other2.m2
#        ans3=self.m3+other1.m3+other2.m3
#        return ans1,ans2,ans3
#obj1=A(2,8,3)
#obj2=A(5,1,2)
#obj3=A(7,4,5)
#ans1,ans2,ans3=obj1.__add__(obj2,obj3)
#print(ans1,ans2,ans3)

