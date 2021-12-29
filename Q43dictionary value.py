dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
list={}
for i in range(len(dict)):
    list.update(dict[i])
print(list)
