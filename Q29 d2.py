# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# for x in dic2:
#     dic1[x]=dic2[x]
# for x in dic3:
#     dic1[x]=dic3[x]
# print(dic1)


# # dic={'W3resource'}
# str1=input("enter the character:")
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# num=int(input("enter the num value:"))
# b={}
# for i in range(num):
#     dict={i:i**2}
#     print(dict,end="")

# num=15
# for i in range(num):
#     dict={i:i**2}
#     print(dict,end="")

# num={1:2,3:4,4:3,2:1,0:0}
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a = sorted(a.items() , reverse=True, key=lambda x: x[1])
# b={}
# for i in a :
#     b.update(a)
# print(b,":",end="")


# num= sorted(num.items() , reverse=True, key=lambda x: x[1])
# b={}
# for i in num :
#     b.update(num)
# print(b,":",end="")


n = 125
for j in range(1, n +1):
    if n % j == 0:
        print(j)