

# d3={}
# d4={}
# for e,f in d1.items():
#     for x,y in d2.items():
#         if e==x:
#             d3[e]=(f+y)
# print(d3)


# str1 = 'w3resource' 
str1=input("enter the character:")
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


# name=input("enter the name:")
# i=0
# dic={}
# while (i<len(name)):
#     j=0
#     count=0
#     while(j<len(name)):
#         if (name[i]==name[j]):
#             count+=1
#         j+=1
#     dic[name[i]]=count
#     i+=1
# print(dic)































# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# j=1
# while i< len(a):
#     print(a[i],b[-j])
#     j=j+1
#     i=i+1