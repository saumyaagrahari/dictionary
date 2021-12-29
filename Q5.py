# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 



# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# a = {'a':1,'b':2,'c':3}
# for i in a:
#     print (i,"=",a[i])



# dic={}
# for i in range(10):
#     name=input("enter name:")
#     marks=int(input("enter the number:"))
#     # a=({name:marks})
#     dic.update({name:marks})
#     # dic.update(a)
# print(dic)



dict = {
'Alex': ['subj1', 'subj2', 'subj3'],
'David': ['subj1', 'subj2']}
count=0
sum=[]
for i in dict.values():
    sum=sum+i
# print(sum)
i=0
while i<len(sum):
    a=sum[i]
    count+=1
    i+=1
print(count)




# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.sort()
# print(numbers)
# print(numbers[-2])


# a={'a':12,'b':20,'c':25}
# b=[]
# for x in a:
#     b.append(a[x])
# print(b)

# a=[{'a':23,'b':32},{'c':4},{'d':7,'e':8}]
# b={}
# c=[]
# for i in a:
#     for j in i.keys():
#         c.append(j)
# print(c)
    # print(a)
    # break

