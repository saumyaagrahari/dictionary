my_dict = {
'arav':50,
'bhavna':58,
'sachin':56,
'deepa':40,
'anu':100,
'fatima':20
}
first_max=max(my_dict.values())
print("first maximum number",first_max)
second_max=0
for i in my_dict.values():
    if i>second_max:
        if i!=first_max:
            second_max=i
print("second maximum number",second_max)
third_max=0
for i in my_dict.values():
    if i>third_max:
        if i!=first_max and i!=second_max:
            third_max=i
print("third maximum number",third_max)

