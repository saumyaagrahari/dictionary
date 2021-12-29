from typing import KeysView


dic={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

print(dic['x'][4])
print(dic['y'][4])
print(dic['z'][4])
for x in dic:
    print(x,"has value",dic[x])