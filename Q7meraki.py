dict=[
{"first":"1"},
{"second": "2"},
{"third": "1"},
{"four": "5"},
{"five":"5"},
{"six":"9"},
{"seven":"7"}
]
list=[]
for i in dict:    
    for j in i.values():
        if j not in list:
            list.append(j)
print(list)

