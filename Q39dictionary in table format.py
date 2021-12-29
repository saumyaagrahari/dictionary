# my_dict = {'C':[1,2,3],'C':[5,6,7],'C':[9,10,11]}
# a={}
# i=0
# for i in my_dict:
#     print(i)
#     for j in i:
#         print(j)


my_dict = {'C1':[1,2,3,6],'C2':[5,6,7,8],'C3':[9,10,11,8],'C4':[9,8,7,6]}
list=[]
k=0
for i,j in my_dict.items():
    print(i,end=" ")
    list.append(j)
print("\n")
# i=0
# while i<len(list):
#         j=0
#         while j<len(list[i]):
#             print(list[j][i],end=" ")
#             j+=1
#         print("\n")
#         i+=1

for i in range (0,len(list[0])):
    for j in range (0,len(list)):
        print(list[j][i],end=" ")
    print("\n")


