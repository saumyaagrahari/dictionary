# my_dict = {
# 'a':50,
# 'b':100,
# 'c': 56,
# 'd':40,
# 'e':12,
# 'f':20
# }

# large=0  
# ke=0    
# for i in my_dict:
#     if(my_dict[i]>large):
#         key_1=i
#         large=my_dict[i]
# print(key_1)

# first_max=max(my_dict.values())
# print("first maximum keys",first_max)
# print(my_dict[first_max])
# second_max=0
# for i in my_dict.values():
#     if i>second_max:
#         if i!=first_max:
#             second_max=i
# print("second maximum kyes",second_max)
# third_max=0
# for i in my_dict.values():
#     if i>third_max:
#         if i!=first_max and i!=second_max:
#             third_max=i
# print("third maximum keys",third_max)

my_dict = {
'a':50,
'b':58,
'c': 56,
'd':40,
'e':100,
'f':20
}

max=0
max1=0
max2=0
k=[]
for x in my_dict:
    if my_dict[x]>max:
        max2=max1
        max1=max
        max=my_dict[x]
print(max,max1,max2)