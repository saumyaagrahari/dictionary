# dic={'A':100,'B':20,'C':50,'D':70,'E':55,'F':78}
# first_max = max(dic.values())
# print('first maximum number:',first_max)
# second_max = 0
# for i in dic.values():
#     if i>second_max:
#         if i!=first_max:
#             second_max=i
# print('second maximum number:',second_max)
# third_max=0
# for i in dic.values():
#     if i>third_max:
#         if i!=first_max and i!=second_max:
#             third_max=i
# print('third maximum number:',third_max)


# dic = {'a':19,'b':45,'c':33,'d':9,'e':99}
# a=[]
# for i in dic:
#     a.append(dic[i])
# print(a)


# dic = {'a':19,'b':45,'c':33,'d':9,'e':99}
# a=[]
# for i in dic.keys():
#     a.append(i)
# print(a)


# dic = {'a':19,'b':45,'c':33,'d':9,'e':99}
# a=[]
# b=[]
# for i in dic:
#     a.append(i)
#     b.append(dic[i])
# print(a,b)


# dict = {'Gfg':1,'is':2,'Best':3}
# a=[]
# b=[]
# for i in dict:
#     a.append(i)
#     b.append(dict[i])
# print(a+b)


# output {'b':{'a':{}},'e':{'d':{}},'g':{'f':{}}}

# dict = {'a':{'b':{}},'d':{'e':{}},'f':{'g':{}}}
# a=[]
# b=[]
# for i in dict.items():
#     a.append(dict[i])
#     b.append(i)
# print(b,a)


# a={'a':54,'b':55,'c':77,'d':66,'e':44}
# b=[]
























# num=int(input("enter the number:"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count == 2:
#     print("it is a prime number:",num)
# else:
#     print("it is a not prime number:",num)