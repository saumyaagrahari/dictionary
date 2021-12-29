dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
sum=0
for i,j in dict.items():
    sum+=len(j)
print(sum)