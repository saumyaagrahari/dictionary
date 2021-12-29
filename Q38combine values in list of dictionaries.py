# Counter({'item1': 1150, 'item2': 300})

dic=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
'amount': 750}]
newdict={}
for i in dic:
    if i['item'] not in newdict:
        newdict[i['item']]=i['amount']
    else:
        newdict[i['item']]=newdict[i['item']]+i['amount']
print(newdict)