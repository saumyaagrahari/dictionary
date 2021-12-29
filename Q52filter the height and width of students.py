a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
66)}
dic={}
for x in a:
    if a[x][0]>=6 and a[x][1]>=70:
        dic.update(x=a[x])
print(dic)


