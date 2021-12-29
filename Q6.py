
# my_dict = {
# 'a':50,
# 'b':58,
# 'c': 56,
# 'd':40,
# 'e':100,
# 'f':20
# }
# first_max=max(my_dict.values())
# print("first maximum keys",first_max)
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
max_key = max(my_dict, key=my_dict.get)
print(max_key)
first_max=max(my_dict.items())
print("first maximum keys",first_max)
second_max=0
for i,j in my_dict.items():
    if j>second_max:
        if j!=first_max:
            second_max=j
print("second maximum kyes",i,second_max)
third_max=0
for i,j in my_dict.items():
    if j>third_max:
        if j!=first_max and j!=second_max:
            third_max=j
print("third maximum keys",i,third_max)


