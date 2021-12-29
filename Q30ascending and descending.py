b={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
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