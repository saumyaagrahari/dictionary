# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a = sorted(a.items() , reverse=True, key=lambda x: x[1])
# b={}
# c={}
# for i in a :
#     b.update(a)
# print(b,":",end="")
# for i in b:
#     c.update(b)
# print(-c,":",end="")

b={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=[]
for i in b:
    a.append(b[i])
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j+=1
    i+=1
n={}
j=0
while j<len(a): 
    for i in b:
        if a[j]==b[i]:
            n[i]=b[i]
    j+=1
print(n) 


a=[]
for i in b:
    a.append(b[i])
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j+=1
    i+=1
n={}
j=0
while j<len(a): 
    for i in b:
        if a[j]==b[i]:
            n[i]=b[i]
    j+=1
print(n) 