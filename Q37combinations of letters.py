dic={'1':['a','b'], '2':['c','d']}
l=[]
for i,j in dic.items():
    # print(j)
    # l=[]
    for k in range(len(j)):
        l.append(j[k][0])
# print(l)
for i in range(len(l)-2):
    print(l[i],l[2])
    print(l[i],l[3])



# a={}
# dict={'a':1,'b':2,'c':3,'d':4}
# print(dict)
# for i,j in dict.items():
#     a.update({j:i})
# print(a)