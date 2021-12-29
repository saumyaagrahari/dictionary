a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
b={}
for i in a:
    for j in range(len(i)-2):
        c=[i[j+1],i[j+2]]        
        b.update({i[j]:c})
        # print(j)
print(b)