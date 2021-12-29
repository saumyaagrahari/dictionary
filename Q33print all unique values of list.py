list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
# i=0
# a=[]
# while(i<len(list)):
#     for x in list[i]:
#         a.append(list[i][x])
#     i+=1
# print(a)
# b=[]
# i=0
# while (i<len(a)):
#     if a[i]not in b:
#         b.append(a[i])
#     i+=1
# print(b)

i=0
a=[]
b=[]
while(i<len(list)):
    for x in list[i]:
        a.append(list[i][x])
        if a[i] not in b:
            b.append(a[i])
        i+=1
print(b)
